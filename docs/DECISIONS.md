# DECISIONS — BoatMaster

## Content-First statt Design-First
**Entscheidung:** Erst echte Inhalte aus PDFs extrahieren, dann App um Inhalte herum bauen.
**Grund:** Stitch-generiertes UI war leer und generisch. Angelo: "Da schau ich rein und seh nur Scheisse." Echte Bilder und Inhalte muessen im Zentrum stehen.

## Vanilla HTML/CSS/JS statt Framework
**Entscheidung:** Kein React/Vue/etc., reine Single-Page HTML-App.
**Grund:** Einfachheit, keine Build-Pipeline noetig, laeuft ueberall, kein Overhead fuer eine Lern-App.

## ElevenLabs statt Web Speech API fuer Hoerbuch
**Entscheidung:** ElevenLabs API fuer vorproduzierte Audio-Segmente.
**Grund:** Natuerlichere Stimmen, mehrsprachig (DE + EN), konsistente Qualitaet. Web Speech API bleibt fuer spontanes Vorlesen einzelner Begriffe.

## Zwei-Sprecher-Format fuer Hoerbuch
**Entscheidung:** Deutscher Erklaerer + englischer Fachbegriff-Sprecher.
**Grund:** Andreas ist Deutsch-Muttersprachler. Konzepte auf Deutsch erklaeren, englische Begriffe gezielt einfuehren — wie ein echter Sprachlehrer.

## Deutsche Stimme: HzBCRGsOskP44taMg2CT
**Entscheidung:** Vom User explizit gewaehlte Stimme statt "Dieter".
**Grund:** "Dieter" (bYMNUlc3OdXdptMmaetI) wurde vom Ersteller deaktiviert. Angelo hat die Alternative selbst ausgesucht.

## Hoerbuch und KI-Tutor als separate Features
**Entscheidung:** Hoerbuch = vorproduziert, passiv. KI-Tutor = interaktiv, Echtzeit.
**Grund:** Angelo: "Das sind zwei verschiedene Paar Schuhe." Hoerbuch zum Anhoeren, KI-Tutor zum aktiven Lernen und Fragen stellen.

## Dark Maritime Theme
**Entscheidung:** Dunkles Design (#0a1628) mit Blau-Akzenten.
**Grund:** Passt zum Thema Seefahrt, angenehm fuer die Augen, kein "weisses Standard-Design" (Angelo-Vorgabe).

## Senior-freundliche UX
**Entscheidung:** 18px Basisschrift, 54px min Button-Hoehe, klare Navigation.
**Grund:** Zielgruppe ist 62 Jahre alt, nicht technikaffin.

## KI-Tutor: Sprach-Interface statt Chat (2026-04-02)
**Entscheidung:** Der KI-Tutor ist ein Sprach-Interface wie ein Telefonat, KEIN Chat mit Textverlauf.
**Grund:** Angelo: "Wir haben nie von einem Chat-Fenster gesprochen." Die App soll eine Lern-App bleiben, kein ChatGPT-Klon. Natuerliche Konversation in Echtzeit.

## KI-Tutor: Claude API direkt vom Browser (2026-04-02)
**Entscheidung:** Keine Server-Infrastruktur, API-Calls direkt vom Client. API-Key in localStorage.
**Grund:** BoatMaster ist eine persoenliche Lern-App, kein SaaS. Ein Proxy-Server waere Overengineering. Kann spaeter nachgeruestet werden.

## KI-Tutor: Deutsch → Englisch Stufenmodell (2026-04-02)
**Entscheidung:** Kapitaen startet auf Deutsch, mischt schrittweise Englisch rein, basierend auf SR-Lernstand.
**Grund:** Angelo: "Er muss ihn an das Englisch heranfuehren." Die Pruefung ist auf Englisch, aber der User muss dort abgeholt werden wo er steht.
