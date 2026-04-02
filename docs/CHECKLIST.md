# CHECKLIST — BoatMaster

## PDF-Extraktion
- [x] Englischen PDF-Text extrahieren (140 Seiten → text_en.json)
- [x] Deutschen PDF-Text extrahieren (141 Seiten → text_de.json)
- [x] Bilder extrahieren und filtern (386 → 238 relevante Bilder)

## Kapitelstruktur
- [x] PDFs in 11 Kapitel / 24 Lerneinheiten aufteilen
- [x] chapter_01.json bis chapter_11.json erstellen

## Prototyp — IALA Lerneinheit
- [x] 14 Lernkarten kuratieren (4 Vokabel, 6 Lern, 3 MC-Quiz, 1 Freitext)
- [x] data.js mit Base64-Bildern und Karten generieren
- [x] App mit Karten, Quiz, Fortschrittspunkten, DE-Toggle, TTS
- [x] Dark Maritime Theme, Senior-freundlich

## Hoerbuch — IALA Einheit
- [x] Hoerbuch-Skript schreiben (25 Segmente, DE/EN Dialog)
- [x] ElevenLabs Stimmen auswaehlen (DE: HzBCRGsOskP44taMg2CT, EN: George)
- [x] 25 Audio-Segmente generieren (3.7 MB gesamt)
- [x] Hoerbuch-Player in App einbauen
- [x] Fortschritts-Tracking (localStorage, Segment + Datum)
- [x] Tab-Navigation (Lernen | Hoerbuch | Wiederholen | Pruefung)

## Projekt-Dokumentation
- [x] MASTER_BRIEF.md
- [x] CHECKLIST.md
- [x] PROJECT_STATUS.md
- [x] PROJECT_LOG.md
- [x] DECISIONS.md

## Alle 13 Kapitel — Lernkarten
- [x] Unit-JSONs fuer alle 13 Kapitel erstellen (128 Karten gesamt)
- [x] build_app_data.py Pipeline (Units → data.js mit Bildern)
- [x] Kapitelauswahl-Screen in App

## Alle 13 Kapitel — Hoerbuch
- [x] Hoerbuch-Scripts fuer alle 13 Kapitel schreiben (214 Segmente gesamt)
- [x] Audio fuer alle 13 Kapitel generieren (30 MB, 214 MP3s)
- [x] build_audiobook_data.py Pipeline (Scripts → audiobook_data.js)
- [x] Multi-Kapitel Hoerbuch-Player in App (Kapitelauswahl + Player + Fortschritt pro Kapitel)

## Alle 25 Kapitel — Sub-Units komplett
- [x] 12 fehlende Sub-Unit-Karten erstellen (96 neue Karten → gesamt 224)
- [x] 12 Hoerbuch-Scripts schreiben (161 neue Segmente → gesamt 375)
- [x] Audio fuer alle 12 neuen Kapitel generieren (57.6 MB gesamt, 375 MP3s)
- [x] Pipelines aktualisiert (build_app_data.py + build_audiobook_data.py)
- [x] App zeigt 25 Lernkapitel + 25 Hoerbuch-Kapitel

## Pruefungsmodus
- [x] Pruefungssimulator mit Konfigurations-Screen (10/20/alle Fragen)
- [x] Zufaellige Fragen aus allen 25 Kapiteln (72 Pruefungsfragen)
- [x] MC-Quiz und Freitext-Fragen mit Selbstbewertung
- [x] Ergebnis-Screen mit Bestanden/Nicht bestanden (>=60%)
- [x] Detailauswertung welche Fragen richtig/falsch
- [x] Pruefungshistorie in localStorage

## Spaced Repetition
- [x] Spaced Repetition Algorithmus (SM-2 Variante, in Session 4 gebaut)

## KI-Tutor mit Avatar (Stufe 2)
- [x] Brainstorming + Design-Entscheidungen
- [x] Design-Spec geschrieben (`docs/superpowers/specs/2026-04-02-ki-tutor-design.md`)
- [ ] Implementierungsplan erstellen
- [ ] Claude API Integration (Browser → Haiku, Streaming)
- [ ] Sprach-Ein/Ausgabe (TTS + Speech Recognition, DE/EN)
- [ ] Kapitaen Kai Avatar mit Animationen
- [ ] Tutor-Tab (3 Modi: Lernen | Gespraech | Pruefung)
- [ ] "Frag den Kapitaen" Button auf Lernkarten
- [ ] SR-Daten Integration (Schwaechen erkennen)
- [ ] Deutsch → Englisch stufenweiser Uebergang
