#!/usr/bin/env python3
"""
MERGE VIEWER — Monaco diff, normalized text, readable colors.
Less is more. Both full papers, side by side, every line visible.
"""
import os, re, json

DOCK = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock'

def read(f):
    with open(os.path.join(DOCK, f), 'r') as fh:
        return fh.read()

def extract_text(md):
    lines = md.split('\n')
    out, capture = [], False
    for line in lines:
        if line.startswith('## TEXT') or line.startswith("## PART A") or \
           line.startswith("## PART B") or line.startswith("## WATSON'S TEXT"):
            capture = True; continue
        if line.startswith("## SEAM POINT") or line.startswith("## JAY'S STUB"): continue
        if capture and (line.startswith('## CITATIONS') or
                        line.startswith('## STATUS') or
                        line.startswith('## MISSING')):
            capture = False; continue
        if capture and line.startswith('> **'): continue
        if capture and line.strip() == '---': continue
        if capture: out.append(line)
    return '\n'.join(out).strip()

# ── Build OUR text with section headers ──────────────────────────────
sections = [
    ("ABSTRACT",                                       'BULKHEAD-00_abstract.md'),
    ("INTRODUCTION",                                   'BULKHEAD-01_introduction.md'),
    ("OPERATIVE EKPHRASIS AND THE IMAGETEXT",          'BULKHEAD-02_operative-ekphrasis.md'),
    ("PROMPTING AS PERFORMANCE AND THICK DESCRIPTION", 'BULKHEAD-03_thick-description.md'),
    ("THE SHIELD AS PERFORMANCE AND PROCESS",          'BULKHEAD-04_shield-performance.md'),
    ("THE SHIELD AND THE NATURAL SIGN",                'BULKHEAD-05_shield-natural-sign.md'),
    ("THE SHIELD AS WORLDTEXT",                        'BULKHEAD-06_shield-as-worldtext.md'),
    ("CONCLUSION",                                     'BULKHEAD-07_conclusion.md'),
]

our_parts = []
for title, f in sections:
    text = extract_text(read(f))
    our_parts.append(f"=== {title} ===\n\n{text}")
our_full = "\n\n\n".join(our_parts)

# ── Build JAY's text with MATCHING section headers ───────────────────
jay_raw = read('00_PLIMSOLL-LINE/portugal-draft.md')

def norm(h):
    return re.sub(r'[^a-z ]', '', h.lower()).strip()

HMAP = {}
for title, _ in sections:
    HMAP[norm(title)] = title
HMAP[norm("the shield of achilles as performance and process")] = \
    "THE SHIELD AS PERFORMANCE AND PROCESS"
HMAP[norm("prompting as performance and thick description")] = \
    "PROMPTING AS PERFORMANCE AND THICK DESCRIPTION"

jay_lines = jay_raw.split('\n')
jay_parts = []
cur_title = None
cur_body = []
found = False

for line in jay_lines:
    n = norm(line.strip())
    if n in HMAP:
        if found and cur_title:
            jay_parts.append(f"=== {cur_title} ===\n\n" + '\n'.join(cur_body).strip())
        found = True
        cur_title = HMAP[n]
        cur_body = []
    elif n == "references":
        if found and cur_title:
            jay_parts.append(f"=== {cur_title} ===\n\n" + '\n'.join(cur_body).strip())
        found = True
        cur_title = "REFERENCES"
        cur_body = []
    elif found:
        cur_body.append(line)

if found and cur_title:
    jay_parts.append(f"=== {cur_title} ===\n\n" + '\n'.join(cur_body).strip())

jay_full = "\n\n\n".join(jay_parts)

# ── Generate HTML ────────────────────────────────────────────────────
html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>MERGE VIEWER</title>
    <style>
        html, body { margin:0; padding:0; height:100%; overflow:hidden;
                     font-family:monospace; background:#fff; color:#000; }
        #bar { height:44px; background:#000; color:#fff; display:flex;
               align-items:center; padding:0 16px; justify-content:space-between; }
        #bar .t { font-weight:900; font-size:14px; text-transform:uppercase;
                  letter-spacing:.06em; }
        #bar button { background:#fff; color:#000; border:0; padding:6px 14px;
                      font:inherit; font-size:11px; font-weight:900;
                      cursor:pointer; text-transform:uppercase; }
        #bar button:hover { opacity:.7; }
        .labels { display:flex; height:24px; border-bottom:2px solid #000;
                  font-weight:900; font-size:11px; text-transform:uppercase; }
        .labels > div { flex:1; display:flex; align-items:center;
                        justify-content:center; }
        .labels > div:first-child { border-right:2px solid #000; }
        #editor { height:calc(100% - 68px); width:100%; }

        /* Make diffs READABLE: light gray backgrounds, black text stays */
        .monaco-editor .line-insert,
        .monaco-editor .line-delete {
            background-color: transparent !important;
        }
        .monaco-editor .char-insert {
            background-color: #ccc !important;
        }
        .monaco-editor .char-delete {
            background-color: #eee !important;
            text-decoration: line-through;
        }
        /* Gutter markers */
        .monaco-editor .insert-sign {
            background-color: #000 !important;
        }
        .monaco-editor .delete-sign {
            background-color: #888 !important;
        }
    </style>
    <script>var require={paths:{'vs':'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'}};</script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs/loader.min.js"></script>
</head>
<body>
    <div id="bar">
        <div class="t">MERGE VIEWER</div>
        <div>
            <button onclick="saveLeft()">Save Left</button>
            <button onclick="saveRight()">Save Right</button>
        </div>
    </div>
    <div class="labels">
        <div>OUR BULKHEADS</div>
        <div>JAY'S DRAFT [EDITABLE]</div>
    </div>
    <div id="editor"></div>

    <script>
        var LEFT = __LEFT__;
        var RIGHT = __RIGHT__;
        var diffEditor;

        require(['vs/editor/editor.main'], function() {
            diffEditor = monaco.editor.createDiffEditor(
                document.getElementById('editor'), {
                    renderSideBySide: true,
                    enableSplitViewResizing: true,
                    wordWrap: 'on',
                    wrappingIndent: 'same',
                    ignoreTrimWhitespace: true,
                    theme: 'vs',
                    fontSize: 13,
                    lineHeight: 22,
                    minimap: { enabled: false },
                    readOnly: false,
                    originalEditable: true,
                    renderIndicators: true,
                    scrollBeyondLastLine: false
                }
            );
            diffEditor.setModel({
                original: monaco.editor.createModel(LEFT, 'plaintext'),
                modified: monaco.editor.createModel(RIGHT, 'plaintext')
            });
        });

        function dl(text, name) {
            var blob = new Blob([text], {type:'text/markdown'});
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = name;
            a.click();
        }
        function saveLeft() {
            dl(diffEditor.getModel().original.getValue(), 'BULKHEADS_EDITED.md');
        }
        function saveRight() {
            dl(diffEditor.getModel().modified.getValue(), 'JAY_EDITED.md');
        }
    </script>
</body>
</html>"""

html = html.replace('__LEFT__', json.dumps(our_full))
html = html.replace('__RIGHT__', json.dumps(jay_full))

out = os.path.join(DOCK, 'MERGE_VIEWER.html')
with open(out, 'w') as f:
    f.write(html)

print(f"Done. {os.path.getsize(out)//1024}KB")
print(f"  Left:  {len(our_full.splitlines())} lines")
print(f"  Right: {len(jay_full.splitlines())} lines")
