#!/usr/bin/env python3
"""Build compilation-resonance.html — split-pane paper+pipeline viewer."""
import os, re, json, html as H

DOCK = '/Users/gaia/OPERATION-DESCRIBE/Dry-Dock'
HOLD = os.path.join(DOCK, 'HOLD')

def read(p):
    with open(p, 'r') as f: return f.read()

# Read paper
paper_md = read('/Users/gaia/OPERATION-DESCRIBE/Z-Port/final-assembled-draft.md')

# Convert markdown to HTML paragraphs with resonate triggers
TRIGGERS = {
    'shield of Achilles': '00', 'Shield of Achilles': '00',
    'constellations': '01', 'Pleiades': '01', 'cosmic': '01', 'Cosmic Design': '01',
    'two cities': '02', 'Two Cities': '02', 'brides': '02',
    'war': '03', 'ambush': '03', 'War and Ambush': '03',
    'vineyard': '04', 'ploughmen': '04', 'reapers': '04', 'Labors': '04',
    'cattle': '05', 'lions': '05', 'oxen': '05', 'sheep': '05',
    'dance': '06', 'Dance': '06', 'Ocean': '06', 'Oceanus': '06',
}

def md_to_html(md):
    lines = md.split('\n')
    out = []
    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('# '):
            out.append(f'<h2 class="paperH">{H.escape(line[2:])}</h2>')
        elif line.startswith('## '):
            out.append(f'<h3 class="paperS">{H.escape(line[3:])}</h3>')
        elif line == '---':
            out.append('<hr class="paperHR">')
        elif line.startswith('**') and line.endswith('**'):
            out.append(f'<p class="paperA"><strong>{H.escape(line[2:-2])}</strong></p>')
        else:
            t = H.escape(line)
            # Inject resonate triggers
            for phrase, zone in TRIGGERS.items():
                ep = H.escape(phrase)
                t = t.replace(ep, f'<span class="rt" data-z="{zone}">{ep}</span>', 1)
            out.append(f'<p class="paperP">{t}</p>')
    return '\n'.join(out)

paper_html = md_to_html(paper_md)

# Read source texts
src_full = H.escape(read(os.path.join(HOLD, 'a-full-source.md')))
src_seg = H.escape(read(os.path.join(HOLD, 'a-source.md')))
prompt_txt = H.escape(read(os.path.join(HOLD, 'a-prompt.md')))

# Section manifest for pipeline
ZONES = [
    {"id":"00","name":"Whole Shield","code":"00-the-shield-abc-macro (16).txt",
     "sheet":"00-the-shield-ABC_SHEET_85f.png","flesh":"00-the-shield.png"},
    {"id":"01","name":"Cosmic Design","code":"01-Construction-and-Cosmic-Design/01-cosmic-abc-macro (19).txt",
     "sheet":"01-Construction-and-Cosmic-Design/01-cosmic-design.png",
     "flesh":"01-Construction-and-Cosmic-Design/01-cosmic-gemini.png"},
    {"id":"02","name":"Peace & Law","code":"02-Two-Cities-Peace-and-Law/02-brides-lawabc-macro (13).txt",
     "sheet":"02-Two-Cities-Peace-and-Law/ABC_SHEET_60f (2).png",
     "flesh":"02-Two-Cities-Peace-and-Law/02-bride-law-Gemini_Generated_Image_6oi6ce6oi6ce6oi6.jpeg"},
    {"id":"03","name":"War & Ambush","code":"03-Two-Cities-War-and-Ambush/03-cities-war-abc-macro (14).txt",
     "sheet":"03-Two-Cities-War-and-Ambush/ABC_SHEET_78f.png",
     "flesh":"03-Two-Cities-War-and-Ambush/Gemini_Generated_Image_2ylbjn2ylbjn2ylb.jpeg"},
    {"id":"04","name":"Labors","code":"04-Labors-of-the-Field/04-labors-abc-macro (15).txt",
     "sheet":"04-Labors-of-the-Field/ABC_SHEET_76f.png",
     "flesh":"04-Labors-of-the-Field/Gemini_Generated_Image_ffbktcffbktcffbk.jpeg"},
    {"id":"05","name":"Cattle & Lions","code":"05-Cattle-Lions-and-Sheep/05-lion-abc-macro (18).txt",
     "sheet":"05-Cattle-Lions-and-Sheep/05-cattle-and-lions.png",
     "flesh":"05-Cattle-Lions-and-Sheep/Gemini_Generated_Image_5kxfd95kxfd95kxf.jpeg"},
    {"id":"06","name":"Dance & Rim","code":"06-Dance-and-Ocean-Rim/06_DANCE_abc-macro (17).txt",
     "sheet":"06-Dance-and-Ocean-Rim/06-dance.png","flesh":""},
]

zones_json = json.dumps(ZONES)

# Build zone tabs HTML
ztabs = ''
for z in ZONES:
    cls = ' on' if z['id'] == '00' else ''
    ztabs += f'<button class="zt{cls}" data-z="{z["id"]}">{z["id"]} {z["name"]}</button>'

# Build comic page HTML (all zones in printable grid)
comic = '<div class="comic-grid">'
for z in ZONES:
    comic += f'''<div class="comic-cell">
<div class="comic-label">{z["id"]} · {z["name"]}</div>
<div class="comic-pair">
<div class="comic-img"><img src="{z["sheet"]}" alt="Contact Sheet"><div class="comic-cap">SYMBOLIC</div></div>'''
    if z["flesh"]:
        comic += f'<div class="comic-img"><img src="{z["flesh"]}" alt="Vision"><div class="comic-cap">NEURAL</div></div>'
    else:
        comic += '<div class="comic-img missing">⚠ NO IMAGE</div>'
    comic += '</div></div>'
comic += '</div>'

# Build timeline HTML
timeline = '<div class="tl-track">'
for z in ZONES:
    timeline += f'''<div class="tl-zone">
<div class="tl-label">{z["id"]}</div>
<div class="tl-name">{z["name"]}</div>
<div class="tl-step"><img src="{z["sheet"]}" alt="Sheet"></div>
<div class="tl-arrow">→</div>'''
    if z["flesh"]:
        timeline += f'<div class="tl-step"><img src="{z["flesh"]}" alt="Vision"></div>'
    else:
        timeline += '<div class="tl-step missing">⚠</div>'
    timeline += '</div>'
timeline += '</div>'

OUT = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>COMPILATION RESONANCE — Operative Ekphrasis Process Paper</title>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%;overflow:hidden;font-family:monospace}}

/* SPLIT PANE */
.split{{display:flex;height:100%}}
.left{{flex:0 0 50%;height:100%;overflow-y:auto;background:#f9f6f0;color:#1a1a1a;padding:40px 32px 80px;font-family:'EB Garamond',Georgia,serif;border-right:3px solid #000}}
.right{{flex:0 0 50%;height:100%;overflow-y:auto;background:#0a0a0f;color:#e0e0d8;font-family:'JetBrains Mono',monospace}}

/* LEFT — PAPER */
.left::-webkit-scrollbar{{width:6px}}
.left::-webkit-scrollbar-thumb{{background:#ccc}}
.paperH{{font-size:22px;font-weight:600;margin:32px 0 12px;line-height:1.3}}
.paperS{{font-size:17px;font-weight:500;margin:28px 0 10px;border-bottom:1px solid #ddd;padding-bottom:6px}}
.paperHR{{border:none;border-top:1px solid #ddd;margin:20px 0}}
.paperA{{font-size:14px;margin:8px 0}}
.paperP{{font-size:15px;line-height:1.8;margin:10px 0;text-align:justify;hyphens:auto}}
.rt{{cursor:pointer;border-bottom:2px solid #c9a84c;transition:background .15s}}
.rt:hover{{background:rgba(201,168,76,.2)}}
.rt.active{{background:rgba(201,168,76,.35);padding:0 2px}}

/* RIGHT — PIPELINE */
.right::-webkit-scrollbar{{width:6px}}
.right::-webkit-scrollbar-thumb{{background:#333}}
.rHdr{{background:#000;padding:12px 16px;border-bottom:2px solid #333;position:sticky;top:0;z-index:10}}
.rHdr h1{{font-size:12px;font-weight:900;text-transform:uppercase;letter-spacing:.08em;color:#fff;margin-bottom:6px}}

/* ZONE TABS */
.zTabs{{display:flex;flex-wrap:wrap;gap:2px}}
.zt{{background:#111;color:#777;border:1px solid #333;padding:4px 8px;font:inherit;font-size:9px;font-weight:700;cursor:pointer;text-transform:uppercase}}
.zt.on{{background:#c9a84c;color:#000;border-color:#c9a84c}}
.zt:hover{{color:#fff}}

/* VIEW TABS */
.vTabs{{display:flex;gap:0;margin:0;border-bottom:2px solid #333}}
.vt{{flex:1;padding:8px;text-align:center;font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.06em;cursor:pointer;background:#0a0a0f;color:#555;border:none;border-right:1px solid #222}}
.vt.on{{color:#c9a84c;border-bottom:2px solid #c9a84c}}
.vt:hover{{color:#aaa}}
.vPanel{{display:none;padding:16px}}
.vPanel.on{{display:block}}

/* PIPELINE VIEW */
.pipeStep{{border:1px solid #333;margin:10px 0;overflow:hidden}}
.pipeH{{background:#1a1a1a;padding:8px 12px;font-size:10px;font-weight:900;text-transform:uppercase;letter-spacing:.06em;color:#c9a84c;display:flex;justify-content:space-between}}
.pipeB{{padding:12px}}
.pipeCode{{background:#111;border:1px solid #222;padding:10px;font-size:10px;line-height:1.5;max-height:300px;overflow-y:auto;white-space:pre-wrap;word-wrap:break-word;color:#aaa}}
.pipeCode.loading{{color:#555;font-style:italic}}
.pipeImg{{display:grid;grid-template-columns:1fr 1fr;gap:2px}}
.pipeImg img{{width:100%;height:auto;display:block}}
.pipeCap{{font-size:8px;font-weight:700;text-transform:uppercase;color:#555;padding:4px 6px;text-align:center;background:#111}}
.pipeBlend{{position:relative;overflow:hidden}}
.pipeBlend img{{display:block;width:100%}}
.blendSlider{{position:absolute;top:0;left:50%;width:50%;height:100%;overflow:hidden;border-left:2px solid #c9a84c}}
.blendSlider img{{position:absolute;top:0;right:0;width:200%;height:100%;object-fit:cover}}
.blendHandle{{position:absolute;top:0;bottom:0;width:2px;background:#c9a84c;cursor:ew-resize}}

/* BEFLIX CANVAS */
.bflixWrap{{text-align:center;margin:8px 0}}
.bflixWrap canvas{{border:1px solid #333;image-rendering:pixelated;background:#000}}
.bflixBtn{{background:#1a1a1a;color:#aaa;border:1px solid #333;padding:6px 12px;font:inherit;font-size:9px;cursor:pointer;margin:4px}}
.bflixBtn:hover{{color:#fff}}

/* COMIC PAGE */
.comic-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:2px}}
.comic-cell{{background:#111;border:1px solid #333;overflow:hidden}}
.comic-label{{padding:6px 8px;font-size:9px;font-weight:900;text-transform:uppercase;color:#c9a84c;border-bottom:1px solid #333}}
.comic-pair{{display:grid;grid-template-columns:1fr 1fr;gap:1px}}
.comic-img{{position:relative}}
.comic-img img{{display:block;width:100%;height:auto}}
.comic-cap{{position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,.8);color:#888;font-size:7px;font-weight:900;text-align:center;padding:2px;text-transform:uppercase}}
.comic-img.missing{{display:flex;align-items:center;justify-content:center;min-height:80px;background:#1a1a1a;color:#555;font-size:9px;font-weight:900}}

/* TIMELINE */
.tl-track{{display:flex;gap:2px;overflow-x:auto;padding-bottom:8px}}
.tl-zone{{flex:0 0 180px;background:#111;border:1px solid #333;padding:8px;text-align:center}}
.tl-label{{font-size:20px;font-weight:900;color:#c9a84c}}
.tl-name{{font-size:8px;font-weight:700;text-transform:uppercase;color:#777;margin-bottom:8px}}
.tl-step img{{width:100%;height:auto;border:1px solid #333;margin-bottom:4px}}
.tl-step.missing{{min-height:60px;background:#1a1a1a;display:flex;align-items:center;justify-content:center;color:#555;font-size:10px;border:1px solid #333}}
.tl-arrow{{color:#c9a84c;font-size:14px;margin:4px 0}}

/* PRINT */
@media print{{
  .split{{display:block}}
  .left{{display:none}}
  .right{{width:100%;overflow:visible;background:#fff;color:#000}}
  .comic-grid{{grid-template-columns:repeat(2,1fr)}}
  .comic-label{{color:#000}}
  .pipeCap{{color:#000}}
}}
</style>
</head>
<body>
<div class="split">

<!-- LEFT: PAPER -->
<div class="left" id="paper">
{paper_html}
</div>

<!-- RIGHT: PIPELINE -->
<div class="right">
<div class="rHdr">
<h1>COMPILATION RESONANCE — Pipeline Forge</h1>
<div class="zTabs" id="zTabs">{ztabs}</div>
</div>
<div class="vTabs">
<button class="vt on" data-v="pipeline">Pipeline</button>
<button class="vt" data-v="comic">Comic Page</button>
<button class="vt" data-v="timeline">Timeline</button>
</div>

<!-- PIPELINE VIEW -->
<div class="vPanel on" id="v-pipeline">
<div class="pipeStep">
<div class="pipeH"><span>① SEMANTIC SOURCE</span><span id="zLabel">ZONE 00</span></div>
<div class="pipeB"><div class="pipeCode" id="pSrc">{src_full[:2000]}…</div></div>
</div>
<div class="pipeStep">
<div class="pipeH"><span>② PROMPT ENGINE</span><span>a-prompt.md</span></div>
<div class="pipeB"><div class="pipeCode">{prompt_txt}</div></div>
</div>
<div class="pipeStep">
<div class="pipeH"><span>③ SYMBOLIC CODE (B-FLIX)</span><span id="codeLabel"></span></div>
<div class="pipeB">
<div class="pipeCode loading" id="pCode">Select a zone to load BEFLIX code…</div>
<div class="bflixWrap">
<canvas id="bflix" width="128" height="96" style="width:384px;height:288px"></canvas>
<div><button class="bflixBtn" onclick="renderBflix()">▶ RENDER FIRST FRAME</button>
<button class="bflixBtn" onclick="window.open('abc-flix-pro-viewer.html')">OPEN ABC-FLIX</button></div>
</div>
</div>
</div>
<div class="pipeStep">
<div class="pipeH"><span>④ CONTACT SHEET (DETERMINISTIC)</span><span>The missing middle</span></div>
<div class="pipeB"><img id="pSheet" src="00-the-shield-ABC_SHEET_85f.png" style="width:100%;border:1px solid #333" alt="Contact sheet"></div>
</div>
<div class="pipeStep">
<div class="pipeH"><span>⑤ VISION REHYDRATION (PROBABILISTIC)</span><span>The afterimage</span></div>
<div class="pipeB">
<div class="pipeImg">
<div><img id="pSheet2" src="00-the-shield-ABC_SHEET_85f.png" alt="Skeleton"><div class="pipeCap">Symbolic Skeleton</div></div>
<div><img id="pFlesh" src="00-the-shield.png" alt="Vision"><div class="pipeCap">Neural Flesh</div></div>
</div>
</div>
</div>
</div>

<!-- COMIC PAGE VIEW -->
<div class="vPanel" id="v-comic">
<div style="padding:8px 0;font-size:10px;font-weight:900;color:#c9a84c;text-transform:uppercase;text-align:center;border-bottom:1px solid #333;margin-bottom:8px">
NEUROSYMBOLIC RESONANCE — CONTACT SHEETS × VISION REHYDRATIONS — PRINT THIS PAGE (Ctrl+P)
</div>
{comic}
</div>

<!-- TIMELINE VIEW -->
<div class="vPanel" id="v-timeline">
<div style="padding:8px 0;font-size:10px;font-weight:900;color:#c9a84c;text-transform:uppercase;text-align:center;border-bottom:1px solid #333;margin-bottom:8px">
COMPILATION TIMELINE — SOURCE → CODE → CONTACT SHEET → VISION IMAGE
</div>
{timeline}
</div>

</div>
</div>

<script>
var ZONES = {zones_json};
var currentZone = ZONES[0];
var loadedCode = '';

/* ZONE SWITCHING */
document.querySelectorAll('.zt').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.querySelectorAll('.zt').forEach(function(x){{x.classList.remove('on')}});
    b.classList.add('on');
    var z = ZONES.find(function(z){{return z.id===b.dataset.z}});
    if(!z) return;
    currentZone = z;
    document.getElementById('zLabel').textContent = 'ZONE '+z.id+' — '+z.name;
    document.getElementById('codeLabel').textContent = z.code;
    document.getElementById('pSheet').src = z.sheet;
    document.getElementById('pSheet2').src = z.sheet;
    if(z.flesh){{document.getElementById('pFlesh').src=z.flesh}}
    else{{document.getElementById('pFlesh').src=''}}
    // Load source
    if(z.id==='00'){{
      fetch('a-full-source.md').then(function(r){{return r.text()}}).then(function(t){{
        document.getElementById('pSrc').textContent=t.substring(0,2000)+'…';
      }}).catch(function(){{}});
    }}else{{
      fetch('a-source.md').then(function(r){{return r.text()}}).then(function(t){{
        var idx=parseInt(z.id)-1;
        var secs=t.split(/(?=The (?:Construction|Two Cities|Labors|Cattle|Dance))/);
        document.getElementById('pSrc').textContent=(secs[idx]||t).substring(0,2000);
      }}).catch(function(){{}});
    }}
    // Load code
    var cel=document.getElementById('pCode');
    cel.textContent='Loading '+z.code+'…';
    cel.classList.add('loading');
    fetch(z.code).then(function(r){{return r.text()}}).then(function(t){{
      loadedCode=t;
      var lines=t.split('\\n');
      cel.textContent=lines.slice(0,150).join('\\n')+'\\n\\n… ['+lines.length+' total lines]';
      cel.classList.remove('loading');
    }}).catch(function(e){{
      cel.textContent='⚠ Could not load (run python3 -m http.server in HOLD/)';
      cel.classList.remove('loading');
    }});
  }});
}});

/* VIEW SWITCHING */
document.querySelectorAll('.vt').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.querySelectorAll('.vt').forEach(function(x){{x.classList.remove('on')}});
    document.querySelectorAll('.vPanel').forEach(function(x){{x.classList.remove('on')}});
    b.classList.add('on');
    var p=document.getElementById('v-'+b.dataset.v);
    if(p)p.classList.add('on');
  }});
}});

/* RESONATE TRIGGERS */
document.querySelectorAll('.rt').forEach(function(s){{
  s.addEventListener('click',function(){{
    var z=s.dataset.z;
    document.querySelectorAll('.rt').forEach(function(x){{x.classList.remove('active')}});
    s.classList.add('active');
    var btn=document.querySelector('.zt[data-z="'+z+'"]');
    if(btn)btn.click();
  }});
}});

/* BEFLIX RENDERER */
function renderBflix(){{
  if(!loadedCode)return;
  var canvas=document.getElementById('bflix');
  var ctx=canvas.getContext('2d');
  var W=128,H=96;
  var grid=new Uint8Array(W*H);
  var GRAYS=[255,220,190,160,128,96,48,0];
  var lines=loadedCode.split('\\n');
  for(var i=0;i<lines.length&&i<8000;i++){{
    var ln=lines[i].trim();
    if(!ln||ln[0]==='C'||ln[0]===';'||ln[0]==='@')continue;
    var p=ln.split(/\\s+/);
    var cmd=p[0];
    if(cmd==='CLR'){{grid.fill(parseInt(p[1])||0)}}
    else if(cmd==='PNT'){{
      var x=parseInt(p[1]),y=parseInt(p[2]),w=parseInt(p[3]),h=parseInt(p[4]),v=parseInt(p[5]);
      for(var dy=0;dy<h&&dy<H;dy++)for(var dx=0;dx<w&&dx<W;dx++){{
        var px=x+dx,py=y+dy;
        if(px>=0&&px<W&&py>=0&&py<H)grid[py*W+px]=v;
      }}
    }}
    else if(cmd==='LIN'){{
      var x0=parseInt(p[1]),y0=parseInt(p[2]),x1=parseInt(p[3]),y1=parseInt(p[4]),v=parseInt(p[5]);
      var ddx=Math.abs(x1-x0),ddy=Math.abs(y1-y0);
      var sx=x0<x1?1:-1,sy=y0<y1?1:-1,err=ddx-ddy;
      for(var s=0;s<500;s++){{
        if(x0>=0&&x0<W&&y0>=0&&y0<H)grid[y0*W+x0]=v;
        if(x0===x1&&y0===y1)break;
        var e2=2*err;
        if(e2>-ddy){{err-=ddy;x0+=sx}}
        if(e2<ddx){{err+=ddx;y0+=sy}}
      }}
    }}
    else if(cmd==='REC')break;
  }}
  var img=ctx.createImageData(W,H);
  for(var j=0;j<W*H;j++){{
    var g=GRAYS[grid[j]||0];
    img.data[j*4]=g;img.data[j*4+1]=g;img.data[j*4+2]=g;img.data[j*4+3]=255;
  }}
  ctx.putImageData(img,0,0);
}}

/* AUTO-LOAD ZONE 00 CODE */
document.querySelector('.zt[data-z="00"]').click();
</script>
</body>
</html>'''

with open(os.path.join(HOLD, 'compilation-resonance.html'), 'w') as f:
    f.write(OUT)
print(f"Done: {os.path.getsize(os.path.join(HOLD,'compilation-resonance.html'))//1024}KB")
