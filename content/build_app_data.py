#!/usr/bin/env python3
"""Build app/data.js from all unit JSON files, with images as base64."""

import json
import base64
import os
import glob

UNITS_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/units"
IMAGES_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/images"
IALA_DEMO = "/Users/angelojuric/Documents/Bootsführerschein/content/unit_iala_demo.json"
OUTPUT = "/Users/angelojuric/Documents/Bootsführerschein/app/data.js"

# Chapter metadata
CHAPTERS = [
    {"id": "iala", "title_de": "IALA Tonnensystem", "title_en": "IALA Buoyage System", "file": IALA_DEMO},
    {"id": "1_1", "title_de": "Seekarten — Grundlagen", "title_en": "Nautical Charts - Basics"},
    {"id": "1_2a", "title_de": "IALA — Lichter & Lateralzeichen", "title_en": "IALA - Lights & Lateral Marks"},
    {"id": "1_2b", "title_de": "IALA — Kardinal- & Sonderzeichen", "title_en": "IALA - Cardinal & Special Marks"},
    {"id": "1_3a", "title_de": "Koordinaten & Navigation", "title_en": "Coordinates & Navigation"},
    {"id": "1_3b", "title_de": "Kompass, Kurs & Azimut", "title_en": "Compass, Course & Azimuth"},
    {"id": "1_4", "title_de": "Terrestrische Navigation", "title_en": "Terrestrial Navigation"},
    {"id": "1_6a", "title_de": "Radar", "title_en": "Radar Navigation"},
    {"id": "1_6b", "title_de": "GPS, Echolot & Autopilot", "title_en": "GPS, Echo Sounder & Autopilot"},
    {"id": "1_7", "title_de": "Toernplanung", "title_en": "Voyage Planning"},
    {"id": "2_1", "title_de": "Bootsmotoren", "title_en": "Boat Engines"},
    {"id": "2_2", "title_de": "Motorsysteme & Wartung", "title_en": "Engine Systems & Maintenance"},
    {"id": "3_1", "title_de": "Kroatisches Seerecht", "title_en": "Croatian Maritime Law"},
    {"id": "3_2", "title_de": "Registrierung & Dokumente", "title_en": "Registration & Documents"},
    {"id": "4_1", "title_de": "Bootstypen & Ausrüstung", "title_en": "Boat Types & Equipment"},
    {"id": "4_2", "title_de": "Knoten & Ankern", "title_en": "Knots & Anchoring"},
    {"id": "5_1", "title_de": "Stabilität von Booten", "title_en": "Boat Stability"},
    {"id": "6_1", "title_de": "Erste Hilfe an Bord", "title_en": "First Aid on Board"},
    {"id": "7_1", "title_de": "Wetter & Winde", "title_en": "Weather & Winds"},
    {"id": "7_2", "title_de": "Wolken, Gezeiten & Vorhersage", "title_en": "Clouds, Tides & Forecasting"},
    {"id": "8_1", "title_de": "Manövrieren", "title_en": "Maneuvering"},
    {"id": "9_1", "title_de": "Kollisionsverhütung", "title_en": "Collision Prevention"},
    {"id": "9_2", "title_de": "Navigationslichter & Signale", "title_en": "Navigation Lights & Signals"},
    {"id": "10_1", "title_de": "Sicherheit auf See", "title_en": "Safety at Sea"},
    {"id": "11_1", "title_de": "Seefunk (VHF)", "title_en": "Maritime Communications"},
]

def image_to_base64(filename):
    """Convert image file to base64 data URI."""
    filepath = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(filepath):
        return None
    ext = os.path.splitext(filename)[1].lower()
    mime = {"png": "image/png", "jpeg": "image/jpeg", "jpg": "image/jpeg"}.get(ext.lstrip("."), "image/png")
    with open(filepath, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{data}"

# Collect all referenced images
all_images = {}
all_chapters = []

for ch in CHAPTERS:
    unit_file = ch.get("file", os.path.join(UNITS_DIR, f"unit_{ch['id']}.json"))
    if not os.path.exists(unit_file):
        print(f"  SKIP {ch['id']}: file not found")
        continue

    with open(unit_file) as f:
        cards = json.load(f)

    # Collect images
    for card in cards:
        img = card.get("image")
        if img and img not in all_images:
            b64 = image_to_base64(img)
            if b64:
                all_images[img] = b64
                print(f"  Image: {img} ({len(b64)//1024}KB)")

    all_chapters.append({
        "id": ch["id"],
        "title_de": ch["title_de"],
        "title_en": ch["title_en"],
        "cards": cards
    })
    print(f"  Chapter {ch['id']}: {ch['title_de']} — {len(cards)} cards")

# Write output
print(f"\nTotal: {len(all_chapters)} chapters, {sum(len(c['cards']) for c in all_chapters)} cards, {len(all_images)} images")

with open(OUTPUT, "w") as f:
    f.write("// Auto-generated from content/units/*.json\n")
    f.write(f"// {len(all_chapters)} chapters, {sum(len(c['cards']) for c in all_chapters)} cards, {len(all_images)} images\n\n")

    # Images object
    f.write("const IMAGES = ")
    f.write(json.dumps(all_images, indent=0))
    f.write(";\n\n")

    # Chapters array
    f.write("const CHAPTERS_DATA = ")
    f.write(json.dumps(all_chapters, indent=2, ensure_ascii=False))
    f.write(";\n\n")

    # Default CARDS for backwards compatibility (first chapter)
    f.write("// Backwards compatibility: CARDS = first chapter's cards\n")
    f.write("let CARDS = CHAPTERS_DATA[0].cards;\n")

print(f"\nWritten to {OUTPUT}")
print(f"File size: {os.path.getsize(OUTPUT) / 1024:.0f} KB")
