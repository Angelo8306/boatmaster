#!/usr/bin/env python3
"""Create audiobook scripts for the 12 new sub-units."""

import json
import os

SCRIPTS_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/audiobook_scripts"

scripts = {}

# ============================================================
# 1.2a — IALA Lights & Lateral Marks
# ============================================================
scripts["script_1_2a.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "IALA — Lichter und Lateralzeichen. In dieser Lektion geht es um die Seitenmarkierungen und ihre Lichter, die dir zeigen wo die Fahrrinne ist."},
    {"speaker": "george", "lang": "en", "text": "IALA buoyage system. Lateral marks and light characteristics. How to identify navigation marks by their lights at night."},
    {"speaker": "dieter", "lang": "de", "text": "Zuerst das Wichtigste: In IALA Region A — und dazu gehört ganz Europa und Kroatien — gilt diese Regel:"},
    {"speaker": "dieter", "lang": "de", "text": "Wenn du von See in einen Hafen einfährst: ROTE Bojen sind LINKS, also an Backbord. GRÜNE Bojen sind RECHTS, also an Steuerbord. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Red to port, green to starboard, when entering from sea. Port-hand marks are red, cylindrical shape, with red light. Starboard-hand marks are green, conical shape, with green light."},
    {"speaker": "dieter", "lang": "de", "text": "Backbord-Zeichen: rot, zylindrisch wie eine Tonne, rotes Licht. Steuerbord-Zeichen: grün, kegelförmig wie eine Spitztonne, grünes Licht."},
    {"speaker": "dieter", "lang": "de", "text": "Manchmal teilt sich eine Fahrrinne in zwei Richtungen. Dann gibt es Bevorzugte-Fahrwasser-Zeichen. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Preferred channel buoy. A red buoy with a green horizontal band means the preferred channel is to starboard. A green buoy with a red horizontal band means the preferred channel is to port."},
    {"speaker": "dieter", "lang": "de", "text": "Merke: Die Hauptfarbe sagt dir die Seite. Der Querstreifen zeigt an, dass sich die Fahrrinne hier teilt."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt zu den Lichtern. Jedes Seezeichen hat nachts ein bestimmtes Blinkrhythmus, damit du es identifizieren kannst. Die wichtigsten auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Fixed light, F — continuous steady light. Flashing, Fl — light shorter than dark. Occulting, Oc — light longer than dark. Quick, Q — fifty to seventy-nine flashes per minute. Isophase, Iso — equal light and dark periods."},
    {"speaker": "dieter", "lang": "de", "text": "Festfeuer brennt durchgehend. Blinkfeuer blitzt kurz auf. Unterbrochenes Feuer ist meistens an und wird kurz unterbrochen. Schnelles Blinkfeuer blinkt fünfzig bis neunundsiebzig Mal pro Minute."},
    {"speaker": "dieter", "lang": "de", "text": "Jedes Licht hat drei Merkmale: Farbe, Periode — also die Zeit für einen kompletten Zyklus — und Tragweite in Seemeilen. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Every light has three characteristics: color, period — the time for one complete cycle, and range — visibility distance in nautical miles."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Rot links, grün rechts bei Einfahrt von See. Bevorzugte-Fahrwasser-Zeichen haben einen Querstreifen. Lichter erkennt man am Rhythmus: Blinkfeuer, Festfeuer, unterbrochenes Feuer."}
]

# ============================================================
# 1.2b — IALA Cardinal & Special Marks
# ============================================================
scripts["script_1_2b.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "IALA — Kardinalzeichen und Sonderzeichen. Diese Zeichen warnen vor Gefahren und zeigen dir, auf welcher Seite du sicher passieren kannst."},
    {"speaker": "george", "lang": "en", "text": "Cardinal marks. They show where safe water lies relative to a danger. Named after compass directions: North, South, East, West."},
    {"speaker": "dieter", "lang": "de", "text": "Kardinalzeichen sind schwarz und gelb. Und jetzt kommt der Trick: Die Position von SCHWARZ zeigt dir die Richtung."},
    {"speaker": "dieter", "lang": "de", "text": "Nord-Kardinalzeichen: Schwarz OBEN. Stell dir vor, das Schwarz zeigt nach oben wie ein Pfeil nach Norden. Du fährst NÖRDLICH daran vorbei."},
    {"speaker": "george", "lang": "en", "text": "North cardinal: black on top, yellow below. Top mark: two cones pointing UP. Pass to the NORTH. Light: continuous quick flashing."},
    {"speaker": "dieter", "lang": "de", "text": "Süd-Kardinalzeichen: Schwarz UNTEN. Das Schwarz zeigt nach unten, also nach Süden. Du fährst SÜDLICH vorbei."},
    {"speaker": "george", "lang": "en", "text": "South cardinal: yellow on top, black below. Top mark: two cones pointing DOWN. Pass to the SOUTH. Light: six flashes plus one long flash."},
    {"speaker": "dieter", "lang": "de", "text": "Ost-Kardinalzeichen: Schwarz OBEN und UNTEN, Gelb in der Mitte. Du fährst ÖSTLICH vorbei."},
    {"speaker": "george", "lang": "en", "text": "East cardinal: black on top and bottom, yellow in the middle. Top mark: two cones base to base, like a diamond. Pass to the EAST. Light: three flashes."},
    {"speaker": "dieter", "lang": "de", "text": "West-Kardinalzeichen: Gelb oben und unten, Schwarz in der MITTE — wie ein Gürtel. Du fährst WESTLICH vorbei."},
    {"speaker": "george", "lang": "en", "text": "West cardinal: yellow on top and bottom, black in the middle. Top mark: two cones point to point, like an hourglass. Pass to the WEST. Light: nine flashes."},
    {"speaker": "dieter", "lang": "de", "text": "Und jetzt der Uhr-Trick für die Lichter: Ost ist drei Blitze — wie drei Uhr. Süd ist sechs Blitze plus Langblitz — wie sechs Uhr. West ist neun Blitze — wie neun Uhr. Und Nord blinkt durchgehend."},
    {"speaker": "dieter", "lang": "de", "text": "Dann gibt es noch das Einzelgefahrenzeichen. Das steht DIREKT über einer Gefahr — einem Felsen oder Wrack. Du kannst auf JEDER Seite vorbeifahren. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Isolated danger mark. Black with red horizontal bands. Top mark: two black spheres. Light: white, group flashing two. You may pass on any side."},
    {"speaker": "dieter", "lang": "de", "text": "Und das Sicheres-Wasser-Zeichen — rot-weiß gestreift mit einer roten Kugel oben drauf. Es zeigt befahrbares Wasser rundherum an, zum Beispiel die Fahrwassermitte."},
    {"speaker": "george", "lang": "en", "text": "Safe water mark. Red and white vertical stripes. Spherical shape. Top mark: single red sphere. Indicates navigable water all around."},
    {"speaker": "dieter", "lang": "de", "text": "Zu guter Letzt: Sonderzeichen sind GELB mit einem X-förmigen Toppzeichen. Sie kennzeichnen besondere Gebiete wie Militärzonen, Naturschutzgebiete oder Wasserskibereiche."},
    {"speaker": "george", "lang": "en", "text": "Special marks. Yellow color, X-shaped top mark, yellow light. Mark special areas: military zones, nature reserves, water ski areas, cable zones."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Kardinalzeichen — Schwarz zeigt die Richtung, Uhr-Trick für die Lichter. Einzelgefahrenzeichen — schwarz mit roten Streifen, auf jeder Seite passierbar. Sonderzeichen — gelb mit X."}
]

# ============================================================
# 1.3b — Compass, Course & Azimuth
# ============================================================
scripts["script_1_3b.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Kompass, Kurs und Azimut. In dieser Lektion geht es darum, wie du deinen Kurs berechnest und warum es drei verschiedene Arten von Nord gibt."},
    {"speaker": "george", "lang": "en", "text": "Compass, course, and azimuth. Three types of north: true north, magnetic north, and compass north."},
    {"speaker": "dieter", "lang": "de", "text": "Geographisch Nord — das ist der echte Nordpol, wie er auf der Karte steht. Magnetisch Nord — da zeigt die Kompassnadel hin. Und Kompassnord — das zeigt der Kompass auf DEINEM Boot an."},
    {"speaker": "dieter", "lang": "de", "text": "Der Unterschied zwischen geographisch Nord und magnetisch Nord heißt Missweisung. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Magnetic variation or declination. The angle between true north and magnetic north. Found on the compass rose of every chart. Changes slowly over time."},
    {"speaker": "dieter", "lang": "de", "text": "Und der Unterschied zwischen magnetisch Nord und Kompassnord heißt Deviation — verursacht durch den Motor, die Elektronik und Metallteile auf deinem Boot."},
    {"speaker": "george", "lang": "en", "text": "Deviation. The compass error caused by the boat's own magnetic influences. Varies with heading. Recorded in a deviation table."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt die Umrechnung. Vom rechtweisenden Kurs zum Kompasskurs: Rechtweisender Kurs plus oder minus Missweisung ergibt den missweisenden Kurs. Plus oder minus Deviation ergibt den Kompasskurs."},
    {"speaker": "george", "lang": "en", "text": "True course plus or minus variation equals magnetic course. Magnetic course plus or minus deviation equals compass course. West: add. East: subtract."},
    {"speaker": "dieter", "lang": "de", "text": "Merke dir: West wird addiert, Ost wird subtrahiert. Ein Beispiel: Rechtweisender Kurs neunzig Grad, Missweisung drei Grad West. Dann ist der missweisende Kurs neunzig plus drei gleich dreiundneunzig Grad."},
    {"speaker": "dieter", "lang": "de", "text": "Peilung oder Azimut ist der Winkel von Nord zu einem Objekt, gemessen im Uhrzeigersinn. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Bearing or azimuth. The horizontal angle measured clockwise from north to an object. Used for position fixing and navigation."},
    {"speaker": "dieter", "lang": "de", "text": "Und noch die Grundformel für die Navigation: Geschwindigkeit mal Zeit gleich Strecke. Geschwindigkeit wird in Knoten gemessen, Strecke in Seemeilen."},
    {"speaker": "george", "lang": "en", "text": "Speed in knots, distance in nautical miles, time in hours. Speed equals distance divided by time. One knot equals one nautical mile per hour."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Drei Arten von Nord, Missweisung kommt von der Erde, Deviation kommt vom Boot. West addieren, Ost subtrahieren. Peilung ist der Winkel zu einem Objekt."}
]

# ============================================================
# 1.4 — Terrestrial Navigation
# ============================================================
scripts["script_1_4.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Terrestrische Navigation — wie du deine Position auf See bestimmst, ohne GPS. Das klingt altmodisch, ist aber Pflichtprüfungsstoff und kann dir das Leben retten wenn die Elektronik ausfällt."},
    {"speaker": "george", "lang": "en", "text": "Terrestrial navigation. Five basic factors: course, speed, time, distance, and depth."},
    {"speaker": "dieter", "lang": "de", "text": "Die einfachste Methode ist die Koppelnavigation. Du weißt wo du warst, du kennst deinen Kurs und deine Geschwindigkeit, und berechnest daraus wo du jetzt sein müsstest."},
    {"speaker": "george", "lang": "en", "text": "Dead reckoning. Estimating position from a known previous position using course, speed, and elapsed time. Abbreviated D R."},
    {"speaker": "dieter", "lang": "de", "text": "Das Problem: Wind und Strömung schieben dich vom Kurs ab. Deshalb wird die Koppelnavigation mit der Zeit immer ungenauer. Du brauchst regelmäßig eine echte Standortbestimmung."},
    {"speaker": "dieter", "lang": "de", "text": "Die beste Methode ist die Kreuzpeilung — du peilst zwei oder drei bekannte Objekte an Land, zum Beispiel Leuchttürme oder Kirchturmspitzen."},
    {"speaker": "george", "lang": "en", "text": "Cross bearings. Take bearings on two or three known objects. Plot the bearing lines on the chart. Your position is where they cross. Three bearings are preferred."},
    {"speaker": "dieter", "lang": "de", "text": "Ideal sind drei Peilungen mit etwa sechzig Grad Abstand. Die drei Linien bilden ein kleines Dreieck — deine Position ist in der Mitte davon."},
    {"speaker": "dieter", "lang": "de", "text": "Noch eine Methode: Peilung plus Entfernung. Du peilst ein Objekt und misst gleichzeitig die Entfernung — zum Beispiel per Radar."},
    {"speaker": "george", "lang": "en", "text": "Bearing plus distance. One bearing to a known object combined with a distance measurement gives you a position fix."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Koppelnavigation als Grundlage, aber regelmäßig mit Kreuzpeilungen oder Radar korrigieren. Immer mindestens zwei Standlinien für eine Positionsbestimmung."}
]

# ============================================================
# 1.6a — Radar
# ============================================================
scripts["script_1_6a.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Radar — das Auge bei Nacht und Nebel. Radar steht für Radio Detection And Ranging, also Funkortung und Entfernungsmessung."},
    {"speaker": "george", "lang": "en", "text": "Radar. Radio Detection And Ranging. Sends microwave pulses, measures reflected echoes. Works in darkness, fog, and rain."},
    {"speaker": "dieter", "lang": "de", "text": "So funktioniert es: Der Sender schickt kurze Mikrowellenimpulse über eine drehende Antenne. Die Impulse treffen auf Objekte und werden reflektiert. Aus der Zeitverzögerung berechnet das Radar die Entfernung."},
    {"speaker": "dieter", "lang": "de", "text": "Auf dem Bildschirm ist dein Boot in der Mitte. Andere Schiffe, Land und Bojen erscheinen als helle Punkte. Das zeigt dir Entfernung und Richtung zu jedem Objekt."},
    {"speaker": "george", "lang": "en", "text": "Range: distance to a target, from echo delay. Bearing: direction to a target, from antenna position. Display shows your vessel at center, targets as bright dots."},
    {"speaker": "dieter", "lang": "de", "text": "Moderne Radargeräte haben ARPA — das steht für Automatic Radar Plotting Aid. ARPA verfolgt andere Schiffe automatisch und berechnet, ob Kollisionsgefahr besteht."},
    {"speaker": "george", "lang": "en", "text": "ARPA. Automatic Radar Plotting Aid. Tracks targets, calculates their course and speed. Shows CPA — closest point of approach — and TCPA — time to closest point of approach."},
    {"speaker": "dieter", "lang": "de", "text": "CPA ist der nächste Passierabstand — also wie nah dir ein anderes Schiff kommen wird. TCPA ist die Zeit bis dahin. Beides entscheidend um Kollisionen zu vermeiden."},
    {"speaker": "dieter", "lang": "de", "text": "Aber Radar hat Grenzen. Schattenbereich hinter dem Mast, Falschechos von Wellen und Regen, und kleine Holz- oder GFK-Boote reflektieren schlecht."},
    {"speaker": "george", "lang": "en", "text": "Radar limitations: shadow sectors behind the mast, sea clutter from waves, rain clutter, and small wooden or fiberglass boats may not appear. Never rely on radar alone."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Radar zeigt Entfernung und Richtung zu Objekten. ARPA berechnet Kollisionsrisiko mit CPA und TCPA. Aber Radar hat Grenzen — immer auch visuellen Ausguck halten!"}
]

# ============================================================
# 1.6b — GPS, Echo Sounder, Autopilot
# ============================================================
scripts["script_1_6b.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "GPS, Echolot und Autopilot — die drei elektronischen Helfer, die auf fast jedem Boot zu finden sind."},
    {"speaker": "george", "lang": "en", "text": "GPS. Global Positioning System. Satellite navigation providing position, speed, and time. Accuracy about ten to fifteen meters."},
    {"speaker": "dieter", "lang": "de", "text": "GPS empfängt Signale von mindestens vier Satelliten und berechnet daraus deine Position auf zehn bis fünfzehn Meter genau. Es zeigt dir auch Geschwindigkeit über Grund und Kurs über Grund."},
    {"speaker": "dieter", "lang": "de", "text": "Auf Englisch heißt Geschwindigkeit über Grund S O G — Speed Over Ground. Und Kurs über Grund C O G — Course Over Ground."},
    {"speaker": "george", "lang": "en", "text": "SOG — speed over ground. COG — course over ground. Both measured by GPS from position changes. Important: these are ground-referenced, not water-referenced."},
    {"speaker": "dieter", "lang": "de", "text": "Das ist ein wichtiger Unterschied! GPS zeigt die Bewegung über GRUND. Aber Wind und Strömung können dein Boot vom Kurs durchs Wasser ablenken. Deshalb: GPS allein reicht nicht."},
    {"speaker": "dieter", "lang": "de", "text": "Das Echolot misst die Wassertiefe unter dem Boot. Es sendet Schallimpulse zum Meeresboden und misst die Rücklaufzeit. Auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Echo sounder or depth sounder. Sends sound pulses to the seabed, measures return time to calculate depth. Essential in shallow waters."},
    {"speaker": "dieter", "lang": "de", "text": "Und der Autopilot steuert das Boot automatisch auf einem eingestellten Kurs. Er ist mit dem Kompass oder GPS verbunden. Aber Achtung: auch mit Autopilot musst du immer Ausguck halten!"},
    {"speaker": "george", "lang": "en", "text": "Autopilot. Automatically steers the vessel on a set course. Connected to compass or GPS. The skipper must still maintain lookout at all times."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: GPS für Position und Geschwindigkeit über Grund, Echolot für Wassertiefe, Autopilot für automatische Kurssteuerung. Aber nie blind auf Elektronik verlassen!"}
]

# ============================================================
# 1.7 — Voyage Planning
# ============================================================
scripts["script_1_7.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Törnplanung — bevor du den Hafen verlässt, musst du deine Reise gründlich planen. Das ist Pflicht und kann in der Prüfung abgefragt werden."},
    {"speaker": "george", "lang": "en", "text": "Passage planning. A detailed plan for a voyage including route, waypoints, weather, tides, fuel, and safety. Must be prepared before departure."},
    {"speaker": "dieter", "lang": "de", "text": "Die wichtigsten Schritte: Erstens, wähle die richtigen Seekarten und prüfe, ob sie aktuell sind. Zweitens, zeichne die Route ein und markiere Wegpunkte."},
    {"speaker": "dieter", "lang": "de", "text": "Drittens, prüfe den Wetterbericht für die gesamte Reisedauer. Viertens, berechne den Treibstoffbedarf. Und hier gilt die Drittel-Regel:"},
    {"speaker": "george", "lang": "en", "text": "The rule of thirds for fuel: one-third for the outward journey, one-third for the return, one-third as reserve. Always carry at least thirty-three percent more fuel than calculated."},
    {"speaker": "dieter", "lang": "de", "text": "Ein Drittel hin, ein Drittel zurück, ein Drittel Reserve. Also mindestens dreiunddreißig Prozent mehr Treibstoff als berechnet."},
    {"speaker": "dieter", "lang": "de", "text": "Fünftens, prüfe die Sicherheitsausrüstung und weise die Crew in Notfallverfahren ein. Sechstens, teste den Funk und informiere jemanden an Land über deine Pläne."},
    {"speaker": "george", "lang": "en", "text": "Before departure: check charts, plot route, check weather, calculate fuel, inspect safety equipment, test VHF radio, inform someone ashore."},
    {"speaker": "dieter", "lang": "de", "text": "Bei der Routenwahl: Wähle die sicherste Route, nicht nur die kürzeste. Plane Alternative-Häfen entlang der Strecke ein, falls das Wetter umschlägt. Und bei unbekanntem Hafen: vor Einbruch der Dunkelheit ankommen!"},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Karten prüfen, Route planen, Wetter checken, Treibstoff nach Drittel-Regel, Sicherheitsausrüstung kontrollieren, Funk testen, Plan an Land mitteilen."}
]

# ============================================================
# 2.2 — Engine Systems & Maintenance
# ============================================================
scripts["script_2_2.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Motorsysteme und Wartung. Der Motor ist das Herz deines Bootes — wenn er ausfällt, hast du ein ernstes Problem. Deshalb ist die richtige Wartung so wichtig."},
    {"speaker": "george", "lang": "en", "text": "Engine systems and maintenance. Cooling system, fuel system, and pre-departure checks."},
    {"speaker": "dieter", "lang": "de", "text": "Fangen wir mit dem Kühlsystem an. Bootsmotoren werden mit Seewasser gekühlt. Es gibt zwei Systeme:"},
    {"speaker": "dieter", "lang": "de", "text": "Erstens, direkte Kühlung: Seewasser wird direkt durch den Motor gepumpt. Einfach, aber Salzablagerungen und Korrosion sind ein Problem."},
    {"speaker": "george", "lang": "en", "text": "Direct cooling: seawater pumped directly through the engine. Simple but risk of salt deposits and corrosion."},
    {"speaker": "dieter", "lang": "de", "text": "Zweitens, indirekte Kühlung: Ein geschlossener Süßwasserkreislauf kühlt den Motor, und Seewasser kühlt das Süßwasser über einen Wärmetauscher. Besser für den Motor."},
    {"speaker": "george", "lang": "en", "text": "Indirect cooling: closed freshwater circuit cools the engine. Seawater cools the freshwater through a heat exchanger. Less corrosion, better for the engine."},
    {"speaker": "dieter", "lang": "de", "text": "Das wichtigste Verschleißteil ist der Impeller — das Gummi-Pumpenrad in der Seekühlwasserpumpe. Wenn der kaputt geht, überhitzt der Motor sofort. Deshalb: jährlich wechseln!"},
    {"speaker": "george", "lang": "en", "text": "Impeller. The rubber pump wheel in the seawater cooling pump. Most common cause of overheating. Replace annually. Always carry a spare."},
    {"speaker": "dieter", "lang": "de", "text": "Ein einfacher Test: Kommt Wasser aus dem Auspuff? Wenn ja, die Kühlung funktioniert. Wenn nicht, sofort Motor abstellen und Ursache suchen!"},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt die Checkliste vor jeder Abfahrt: Motoröl am Peilstab prüfen. Kühlmittel kontrollieren. Treibstoff ausreichend? Keilriemen gespannt und ohne Risse?"},
    {"speaker": "george", "lang": "en", "text": "Pre-departure checks: oil level, coolant level, fuel quantity, drive belts, seawater intake valve open, strainer clean. After starting: check water exhaust, oil pressure, temperature."},
    {"speaker": "dieter", "lang": "de", "text": "Seekühlwasser-Ventil offen? Seiher sauber? Bilge auf Lecks prüfen. Propeller auf Leinen oder Müll kontrollieren. Und nach dem Starten: Wasserfluss am Auspuff, Öldruck und Temperatur."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Impeller jährlich wechseln, Wasserfluss am Auspuff kontrollieren, vor jeder Fahrt die Checkliste durchgehen. Ein gut gewarteter Motor ist ein zuverlässiger Motor."}
]

# ============================================================
# 3.2 — Registration & Documents
# ============================================================
scripts["script_3_2.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Registrierung und Dokumente. Was du an Bord haben musst, wenn du in Kroatien fährst — und was die Hafenpolizei bei einer Kontrolle sehen will."},
    {"speaker": "george", "lang": "en", "text": "Required documents for Croatian waters. Registration certificate, boat license, crew list, vignette, insurance, and radio license."},
    {"speaker": "dieter", "lang": "de", "text": "Der Bootsführerschein heißt in Kroatien Voditelj Brodice, Kategorie C. Damit darfst du Boote bis dreißig Bruttotonnen in Küstengewässern fahren."},
    {"speaker": "george", "lang": "en", "text": "Voditelj Brodice, Category C. Croatian boat license for vessels up to thirty gross tons in coastal waters. Oral exam in English."},
    {"speaker": "dieter", "lang": "de", "text": "Für ausländische Boote gibt es die Vignette — eine Jahresfahrerlaubnis die du innerhalb von achtundvierzig Stunden nach Ankunft kaufen musst."},
    {"speaker": "george", "lang": "en", "text": "Vignette. Annual cruising permit for foreign vessels. Must be purchased within forty-eight hours of entering Croatian waters."},
    {"speaker": "dieter", "lang": "de", "text": "Was muss alles an Bord sein? Registrierungsbescheinigung, Bootsführerschein, Crewliste mit Passnummern, Vignette, Haftpflichtversicherung, und Funklizenz wenn ein VHF-Radio installiert ist."},
    {"speaker": "dieter", "lang": "de", "text": "Boote müssen auch regelmäßig inspiziert werden. Bis zwanzig Jahre alt: alle fünf Jahre. Über zwanzig Jahre: alle zwei Jahre."},
    {"speaker": "george", "lang": "en", "text": "Boat inspections: up to twenty years old, every five years. Over twenty years, every two years. Checks hull, engine, safety equipment, lights, electrical systems."},
    {"speaker": "dieter", "lang": "de", "text": "Die Hafenpolizei kann jederzeit kontrollieren. Halte alle Dokumente griffbereit. Fehlende Dokumente bedeuten Geldstrafen."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Voditelj Brodice Kat C, Vignette innerhalb achtundvierzig Stunden, alle Dokumente griffbereit an Bord, regelmäßige Bootsinspektionen."}
]

# ============================================================
# 4.1 — Boat Types, Equipment & Flags
# ============================================================
scripts["script_4_1.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Bootstypen, Ausrüstung und Flaggen. Was du über verschiedene Rumpfformen, Pflichtausrüstung und Flaggenführung wissen musst."},
    {"speaker": "george", "lang": "en", "text": "Boat types and equipment. Displacement hulls, planing hulls, required safety equipment, and flags."},
    {"speaker": "dieter", "lang": "de", "text": "Zwei grundlegende Rumpfarten: Der Verdränungsrumpf — er schiebt sich durchs Wasser. Segelboote und schwere Motorboote haben so einen Rumpf. Die Geschwindigkeit ist begrenzt durch die Wasserlinie."},
    {"speaker": "george", "lang": "en", "text": "Displacement hull. Moves through the water, pushing it aside. Speed limited by waterline length. More fuel-efficient at lower speeds."},
    {"speaker": "dieter", "lang": "de", "text": "Und der Gleitrumpf — bei höherer Geschwindigkeit hebt er sich aus dem Wasser und gleitet auf der Oberfläche. Schnellboote und kleine Motorboote. Braucht viel mehr Leistung, ist aber deutlich schneller."},
    {"speaker": "george", "lang": "en", "text": "Planing hull. Lifts and glides on the water surface at speed. Used by speedboats. Requires more power but much faster."},
    {"speaker": "dieter", "lang": "de", "text": "In Kroatien unterscheidet das Gesetz: Ein Boot — brodica — ist bis zwölf Meter lang und bis dreißig GT. Eine Yacht ist über zwölf Meter oder über dreißig GT."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt zur Pflichtausrüstung. Rettungswesten für JEDE Person an Bord, mindestens ein Rettungsring, sechs rote Handfackeln, Feuerlöscher, Erste-Hilfe-Kasten, Signalhorn und Taschenlampe."},
    {"speaker": "george", "lang": "en", "text": "Required equipment: life jackets for all persons, lifebuoy, six red hand flares, fire extinguisher, first aid kit, sound signal device, flashlight, anchor with line, bilge pump, navigation lights."},
    {"speaker": "dieter", "lang": "de", "text": "Bei den Flaggen: Die Nationalflagge am Heck zeigt deine Bootsnationalität. Die Gastlandflagge — in Kroatien also die kroatische Flagge — wird an der Steuerbord-Saling gefahren."},
    {"speaker": "george", "lang": "en", "text": "National flag at the stern. Courtesy flag — the flag of the country you are visiting — on the starboard spreader. Q flag — yellow — means you request health clearance when entering a country."},
    {"speaker": "dieter", "lang": "de", "text": "Die gelbe Q-Flagge zeigst du beim Einlaufen in ein fremdes Land: Ich bitte um Gesundheitsfreigabe. Die Tauchflagge — rot mit weißem Diagonal — bedeutet: Taucher im Wasser, fünfzig Meter Abstand halten!"},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Verdränger fährt durchs Wasser, Gleiter gleitet drauf. Pflichtausrüstung unbedingt vollständig und in Ordnung. Nationalflagge am Heck, Gastlandflagge an Steuerbord."}
]

# ============================================================
# 7.2 — Clouds, Fog, Tides & Forecasting
# ============================================================
scripts["script_7_2.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Wolken, Gezeiten und Wettervorhersage. Wer die Wolken lesen kann, wird vom Wetter nicht überrascht."},
    {"speaker": "george", "lang": "en", "text": "Clouds, tides, and weather forecasting. The Beaufort scale. Cloud types and what they tell you about coming weather."},
    {"speaker": "dieter", "lang": "de", "text": "Die Beaufort-Skala kennt jeder Seemann. Sie reicht von null — Windstille — bis zwölf — Orkan. Für die Prüfung solltest du die wichtigsten Stufen kennen:"},
    {"speaker": "george", "lang": "en", "text": "Beaufort scale: zero is calm. Four is moderate breeze, eleven to sixteen knots. Seven is near gale, twenty-eight to thirty-three knots. Ten is storm, forty-eight to fifty-five knots."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt zu den Wolken. Cirrus — hoch, dünn, federartig. Sieht nach schönem Wetter aus, kann aber eine Warmfront ankündigen, also Regen in ein bis zwei Tagen."},
    {"speaker": "dieter", "lang": "de", "text": "Cumulus — die weißen Schäfchenwolken. Wenn sie klein und vereinzelt sind: schönes Wetter. Wenn sie wachsen und sich auftürmen: Vorsicht!"},
    {"speaker": "george", "lang": "en", "text": "Cumulonimbus. The thunderstorm cloud. Towering vertical development. DANGER: strong gusts, lightning, heavy rain, and waterspouts."},
    {"speaker": "dieter", "lang": "de", "text": "Cumulonimbus ist die Gewitterwolke — riesig, türmt sich auf wie ein Amboss. Wenn du die siehst: Sofort Schutz suchen! Sturmböen, Blitz, Starkregen, möglicherweise Wasserhosen."},
    {"speaker": "dieter", "lang": "de", "text": "Stratus — tief, grau, flach wie eine Decke. Bringt Nieselregen und schlechte Sicht. Nimbostratus — dick und dunkel, bringt Dauerregen."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt zu den Gezeiten in der Adria. Die sind relativ gering — durchschnittlich nur dreißig bis fünfzig Zentimeter Tidenhub."},
    {"speaker": "george", "lang": "en", "text": "Tides in the Adriatic: average range zero point three to zero point five meters. Spring tides during full and new moon: up to one meter. Semi-diurnal: two high and two low tides per day."},
    {"speaker": "dieter", "lang": "de", "text": "Springtide bei Voll- und Neumond — da ist der Tidenhub am größten. Nipptide bei Halbmond — da ist er am kleinsten. Das hat nichts mit der Jahreszeit zu tun!"},
    {"speaker": "dieter", "lang": "de", "text": "Wetterinformationen bekommst du über VHF Kanal siebenundsechzig und dreiundsiebzig von der kroatischen Küstenwache, über NAVTEX, oder online über Windy und andere Apps."},
    {"speaker": "george", "lang": "en", "text": "Weather sources: VHF Channel sixty-seven and seventy-three, NAVTEX, internet forecasts. A falling barometer means bad weather approaching."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Beaufort-Skala lernen, Cumulonimbus bedeutet Gefahr, Gezeiten in der Adria sind gering aber beachten, und immer den Wetterbericht prüfen!"}
]

# ============================================================
# 9.2 — Navigation Lights & Signals
# ============================================================
scripts["script_9_2.json"] = [
    {"speaker": "dieter", "lang": "de", "text": "Navigationslichter und Signale. Nachts auf See erkennst du andere Schiffe nur an ihren Lichtern — deshalb ist das ein zentrales Prüfungsthema."},
    {"speaker": "george", "lang": "en", "text": "Navigation lights and sound signals. Required between sunset and sunrise and in reduced visibility. Defined by COLREGS."},
    {"speaker": "dieter", "lang": "de", "text": "Jedes Boot zeigt drei Grundlichter: Das Topplicht — weiß am Mast, sichtbar von vorn. Seitenlichter — rot an Backbord, grün an Steuerbord. Und das Hecklicht — weiß am Heck."},
    {"speaker": "george", "lang": "en", "text": "Masthead light: white, forward, two hundred twenty-five degree arc. Sidelights: red on port, green on starboard, each one hundred twelve point five degrees. Stern light: white, aft, one hundred thirty-five degrees."},
    {"speaker": "dieter", "lang": "de", "text": "Und jetzt der wichtigste Teil: Was du SIEHST, sagt dir was passiert. Wenn du BEIDE Seitenlichter und das Topplicht siehst — rot und grün nebeneinander — dann kommt ein Schiff DIREKT auf dich zu!"},
    {"speaker": "dieter", "lang": "de", "text": "Siehst du nur das ROTE Seitenlicht plus Topplicht — dann kreuzt ein Maschinenfahrzeug von rechts nach links."},
    {"speaker": "george", "lang": "en", "text": "Red sidelight plus masthead light: vessel crossing from your right to left. Green sidelight plus masthead light: vessel crossing from left to right. Stern light only: vessel moving away."},
    {"speaker": "dieter", "lang": "de", "text": "Ein Segelboot unter Segeln zeigt KEIN Topplicht! Nur Seitenlichter und Hecklicht. Optional rot über grün am Mast. Merkspruch auf Englisch:"},
    {"speaker": "george", "lang": "en", "text": "Red over green, sailing machine. A sailing vessel may show red over green all-round lights at the masthead. But NO masthead light — that would indicate engine power."},
    {"speaker": "dieter", "lang": "de", "text": "Vor Anker: nur ein weißes Rundumlicht. Manövrierunfähig: zwei rote Rundumlichter übereinander. Fischend: rot über weiß."},
    {"speaker": "dieter", "lang": "de", "text": "Jetzt zu den Schallsignalen. Ein kurzer Ton: Ich drehe nach Steuerbord. Zwei kurze Töne: Ich drehe nach Backbord. Drei kurze Töne: Meine Maschine geht rückwärts."},
    {"speaker": "george", "lang": "en", "text": "One short blast: turning to starboard. Two short blasts: turning to port. Three short blasts: engines going astern. Five short blasts: danger signal — I doubt your intentions."},
    {"speaker": "dieter", "lang": "de", "text": "Fünf kurze Töne — das ist das Gefahrensignal. Das heißt: Ich verstehe deine Absichten nicht, oder du fährst in eine Gefahr!"},
    {"speaker": "dieter", "lang": "de", "text": "Bei Nebel gibt es besondere Signale, alle zwei Minuten: Maschinenfahrzeug in Fahrt: ein langer Ton. Gestoppt: zwei lange Töne. Segler oder Fischer: ein langer und zwei kurze Töne."},
    {"speaker": "george", "lang": "en", "text": "Fog signals every two minutes. Power vessel making way: one prolonged blast. Stopped: two prolonged blasts. Sailing vessel: one prolonged plus two short blasts."},
    {"speaker": "dieter", "lang": "de", "text": "Zusammenfassung: Topplicht zeigt Maschinenantrieb, Segler hat kein Topplicht. Rotes Seitenlicht heißt: die Backbordseite zeigt zu dir. Fünf kurze Töne bedeuten Gefahr!"}
]

# ============================================================
# Write all script files
# ============================================================
for filename, segments in scripts.items():
    filepath = os.path.join(SCRIPTS_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(segments, f, indent=2, ensure_ascii=False)
    print(f"  {filename}: {len(segments)} segments")

print(f"\nTotal: {len(scripts)} scripts")
print(f"Total segments: {sum(len(s) for s in scripts.values())}")
