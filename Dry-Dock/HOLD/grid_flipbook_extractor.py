#!/usr/bin/env python3
"""
Grid Flipbook Extractor — cuts contact sheets into ordered frames,
exports MP4 + GIF + HTML viewer.

Theory: <contact-sheet> [grid-detect] → <frames> [order] → <flipbook>
"""
import os, sys, json, glob, argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HOLD = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock/HOLD'

def detect_grid(img, expected_cols=5, expected_rows=17):
    """Detect grid centers by column/row projection on non-white pixels."""
    arr = np.array(img.convert('L'))
    # Threshold: anything darker than 240 is content
    mask = (arr < 240).astype(np.float32)
    
    col_proj = mask.sum(axis=0)  # sum each column
    row_proj = mask.sum(axis=1)  # sum each row
    
    # Find peaks by binning
    W, H = img.size
    col_bin = W // expected_cols
    row_bin = H // expected_rows
    
    x_centers = []
    for c in range(expected_cols):
        start = c * col_bin
        end = min((c + 1) * col_bin, W)
        segment = col_proj[start:end]
        peak = start + int(np.argmax(segment))
        x_centers.append(start + col_bin // 2)
    
    y_centers = []
    for r in range(expected_rows):
        start = r * row_bin
        end = min((r + 1) * row_bin, H)
        segment = row_proj[start:end]
        peak = start + int(np.argmax(segment))
        y_centers.append(start + row_bin // 2)
    
    return x_centers, y_centers, col_bin, row_bin

def extract_frames(img_path, out_dir, skip_title=True):
    """Extract frames from a contact sheet. Returns list of frame paths + manifest."""
    img = Image.open(img_path)
    W, H = img.size
    
    # Try to detect grid
    # Heuristic: estimate rows from aspect ratio and frame count in filename
    fname = os.path.basename(img_path)
    # Try to get frame count from filename (e.g., "85f" or "60f")
    import re
    m = re.search(r'(\d+)f', fname)
    if m:
        total = int(m.group(1))
    else:
        total = 85  # default guess
    
    # Estimate grid: ~5 cols is typical for ABC-Flix sheets
    cols = 5
    rows = (total + cols - 1) // cols + (1 if skip_title else 0)
    
    x_centers, y_centers, cw, rh = detect_grid(img, cols, rows)
    
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(os.path.join(out_dir, 'frames'), exist_ok=True)
    
    manifest = []
    idx = 0
    
    for r, yc in enumerate(y_centers):
        for c, xc in enumerate(x_centers):
            if skip_title and r == 0 and c == 0:
                continue  # skip title cell
            
            x1 = max(0, xc - cw // 2)
            y1 = max(0, yc - rh // 2)
            x2 = min(W, xc + cw // 2)
            y2 = min(H, yc + rh // 2)
            
            crop = img.crop((x1, y1, x2, y2))
            
            # Pad to square
            sz = max(crop.size)
            sq = Image.new('RGB', (sz, sz), (255, 255, 255))
            ox = (sz - crop.size[0]) // 2
            oy = (sz - crop.size[1]) // 2
            sq.paste(crop, (ox, oy))
            
            frame_path = os.path.join(out_dir, 'frames', f'frame_{idx:03d}.png')
            sq.save(frame_path)
            
            manifest.append({
                'index': idx,
                'row': r,
                'col': c,
                'bbox': [x1, y1, x2, y2],
                'path': f'frames/frame_{idx:03d}.png'
            })
            idx += 1
    
    # Save manifest
    with open(os.path.join(out_dir, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    return manifest, img

def export_mp4(out_dir, manifest, fps=8):
    """Export MP4 from extracted frames using ffmpeg."""
    frame_list = os.path.join(out_dir, 'frames', 'frame_%03d.png')
    mp4_path = os.path.join(out_dir, 'flipbook.mp4')
    
    cmd = (f'ffmpeg -y -framerate {fps} -i "{frame_list}" '
           f'-vf "scale=384:384:flags=neighbor" '
           f'-c:v libx264 -pix_fmt yuv420p -crf 18 "{mp4_path}"')
    os.system(cmd)
    return mp4_path

def export_gif(out_dir, manifest, fps=8):
    """Export GIF from extracted frames."""
    import imageio
    frames = []
    for m in manifest:
        img = Image.open(os.path.join(out_dir, m['path']))
        img = img.resize((256, 256), Image.NEAREST)
        frames.append(np.array(img))
    
    gif_path = os.path.join(out_dir, 'flipbook.gif')
    imageio.mimsave(gif_path, frames, duration=1000//fps, loop=0)
    return gif_path

def build_viewer(out_dir, manifest, sheet_name):
    """Build brutalist HTML flipbook viewer."""
    n = len(manifest)
    html = f'''<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<title>SHIELD FLIPBOOK — {sheet_name}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#fff;color:#000;font-family:ui-monospace,monospace;height:100vh;display:flex;flex-direction:column}}
.hdr{{background:#000;color:#fff;padding:10px 16px;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.06em;display:flex;justify-content:space-between;align-items:center}}
.hdr .sub{{font-size:9px;opacity:.6}}
.main{{flex:1;display:flex;overflow:hidden}}
.view{{flex:1;display:flex;align-items:center;justify-content:center;background:#f5f5f5;border-right:2px solid #000;position:relative}}
.view img{{max-width:90%;max-height:90%;image-rendering:pixelated}}
.info{{position:absolute;bottom:8px;left:8px;font-size:10px;font-weight:900;background:#000;color:#fff;padding:3px 8px}}
.side{{flex:0 0 280px;display:flex;flex-direction:column;overflow:hidden}}
.ctrl{{padding:10px;border-bottom:2px solid #000}}
.ctrl label{{font-size:9px;font-weight:900;text-transform:uppercase;display:block;margin-bottom:4px}}
.ctrl input[type=range]{{width:100%;margin:4px 0}}
.ctrl .btns{{display:flex;gap:4px;margin-top:6px}}
.ctrl button{{flex:1;padding:8px;background:#000;color:#fff;border:0;font:inherit;font-size:10px;font-weight:900;cursor:pointer;text-transform:uppercase}}
.ctrl button:hover{{opacity:.7}}
.grid{{flex:1;overflow-y:auto;display:grid;grid-template-columns:repeat(5,1fr);gap:1px;padding:1px;background:#000}}
.grid img{{width:100%;display:block;cursor:pointer;background:#fff;transition:opacity .1s}}
.grid img:hover{{opacity:.7}}
.grid img.on{{outline:3px solid #000;outline-offset:-3px}}
</style>
</head><body>
<div class="hdr">
<span>SHIELD FLIPBOOK — {sheet_name} — {n} FRAMES</span>
<span class="sub">Arrow keys · Space = play · Click thumbnail</span>
</div>
<div class="main">
<div class="view">
<img id="big" src="frames/frame_000.png" alt="Frame">
<div class="info" id="lbl">FRAME 0 / {n-1}</div>
</div>
<div class="side">
<div class="ctrl">
<label>Frame <span id="fnum">0</span> / {n-1}</label>
<input type="range" id="scrub" min="0" max="{n-1}" value="0">
<div class="btns">
<button onclick="prev()">◀ PREV</button>
<button id="playBtn" onclick="togglePlay()">▶ PLAY</button>
<button onclick="next()">NEXT ▶</button>
</div>
</div>
<div class="grid" id="grid"></div>
</div>
</div>
<script>
var N={n},cur=0,playing=false,timer=null;
var grid=document.getElementById('grid');
for(var i=0;i<N;i++){{
  var img=document.createElement('img');
  img.src='frames/frame_'+String(i).padStart(3,'0')+'.png';
  img.dataset.i=i;
  img.addEventListener('click',function(){{go(parseInt(this.dataset.i))}});
  grid.appendChild(img);
}}
function go(i){{
  cur=Math.max(0,Math.min(N-1,i));
  document.getElementById('big').src='frames/frame_'+String(cur).padStart(3,'0')+'.png';
  document.getElementById('scrub').value=cur;
  document.getElementById('fnum').textContent=cur;
  document.getElementById('lbl').textContent='FRAME '+cur+' / '+(N-1);
  grid.querySelectorAll('img').forEach(function(x){{x.classList.remove('on')}});
  grid.children[cur].classList.add('on');
  grid.children[cur].scrollIntoView({{block:'nearest'}});
}}
function next(){{go(cur+1)}}
function prev(){{go(cur-1)}}
function togglePlay(){{
  playing=!playing;
  document.getElementById('playBtn').textContent=playing?'⏸ STOP':'▶ PLAY';
  if(playing)timer=setInterval(function(){{if(cur>=N-1){{togglePlay();return}}next()}},125);
  else clearInterval(timer);
}}
document.getElementById('scrub').addEventListener('input',function(){{go(parseInt(this.value))}});
document.addEventListener('keydown',function(e){{
  if(e.key==='ArrowRight')next();
  if(e.key==='ArrowLeft')prev();
  if(e.key===' '){{e.preventDefault();togglePlay()}}
}});
go(0);
</script>
</body></html>'''
    
    path = os.path.join(out_dir, 'flipbook_viewer.html')
    with open(path, 'w') as f:
        f.write(html)
    return path

# ── MAIN ──────────────────────────────────────────────────────────────
SHEETS = [
    ('00-the-shield-ABC_SHEET_85f.png', '00-whole-shield', True),
    ('01-Construction-and-Cosmic-Design/01-cosmic-design.png', '01-cosmic', True),
    ('02-Two-Cities-Peace-and-Law/ABC_SHEET_60f (2).png', '02-peace-law', True),
    ('03-Two-Cities-War-and-Ambush/ABC_SHEET_78f.png', '03-war-ambush', True),
    ('04-Labors-of-the-Field/ABC_SHEET_76f.png', '04-labors', True),
    ('05-Cattle-Lions-and-Sheep/05-cattle-and-lions.png', '05-cattle', True),
    ('06-Dance-and-Ocean-Rim/06-dance.png', '06-dance', True),
]

for sheet_file, out_name, skip in SHEETS:
    sheet_path = os.path.join(HOLD, sheet_file)
    if not os.path.exists(sheet_path):
        print(f'  ⚠ SKIP: {sheet_file} not found')
        continue
    
    out_dir = os.path.join(HOLD, 'flipbooks', out_name)
    print(f'Processing {sheet_file}…')
    
    manifest, img = extract_frames(sheet_path, out_dir, skip_title=skip)
    print(f'  → {len(manifest)} frames extracted')
    
    mp4 = export_mp4(out_dir, manifest, fps=8)
    print(f'  → MP4: {mp4}')
    
    gif = export_gif(out_dir, manifest, fps=8)
    print(f'  → GIF: {gif}')
    
    viewer = build_viewer(out_dir, manifest, out_name)
    print(f'  → Viewer: {viewer}')

print('\nDone. All flipbooks in HOLD/flipbooks/')
