#!/usr/bin/env python3
"""Generate ElevenLabs audio for ALL audiobook scripts."""

import json
import os
import time
import urllib.request
import urllib.error
import glob

API_KEY = os.environ.get("ELEVENLABS_API_KEY")
if not API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not set")

VOICES = {
    "dieter": "HzBCRGsOskP44taMg2CT",
    "george": "JBFqnCBsd6RMkjVDRZzb",
}

SCRIPTS_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/audiobook_scripts"
AUDIO_BASE = "/Users/angelojuric/Documents/Bootsführerschein/content/audio"
APP_AUDIO = "/Users/angelojuric/Documents/Bootsführerschein/app/audio"

scripts = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "script_*.json")))
print(f"Found {len(scripts)} scripts to process\n")

for script_path in scripts:
    chapter_id = os.path.basename(script_path).replace("script_", "").replace(".json", "")
    out_dir = os.path.join(AUDIO_BASE, chapter_id)
    app_dir = os.path.join(APP_AUDIO, chapter_id)
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(app_dir, exist_ok=True)

    with open(script_path) as f:
        segments = json.load(f)

    print(f"=== Chapter {chapter_id}: {len(segments)} segments ===")

    for i, seg in enumerate(segments):
        output_file = os.path.join(out_dir, f"seg_{i:02d}.mp3")
        app_file = os.path.join(app_dir, f"seg_{i:02d}.mp3")

        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            # Copy to app dir if needed
            if not os.path.exists(app_file):
                import shutil
                shutil.copy2(output_file, app_file)
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
                # Also copy to app dir
                with open(app_file, "wb") as out:
                    out.write(audio_data)
                print(f"  [{i+1}/{len(segments)}] {seg['speaker']}: {len(audio_data)} bytes")
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            print(f"  [{i+1}/{len(segments)}] ERROR {e.code}: {error_body}")
            if e.code == 429:
                print("  Rate limited, waiting 30 seconds...")
                time.sleep(30)
                # Retry once
                try:
                    with urllib.request.urlopen(req) as resp:
                        audio_data = resp.read()
                        with open(output_file, "wb") as out:
                            out.write(audio_data)
                        with open(app_file, "wb") as out:
                            out.write(audio_data)
                        print(f"  [{i+1}/{len(segments)}] RETRY OK: {len(audio_data)} bytes")
                except Exception as e2:
                    print(f"  [{i+1}/{len(segments)}] RETRY FAILED: {e2}")
                    break
            else:
                break

        time.sleep(0.5)

    print()

print("Done! Checking totals...")
total_files = 0
total_size = 0
for d in glob.glob(os.path.join(APP_AUDIO, "*")):
    if os.path.isdir(d):
        files = glob.glob(os.path.join(d, "*.mp3"))
        size = sum(os.path.getsize(f) for f in files)
        total_files += len(files)
        total_size += size
        print(f"  {os.path.basename(d)}: {len(files)} files, {size/1024:.0f} KB")

print(f"\nTotal: {total_files} files, {total_size/1024/1024:.1f} MB")
