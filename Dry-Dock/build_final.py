#!/usr/bin/env python3
"""Build the final shipworthy HTML document from bulkhead markdown files."""
import re, os, base64

DOCK = os.path.dirname(os.path.abspath(__file__))

def read(f):
    with open(os.path.join(DOCK, f), 'r') as fh:
        return fh.read()

def extract_text(md):
    lines = md.split('\n')
    out, capture = [], False
    for line in lines:
        if line.startswith('## TEXT') or line.startswith("## PART A") or line.startswith("## PART B: WATSON") or line.startswith("## WATSON'S TEXT"):
            capture = True; continue
        if line.startswith("## SEAM POINT"): continue
        if capture and (line.startswith('## CITATIONS') or line.startswith('## STATUS') or line.startswith('## MISSING')): capture = False; continue
        if capture and line.startswith('> **'): continue
        if capture and line.strip() == '---': continue
        if capture: out.append(line)
    return '\n'.join(out).strip()

def img_b64(rel_path):
    full = os.path.join(DOCK, rel_path)
    if not os.path.exists(full): return None
    ext = full.split('.')[-1].lower()
    mime = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg'}.get(ext,'image/png')
    with open(full, 'rb') as f:
        return f'data:{mime};base64,{base64.b64encode(f.read()).decode()}'

def fig(rel_path, cap, fid):
    src = img_b64(rel_path)
    if src:
        return f'<figure id="{fid}"><img src="{src}" alt="{fid}"><figcaption>{cap}</figcaption></figure>'
    return f'<figure id="{fid}"><div class="ph">[IMAGE: {rel_path}]</div><figcaption>{cap}</figcaption></figure>'

def paras(text):
    blocks = re.split(r'\n\n+', text.strip())
    html = []
    for b in blocks:
        b = b.strip()
        if not b or b.startswith('> ') or b.startswith('- [') or b.startswith('#'): continue
        b = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', b)
        b = re.sub(r'\*(.+?)\*', r'<em>\1</em>', b)
        html.append(f'<p>{b}</p>')
    return '\n'.join(html)

# --- Extract ---
abstract = extract_text(read('BULKHEAD-00_abstract.md'))
intro = extract_text(read('BULKHEAD-01_introduction.md'))
ek = extract_text(read('BULKHEAD-02_operative-ekphrasis.md'))
thick = extract_text(read('BULKHEAD-03_thick-description.md'))
perf = extract_text(read('BULKHEAD-04_shield-performance.md'))
sign = extract_text(read('BULKHEAD-05_shield-natural-sign.md'))
world = extract_text(read('BULKHEAD-06_shield-as-worldtext.md'))
conc = extract_text(read('BULKHEAD-07_conclusion.md'))

# --- References ---
refs_raw = read('BULKHEAD-08_references.md')
ref_entries = []
for line in refs_raw.split('\n'):
    line = line.strip()
    if not line or line.startswith('#') or line.startswith('>') or line.startswith('---') or line.startswith('- ['):
        continue
    ref_entries.append(line)

refs_html = []
for r in ref_entries:
    r = re.sub(r'\*(.+?)\*', r'<em>\1</em>', r)
    refs_html.append(f'<p>{r}</p>')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Operative Ekphrasis: From Imagetext to Worldtext</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Inter:wght@400;500;600&display=swap');
:root { --t:#1a1a1a; --bg:#fff; --ac:#8b0000; --g:#555; --lt:#f7f6f3; --bd:#d0d0d0; }
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'EB Garamond',Georgia,serif;font-size:12pt;line-height:1.75;color:var(--t);background:var(--bg);max-width:40em;margin:0 auto;padding:2in 0}

/* Title */
.tb{text-align:center;margin-bottom:2.5em;page-break-after:always}
.tb h1{font-size:1.7em;font-weight:600;line-height:1.25;margin-bottom:.4em}
.tb .au{font-size:1.05em;margin:.2em 0}
.tb .af{font-size:.92em;color:var(--g);font-style:italic}

/* Sections */
section{margin-bottom:1.8em;position:relative}
h2{font-size:1.1em;font-weight:600;text-transform:uppercase;letter-spacing:.08em;margin:2em 0 .7em;border-bottom:1px solid var(--bd);padding-bottom:.2em}
h3{font-size:1em;font-weight:600;font-style:italic;margin:1.2em 0 .4em}
p{margin-bottom:.75em;text-align:justify;text-indent:1.5em}
section>p:first-of-type{text-indent:0}

/* Copy button */
.cpb{position:absolute;top:0;right:0;background:var(--lt);border:1px solid var(--bd);font-family:Inter,sans-serif;font-size:.65em;padding:3px 8px;cursor:pointer;color:var(--g);border-radius:3px;opacity:0;transition:opacity .2s}
section:hover .cpb{opacity:1}
.cpb:hover{background:#e8e6e1}

/* Figures */
figure{margin:1.5em auto;text-align:center;page-break-inside:avoid;max-width:85%}
figure img{max-width:100%;max-height:420px;height:auto;width:auto;object-fit:contain;border:1px solid #ddd}
figcaption{font-family:Inter,sans-serif;font-size:.78em;color:var(--g);margin-top:.5em;text-align:left;line-height:1.5;text-indent:0}
.fig-sm img{max-height:320px}

/* Jay placeholder */
.jp{border:2px dashed var(--ac);padding:1.2em;margin:1.5em auto;text-align:center;color:var(--ac);font-family:Inter,sans-serif;font-size:.82em;background:#fff8f8;max-width:85%;page-break-inside:avoid}

/* Appendix figures */
.appendix-fig{background:var(--lt);border:1px solid var(--bd);padding:1.2em;margin:1.2em 0;page-break-inside:avoid}
.appendix-fig h4{font-family:Inter,sans-serif;font-size:.8em;font-weight:600;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.6em;color:var(--t)}
.appendix-fig img{max-width:100%;max-height:350px;height:auto;width:auto;object-fit:contain;display:block;margin:0 auto .6em}
.appendix-fig p{text-indent:0;text-align:left;font-size:.88em;margin-bottom:.3em}
.appendix-fig .cap{font-family:Inter,sans-serif;font-size:.78em;color:var(--g);line-height:1.5}
.appendix-fig .ref{font-family:Inter,sans-serif;font-size:.72em;color:#888;font-style:italic}

/* Code block */
.code-fig{background:#f5f3ef;border:1px solid #ddd;padding:1em;font-family:'SF Mono',Consolas,monospace;font-size:.7em;overflow-x:auto;max-height:10em;text-align:left;margin:0 auto;max-width:85%;line-height:1.5}

/* References */
.refs p{text-indent:-2em;padding-left:2em;margin-bottom:.35em;font-size:.88em;text-align:left}

/* Print */
@media print{body{padding:0;font-size:11pt}.tb{page-break-after:always}h2{page-break-after:avoid}figure,.appendix-fig{page-break-inside:avoid}.cpb{display:none}}
@media screen{body{padding:1in 1.5em}}
</style>
</head>
<body>

<div class="tb">
<h1>Operative Ekphrasis:<br>From Imagetext to Worldtext</h1>
<div class="au">Jay David Bolter &amp; Watson Hartsoe</div>
<div class="af">Georgia Institute of Technology · Digital Media Program</div>
</div>

<section id="abstract">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>Abstract</h2>
''' + paras(abstract) + '''
</section>

<section id="s1">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>1. Introduction</h2>
''' + paras(intro) + '''
</section>

<section id="s2">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>2. Operative Ekphrasis and the Imagetext</h2>
''' + paras(ek) + '''
</section>

<section id="s3">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>3. Prompting as Performance and Thick Description</h2>
''' + paras(thick) + '''
</section>

<section id="s4">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>4. The Shield as Performance and Process</h2>
''' + paras(perf) + '''
</section>

<section id="s5">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>5. The Shield and the Natural Sign</h2>
''' + paras(sign) + '''
<div class="jp"><strong>⬚ Fig. 1</strong> — Jay to supply.<br>Gemini 3 Flash output from full Greek-language prompt of <em>Iliad</em> 18.478–608.</div>
<div class="jp"><strong>⬚ Fig. 2</strong> — Jay to supply.<br>Gemini 3 Flash output from vineyard passage (18.561–572) in Greek.</div>
</section>

<section id="s6">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>6. The Shield as Worldtext</h2>
''' + paras(world) + '''
</section>

<section id="s7">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>7. Conclusion: Where Ekphrasis No Longer Ends</h2>
''' + paras(conc) + '''
</section>

<!-- ===== PLATE A ===== -->
<section id="plate-a">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>Plate A — The Compiled Workflow</h2>
<p style="text-indent:0;font-style:italic;font-size:.92em;color:var(--g)">Three states of ACHILLES // OPTICAL_GRID v10 (Hartsoe, 2025). The interface partitions Homer's shield into five textual zones and maps them onto a UV-wrapped spherical cap, demonstrating that the prompt is the entire compilation graph—not a sentence. See §3 and §6.</p>

''' + fig('CARGO/GRID/ACHILLES_SCENE_PHOTO_1772285420283.png',
  'Fig. A1. Watson Hartsoe, <em>ACHILLES // OPTICAL_GRID v10</em>, 2025. Homer, <em>Iliad</em> 18.478–608 (Buckley, 1851), UV-mapped as navigable texture. Five zones (CORE–RIM) inscribed into geometry. The Homeric text functions as both source code and visual surface.',
  'fig-a1') + '''

''' + fig('CARGO/GRID/ACHILLES_SCENE_PHOTO_1772278568713.png',
  'Fig. A2. Zone selection. Cyan boundary isolates the MIDDLE zone (Il. 18.541–572). A pointer raycast extracts a stochastic micro-spec of 5–8 contiguous words, wrapped with material constraints (SCENE OPTIMIZED / NO TEXT), and compiled as input to Imagen 3.0.',
  'fig-a2') + '''

''' + fig('CARGO/GRID/ACHILLES_SCENE_PHOTO_1772277387786.png',
  'Fig. A3. Fully populated shield. Generated patches diegetically forged—stamped, feathered, baked—into the live WebGL texture atlas. Each zone\'s imagery was generated from a micro-spec extraction. The compositing creates persistent world texture that subsequent operations inherit.',
  'fig-a3') + '''
</section>

<!-- ===== PLATE B ===== -->
<section id="plate-b">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>Plate B — Neurosymbolic Resonance</h2>
<p style="text-indent:0;font-style:italic;font-size:.92em;color:var(--g)">The same Homeric text compiles into both deterministic animation code (B-flix) and probabilistic imagery (Gemini), demonstrating that the prompt can act as both surface and structure. See §6.</p>

<figure id="fig-b1" class="fig-sm">
<div class="code-fig">; @ICARO-PRO v1.0
; @FRAMES 85
; @GRID 128x96
; @GENERATED 2026-05-04T18:07:59.012Z
C FRAME 1
CLR 2
PNT 0 0 128 1 0
PNT 2 2 62 1 1
PNT 64 2 1 1 5
PNT 65 2 61 1 1
…
<em>; 41,477 lines · 666,798 bytes · 85 frames</em></div>
<figcaption>Fig. B1. Watson Hartsoe, "The Shield of Achilles," B-flix macro, 2026. BEFLIX-128 animation code compiled by Gemini from Homer, <em>Iliad</em> 18.478–608 (Buckley, 1851). Each <code>PNT</code> instruction specifies a pixel run at exact coordinates—the deterministic channel of the neurosymbolic pair.</figcaption>
</figure>

''' + fig('HOLD/00-the-shield-ABC_SHEET_85f.png',
  'Fig. B2. Watson Hartsoe, "The Shield of Achilles," ABC-Flix contact sheet, 2026. 85 frames rendered from B-flix code by the ABC-Flix engine (Hartsoe, 2024). Every pixel determined by the code. No probabilistic inference.',
  'fig-b2') + '''

''' + fig('HOLD/00-the-shield.png',
  'Fig. B3. Watson Hartsoe, "The Shield of Achilles," vision model refinement, 2026. The contact sheet (Fig. B2) submitted to Gemini as a visual prompt. Same 85-frame structure and construction-order sequence preserved—the deterministic grid translated into materially rich imagery. The contact sheet <em>is</em> the prompt.',
  'fig-b3') + '''
</section>

<!-- ===== APPENDIX: ON-DECK FIGURES ===== -->
<section id="appendix">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>Appendix — Supplementary Figures</h2>
<p style="text-indent:0;font-style:italic;font-size:.92em;color:var(--g)">Additional empirical assets staged for potential inline use. Each figure includes its caption, source, and the section it would support.</p>

<div class="appendix-fig">
<h4>Fig. S1 — Sora Shield Synthesis</h4>
''' + (f'<img src="{img_b64("CARGO/frames1/frame_011.jpg")}" alt="Sora contact sheet">' if img_b64("CARGO/frames1/frame_011.jpg") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">Sora-generated shield sequence. The contact sheet format reveals the temporal structure of the prompt: each frame is a diagnostic return, not a final product. Thick prompting is visible in the iterative workflow, not in sentence length.</p>
<p class="ref">Supports §3 — "The image is not the product. The image is feedback."</p>
</div>

<div class="appendix-fig">
<h4>Fig. S2 — Seedance First-Person Vineyard</h4>
''' + (f'<img src="{img_b64("CARGO/frames2/frame_014.jpg")}" alt="Seedance first-person">' if img_b64("CARGO/frames2/frame_014.jpg") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">First-person vineyard scene generated from the Dual Sensorium POML prompt via Seedance. The embedded inhabitant perspective breaks through platform realism into embodied point-of-view—a result that standard prompting cannot produce.</p>
<p class="ref">Supports §5 — "we focused on the vineyard scene (18.561–572)."</p>
</div>

<div class="appendix-fig">
<h4>Fig. S3 — Genie 3 Navigable World</h4>
''' + (f'<img src="{img_b64("CARGO/frames2/frame_027.jpg")}" alt="Genie 3 world">' if img_b64("CARGO/frames2/frame_027.jpg") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">Genie 3 navigable environment generated from a shield-derived prompt. The ekphrastic object becomes habitable: the image model yields to the world model. The user can enter and move through the scene.</p>
<p class="ref">Supports §6 — "Google DeepMind with its Genie series… offering generative platforms through which a user can bring forth their own 3D world."</p>
</div>

<div class="appendix-fig">
<h4>Fig. S4 — Mall Surveillance Feed</h4>
''' + (f'<img src="{img_b64("CARGO/frames2/frame_023.jpg")}" alt="Mall surveillance">' if img_b64("CARGO/frames2/frame_023.jpg") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">AI-generated shopping mall as surveillance feed, produced from a shield-zone prompt remapped to a contemporary commercial interior. The shield's concentric zone architecture (Cosmos → Peace City → War City → Vineyard → Pasture → Dance → Oceanus) survives translation into CCTV grid composition—demonstrating that the structural rules are deeper than the surface.</p>
<p class="ref">Supports §7 — "The politics of a worldtext will appear not in its explicit content but in its affordances."</p>
</div>

<div class="appendix-fig">
<h4>Fig. S5 — OPTICAL_GRID: Text-as-World</h4>
''' + (f'<img src="{img_b64("CARGO/GRID/ACHILLES_SCENE_1773093492834.png")}" alt="Optical Grid text world">' if img_b64("CARGO/GRID/ACHILLES_SCENE_1773093492834.png") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">Rotated view of the OPTICAL_GRID showing the Homeric text wrapping the shield's equatorial band. The Dance Court zone is visible with generated imagery composited over the Buckley translation. Text and image coexist on the same surface—the literal imagetext.</p>
<p class="ref">Supports §6 — "The prompt becomes the image, but the same prompt also acts as the code to make the image."</p>
</div>

<div class="appendix-fig">
<h4>Fig. S6 — OPTICAL_GRID: UV Text Overlay</h4>
''' + (f'<img src="{img_b64("CARGO/GRID/ACHILLES_SCENE_PHOTO_1772276368381.png")}" alt="Optical Grid UV overlay">' if img_b64("CARGO/GRID/ACHILLES_SCENE_PHOTO_1772276368381.png") else '<div class="ph">[IMAGE]</div>') + '''
<p class="cap">Full shield with UV text overlay visible. The concentric zone grid (gold target pattern at center) governs which Homeric passages are available for extraction at any coordinate. The yellow rings are the selection grammar; the cyan boundary is the Oceanus rim.</p>
<p class="ref">Supports §6 — "the shield's structure matters more than its surface."</p>
</div>
</section>

<!-- ===== REFERENCES ===== -->
<section id="references" class="refs">
<button class="cpb" onclick="copySection(this)">Copy §</button>
<h2>References</h2>
''' + '\n'.join(refs_html) + '''
</section>

<script>
function copySection(btn){
  const sec = btn.parentElement;
  const range = document.createRange();
  range.selectNodeContents(sec);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  document.execCommand('copy');
  btn.textContent = 'Copied ✓';
  setTimeout(() => { btn.textContent = 'Copy §'; sel.removeAllRanges(); }, 1500);
}
// Copy-all button
const ca = document.createElement('button');
ca.textContent = 'Copy Entire Paper';
ca.style.cssText = 'position:fixed;bottom:1em;right:1em;font-family:Inter,sans-serif;font-size:.75em;padding:8px 14px;background:#1a1a1a;color:#fff;border:none;border-radius:4px;cursor:pointer;z-index:999;opacity:.7';
ca.onmouseover = () => ca.style.opacity = '1';
ca.onmouseout = () => ca.style.opacity = '.7';
ca.onclick = () => {
  const r = document.createRange();
  r.selectNodeContents(document.body);
  const s = window.getSelection();
  s.removeAllRanges(); s.addRange(r);
  document.execCommand('copy');
  ca.textContent = 'Copied ✓';
  setTimeout(() => { ca.textContent = 'Copy Entire Paper'; s.removeAllRanges(); }, 2000);
};
document.body.appendChild(ca);
</script>
</body>
</html>'''

out = os.path.join(DOCK, 'FINAL_SHIPWORTHY.html')
with open(out, 'w') as f:
    f.write(html)
print(f"Written: {out}")
print(f"Size: {len(html):,} bytes")
