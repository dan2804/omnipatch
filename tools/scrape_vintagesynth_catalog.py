#!/usr/bin/env python3
"""
Vintage Synth Explorer Catalog Scraper & Classifier
Parses all 892 synth models from Vintage Synth Explorer and extracts specifications:
- Control (MIDI, CV/Gate, None)
- Memory (Presets, Patches, Banks, None)
- Date Produced
- Software vs Hardware
- Polyphony, Synthesis type
"""

import json
import urllib.request
import re
import os
import time
import concurrent.futures

INPUT_SETTINGS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources', 'vintagesynth_settings.json')
OUTPUT_CATALOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources', 'vintagesynth_catalog.json')

def parse_specs(html):
    specs = {}
    items = re.findall(r'<span class="specification-term" title="([^"]+)"[^>]*>([^<]+)</span>\s*<span class="specification-value">(.*?)</span>', html, re.DOTALL)
    for title, term, val in items:
        clean_val = re.sub(r'<[^>]+>', ' ', val).strip()
        clean_val = re.sub(r'\s+', ' ', clean_val)
        specs[title.strip()] = clean_val
    return specs

def fetch_synth(entry):
    url = entry["url"]
    slug = entry["slug"]
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        specs = parse_specs(html)
        
        control = specs.get("Control", "")
        memory = specs.get("Memory", "")
        date_prod = specs.get("Date Produced", "")
        polyphony = specs.get("Polyphony", "")
        oscillators = specs.get("Oscillators", "")
        
        is_software = (
            "Windows Requirements" in specs or 
            "Macintosh Requirements" in specs or
            "software" in control.lower() or
            "vst" in control.lower() or
            entry["mfg"].lower() in ["native instruments", "arturia", "bitheadz", "bomb factory studios", "gforce software", "propellerhead software", "prosoniq", "steinberg", "lennar digital", "way out ware", "vaz synths", "image line", "tc|works", "applied acoustics"]
        )
        
        has_midi = bool(re.search(r'\bmidi\b', control, re.I))
        has_memory = bool(re.search(r'\b(patch|preset|kit|pattern|bank|program|user|ram|rom)\b', memory, re.I)) and not bool(re.search(r'^(none|no|0)\b', memory.strip(), re.I))
        
        entry["specs"] = specs
        entry["is_software"] = is_software
        entry["has_midi"] = has_midi
        entry["has_memory"] = has_memory
        entry["control"] = control
        entry["memory"] = memory
        entry["date_produced"] = date_prod
        entry["polyphony"] = polyphony
        entry["status"] = "ok"
    except Exception as e:
        entry["status"] = f"error: {str(e)}"
        entry["is_software"] = False
        entry["has_midi"] = False
        entry["has_memory"] = False
        
    return entry

def main():
    with open(INPUT_SETTINGS, "r") as f:
        d = json.load(f)
        
    menu = d["vsTermMenuLink"]["2bc6f1c9-2166-4e9a-90eb-c184c897611a"]
    terms = menu["terms"]
    nodes = menu["nodes"]
    
    entries = []
    for mfg_id, items in nodes.items():
        mfg_name = terms.get(mfg_id, {}).get("title", "Unknown")
        for node_id, info in items.items():
            title = info["title"].strip()
            url = info["url"]
            entries.append({
                "mfg": mfg_name,
                "title": title,
                "url": url,
                "slug": url.split("/")[-1]
            })
            
    print(f"Loaded {len(entries)} models. Starting concurrent fetch...")
    t0 = time.time()
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for i, res in enumerate(executor.map(fetch_synth, entries)):
            results.append(res)
            if (i + 1) % 100 == 0 or (i + 1) == len(entries):
                print(f"  Processed {i+1}/{len(entries)} ({time.time() - t0:.1f}s)...")
                
    with open(OUTPUT_CATALOG, "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"Saved {len(results)} parsed instruments to {OUTPUT_CATALOG} in {time.time() - t0:.1f}s")

if __name__ == "__main__":
    main()
