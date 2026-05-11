#!/usr/bin/env python3
"""
Gemini Frame Extractor v7 — LLM-Annotated + Gradient-Snapped Grid.

Each sheet is manually annotated with its column count and approximate
row count. The extractor then snaps each grid line to the strongest
gradient peak near the expected position. Auto-trims and pads each cell.

Manual annotations based on visual inspection of each image:
- 00: 5 cols, diamond tiles on white bg, ~17 rows, title top-left
- 01: 5 cols, circular medallions on parchment, ~18 rows, title block top-left
- 02: 5 cols, rectangular on white, ~13 rows, title top-left
- 03: 5 cols, comic panels on dark bg, ~17 rows, title top-left
- 04: 5 cols, rectangular on dark bg, ~17 rows, title top-left
- 05: 5 cols, rectangular on dark bg, ~18 rows, title top-left
"""
import os, json
import numpy as np
from PIL import Image
import imageio

HOLD = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock/HOLD'
FLIPBOOKS = os.path.join(HOLD, 'flipbooks')

# Manual annotations: cols, expected_rows, skip_title_cell
SHEETS = [
    {'id': '00', 'cols': 5, 'rows': 17, 'skip_title': True,
     'file': '00-the-shield.png', 'dir': '00-whole-shield-gemini'},
    {'id': '01', 'cols': 5, 'rows': 18, 'skip_title': True,
     'file': '01-Construction-and-Cosmic-Design/01-cosmic-gemini.png', 'dir': '01-cosmic-gemini'},
    {'id': '02', 'cols': 5, 'rows': 13, 'skip_title': True,
     'file': '02-Two-Cities-Peace-and-Law/02-bride-law-Gemini_Generated_Image_6oi6ce6oi6ce6oi6.jpeg', 'dir': '02-peace-law-gemini'},
    {'id': '03', 'cols': 5, 'rows': 17, 'skip_title': True,
     'file': '03-Two-Cities-War-and-Ambush/Gemini_Generated_Image_2ylbjn2ylbjn2ylb.jpeg', 'dir': '03-war-ambush-gemini'},
    {'id': '04', 'cols': 5, 'rows': 17, 'skip_title': True,
     'file': '04-Labors-of-the-Field/Gemini_Generated_Image_ffbktcffbktcffbk.jpeg', 'dir': '04-labors-gemini'},
    {'id': '05', 'cols': 5, 'rows': 18, 'skip_title': True,
     'file': '05-Cattle-Lions-and-Sheep/Gemini_Generated_Image_5kxfd95kxfd95kxf.jpeg', 'dir': '05-cattle-gemini'},
]


def snap_grid(img_path, expected_cols, expected_rows):
    """Find grid lines by snapping to strongest gradient near expected positions."""
    img = Image.open(img_path).convert('L')
    W, H = img.size
    arr = np.array(img, dtype=float)
    
    # Column gradient (vertical edges)
    col_grad = np.abs(np.diff(arr, axis=1)).mean(axis=0)
    cell_w = W / expected_cols
    search_w = int(cell_w * 0.15)
    
    x_lines = []
    for i in range(1, expected_cols):
        cx = int(i * cell_w)
        lo = max(0, cx - search_w)
        hi = min(len(col_grad), cx + search_w)
        best = lo + int(np.argmax(col_grad[lo:hi]))
        x_lines.append(best)
    
    # Row gradient (horizontal edges)
    row_grad = np.abs(np.diff(arr, axis=0)).mean(axis=1)
    cell_h = H / expected_rows
    search_h = int(cell_h * 0.2)
    
    y_lines = []
    for i in range(1, expected_rows):
        cy = int(i * cell_h)
        lo = max(0, cy - search_h)
        hi = min(len(row_grad), cy + search_h)
        best = lo + int(np.argmax(row_grad[lo:hi]))
        y_lines.append(best)
    
    xs = [0] + x_lines + [W]
    ys = [0] + y_lines + [H]
    return xs, ys


def auto_trim_cell(img, padding=2):
    """Trim border pixels matching the outer ring color."""
    arr = np.array(img.convert('L'), dtype=float)
    H, W = arr.shape
    if H < 10 or W < 10:
        return img
    
    ring = np.concatenate([arr[0:3,:].ravel(), arr[-3:,:].ravel(),
                           arr[:,0:3].ravel(), arr[:,-3:].ravel()])
    bg = np.median(ring)
    mask = np.abs(arr - bg) > 20
    
    if not mask.any():
        return img
    
    rows_any = mask.any(axis=1)
    cols_any = mask.any(axis=0)
    if not rows_any.any() or not cols_any.any():
        return img
    
    y0 = max(0, int(np.argmax(rows_any)) - padding)
    y1 = min(H, int(H - np.argmax(rows_any[::-1])) + padding)
    x0 = max(0, int(np.argmax(cols_any)) - padding)
    x1 = min(W, int(W - np.argmax(cols_any[::-1])) + padding)
    
    if x1 - x0 < 8 or y1 - y0 < 8:
        return img
    return img.crop((x0, y0, x1, y1))


def process(spec):
    path = os.path.join(HOLD, spec['file'])
    if not os.path.exists(path):
        print(f'  ⚠ SKIP: {spec["file"]}')
        return 0
    
    img = Image.open(path).convert('RGB')
    W, H = img.size
    
    xs, ys = snap_grid(path, spec['cols'], spec['rows'])
    cols = len(xs) - 1
    rows = len(ys) - 1
    
    out = os.path.join(FLIPBOOKS, spec['dir'])
    os.makedirs(os.path.join(out, 'frames'), exist_ok=True)
    
    # Check column widths
    cw = [xs[i+1]-xs[i] for i in range(cols)]
    ch = [ys[i+1]-ys[i] for i in range(rows)]
    print(f'  {W}×{H} → {cols}c × {rows}r = {cols*rows} cells')
    print(f'  Col widths: {cw}')
    print(f'  Row heights range: {min(ch)}-{max(ch)}')
    
    manifest = []
    idx = 0
    
    for r in range(rows):
        for c in range(cols):
            if spec['skip_title'] and r == 0 and c == 0:
                continue
            
            crop = img.crop((xs[c], ys[r], xs[c+1], ys[r+1]))
            trimmed = auto_trim_cell(crop, padding=2)
            
            tw, th = trimmed.size
            sz = max(tw, th)
            sq = Image.new('RGB', (sz, sz), (255, 255, 255))
            sq.paste(trimmed, ((sz-tw)//2, (sz-th)//2))
            
            frame_path = os.path.join(out, 'frames', f'frame_{idx:03d}.png')
            sq.save(frame_path)
            manifest.append({'index': idx, 'bbox': [int(xs[c]),int(ys[r]),int(xs[c+1]),int(ys[r+1])],
                             'path': f'frames/frame_{idx:03d}.png'})
            idx += 1
    
    # Clean stale frames
    for f in os.listdir(os.path.join(out, 'frames')):
        if f.startswith('frame_'):
            n = int(f.split('_')[1].split('.')[0])
            if n >= idx:
                os.remove(os.path.join(out, 'frames', f))
    
    with open(os.path.join(out, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    return idx


def export(outdir, n, name):
    out = os.path.join(FLIPBOOKS, outdir)
    if n < 1:
        return
    os.system(f'ffmpeg -y -framerate 6 -i "{out}/frames/frame_%03d.png" '
              f'-vf "scale=512:512:flags=lanczos" '
              f'-c:v libx264 -pix_fmt yuv420p -crf 18 "{out}/flipbook.mp4" 2>/dev/null')
    
    frames = []
    for i in range(n):
        im = Image.open(os.path.join(out, 'frames', f'frame_{i:03d}.png'))
        im = im.resize((256, 256), Image.LANCZOS)
        frames.append(np.array(im))
    imageio.mimsave(os.path.join(out, 'flipbook.gif'), frames, duration=167, loop=0)
    
    html = f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>GEMINI — {name}</title>
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#0a0a0f;color:#e0e0d8;font-family:monospace;height:100vh;display:flex;flex-direction:column}}.hdr{{background:#1a1a1a;color:#c9a84c;padding:10px 16px;font-size:11px;font-weight:900;text-transform:uppercase;border-bottom:2px solid #333}}.main{{flex:1;display:flex;overflow:hidden}}.view{{flex:1;display:flex;align-items:center;justify-content:center;position:relative}}.view img{{max-width:90%;max-height:90%}}.info{{position:absolute;bottom:8px;left:8px;font-size:10px;font-weight:900;background:#c9a84c;color:#000;padding:3px 8px}}.side{{flex:0 0 260px;display:flex;flex-direction:column;border-left:2px solid #333}}.ctrl{{padding:10px;border-bottom:2px solid #333}}.ctrl label{{font-size:9px;font-weight:900;text-transform:uppercase;display:block;margin-bottom:4px;color:#c9a84c}}.ctrl input[type=range]{{width:100%}}.btns{{display:flex;gap:4px;margin-top:6px}}.btns button{{flex:1;padding:8px;background:#c9a84c;color:#000;border:0;font:inherit;font-size:10px;font-weight:900;cursor:pointer}}.grid{{flex:1;overflow-y:auto;display:grid;grid-template-columns:repeat(5,1fr);gap:1px;padding:1px;background:#333}}.grid img{{width:100%;display:block;cursor:pointer;background:#111}}.grid img.on{{outline:2px solid #c9a84c}}</style></head><body>
<div class="hdr">{name} — {n} FRAMES (v7)</div>
<div class="main"><div class="view"><img id="big" src="frames/frame_000.png"><div class="info" id="lbl">0/{n-1}</div></div>
<div class="side"><div class="ctrl"><label>Frame <span id="fn">0</span>/{n-1}</label><input type="range" id="s" min="0" max="{n-1}" value="0"><div class="btns"><button onclick="prev()">◀</button><button id="pb" onclick="tp()">▶</button><button onclick="next()">▶</button></div></div>
<div class="grid" id="g"></div></div></div>
<script>var N={n},c=0,p=false,t=null,g=document.getElementById('g');for(var i=0;i<N;i++){{var m=document.createElement('img');m.src='frames/frame_'+String(i).padStart(3,'0')+'.png';m.dataset.i=i;m.onclick=function(){{go(+this.dataset.i)}};g.appendChild(m)}}function go(i){{c=Math.max(0,Math.min(N-1,i));document.getElementById('big').src='frames/frame_'+String(c).padStart(3,'0')+'.png';document.getElementById('s').value=c;document.getElementById('fn').textContent=c;document.getElementById('lbl').textContent=c+'/'+(N-1);g.querySelectorAll('img').forEach(function(x,j){{x.classList.toggle('on',j===c)}});if(g.children[c])g.children[c].scrollIntoView({{block:'nearest'}})}}function next(){{go(c+1)}}function prev(){{go(c-1)}}function tp(){{p=!p;document.getElementById('pb').textContent=p?'⏸':'▶';if(p)t=setInterval(function(){{if(c>=N-1)go(0);else next()}},150);else clearInterval(t)}}document.getElementById('s').oninput=function(){{go(+this.value)}};document.onkeydown=function(e){{if(e.key==='ArrowRight')next();if(e.key==='ArrowLeft')prev();if(e.key===' '){{e.preventDefault();tp()}}}};go(0);</script></body></html>'''
    with open(os.path.join(out, 'flipbook_viewer.html'), 'w') as f:
        f.write(html)


# ── MAIN ──
counts = {}
for spec in SHEETS:
    print(f'\n[{spec["id"]}] {spec["dir"]}:')
    n = process(spec)
    if n > 0:
        export(spec['dir'], n, spec['dir'])
        print(f'  ✓ {n} frames → MP4 + GIF + viewer')
    counts[spec['dir']] = n

print('\n=== FOR index.html ===')
for d, n in counts.items():
    print(f'  {d}: {n}')
