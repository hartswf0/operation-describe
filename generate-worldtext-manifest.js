#!/usr/bin/env node
/**
 * WORLDTEXT COSMOS → DOUBLE BARREL MANIFEST GENERATOR
 * 
 * Parses the worldtext/ directory structure and the
 * "Operative Ekphrasis, Thick Description.json" evidence corpus
 * into a manifest.json that the Double Barrel Voronoi + Sediment
 * visualization can consume.
 * 
 * Architecture mapping:
 *   Galaxy     → Top-level Voronoi territory  
 *   World      → Second-level territory (inside galaxy)
 *   Species    → File type color (entity, place, ritual, etc.)
 *   Sources    → Evidence stratum (sediment layers)
 *   Cross-links → refs array for navigation
 * 
 * Usage: node generate-worldtext-manifest.js
 */

const fs = require('fs');
const path = require('path');

const WORLDTEXT_DIR = path.join(__dirname, 'worldtext');
const EVIDENCE_JSON = path.join(__dirname, 'Operative Ekphrasis, Thick Description.json');
const OUTPUT = path.join(__dirname, 'worldtext-manifest.json');

// ── Parse all markdown files ──────────────────────────────────
function parseWorldTextFiles() {
    const files = [];
    
    function walk(dir, rel) {
        const entries = fs.readdirSync(dir, { withFileTypes: true });
        for (const entry of entries) {
            const fullPath = path.join(dir, entry.name);
            const relPath = rel ? `${rel}/${entry.name}` : entry.name;
            
            if (entry.isDirectory()) {
                walk(fullPath, relPath);
            } else if (entry.name.endsWith('.md') || entry.name.endsWith('.txt')) {
                const stat = fs.statSync(fullPath);
                const content = fs.readFileSync(fullPath, 'utf-8');
                
                // Extract wiki-links [[...]]
                const wikiLinks = [];
                const linkRe = /\[\[([^\]]+)\]\]/g;
                let match;
                while ((match = linkRe.exec(content)) !== null) {
                    wikiLinks.push(match[1]);
                }
                
                // Extract species/scale from blockquote header
                let species = 'unknown';
                let scale = 'unknown';
                let worldType = '';
                let galaxy = '';
                const speciesMatch = content.match(/\*\*Species\*\*:\s*(\S+)/);
                const scaleMatch = content.match(/\*\*Scale\*\*:\s*(\S+)/);
                const wtMatch = content.match(/\*\*World-Type\*\*:\s*\[\[([^\]]+)\]\]/);
                const galaxyMatch = content.match(/\*\*(?:Parent )?Galaxy\*\*:\s*\[\[([^\]]+)\]\]/);
                
                if (speciesMatch) species = speciesMatch[1];
                if (scaleMatch) scale = scaleMatch[1];
                if (wtMatch) worldType = wtMatch[1];
                if (galaxyMatch) galaxy = galaxyMatch[1];
                
                // Extract title (first H1)
                const titleMatch = content.match(/^#\s+(.+)$/m);
                const title = titleMatch ? titleMatch[1] : entry.name.replace('.md', '');
                
                // Extract summary (first paragraph after ---)
                let summary = '';
                const sections = content.split('---');
                if (sections.length > 2) {
                    const body = sections.slice(2).join('---').trim();
                    const firstPara = body.split('\n\n')[0];
                    if (firstPara && !firstPara.startsWith('#') && !firstPara.startsWith('>')) {
                        summary = firstPara.substring(0, 300).replace(/\n/g, ' ');
                    }
                }
                
                // Determine the category from the directory path
                const category = relPath.split('/')[0]; // e.g., 'worlds', 'entities', 'places'
                
                const ext = entry.name.endsWith('.txt') ? 'txt' : 'md';
                files.push({
                    path: `worldtext/${relPath}`,
                    realPath: `worldtext/${relPath}`,
                    size: stat.size,
                    ext,
                    created: stat.birthtime.toISOString().split('T')[0],
                    modified: stat.mtime.toISOString().split('T')[0],
                    refs: [...new Set(wikiLinks)],
                    summary: summary || title,
                    // WorldText metadata
                    _wt: {
                        species,
                        scale,
                        worldType,
                        galaxy,
                        title,
                        category
                    }
                });
            }
        }
    }
    
    walk(WORLDTEXT_DIR, '');
    return files;
}

// ── Parse evidence JSON into virtual source files ─────────────
function parseEvidence() {
    if (!fs.existsSync(EVIDENCE_JSON)) {
        console.warn('⚠ Evidence JSON not found, skipping');
        return [];
    }
    
    const raw = JSON.parse(fs.readFileSync(EVIDENCE_JSON, 'utf-8'));
    const files = [];
    
    raw.forEach((entry, idx) => {
        const author = entry.author?.[0]?.family || 'unknown';
        const year = entry.issued?.['date-parts']?.[0]?.[0] || 'n.d.';
        const title = entry.title || `Source ${idx}`;
        const type = entry.type || 'document';
        const abstract = entry.abstract || '';
        
        // Build a slug
        const slug = `${author.toLowerCase()}-${year}-${title.substring(0, 40).toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
        
        // Estimate "size" based on content density
        const contentSize = (abstract.length || 50) + (title.length * 10);
        
        // Determine galaxy affiliation by keyword matching
        // Priority: AI/tech > thick description > intermedial > ekphrastic (catch-all)
        let galaxy = 'unaffiliated';
        const searchText = `${title} ${abstract}`.toLowerCase();
        
        // Check AI/generative FIRST (these are more specific)
        if (/diffusion|text-to-image|latent space|stable diffusion|dall-?e|midjourney|prompt engineer|gpt-?[234]|llm|neural net|deep learn|generative ai|transformer|machine learn|image generat|text generat/.test(searchText)) {
            galaxy = 'galaxy-of-generative-ai-worlds';
        } else if (/thick descri|geertz|ethnograph|anthropolog|phenomenol|fieldwork|participant observ|interpreta|hermeneutic/.test(searchText)) {
            galaxy = 'galaxy-of-thick-description-worlds';
        } else if (/intermedia|transmedia|adaptation|semiot|translation|remediat|multimodal|cross-media|iconotext/.test(searchText)) {
            galaxy = 'galaxy-of-intermedial-worlds';
        } else if (/ekphrasis|ekphrastic|paragone|verbal.*visual|museum of word|poetics of/.test(searchText)) {
            galaxy = 'galaxy-of-ekphrastic-worlds';
        } else if (/prompt|creative ai|co-creat|human-ai|ai art|computat.*creativ|ai-generat/.test(searchText)) {
            galaxy = 'galaxy-of-generative-ai-worlds';
        } else if (/word.*image|visual.*verbal|image.*text|picture theory|visual culture|art.*descript/.test(searchText)) {
            galaxy = 'galaxy-of-ekphrastic-worlds';
        }
        
        files.push({
            path: `evidence/${galaxy}/${type}/${slug}.json`,
            size: contentSize,
            ext: 'json',
            created: `${year}-01-01`,
            modified: `${year}-01-01`,
            refs: [],
            summary: `[${author} ${year}] ${title.substring(0, 120)}`,
            _wt: {
                species: 'evidence',
                scale: 'source',
                worldType: '',
                galaxy,
                title: `${author} ${year}: ${title}`,
                category: 'evidence',
                zoteroId: entry.id,
                type: type
            }
        });
    });
    
    return files;
}

// ── Build the cosmological hierarchy ──────────────────────────
// Instead of raw filesystem paths, we restructure by cosmological ontology:
//   COSMOS
//   ├── Galaxy: Ekphrastic Worlds
//   │   ├── World: Classical Ekphrasis
//   │   │   ├── entities/...
//   │   │   ├── places/...
//   │   │   └── sources/...
//   │   └── World: Shield of Achilles
//   ├── Galaxy: Generative AI Worlds
//   │   ├── World: Latent Space
//   │   └── World: Operative Ekphrasis  
//   └── META (chronicle, atlas, taxonomies)

function buildCosmologicalManifest(wtFiles, evidenceFiles) {
    const allFiles = [];
    
    // ── 1. COSMOLOGICAL LAYER: reorganize worldtext by galaxy/world ──
    
    // Identify galaxy files and world files
    const galaxyFiles = wtFiles.filter(f => f._wt.category === 'galaxies');
    const worldFiles = wtFiles.filter(f => f._wt.category === 'worlds');
    const metaFiles = wtFiles.filter(f => 
        ['chronicle.md', 'atlas.md', 'cosmology.md'].some(m => f.path.endsWith(m))
    );
    const taxonomyFiles = wtFiles.filter(f => f._wt.category === 'taxonomies');
    const synthesisFiles = wtFiles.filter(f => f._wt.category === 'syntheses');
    const questionFiles = wtFiles.filter(f => f._wt.category === 'questions');
    
    // Object-type files (entities, places, rituals, etc.)
    const objectCategories = [
        'entities', 'places', 'rituals', 'thresholds', 'distinctions',
        'conflicts', 'atmospheres', 'epochs', 'constellations',
        'systems', 'governance', 'infrastructures', 'flows',
        'regions', 'scenes', 'fragments', 'memories'
    ];
    const objectFiles = wtFiles.filter(f => objectCategories.includes(f._wt.category));
    const sourceFiles = wtFiles.filter(f => f._wt.category === 'sources');
    
    // ── Restructure into cosmological paths ──
    
    // Helper: remap path but keep realPath
    const remap = (f, newPath) => ({ ...f, path: newPath, realPath: f.realPath || f.path });
    
    // Meta-level governance
    metaFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/${name}`));
    });
    taxonomyFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/taxonomies/${name}`));
    });
    synthesisFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/syntheses/${name}`));
    });
    questionFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/questions/${name}`));
    });
    
    // Galaxy level
    galaxyFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/galaxies/${name}`));
    });
    
    // Map worlds into their parent galaxies
    worldFiles.forEach(f => {
        const galaxy = f._wt.galaxy || 'unaffiliated';
        const baseName = f.path.split('/').pop().replace('.md', '');
        const worldName = baseName;
        allFiles.push(remap(f, `cosmos/${galaxy}/${worldName}/${baseName}.md`));
    });
    
    // Map objects into their closest world by cross-link analysis
    objectFiles.forEach(f => {
        let parentWorld = 'unplaced';
        let parentGalaxy = 'unaffiliated';
        
        for (const ref of f.refs) {
            const worldFile = worldFiles.find(w => {
                const wName = w.path.split('/').pop().replace('.md', '');
                return ref === wName;
            });
            if (worldFile) {
                parentWorld = worldFile.path.split('/').pop().replace('.md', '');
                parentGalaxy = worldFile._wt.galaxy || 'unaffiliated';
                break;
            }
        }
        
        if (parentWorld === 'unplaced') {
            allFiles.push(remap(f, `cosmos/unaffiliated/${f._wt.category}/${f.path.split('/').pop()}`));
        } else {
            allFiles.push(remap(f, `cosmos/${parentGalaxy}/${parentWorld}/${f._wt.category}/${f.path.split('/').pop()}`));
        }
    });
    
    // Source summaries — includes both .md analysis and .txt fulltext
    sourceFiles.forEach(f => {
        allFiles.push(remap(f, `cosmos/evidence-stratum/source-summaries/${f.path.split('/').pop()}`));
    });
    
    // Bridge files
    const bridgeFiles = wtFiles.filter(f => f._wt.category === 'bridges');
    bridgeFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/bridges/${name}`));
    });
    
    // Concept files
    const conceptFiles = wtFiles.filter(f => f._wt.category === 'concepts');
    conceptFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/governance/concepts/${name}`));
    });
    
    // Fulltext files (sources-fulltext/)
    const fulltextFiles = wtFiles.filter(f => f.path.includes('sources-fulltext/'));
    fulltextFiles.forEach(f => {
        const name = f.path.split('/').pop();
        allFiles.push(remap(f, `cosmos/evidence-stratum/fulltext/${name}`));
    });
    
    // Evidence corpus (from JSON)
    evidenceFiles.forEach(f => {
        allFiles.push(f);
    });
    
    return allFiles;
}

// ── Main ──────────────────────────────────────────────────────
console.log('🪐 WORLDTEXT COSMOS → MANIFEST GENERATOR');
console.log('=========================================\n');

const wtFiles = parseWorldTextFiles();
console.log(`📄 Parsed ${wtFiles.length} WorldText pages`);

const evidenceFiles = parseEvidence();
console.log(`📚 Parsed ${evidenceFiles.length} evidence entries`);

const cosmologicalFiles = buildCosmologicalManifest(wtFiles, evidenceFiles);
console.log(`\n🌌 Generated ${cosmologicalFiles.length} cosmological entries\n`);

// Statistics
const categories = {};
cosmologicalFiles.forEach(f => {
    const cat = f.path.split('/')[1] || 'root';
    categories[cat] = (categories[cat] || 0) + 1;
});

console.log('Territory distribution:');
Object.entries(categories)
    .sort((a, b) => b[1] - a[1])
    .forEach(([cat, count]) => {
        console.log(`  ${cat}: ${count}`);
    });

// Build manifest in the format double-bar expects
const manifest = {
    generated: new Date().toISOString(),
    cosmos: 'WORLDTEXT — Operative Ekphrasis / Thick Description',
    stats: {
        files: cosmologicalFiles.length,
        totalReferences: cosmologicalFiles.reduce((s, f) => s + (f.refs?.length || 0), 0),
        totalBytes: cosmologicalFiles.reduce((s, f) => s + f.size, 0),
        worldTextPages: wtFiles.length,
        evidenceEntries: evidenceFiles.length,
        galaxies: wtFiles.filter(f => f._wt.category === 'galaxies').length,
        worlds: wtFiles.filter(f => f._wt.category === 'worlds').length,
        worldTypes: 12
    },
    files: cosmologicalFiles.map(f => ({
        path: f.path,
        realPath: f.realPath || f.path,
        size: f.size,
        ext: f.ext,
        created: f.created,
        modified: f.modified,
        refs: f.refs || [],
        summary: f.summary || ''
    }))
};

fs.writeFileSync(OUTPUT, JSON.stringify(manifest, null, 2));
console.log(`\n✅ Manifest written to ${OUTPUT} (${(fs.statSync(OUTPUT).size / 1024).toFixed(1)} KB)`);

// Also write worldtext-data.js for inline loading in double-bar.html
const DATA_JS = path.join(__dirname, 'worldtext-data.js');
const jsContent = 'const WORLDTEXT_MANIFEST = ' + JSON.stringify(manifest) + ';\n';
fs.writeFileSync(DATA_JS, jsContent);
console.log(`✅ Data JS written to ${DATA_JS} (${(fs.statSync(DATA_JS).size / 1024).toFixed(1)} KB)`);
