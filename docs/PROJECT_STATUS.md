# PROJECT STATUS — BoatMaster

## Stand: 2026-04-02 (Ende Session 8b)

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
- **KI-Tutor "Kapitaen Kai"**: Sprachbasierter Tutor mit Claude API
  - Animierter Avatar mit 4 Zustaenden (Idle, Sprechend, Zuhoerend, Denkend)
  - Spracheingabe per Mikrofon (Web Speech Recognition)
  - Sprachausgabe per TTS (Deutsch)
  - 3 Modi: Gefuehrtes Lernen | Freies Gespraech | Pruefungssimulation
  - SR-Daten Integration (erkennt Schwaechen)
  - "Frag Kapitaen Kai" Button auf Lernkarten
- **Tab-Navigation**: Start | Lernen | Tutor | Hoerbuch | Pruefung
- **Content-Pipeline**: PDF → JSON → Lernkarten + Audio vollautomatisch
- **Stitch-Projekt**: 5 Screens generiert (Home, Dashboard, Flashcard, Audiobook, Pruefung) — aber im FALSCHEN Dark-Theme

### KRITISCH — Naechste Session
1. **ElevenLabs Konversationsqualitaet** — Agent unterbricht, reagiert nicht kontextbezogen, legt auf. Muss GRUNDLEGEND recherchiert und richtig konfiguriert werden. ElevenLabs ist fuer perfekte Echtzeit-Konversation bekannt — das aktuelle Ergebnis ist inakzeptabel.
2. **Stitch-Design wirklich 1:1 einbauen** — Bisher nur Start-Screen. Lernen, Hoerbuch, Pruefung muessen auch Stitch-Layouts bekommen.
3. **Startseite Seensucht-Logo** — Das Seensucht-Logo von Andreas' Restaurant einbauen

### Bekannte Probleme
- ElevenLabs Agent: Konversation bricht ab, Agent unterbricht User, reagiert fremd
- Agent-ID: agent_5201kn7rttx4estb9481qa9vw60w
- Design: Nur Start-Screen hat Stitch-Layout, andere Screens sind noch altes CSS
- GitHub Pages CDN-Cache: 10 Minuten Verzoegerung bei Deployments

### Dateistruktur
```
app/
  index.html              — Haupt-App (aktuell Dark-Theme, muss auf hell umgebaut werden)
  data.js                 — 25 Kapitel, 224 Karten, 34 Base64-Bilder (1.9 MB)
  audiobook_data.js       — 25 Hoerbuecher, 375 Segmente
  audio/                  — 25 Unterordner, 375 MP3s (57.6 MB)
content/
  units/                  — 24 Unit-JSON-Dateien
  audiobook_scripts/      — 24 Script-JSON-Dateien
  build_app_data.py       — Baut data.js aus Units
  build_audiobook_data.py — Baut audiobook_data.js aus Scripts
  generate_all_audio.py   — Generiert Audio via ElevenLabs
stitch_designs/           — 5 heruntergeladene Stitch-Screens (Dark, veraltet)
docs/
  MASTER_BRIEF.md, CHECKLIST.md, PROJECT_STATUS.md, PROJECT_LOG.md, DECISIONS.md
  superpowers/specs/2026-04-02-ki-tutor-design.md — KI-Tutor Design-Spec
```
