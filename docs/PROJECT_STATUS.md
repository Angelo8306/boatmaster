# PROJECT STATUS — BoatMaster

## Stand: 2026-04-02 (Ende Session 5)

### Was funktioniert
- **Lern-App**: 25 Kapitel mit 224 Lernkarten, 34 eingebettete Bilder
  - Kapitelauswahl-Screen mit Titel DE/EN und Kartenanzahl
  - Vokabelkarten, Lerninhalte mit echten Bildern, MC-Quiz, Freitext-Quiz
  - Bilingual (EN primaer, DE auf Toggle)
  - TTS via Web Speech API
  - Fortschrittspunkte, Ergebnis-Screen
- **Hoerbuch-Player**: 25 Kapitel mit 375 Audio-Segmenten (57.6 MB)
  - Kapitelauswahl mit Fortschrittsanzeige pro Kapitel
  - ElevenLabs-Stimmen (DE: HzBCRGsOskP44taMg2CT, EN: George)
  - Play/Pause, Vor/Zurueck, Timeline-Seek
  - Auto-Advance zum naechsten Segment
  - Fortschritts-Tracking pro Kapitel (localStorage)
- **Pruefungssimulator**: 72 Fragen, 3 Modi (10/20/alle), Ergebnis + Historie
- **Spaced Repetition**: SM-2 Algorithmus, Fortschrittsbalken pro Kapitel, Wiederholung-faellig Box
- **Tab-Navigation**: Start | Lernen | Hoerbuch | Pruefung
- **Content-Pipeline**: PDF → JSON → Lernkarten + Audio vollautomatisch

### Was als naechstes kommt
1. **KI-Tutor mit Avatar implementieren** (Design-Spec fertig!)
   - Naechster Schritt: Implementierungsplan in neuer Session erstellen
   - Spec: `docs/superpowers/specs/2026-04-02-ki-tutor-design.md`

### Bekannte Probleme
- Keine bekannten Probleme

### Dateistruktur
```
app/
  index.html              — Haupt-App (~1700 Zeilen, alle Features)
  data.js                 — 25 Kapitel, 224 Karten, 34 Base64-Bilder (1.9 MB)
  audiobook_data.js       — 25 Hoerbuecher, 375 Segmente
  audio/                  — 25 Unterordner, 375 MP3s (57.6 MB)
content/
  units/                  — 24 Unit-JSON-Dateien
  audiobook_scripts/      — 24 Script-JSON-Dateien
  build_app_data.py       — Baut data.js aus Units
  build_audiobook_data.py — Baut audiobook_data.js aus Scripts
  generate_all_audio.py   — Generiert Audio via ElevenLabs
docs/
  MASTER_BRIEF.md, CHECKLIST.md, PROJECT_STATUS.md, PROJECT_LOG.md, DECISIONS.md
  superpowers/specs/2026-04-02-ki-tutor-design.md — KI-Tutor Design-Spec
```
