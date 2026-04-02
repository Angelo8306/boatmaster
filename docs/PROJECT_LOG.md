# PROJECT LOG — BoatMaster

## 2026-04-02

### Session 1 (fruehere Conversation)
- Stitch MCP eingerichtet (mehrere Anlaeufe, am Ende via `claude mcp add`)
- Stitch-Design erstellt → von Angelo abgelehnt (generisch, keine echten Inhalte)
- Pivot: Content-First Ansatz statt Design-First
- PDF-Extraktion mit PyMuPDF: Text (EN + DE) + 238 Bilder
- Kapitelstruktur erstellt: 11 Kapitel, 24 Lerneinheiten
- IALA-Einheit als Pilot: 14 kuratierte Lernkarten
- data.js mit Base64-Bildern generiert
- Prototyp-App gebaut: Karten, Quiz, Dark Theme, Senior-UX
- Hoerbuch-Konzept definiert: Zwei Sprecher (DE erklaert + EN Begriffe)
- Hoerbuch-Skript geschrieben: 25 Segmente fuer IALA-Einheit
- ElevenLabs API verifiziert, Stimmen ausgewaehlt
- ElevenLabs API Key in ~/.zshrc gespeichert

### Session 2
- Audio-Generierung: Voice "Dieter" deaktiviert → Angelo gab Alternative (HzBCRGsOskP44taMg2CT)
- 25 Audio-Segmente erfolgreich generiert (3.7 MB)
- Hoerbuch-Player in App eingebaut (Play/Pause, Skip, Timeline, Auto-Advance, Tracking)
- Tab-Navigation hinzugefuegt
- Projekt-Dokumentation angelegt (alle 5 Pflicht-Dateien)

### Session 3
- Alle 13 Kapitel: Unit-JSONs mit 128 Lernkarten erstellt
- build_app_data.py: Automatisierte Pipeline fuer data.js (Units + Base64-Bilder)
- Kapitelauswahl-Screen in App eingebaut
- Hoerbuch-Scripts fuer alle 13 Kapitel geschrieben (214 Segmente)
- generate_all_audio.py: 214 MP3s generiert via ElevenLabs (30 MB)
- build_audiobook_data.py: Pipeline fuer audiobook_data.js
- Multi-Kapitel Hoerbuch-Player:
  - Kapitelauswahl mit Fortschrittsanzeige (% gehoert pro Kapitel)
  - Player mit Segment-Text, DE/EN-Badge, Timeline
  - Fortschritts-Tracking pro Kapitel via localStorage
  - "Anderes Kapitel waehlen" Navigation
- Alten Single-Chapter IALA-Code entfernt, nur noch Multi-Chapter Code
- Docs aktualisiert (CHECKLIST, PROJECT_STATUS, PROJECT_LOG)

### Session 4
- 12 fehlende Sub-Unit-Karten erstellt (96 neue Karten):
  1.2a, 1.2b, 1.3b, 1.4, 1.6a, 1.6b, 1.7, 2.2, 3.2, 4.1, 7.2, 9.2
- build_app_data.py aktualisiert: 25 Kapitel, 224 Karten, 34 Bilder (1.9 MB)
- 12 Hoerbuch-Scripts geschrieben (161 neue Segmente)
- build_audiobook_data.py aktualisiert: 25 Kapitel, 375 Segmente
- Audio generiert via ElevenLabs: 161 neue MP3s (gesamt 375 Dateien, 57.6 MB)
- App zeigt nun alle 25 Kapitel in Lernen UND Hoerbuch
- Pruefungsmodus implementiert:
  - Konfigurations-Screen (Schnelltest 10 / Simulation 20 / Alle 72 Fragen)
  - Zufaellige Fragen kapiteluebergreifend (MC + Freitext)
  - Ergebnis mit BESTANDEN/NICHT BESTANDEN (>=60%), Detailliste
  - Pruefungshistorie in localStorage
- Docs aktualisiert

### Session 5 — KI-Tutor Brainstorming
- Design-Brainstorming fuer KI-Tutor mit Avatar (Stufe 2)
- Entscheidungen getroffen:
  - Sprach-Interface (KEIN Chat) — Echtzeit wie Telefonat
  - Cartoon-Kapitaen "Kapitaen Kai" als Avatar mit Animationen
  - 3 Modi: Gefuehrtes Lernen | Freies Gespraech | Pruefungssimulation
  - Claude API (Haiku) direkt vom Browser, API-Key in localStorage
  - Deutsch → Englisch stufenweiser Uebergang basierend auf Lernfortschritt
  - SR-Daten Integration fuer personalisiertes Lernen
  - Neuer 5. Tab + "Frag den Kapitaen" auf Lernkarten
- Mockups erstellt (Visual Companion):
  - Architektur-Uebersicht (verworfen — Angelo will keine Technik sehen)
  - Chat-Interface (verworfen — Angelo will Sprache, keinen Chat)
  - Sprach-Interface mit Avatar + Schallwellen (genehmigt)
- Design-Spec geschrieben: `docs/superpowers/specs/2026-04-02-ki-tutor-design.md`
- Spec Review bestanden (keine Blocker)
- Naechster Schritt: Implementierungsplan in neuer Session
