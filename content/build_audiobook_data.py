#!/usr/bin/env python3
"""Build audiobook data JS file from all scripts."""

import json
import os
import glob

SCRIPTS_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/audiobook_scripts"
IALA_SCRIPT = "/Users/angelojuric/Documents/Bootsführerschein/content/audiobook_iala_script.json"
OUTPUT = "/Users/angelojuric/Documents/Bootsführerschein/app/audiobook_data.js"

CHAPTER_NAMES = {
    "iala": {"de": "IALA Tonnensystem", "en": "IALA Buoyage System"},
    "1_1": {"de": "Seekarten — Grundlagen", "en": "Nautical Charts"},
    "1_2a": {"de": "IALA — Lichter & Lateralzeichen", "en": "IALA Lights & Lateral Marks"},
    "1_2b": {"de": "IALA — Kardinal- & Sonderzeichen", "en": "IALA Cardinal & Special Marks"},
    "1_3a": {"de": "Koordinaten & Navigation", "en": "Coordinates & Navigation"},
    "1_3b": {"de": "Kompass, Kurs & Azimut", "en": "Compass, Course & Azimuth"},
    "1_4": {"de": "Terrestrische Navigation", "en": "Terrestrial Navigation"},
    "1_6a": {"de": "Radar", "en": "Radar Navigation"},
    "1_6b": {"de": "GPS, Echolot & Autopilot", "en": "GPS, Echo Sounder & Autopilot"},
    "1_7": {"de": "Törnplanung", "en": "Voyage Planning"},
    "2_1": {"de": "Bootsmotoren", "en": "Boat Engines"},
    "2_2": {"de": "Motorsysteme & Wartung", "en": "Engine Systems & Maintenance"},
    "3_1": {"de": "Kroatisches Seerecht", "en": "Maritime Law"},
    "3_2": {"de": "Registrierung & Dokumente", "en": "Registration & Documents"},
    "4_1": {"de": "Bootstypen & Ausrüstung", "en": "Boat Types & Equipment"},
    "4_2": {"de": "Knoten & Ankern", "en": "Knots & Anchoring"},
    "5_1": {"de": "Stabilität", "en": "Stability"},
    "6_1": {"de": "Erste Hilfe", "en": "First Aid"},
    "7_1": {"de": "Wetter & Winde", "en": "Weather & Winds"},
    "7_2": {"de": "Wolken, Gezeiten & Vorhersage", "en": "Clouds, Tides & Forecasting"},
    "8_1": {"de": "Manövrieren", "en": "Maneuvering"},
    "9_1": {"de": "Kollisionsverhütung", "en": "Collision Rules"},
    "9_2": {"de": "Navigationslichter & Signale", "en": "Navigation Lights & Signals"},
    "10_1": {"de": "Sicherheit auf See", "en": "Safety at Sea"},
    "11_1": {"de": "Seefunk (VHF)", "en": "VHF Radio"},
}

audiobooks = []

# IALA first
with open(IALA_SCRIPT) as f:
    segments = json.load(f)
audiobooks.append({
    "id": "iala",
    "title_de": CHAPTER_NAMES["iala"]["de"],
    "title_en": CHAPTER_NAMES["iala"]["en"],
    "audio_dir": "audio/iala",
    "segments": segments
})
print(f"iala: {len(segments)} segments")

# Rest from scripts dir
for script_path in sorted(glob.glob(os.path.join(SCRIPTS_DIR, "script_*.json"))):
    ch_id = os.path.basename(script_path).replace("script_", "").replace(".json", "")
    with open(script_path) as f:
        segments = json.load(f)
    names = CHAPTER_NAMES.get(ch_id, {"de": ch_id, "en": ch_id})
    audiobooks.append({
        "id": ch_id,
        "title_de": names["de"],
        "title_en": names["en"],
        "audio_dir": f"audio/{ch_id}",
        "segments": segments
    })
    print(f"{ch_id}: {len(segments)} segments")

with open(OUTPUT, "w") as f:
    f.write("// Auto-generated audiobook data\n")
    f.write(f"// {len(audiobooks)} chapters, {sum(len(a['segments']) for a in audiobooks)} total segments\n\n")
    f.write("const AUDIOBOOKS = ")
    f.write(json.dumps(audiobooks, indent=2, ensure_ascii=False))
    f.write(";\n")

print(f"\nWritten {len(audiobooks)} audiobooks to {OUTPUT}")
print(f"Total segments: {sum(len(a['segments']) for a in audiobooks)}")
