#!/usr/bin/env python3
"""
SynthQuest PDF Manual Ingestion Tool
Extracts MIDI Implementation Charts, SysEx tables, and Factory Preset lists from synthesizer PDF manuals.
"""

import sys
import os
import re
import json
import subprocess
import argparse

def extract_text_from_pdf(pdf_path, layout=True):
    cmd = ["pdftotext"]
    if layout:
        cmd.append("-layout")
    cmd.extend([pdf_path, "-"])
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace")
    return res.stdout

def scan_midi_keywords(text):
    keywords = ["Exclusive", "SysEx", "F0", "F7", "Checksum", "Parameter", "Bank Select", "CC#", "Control Change"]
    scores = {}
    pages = text.split("\x0c")
    for i, page in enumerate(pages):
        score = sum(page.count(k) for k in keywords)
        if score > 5:
            scores[i + 1] = score
    return scores

def main():
    parser = argparse.ArgumentParser(description="SynthQuest Synth PDF Manual Ingestion Tool")
    parser.add_argument("pdf", help="Path to synthesizer manual PDF")
    parser.add_argument("--scan-midi", action="store_true", help="Locate MIDI and SysEx pages")
    parser.add_argument("--extract-text", help="Save extracted text to file")
    
    args = parser.parse_args()
    if not os.path.exists(args.pdf):
        print(f"Error: {args.pdf} not found", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Processing {args.pdf}...")
    text = extract_text_from_pdf(args.pdf)
    pages = text.split("\x0c")
    print(f"[*] Total pages: {len(pages)}")

    if args.scan_midi:
        midi_pages = scan_midi_keywords(text)
        print(f"[*] Found {len(midi_pages)} pages with high MIDI/SysEx density:")
        for page_num, count in sorted(midi_pages.items(), key=lambda x: x[1], reverse=True)[:15]:
            print(f"    Page {page_num:3d}: relevance score {count}")

    if args.extract_text:
        with open(args.extract_text, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[+] Saved extracted text to {args.extract_text}")

if __name__ == "__main__":
    main()
