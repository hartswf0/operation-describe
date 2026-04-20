const fs = require('fs');
const html = fs.readFileSync('worldtext-reader.html', 'utf8');

// Extract the renderMd logic and testing dependencies
const SECTIONS = [];
const slugPath = {};
const slugLabel = {};
const slugColor = {};
const slugSect = {};

const PREFIX_DIR = {
  'source':         'worldtext/sources',
  'sources':        'worldtext/sources',
};
const PREFIX_STRIP = [
  'synthesis-', 'thick-description-of-', 'cohen-case-',
  'worldtype-', 'dark-matter-', 'placeholder-', 'citation-',
];

function resolveLink(raw) {
  if (slugPath[raw]) return { slug: raw, path: slugPath[raw], label: slugLabel[raw], dynamic: false };
  for (const pfx of PREFIX_STRIP) {
    if (raw.startsWith(pfx)) {
      const bare = raw.slice(pfx.length);
      if (slugPath[bare]) return { slug: bare, path: slugPath[bare], label: slugLabel[bare], dynamic: false };
    }
  }
  for (const [pfx, dir] of Object.entries(PREFIX_DIR)) {
    const pfxDash = pfx + '-';
    if (raw.startsWith(pfxDash)) {
      const filename = raw.slice(pfxDash.length);
      const path = `${dir}/${filename}.md`;
      const label = raw;
      if (!slugPath[raw]) {
        slugPath[raw]  = path;
        slugLabel[raw] = filename.replace(/-/g, ' ');
        slugColor[raw] = 'var(--c-source)';
        slugSect[raw]  = 'sources';
      }
      return { slug: raw, path: slugPath[raw], label: slugLabel[raw], dynamic: true };
    }
  }
  const dynPath = `worldtext/sources/${raw}.md`;
  if (/^[a-z]+-\d{4}/.test(raw)) {
    if (!slugPath[raw]) {
      slugPath[raw]  = dynPath;
      slugLabel[raw] = raw.replace(/-/g, ' ');
      slugColor[raw] = 'var(--c-source)';
      slugSect[raw]  = 'sources';
    }
    return { slug: raw, path: slugPath[raw], label: slugLabel[raw], dynamic: true };
  }
  return null;
}

// pull renderMd from HTML file:
let renderMdCode = html.match(/function renderMd\(md\) \{[\s\S]*?\n\}/)[0];
let escCode = html.match(/function esc\(s\) \{[\s\S]*?\n\}/)[0];

eval(escCode);
eval(renderMdCode);

const testMd = fs.readFileSync('worldtext/concepts/concept-pictorial-third.md', 'utf8');
const result = renderMd(testMd);
fs.writeFileSync('output.html', result.html);
console.log('Done rendering, output written to output.html');
