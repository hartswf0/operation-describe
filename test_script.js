const fs = require('fs');

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

const html = fs.readFileSync('worldtext-reader.html', 'utf8');

// evaluate esc and renderMd functions
let escCode = html.match(/function esc\([\s\S]+?\}\s*(?=<)/)[0].replace(/\}[\s\S]*$/, '}');
let renderMdCode = html.match(/function renderMd\([\s\S]+?return \{ html: md, links: foundLinks \};\n\}/)[0];

const vm = require('vm');
const context = { resolveLink, slugLabel, slugPath, slugColor, slugSect, Set };
vm.createContext(context);
vm.runInContext(escCode, context);
vm.runInContext(renderMdCode, context);

const mdText = fs.readFileSync('worldtext/concepts/concept-pictorial-third.md', 'utf8');
const result = context.renderMd(mdText);

console.log(result.html);
