#!/usr/bin/env python3
"""
WORLDTEXT FULL-TEXT EVIDENCE EXTRACTOR

Extracts text from all PDF and HTML sources in the Zotero export directory,
maps them to their BibTeX keys, and writes plain text files for cosmos ingestion.

Usage: python3 extract-sources.py
"""

import os
import re
import sys
import json
from html.parser import HTMLParser
from pathlib import Path

# Paths
ZOTERO_DIR = Path(__file__).parent / "Operative Ekphrasis, Thick Description"
FILES_DIR = ZOTERO_DIR / "files"
BIB_FILE = ZOTERO_DIR / "Operative Ekphrasis, Thick Description.bib"
JSON_FILE = Path(__file__).parent / "Operative Ekphrasis, Thick Description.json"
OUTPUT_DIR = Path(__file__).parent / "worldtext" / "sources-fulltext"

# ── HTML text extractor ──────────────────────────────────────
class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link'}
        self._skip = False
    
    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self._skip = True
    
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self._skip = False
        if tag in ('p', 'div', 'br', 'h1', 'h2', 'h3', 'h4', 'li', 'tr'):
            self.result.append('\n')
    
    def handle_data(self, data):
        if not self._skip:
            self.result.append(data)
    
    def get_text(self):
        return ''.join(self.result).strip()


def extract_html(filepath):
    """Extract text from an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        parser = HTMLTextExtractor()
        parser.feed(content)
        text = parser.get_text()
        # Clean up excessive whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        return text
    except Exception as e:
        return f"[ERROR extracting HTML: {e}]"


def extract_pdf(filepath):
    """Extract text from a PDF using PyMuPDF."""
    try:
        import fitz  # pymupdf
        doc = fitz.open(str(filepath))
        pages = []
        for i, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                pages.append(f"── PAGE {i+1} ──\n{text}")
        doc.close()
        return '\n\n'.join(pages)
    except Exception as e:
        return f"[ERROR extracting PDF: {e}]"


def parse_bibtex_file_mapping(bib_path):
    """Parse BibTeX to map Zotero file IDs to citation keys."""
    mapping = {}  # zotero_dir_id -> (cite_key, title)
    
    if not bib_path.exists():
        return mapping
    
    with open(bib_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Parse each entry
    entries = re.findall(r'@\w+\{([^,]+),(.+?)(?=\n@|\Z)', content, re.DOTALL)
    
    for cite_key, body in entries:
        cite_key = cite_key.strip()
        
        # Extract title
        title_match = re.search(r'\btitle\s*=\s*\{(.+?)\}', body)
        title = title_match.group(1) if title_match else cite_key
        
        # Extract file references (format: name:files/NNNN/filename.pdf:mimetype)
        file_match = re.search(r'\bfile\s*=\s*\{(.+?)\}', body)
        if file_match:
            file_refs = file_match.group(1)
            # Can have multiple files separated by ;
            for ref in file_refs.split(';'):
                parts = ref.strip().split(':')
                if len(parts) >= 2:
                    file_path = parts[1].strip()
                    # Extract the directory number
                    dir_match = re.search(r'files/(\d+)/', file_path)
                    if dir_match:
                        dir_id = dir_match.group(1)
                        mapping[dir_id] = (cite_key, title)
    
    return mapping


def load_json_metadata(json_path):
    """Load the JSON evidence corpus for additional metadata."""
    if not json_path.exists():
        return {}
    
    with open(json_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)
    
    metadata = {}
    for i, entry in enumerate(entries):
        author = entry.get('author', [{}])
        first_author = author[0].get('family', 'unknown') if author else 'unknown'
        year_parts = entry.get('issued', {}).get('date-parts', [['']])
        year = str(year_parts[0][0]) if year_parts and year_parts[0] else 'n.d.'
        title = entry.get('title', f'Source {i}')
        entry_type = entry.get('type', 'document')
        abstract = entry.get('abstract', '')
        
        metadata[i] = {
            'author': first_author,
            'year': year,
            'title': title,
            'type': entry_type,
            'abstract': abstract
        }
    
    return metadata


def make_safe_filename(s, max_len=80):
    """Convert a string to a safe filename."""
    s = re.sub(r'[^\w\s-]', '', s.lower())
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s[:max_len]


def main():
    print("🪐 WORLDTEXT FULL-TEXT EVIDENCE EXTRACTOR")
    print("=" * 50)
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load BibTeX mapping
    bib_mapping = parse_bibtex_file_mapping(BIB_FILE)
    print(f"\n📚 BibTeX entries with files: {len(bib_mapping)}")
    
    # Load JSON metadata
    json_metadata = load_json_metadata(JSON_FILE)
    print(f"📋 JSON metadata entries: {len(json_metadata)}")
    
    # Find all source files
    if not FILES_DIR.exists():
        print(f"❌ Files directory not found: {FILES_DIR}")
        sys.exit(1)
    
    results = {
        'pdf_success': 0, 'pdf_fail': 0,
        'html_success': 0, 'html_fail': 0,
        'total_chars': 0,
        'files': []
    }
    
    for dir_entry in sorted(FILES_DIR.iterdir()):
        if not dir_entry.is_dir():
            continue
        
        dir_id = dir_entry.name
        
        for file_entry in dir_entry.iterdir():
            ext = file_entry.suffix.lower()
            
            if ext not in ('.pdf', '.html', '.htm'):
                continue
            
            # Get metadata from BibTeX mapping
            cite_key = 'unknown'
            title = file_entry.stem
            if dir_id in bib_mapping:
                cite_key, title = bib_mapping[dir_id]
            
            # Extract text
            print(f"  📄 {dir_id}/{file_entry.name[:60]}...", end=' ')
            
            if ext == '.pdf':
                text = extract_pdf(file_entry)
                if text.startswith('[ERROR'):
                    results['pdf_fail'] += 1
                    print(f"❌ {text[:50]}")
                    continue
                results['pdf_success'] += 1
            else:
                text = extract_html(file_entry)
                if text.startswith('[ERROR'):
                    results['html_fail'] += 1
                    print(f"❌ {text[:50]}")
                    continue
                results['html_success'] += 1
            
            char_count = len(text)
            results['total_chars'] += char_count
            
            # Build output filename
            safe_name = make_safe_filename(cite_key if cite_key != 'unknown' else title)
            output_file = OUTPUT_DIR / f"{safe_name}.txt"
            
            # Write header + extracted text
            header = f"""# {title}
# Source: {file_entry.name}
# BibTeX key: {cite_key}
# Zotero dir: {dir_id}
# Extracted chars: {char_count}
# Format: {ext[1:].upper()}
{'='*60}

"""
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(header + text)
            
            word_count = len(text.split())
            print(f"✅ {word_count:,} words → {output_file.name}")
            
            results['files'].append({
                'cite_key': cite_key,
                'title': title,
                'dir_id': dir_id,
                'format': ext[1:],
                'chars': char_count,
                'words': word_count,
                'output': str(output_file.name)
            })
    
    # Summary
    print(f"\n{'='*50}")
    print(f"📊 EXTRACTION SUMMARY")
    print(f"  PDFs extracted:  {results['pdf_success']} success, {results['pdf_fail']} failed")
    print(f"  HTMLs extracted: {results['html_success']} success, {results['html_fail']} failed")
    print(f"  Total text:      {results['total_chars']:,} chars ({results['total_chars']//1000:,} KB)")
    print(f"  Output files:    {len(results['files'])}")
    print(f"  Output dir:      {OUTPUT_DIR}")
    
    # Write extraction manifest
    manifest_path = OUTPUT_DIR / "_extraction-manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"  Manifest:        {manifest_path}")
    
    # Show top 10 by word count
    print(f"\n📖 TOP 10 BY WORD COUNT:")
    for entry in sorted(results['files'], key=lambda x: x['words'], reverse=True)[:10]:
        print(f"  {entry['words']:>8,} words  {entry['cite_key'][:40]}")


if __name__ == '__main__':
    main()
