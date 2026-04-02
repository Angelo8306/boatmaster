#!/usr/bin/env python3
"""Generate ElevenLabs audio for each segment of the IALA audiobook script."""

import json
import os
import time
import urllib.request
import urllib.error

API_KEY = os.environ.get("ELEVENLABS_API_KEY")
if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not set")

# Voice IDs
VOICES = {
    "dieter": "HzBCRGsOskP44taMg2CT",  # German narrator (user choice)
    "george": "JBFqnCBsd6RMkjVDRZzb",   # British English
}

SCRIPT_PATH = "/Users/angelojuric/Documents/Bootsführerschein/content/audiobook_iala_script.json"
OUTPUT_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/audio/iala"

with open(SCRIPT_PATH, "r") as f:
    segments = json.load(f)

print(f"Generating {len(segments)} audio segments...")

for i, seg in enumerate(segments):
    output_file = os.path.join(OUTPUT_DIR, f"seg_{i:02d}.mp3")

    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        print(f"  [{i+1}/{len(segments)}] Already exists, skipping")
        continue

    voice_id = VOICES[seg["speaker"]]

    payload = json.dumps({
        "text": seg["text"],
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.3
        }
    }).encode("utf-8")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    req = urllib.request.Request(url, data=payload, headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            audio_data = resp.read()
            with open(output_file, "wb") as out:
                out.write(audio_data)
            print(f"  [{i+1}/{len(segments)}] {seg['speaker']}: {len(audio_data)} bytes -> {output_file}")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"  [{i+1}/{len(segments)}] ERROR {e.code}: {error_body}")
        break

    # Small delay to avoid rate limiting
    time.sleep(0.5)

print("\nDone! Files in:", OUTPUT_DIR)
