# MASTER BRIEF — BoatMaster Lernsoftware

## Ursprungsauftrag
Bilinguale Lernsoftware fuer Andreas (62 Jahre, schwaches Englisch, wohnt in Deutschland), der die kroatische Bootsfuehrerschein-Pruefung (Kategorie C, Voditelj brodice) bestehen muss. Die Pruefung ist muendlich auf Englisch vor einer 3-koepfigen Kommission.

## Zielgruppe
- Andreas, 62 Jahre alt
- Nicht technikaffin
- Deutschsprachig, schwaches Englisch
- Muss die Pruefung auf Englisch bestehen

## Quellmaterial
- Script for the exam licence C (Englisch) — 146 Seiten, adrialibar.com
- Script for the exam licence C (Deutsch) — 146 Seiten, adrialibar.com
- 238 extrahierte Bilder (Seekarten, Bojen, Kompassrosen, IALA-Zeichen, Motordiagramme, Knoten etc.)

## Kernfunktionen

### Stufe 1 — Lernkarten + Hoerbuch (aktuell in Arbeit)
- **Lernkarten**: Vokabeln, Lerninhalte, MC-Quiz, Freitext-Quiz (muendliche Pruefungssimulation)
- **Bilingual**: Englisch primaer, Deutsch auf Toggle
- **Echte Bilder**: Aus den PDF-Skripten extrahiert
- **Hoerbuch-Modus**: Vorproduziertes Audio pro Kapitel, deutscher Erklaerer + englische Fachbegriffe
  - Fortschritts-Tracking (welches Segment gehoert, wann)
  - ElevenLabs API fuer natuerliche Stimmen
  - Zwei Sprecher: Deutsch (vom User gewaehlte Stimme HzBCRGsOskP44taMg2CT) + George (Britisch EN)

### Stufe 2 — Interaktiver KI-Tutor mit Avatar (Design fertig, Implementierung steht an)
- **Kapitaen Kai** — Cartoon-Avatar mit Animationen (Schallwellen, Zuhoer-Modus)
- **Sprach-Interface** — Echtzeit wie ein Telefonat, KEIN Chat/Textverlauf
  - Kapitaen spricht per TTS (Web Speech API, spaeter ggf. ElevenLabs)
  - User antwortet per Mikrofon (Web Speech Recognition)
- **3 Modi**: Gefuehrtes Lernen | Freies Gespraech | Pruefungssimulation (10 Fragen)
- **Deutsch → Englisch**: Startet auf Deutsch, mischt schrittweise mehr Englisch rein
- **Personalisiert**: Liest SR-Daten, fokussiert auf Schwaechen
- **Claude API** (Haiku) direkt vom Browser, API-Key in localStorage
- **Neuer 5. Tab** + "Frag den Kapitaen" Button auf jeder Lernkarte
- Design-Spec: `docs/superpowers/specs/2026-04-02-ki-tutor-design.md`

## Design-Anforderungen
- Dark Maritime Theme (#0a1628)
- Senior-freundlich: 18px Basisschrift, 54px min Button-Hoehe
- Mobile First
- Kein generisches AI-Design — echte Bilder, durchdachte UX

## Technologie
- Vanilla HTML/CSS/JS (Single-Page App)
- ElevenLabs API (multilingual v2 Modell)
- Claude API (fuer KI-Tutor)
- LocalStorage fuer Fortschritts-Tracking
- PyMuPDF fuer PDF-Extraktion

## Pruefungsformat
- Muendlich, auf Englisch
- 6 Themenbereiche
- ~15-25 Fragen
- Vor 3-koepfiger Kommission
- Kroatien, Kategorie C (Voditelj brodice)

## Kapitelstruktur
- 11 Kapitel, 24 Lerneinheiten, 242 Bilder
- Kapitel 1: Marine Navigation (9 Einheiten, 160 Bilder)
- Kapitel 2-11: 15 Einheiten, 82 Bilder
