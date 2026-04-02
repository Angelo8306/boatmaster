# KI-Tutor mit Avatar — Design Specification

## Überblick

Ein sprachbasierter KI-Tutor ("Kapitän Kai") für die BoatMaster Bootsführerschein-Lernsoftware. Der Tutor führt natürliche Gespräche per Sprache — wie ein Telefonat mit einem echten Lehrer. Kein Chat-Interface, kein Textverlauf.

## Kernkonzept

Der User sieht einen animierten Cartoon-Kapitän auf dem Bildschirm. Der Kapitän **spricht** mit echter Stimme und der User **antwortet per Mikrofon**. Die Kommunikation ist bidirektional in Echtzeit. Der Kapitän kennt den Lernstand des Users und passt sich an.

## Drei Modi

### 1. Geführte Lernunterhaltung
Der Kapitän führt den User durch ein Thema — Schritt für Schritt im Dialog. Er erklärt Konzepte, stellt Verständnisfragen zwischendurch, gibt Eselsbrücken, und geht gezielt auf Schwächen ein die das SR-System erkannt hat.

**Beispiel-Ablauf:**
- Kapitän: "Lass uns über die IALA Lateralzeichen sprechen. Stell dir vor du fährst in einen Hafen ein..."
- User antwortet
- Kapitän reagiert, korrigiert, erklärt weiter
- Bei richtigem Verständnis: nächstes Konzept
- Bei Schwäche: tiefer bohren, andere Erklärung versuchen

### 2. Freies Gespräch
Der User fragt was er will, der Kapitän antwortet. Keine vordefinierte Struktur. Der User steuert das Thema.

### 3. Prüfungssimulation
Strukturierte Runde mit 10 Fragen. Der Kapitän stellt Fragen wie in einer mündlichen Prüfung, der User antwortet, am Ende gibt es eine Bewertung. Der Kapitän gibt nach jeder Antwort kurzes Feedback.

## Sprachkonzept (DE/EN)

Die kroatische Bootsführerschein-Prüfung wird auf Englisch abgelegt. Der Kapitän führt den User schrittweise vom Deutschen ins Englische:

- **Anfang:** Kapitän spricht hauptsächlich Deutsch, führt Fachbegriffe auf Englisch ein und erklärt sie
- **Fortgeschritten:** Mehr Englisch, Kapitän ermutigt den User auf Englisch zu antworten
- **Prüfungsreif:** Kapitän stellt Fragen auf Englisch, erwartet Antworten auf Englisch
- **Flexibel:** User kann jederzeit auf Deutsch oder Englisch antworten, der Kapitän erkennt beides

Das Englisch-Level wird aus dem SR-System abgeleitet (wie viele Karten auf Englisch gemeistert) und dynamisch angepasst.

## Sprachtechnologie

### Kapitän spricht (Text-to-Speech)
- Claude API generiert Text-Antworten
- Text wird per TTS in Sprache umgewandelt
- Start mit Web Speech API (kostenlos, browser-nativ) — Upgrade auf ElevenLabs möglich falls Stimme nicht gut genug
- Untertitel werden synchron zum Sprechen angezeigt

### User spricht (Speech-to-Text)
- Web Speech API (`SpeechRecognition`) erkennt Sprache
- Sprache wird basierend auf aktuellem EN-Level gesetzt (DE am Anfang, EN bei Fortgeschrittenen). Claude interpretiert gemischte Spracheingaben unabhängig von der STT-Sprache
- Erkannte Wörter erscheinen live auf dem Bildschirm
- Erkannter Text wird an Claude API gesendet

### Echtzeit-Ablauf
1. Kapitän spricht (TTS) → Sound-Wellen-Animation am Avatar
2. Kapitän fertig → Mikrofon aktiviert sich automatisch
3. User spricht → Live-Transkription sichtbar, Avatar zeigt "hört zu"
4. User fertig (Pause-Erkennung) → Text geht an Claude API
5. Claude antwortet → zurück zu Schritt 1

## UI/UX Design

### Tutor-Tab (neuer 5. Tab)
- **Oben:** Drei Modi-Tabs (Lernen | Gespräch | Prüfung)
- **Mitte:** Großer Kapitän-Avatar (Cartoon, ~160px)
  - Beim Sprechen: Schallwellen-Animation um den Avatar
  - Beim Zuhören: Avatar wird dezenter, Mikrofon-Indikator aktiv
- **Darunter:** Sprechblase mit aktuellem Text (Untertitel)
- **Schwächen-Hinweis:** Dezenter Badge zeigt aktuelles Thema/Schwäche
- **Unten:** Mikrofon-Leiste wenn User spricht (Live-Transkription + Sound-Bars)

### "Frag den Kapitän" Button auf Lernkarten
- Button auf jeder Lernkarte im bestehenden Lern-Tab
- Öffnet den Tutor-Tab mit Kontext der aktuellen Karte
- Kapitän weiß welche Karte der User gerade ansieht und kann dazu erklären

### Bottom Navigation
- 5 Tabs statt 4: Start | Lernen | **Tutor** | Hörbuch | Prüfung

## Personalisierung (SR-Integration)

Der Kapitän liest die Spaced-Repetition-Daten aus localStorage:
- Welche Kapitel/Karten wurden gelernt
- Welche sind fällig (due)
- Welche haben niedrige Ease-Faktoren (= schwer für den User)
- Wie oft wurde eine Karte falsch beantwortet

Diese Daten fließen in den System-Prompt an Claude:
- Im Lern-Modus: Kapitän fokussiert auf schwache Themen
- Im Prüfungs-Modus: Fragen kommen bevorzugt aus schwachen Bereichen
- Im freien Gespräch: Kapitän kann proaktiv Themen vorschlagen

## Technische Architektur

### API-Integration
- Direkte Aufrufe an Claude API vom Browser (fetch mit Streaming)
- API-Key wird vom User eingegeben und in localStorage gespeichert
- Model: claude-haiku-4-5-20251001 (schnell, günstig)
- Streaming-Responses für schnelle erste Antwort

### System-Prompt Aufbau
```
Du bist Kapitän Kai, ein erfahrener Seemann und Bootsführerschein-Tutor.
[Rolle + Persönlichkeit]
[Aktueller Modus: Lernen/Gespräch/Prüfung]
[Sprachregeln: DE/EN Level des Users]
[Lernstand: Schwächen aus SR-Daten]
[Kontext: Aktuelle Karte falls von Lernkarten gestartet]
[Kapitel-Inhalte als Referenz]
```

### Daten-Persistenz
- API-Key: localStorage (`tutor_api_key`)
- Chat-Session: nicht gespeichert (kein Verlauf nötig)
- Tutor-Einstellungen: localStorage (`tutor_settings`)

### Avatar
- CSS-animierter Cartoon-Kapitän (Emoji oder SVG)
- Zustände: Idle, Sprechend (Schallwellen), Zuhörend (dezent), Denkend (Punkte)
- Keine externe Bibliothek nötig

## Scope / Grenzen

### In Scope
- Sprach-Tutor mit drei Modi
- Deutsch/Englisch bidirektional
- SR-basierte Personalisierung
- "Frag den Kapitän" auf Lernkarten
- Neuer Tab in Bottom-Navigation

### Nicht in Scope
- Video-Avatar / 3D-Animation
- Chat-Verlauf / Nachrichtenspeicherung
- Offline-Modus für den Tutor (braucht Internet für Claude API)
- Eigener Server / Proxy
