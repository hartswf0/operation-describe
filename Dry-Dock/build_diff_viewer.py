import os, re, json

DOCK = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock'

def read(f):
    with open(os.path.join(DOCK, f), 'r') as fh:
        return fh.read()

def extract_text(md):
    lines = md.split('\n')
    out, capture = [], False
    for line in lines:
        if line.startswith('## TEXT') or line.startswith("## PART A") or line.startswith("## PART B") or line.startswith("## WATSON'S TEXT"):
            capture = True; continue
        if line.startswith("## SEAM POINT") or line.startswith("## JAY'S STUB"): continue
        if capture and (line.startswith('## CITATIONS') or line.startswith('## STATUS') or line.startswith('## MISSING')): capture = False; continue
        if capture and line.startswith('> **'): continue
        if capture and line.strip() == '---': continue
        if capture: out.append(line)
    return '\n'.join(out).strip()

# Build our text
sections = [
    ("Abstract", 'BULKHEAD-00_abstract.md'),
    ("Introduction", 'BULKHEAD-01_introduction.md'),
    ("Operative Ekphrasis and the Imagetext", 'BULKHEAD-02_operative-ekphrasis.md'),
    ("Prompting as Performance and Thick Description", 'BULKHEAD-03_thick-description.md'),
    ("The Shield as Performance and Process", 'BULKHEAD-04_shield-performance.md'),
    ("The Shield and the Natural Sign", 'BULKHEAD-05_shield-natural-sign.md'),
    ("The Shield as Worldtext", 'BULKHEAD-06_shield-as-worldtext.md'),
    ("Conclusion", 'BULKHEAD-07_conclusion.md'),
]

our_parts = []
for title, f in sections:
    text = extract_text(read(f))
    our_parts.append(f"{title}\n\n{text}")

our_full_text = "\n\n".join(our_parts)

# Read Jay's text
jay_full_text = read('00_PLIMSOLL-LINE/portugal-draft.md')

html_template = """<!DOCTYPE html>
<html>
<head>
    <title>Manuscript Diff Viewer</title>
    <style>
        html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: system-ui, -apple-system, sans-serif; background: #1e1e1e; }
        #header { height: 60px; background: #252526; color: white; display: flex; align-items: center; padding: 0 20px; justify-content: space-between; border-bottom: 1px solid #333; }
        #container { height: calc(100% - 90px); width: 100%; }
        .title { font-weight: 600; font-size: 18px; display: flex; align-items: center; gap: 10px; }
        .badge { background: #8b0000; color: white; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .labels { display: flex; width: 100%; box-sizing: border-box; background: #1e1e1e; color: #9cdcfe; font-size: 13px; height: 30px; align-items: center; border-bottom: 1px solid #333; font-family: monospace; }
        .labels > div { flex: 1; padding: 0 20px; }
        .labels > div:last-child { border-left: 1px solid #333; color: #ce9178; }
    </style>
    <script>var require = { paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.39.0/min/vs' } };</script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.39.0/min/vs/loader.min.js"></script>
</head>
<body>
    <div id="header">
        <div class="title">
            <span class="badge">CRITICAL REVIEW</span>
            Manuscript Diff Viewer
        </div>
        <div style="font-size: 13px; color: #aaa;">Review before 5pm sync</div>
    </div>
    <div class="labels">
        <div>← ORIGINAL: Our Final Assembly (Bulkheads 00-07)</div>
        <div>MODIFIED: Jay's Portugal Draft (portugal-draft.md) →</div>
    </div>
    <div id="container"></div>

    <script>
        const originalText = __ORIGINAL_TEXT__;
        const modifiedText = __MODIFIED_TEXT__;

        require(['vs/editor/editor.main'], function() {
            var diffEditor = monaco.editor.createDiffEditor(document.getElementById('container'), {
                enableSplitViewResizing: true,
                renderSideBySide: true,
                wordWrap: 'on',
                ignoreTrimWhitespace: false,
                theme: 'vs-dark',
                fontSize: 14,
                lineHeight: 24,
                minimap: { enabled: true }
            });

            diffEditor.setModel({
                original: monaco.editor.createModel(originalText, 'markdown'),
                modified: monaco.editor.createModel(modifiedText, 'markdown')
            });
        });
    </script>
</body>
</html>"""

html_content = html_template.replace('__ORIGINAL_TEXT__', json.dumps(our_full_text)).replace('__MODIFIED_TEXT__', json.dumps(jay_full_text))

with open(os.path.join(DOCK, 'DIFF_VIEWER.html'), 'w') as f:
    f.write(html_content)

print("Diff viewer generated at DIFF_VIEWER.html")
