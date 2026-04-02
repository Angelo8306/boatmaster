#!/usr/bin/env python3
"""Create all missing unit JSON files from chapter source material."""

import json
import os

UNITS_DIR = "/Users/angelojuric/Documents/Bootsführerschein/content/units"

units = {}

# ============================================================
# UNIT 1.2a — IALA Buoyage System - Lights & Lateral Marks
# ============================================================
units["unit_1_2a.json"] = [
    {
        "type": "vocab",
        "term_en": "Fairway",
        "definition_en": "A sea belt sufficiently deep and wide for safe navigation, marked with proper markings. In Croatia, maintained by Plovput company in Split.",
        "term_de": "Fahrrinne / Fahrwasser",
        "definition_de": "Ein ausreichend tiefer und breiter Meeresstreifen fuer sichere Schifffahrt, mit entsprechenden Markierungen. In Kroatien von der Firma Plovput in Split betreut."
    },
    {
        "type": "vocab",
        "term_en": "Lateral Marks",
        "definition_en": "Buoys marking the sides of a navigable channel. In IALA Region A (Europe/Croatia): red marks on port (left) side, green marks on starboard (right) side when entering from sea.",
        "term_de": "Lateralzeichen / Seitenmarkierungen",
        "definition_de": "Bojen, die die Seiten einer Fahrrinne markieren. In IALA Region A (Europa/Kroatien): rote Zeichen an Backbord (links), gruene an Steuerbord (rechts) bei Einfahrt von See.",
        "image": "p019_img00.jpeg"
    },
    {
        "type": "vocab",
        "term_en": "Light Characteristics",
        "definition_en": "The pattern of a navigation light: Fixed (F), Flashing (Fl), Quick flashing (Q), Occulting (Oc), Isophase (Iso), Group flashing (e.g. Fl(2)). Each buoy has a unique rhythm for identification at night.",
        "term_de": "Lichtkennung",
        "definition_de": "Das Muster eines Navigationslichts: Festfeuer (F), Blinkfeuer (Fl), Schnelles Blinkfeuer (Q), Unterbrochenes Feuer (Oc), Gleichtaktfeuer (Iso), Gruppen-Blinkfeuer (z.B. Fl(2))."
    },
    {
        "type": "learn",
        "title_en": "IALA Region A — The Basic Rule",
        "content_en": "In IALA Region A (Europe, Africa, Asia, Australia — including Croatia):\n\n• RED buoys on PORT (left) side when entering from sea\n• GREEN buoys on STARBOARD (right) side when entering from sea\n\nRemember: 'Red to port when returning from sea'\n\nPort-hand marks: red color, can-shaped (cylindrical), red light\nStarboard-hand marks: green color, cone-shaped (conical), green light",
        "content_de": "In IALA Region A (Europa, Afrika, Asien, Australien — einschliesslich Kroatien):\n\n• ROTE Bojen an BACKBORD (links) bei Einfahrt von See\n• GRUENE Bojen an STEUERBORD (rechts) bei Einfahrt von See\n\nMerke: 'Rot an Backbord bei Einfahrt'\n\nBackbord-Zeichen: rote Farbe, zylindrisch (Tonne), rotes Licht\nSteuerbord-Zeichen: gruene Farbe, kegelfoermig (Spitztonne), gruenes Licht",
        "image": "p019_img02.png"
    },
    {
        "type": "learn",
        "title_en": "Preferred Channel Marks",
        "content_en": "Where a channel divides into two branches, preferred channel marks show the main (more important) channel:\n\n• Preferred channel to starboard: Red buoy with green horizontal band — treat as port-hand mark\n• Preferred channel to port: Green buoy with red horizontal band — treat as starboard-hand mark\n\nThe main color tells you which side the mark belongs to. The horizontal band indicates it's a modified lateral mark.",
        "content_de": "Wo sich eine Fahrrinne in zwei Arme teilt, zeigen Bevorzugte-Fahrwasser-Zeichen den Hauptkanal:\n\n• Bevorzugter Kanal an Steuerbord: Rote Boje mit gruenem Querstreifen — als Backbord-Zeichen behandeln\n• Bevorzugter Kanal an Backbord: Gruene Boje mit rotem Querstreifen — als Steuerbord-Zeichen behandeln\n\nDie Hauptfarbe zeigt die Seite. Der Querstreifen zeigt ein modifiziertes Lateralzeichen an."
    },
    {
        "type": "learn",
        "title_en": "Light Rhythms for Identification",
        "content_en": "Navigation lights use specific rhythms:\n\n• Fixed (F) — continuous steady light\n• Flashing (Fl) — duration of light shorter than dark\n• Quick (Q) — 50-79 flashes per minute\n• Very Quick (VQ) — 80-159 flashes per minute\n• Occulting (Oc) — duration of light longer than dark\n• Isophase (Iso) — equal light and dark periods\n• Long flash (LFl) — flash of 2+ seconds\n\nEvery light has: color, period (time for one complete cycle), range (visibility distance in nautical miles).",
        "content_de": "Navigationslichter verwenden bestimmte Rhythmen:\n\n• Festfeuer (F) — durchgehend\n• Blinkfeuer (Fl) — Lichtdauer kuerzer als Dunkelphase\n• Schnelles Blinkfeuer (Q) — 50-79 Blitze pro Minute\n• Sehr schnelles Blinkfeuer (VQ) — 80-159 Blitze pro Minute\n• Unterbrochenes Feuer (Oc) — Lichtdauer laenger als Dunkelphase\n• Gleichtaktfeuer (Iso) — gleiche Licht- und Dunkelphasen\n• Langes Blinkfeuer (LFl) — Blitz von 2+ Sekunden",
        "image": "p017_img01.png"
    },
    {
        "type": "quiz",
        "question_en": "In IALA Region A, when entering a harbor from sea, which color are the buoys on the port (left) side?",
        "question_de": "In IALA Region A, welche Farbe haben die Bojen an Backbord (links) bei der Einfahrt von See?",
        "options": [
            {"text": "Green", "correct": False},
            {"text": "Red", "correct": True},
            {"text": "Yellow", "correct": False},
            {"text": "Black", "correct": False}
        ],
        "explanation_en": "In IALA Region A (used in Croatia and all of Europe): Red buoys mark the port (left) side when entering from sea. Remember: 'Red to port when returning.'",
        "explanation_de": "In IALA Region A (Kroatien und ganz Europa): Rote Bojen markieren die Backbordseite (links) bei Einfahrt von See. Merke: 'Rot an Backbord bei Einfahrt.'"
    },
    {
        "type": "quiz",
        "question_en": "What does a red buoy with a green horizontal band indicate?",
        "question_de": "Was bedeutet eine rote Boje mit einem gruenen Querstreifen?",
        "options": [
            {"text": "Isolated danger", "correct": False},
            {"text": "Safe water mark", "correct": False},
            {"text": "Preferred channel to starboard", "correct": True},
            {"text": "Special mark", "correct": False}
        ],
        "explanation_en": "A red buoy with a green band is a preferred channel mark indicating the main channel is to starboard. The main color (red) tells you it's on the port side; the band means the channel splits here.",
        "explanation_de": "Eine rote Boje mit gruenem Streifen ist ein Bevorzugtes-Fahrwasser-Zeichen — der Hauptkanal liegt an Steuerbord. Die Hauptfarbe (rot) zeigt Backbord; der Streifen zeigt die Kanalverzweigung."
    },
    {
        "type": "quiz_free",
        "question_en": "Explain the difference between flashing (Fl) and occulting (Oc) light characteristics.",
        "question_de": "Erklaere den Unterschied zwischen Blinkfeuer (Fl) und unterbrochenem Feuer (Oc).",
        "model_answer_en": "Flashing (Fl) means the duration of light is shorter than the duration of darkness — the light flashes briefly in periods of darkness. Occulting (Oc) is the opposite: the duration of light is longer than darkness — it's a steady light that is briefly interrupted by dark periods. Both are used to identify navigation marks at night, with specific patterns unique to each mark.",
        "model_answer_de": "Blinkfeuer (Fl) bedeutet, dass die Lichtdauer kuerzer ist als die Dunkelphase — das Licht blitzt kurz in Dunkelphasen auf. Unterbochenes Feuer (Oc) ist das Gegenteil: die Lichtdauer ist laenger als die Dunkelphase — ein stetiges Licht wird kurz unterbrochen. Beide werden zur Identifikation von Seezeichen bei Nacht verwendet."
    }
]

# ============================================================
# UNIT 1.2b — IALA Cardinal & Special Marks
# ============================================================
units["unit_1_2b.json"] = [
    {
        "type": "vocab",
        "term_en": "Cardinal Marks",
        "definition_en": "Buoys placed around a danger showing where safe water lies, named after compass directions: North, South, East, West. Colors are black and yellow.",
        "term_de": "Kardinalzeichen",
        "definition_de": "Bojen um eine Gefahr herum, die zeigen wo sicheres Wasser ist. Benannt nach Himmelsrichtungen: Nord, Sued, Ost, West. Farben: Schwarz und Gelb.",
        "image": "p022_img00.png"
    },
    {
        "type": "vocab",
        "term_en": "Isolated Danger Mark",
        "definition_en": "A mark placed directly on or above a danger with navigable water all around. Black with red horizontal bands, top mark: two black spheres.",
        "term_de": "Einzelgefahrenzeichen",
        "definition_de": "Ein Zeichen direkt ueber einer Gefahr, mit befahrbarem Wasser rundherum. Schwarz mit roten Querstreifen, Toppzeichen: zwei schwarze Baelle.",
        "image": "p022_img01.png"
    },
    {
        "type": "vocab",
        "term_en": "Safe Water Mark",
        "definition_en": "Indicates navigable water around the mark (mid-channel or fairway). Red and white vertical stripes, spherical shape, top mark: single red sphere.",
        "term_de": "Sicheres-Wasser-Zeichen",
        "definition_de": "Zeigt befahrbares Wasser rundherum an (Fahrwassermitte). Rote und weisse Laengsstreifen, kugelfoermig, Toppzeichen: einzelne rote Kugel."
    },
    {
        "type": "learn",
        "title_en": "Cardinal Marks — How to Remember",
        "content_en": "Cardinal marks use black and yellow — the position of BLACK tells you the direction:\n\n• NORTH: Black on TOP — points up (pass to the north)\n• SOUTH: Black on BOTTOM — points down (pass to the south)\n• EAST: Black on TOP and BOTTOM — (pass to the east)\n• WEST: Black in the MIDDLE — like a waistband (pass to the west)\n\nTop marks are two black cones:\n• North: both pointing UP\n• South: both pointing DOWN\n• East: base to base (diamond shape)\n• West: point to point (hourglass shape)",
        "content_de": "Kardinalzeichen verwenden Schwarz und Gelb — die Position von SCHWARZ zeigt die Richtung:\n\n• NORD: Schwarz OBEN — zeigt nach oben\n• SUED: Schwarz UNTEN — zeigt nach unten\n• OST: Schwarz OBEN und UNTEN\n• WEST: Schwarz in der MITTE — wie ein Guertel\n\nToppzeichen sind zwei schwarze Kegel:\n• Nord: beide nach OBEN\n• Sued: beide nach UNTEN\n• Ost: Basis an Basis (Rautenform)\n• West: Spitze an Spitze (Sanduhrform)",
        "image": "p022_img03.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Cardinal Mark Lights",
        "content_en": "Cardinal marks use white lights with quick (Q) or very quick (VQ) flashing:\n\n• North: Continuous quick flashing — Q or VQ (uninterrupted)\n• East: Groups of 3 — Q(3) or VQ(3) — think '3 o'clock = East'\n• South: Groups of 6 + long flash — Q(6)+LFl or VQ(6)+LFl — '6 o'clock = South'\n• West: Groups of 9 — Q(9) or VQ(9) — '9 o'clock = West'\n\nClock trick: East=3, South=6, West=9, North=continuous (12=all)",
        "content_de": "Kardinalzeichen verwenden weisse Lichter mit schnellem (Q) oder sehr schnellem (VQ) Blinken:\n\n• Nord: Durchgehend schnell — Q oder VQ (ununterbrochen)\n• Ost: Gruppen von 3 — Q(3) oder VQ(3) — '3 Uhr = Ost'\n• Sued: Gruppen von 6 + Langblitz — Q(6)+LFl — '6 Uhr = Sued'\n• West: Gruppen von 9 — Q(9) oder VQ(9) — '9 Uhr = West'\n\nUhr-Trick: Ost=3, Sued=6, West=9, Nord=durchgehend"
    },
    {
        "type": "learn",
        "title_en": "Special Marks",
        "content_en": "Yellow marks for special areas, not primarily for navigation:\n• Indicate special areas: military exercise zones, water ski areas, swimming zones, cable/pipeline areas, nature reserves\n• Color: Yellow\n• Shape: X-shaped top mark\n• Light: Yellow, any rhythm not used by other marks\n\nAlso: Emergency Wreck Marking Buoy — alternating blue and yellow vertical stripes, flashing alternating blue and yellow light.",
        "content_de": "Gelbe Zeichen fuer Sondergebiete, nicht primaer zur Navigation:\n• Kennzeichnen: Militaerische Uebungsgebiete, Wasserskizonen, Schwimmzonen, Kabel-/Pipelinebereiche, Naturschutzgebiete\n• Farbe: Gelb\n• Form: X-foermiges Toppzeichen\n• Licht: Gelb, jeder Rhythmus der nicht von anderen Zeichen verwendet wird\n\nAuch: Notfall-Wrack-Markierung — abwechselnd blaue und gelbe Laengsstreifen."
    },
    {
        "type": "quiz",
        "question_en": "A cardinal mark has black on top and yellow on bottom. Which direction should you pass it?",
        "question_de": "Ein Kardinalzeichen hat Schwarz oben und Gelb unten. In welche Richtung sollst du es passieren?",
        "options": [
            {"text": "Pass to the South", "correct": False},
            {"text": "Pass to the North", "correct": True},
            {"text": "Pass to the East", "correct": False},
            {"text": "Pass to the West", "correct": False}
        ],
        "explanation_en": "Black on top = North cardinal mark. The safe water is to the NORTH of the mark. Remember: black points up = north.",
        "explanation_de": "Schwarz oben = Nord-Kardinalzeichen. Das sichere Wasser liegt NOERDLICH des Zeichens. Merke: Schwarz zeigt nach oben = Nord."
    },
    {
        "type": "quiz",
        "question_en": "How many flashes does an East cardinal mark show?",
        "question_de": "Wie viele Blitze zeigt ein Ost-Kardinalzeichen?",
        "options": [
            {"text": "Continuous", "correct": False},
            {"text": "3 flashes", "correct": True},
            {"text": "6 flashes + long flash", "correct": False},
            {"text": "9 flashes", "correct": False}
        ],
        "explanation_en": "East = 3 flashes (clock trick: 3 o'clock = East). North = continuous, South = 6+long flash, West = 9.",
        "explanation_de": "Ost = 3 Blitze (Uhr-Trick: 3 Uhr = Ost). Nord = durchgehend, Sued = 6+Langblitz, West = 9."
    },
    {
        "type": "quiz_free",
        "question_en": "Describe an isolated danger mark: its colors, top mark, and what it indicates.",
        "question_de": "Beschreibe ein Einzelgefahrenzeichen: Farben, Toppzeichen und was es anzeigt.",
        "model_answer_en": "An isolated danger mark is placed directly on or above a danger such as an underwater rock or wreck. It has navigable water all around it, so you can pass on any side. Colors: black with one or more red horizontal bands. Top mark: two black spheres, one above the other. Light: white, group flashing two — Fl(2).",
        "model_answer_de": "Ein Einzelgefahrenzeichen steht direkt ueber einer Gefahr wie einem Unterwasserfelsen oder Wrack. Es hat befahrbares Wasser rundherum, man kann auf jeder Seite passieren. Farben: Schwarz mit roten Querstreifen. Toppzeichen: zwei schwarze Kugeln uebereinander. Licht: Weiss, Gruppen-Blinkfeuer zwei — Fl(2)."
    }
]

# ============================================================
# UNIT 1.3b — Compass, Course & Azimuth
# ============================================================
units["unit_1_3b.json"] = [
    {
        "type": "vocab",
        "term_en": "Compass Rose",
        "definition_en": "A circle on a chart showing directions. Has an outer ring for true directions (geographic) and an inner ring for magnetic directions. Shows magnetic variation.",
        "term_de": "Kompassrose",
        "definition_de": "Ein Kreis auf der Seekarte mit Richtungsangaben. Aeusserer Ring fuer rechtweisende (geographische) Richtungen, innerer Ring fuer missweisende (magnetische) Richtungen."
    },
    {
        "type": "vocab",
        "term_en": "Magnetic Variation / Declination",
        "definition_en": "The angle between true north and magnetic north at a given location. Changes slowly over time. Found on the compass rose of every chart. Must be corrected for accurate navigation.",
        "term_de": "Missweisung / Deklination",
        "definition_de": "Der Winkel zwischen geographisch Nord und magnetisch Nord an einem bestimmten Ort. Aendert sich langsam. Auf jeder Kompassrose verzeichnet."
    },
    {
        "type": "vocab",
        "term_en": "Deviation",
        "definition_en": "The error in a magnetic compass caused by the boat's own magnetic influences (engine, electronics, metal parts). Varies with heading and is recorded in a deviation table.",
        "term_de": "Deviation / Ablenkung",
        "definition_de": "Der Fehler eines Magnetkompasses durch die magnetischen Einfluesse des Bootes selbst (Motor, Elektronik, Metallteile). Aendert sich mit dem Kurs."
    },
    {
        "type": "vocab",
        "term_en": "Bearing / Azimuth",
        "definition_en": "The horizontal angle measured clockwise from north to an object. True bearing (from true north), magnetic bearing (from magnetic north), compass bearing (from compass north).",
        "term_de": "Peilung / Azimut",
        "definition_de": "Der horizontale Winkel von Nord im Uhrzeigersinn zu einem Objekt gemessen. Rechtweisende Peilung (von geogr. Nord), missweisende Peilung (von magn. Nord), Kompasspeilung."
    },
    {
        "type": "learn",
        "title_en": "True, Magnetic & Compass Course",
        "content_en": "Three types of course (direction):\n\n1. TRUE COURSE (TC) — measured from true/geographic north on the chart\n2. MAGNETIC COURSE (MC) — true course corrected for variation\n3. COMPASS COURSE (CC) — magnetic course corrected for deviation\n\nFormula: CC = TC + Variation + Deviation\n\nVariation: found on chart's compass rose\nDeviation: from the boat's deviation table\n\nWest variation/deviation: ADD to true course\nEast variation/deviation: SUBTRACT from true course\n\nMnemonic: 'Cadbury's Dairy Milk Very Tasty' → CC ± D = MC ± V = TC",
        "content_de": "Drei Kursarten:\n\n1. RECHTWEISENDER KURS (rwK) — von geographisch Nord auf der Karte gemessen\n2. MISSWEISENDER KURS (mwK) — rwK korrigiert um die Missweisung\n3. KOMPASSKURS (KK) — mwK korrigiert um die Deviation\n\nFormel: KK = rwK + Missweisung + Deviation\n\nMissweisung: auf der Kompassrose der Karte\nDeviation: aus der Deviationstabelle des Bootes\n\nWest-Missweisung: ADDIEREN\nOst-Missweisung: SUBTRAHIEREN",
        "image": "p034_img00.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Speed, Distance & Time",
        "content_en": "The basic navigation formula:\n\nSpeed = Distance / Time\nDistance = Speed × Time\nTime = Distance / Speed\n\n• Speed at sea is measured in KNOTS (kn) — 1 knot = 1 nautical mile per hour\n• Distance is measured in NAUTICAL MILES (NM) — 1 NM = 1,852 meters\n• Time in hours and minutes\n\nExample: If speed = 6 knots and time = 2.5 hours → Distance = 6 × 2.5 = 15 NM",
        "content_de": "Die grundlegende Navigationsformel:\n\nGeschwindigkeit = Strecke / Zeit\nStrecke = Geschwindigkeit × Zeit\nZeit = Strecke / Geschwindigkeit\n\n• Geschwindigkeit auf See in KNOTEN (kn) — 1 Knoten = 1 Seemeile pro Stunde\n• Entfernung in SEEMEILEN (sm) — 1 sm = 1.852 Meter\n• Zeit in Stunden und Minuten"
    },
    {
        "type": "learn",
        "title_en": "Types of Compass",
        "content_en": "Two main types of compass on boats:\n\n1. MAGNETIC COMPASS — uses Earth's magnetic field. Simple, reliable, no power needed. But affected by variation and deviation.\n\n2. GYROCOMPASS — uses a spinning gyroscope to find TRUE north. Not affected by magnetism. Expensive, used on larger vessels.\n\nAlso: FLUXGATE COMPASS — electronic magnetic compass, can be connected to autopilot and chart plotter. Needs calibration (swing) to compensate for deviation.",
        "content_de": "Zwei Haupttypen von Kompassen:\n\n1. MAGNETKOMPASS — nutzt das Erdmagnetfeld. Einfach, zuverlaessig, braucht keinen Strom. Aber beeinflusst durch Missweisung und Deviation.\n\n2. KREISELKOMPASS — nutzt einen Kreisel um geographisch Nord zu finden. Nicht magnetisch beeinflusst. Teuer, auf groesseren Schiffen.\n\nAuch: FLUXGATE-KOMPASS — elektronischer Magnetkompass, verbindbar mit Autopilot und Kartenplotter.",
        "image": "p034_img02.png"
    },
    {
        "type": "quiz",
        "question_en": "If the true course is 090° and the magnetic variation is 3° West, what is the magnetic course?",
        "question_de": "Wenn der rechtweisende Kurs 090° und die Missweisung 3° West betraegt, wie lautet der missweisende Kurs?",
        "options": [
            {"text": "087°", "correct": False},
            {"text": "090°", "correct": False},
            {"text": "093°", "correct": True},
            {"text": "096°", "correct": False}
        ],
        "explanation_en": "West variation is ADDED: 090° + 3° = 093°. Remember: 'Variation West, compass best (higher)' — when going from true to compass, add west.",
        "explanation_de": "West-Missweisung wird ADDIERT: 090° + 3° = 093°. Merke: Bei West-Missweisung wird vom rwK zum mwK addiert."
    },
    {
        "type": "quiz",
        "question_en": "What is the difference between magnetic variation and deviation?",
        "question_de": "Was ist der Unterschied zwischen Missweisung und Deviation?",
        "options": [
            {"text": "Variation is caused by the boat, deviation by the Earth", "correct": False},
            {"text": "Variation is caused by the Earth, deviation by the boat", "correct": True},
            {"text": "Both are caused by the Earth's magnetic field", "correct": False},
            {"text": "Both are caused by the boat's equipment", "correct": False}
        ],
        "explanation_en": "Variation is the natural difference between true and magnetic north (caused by Earth's magnetic field). Deviation is caused by the boat's own magnetic influences (engine, electronics, metal). Variation is shown on the chart; deviation depends on the individual boat.",
        "explanation_de": "Missweisung ist der natuerliche Unterschied zwischen geographisch und magnetisch Nord (Erdmagnetfeld). Deviation wird durch die magnetischen Einfluesse des Bootes verursacht (Motor, Elektronik, Metall)."
    },
    {
        "type": "quiz_free",
        "question_en": "Explain the three types of north and how they relate to course corrections.",
        "question_de": "Erklaere die drei Arten von Nord und wie sie mit Kurskorrekturen zusammenhaengen.",
        "model_answer_en": "True north is the geographic north pole, shown on charts. Magnetic north is where a compass needle points, differing from true north by the variation angle. Compass north is what the boat's compass shows, differing from magnetic north by the deviation caused by the boat itself. To convert: True Course plus or minus Variation gives Magnetic Course, plus or minus Deviation gives Compass Course.",
        "model_answer_de": "Geographisch Nord ist der geographische Nordpol, auf Karten. Magnetisch Nord ist wo die Kompassnadel zeigt, unterscheidet sich um die Missweisung. Kompassnord ist was der Bootskompass anzeigt, unterscheidet sich um die Deviation. Umrechnung: rwK plus/minus Missweisung ergibt mwK, plus/minus Deviation ergibt Kompasskurs."
    }
]

# ============================================================
# UNIT 1.4 — Terrestrial Navigation
# ============================================================
units["unit_1_4.json"] = [
    {
        "type": "vocab",
        "term_en": "Dead Reckoning (DR)",
        "definition_en": "Estimating current position based on a known previous position, using course steered, speed, and time elapsed. The most basic form of navigation.",
        "term_de": "Koppelnavigation",
        "definition_de": "Schaetzung der aktuellen Position basierend auf einer bekannten frueheren Position, unter Verwendung von Kurs, Geschwindigkeit und verstrichener Zeit."
    },
    {
        "type": "vocab",
        "term_en": "Fix / Position Fix",
        "definition_en": "A precise determination of a vessel's position using two or more lines of position (bearings, ranges, or other observations). More accurate than dead reckoning.",
        "term_de": "Standort / Standortbestimmung",
        "definition_de": "Eine genaue Bestimmung der Schiffsposition mit zwei oder mehr Standlinien (Peilungen, Entfernungen oder andere Beobachtungen)."
    },
    {
        "type": "vocab",
        "term_en": "Line of Position (LOP)",
        "definition_en": "A line on a chart along which a vessel's position must lie, determined by a single observation such as a bearing or distance measurement.",
        "term_de": "Standlinie",
        "definition_de": "Eine Linie auf der Karte, auf der sich die Schiffsposition befinden muss, bestimmt durch eine einzelne Beobachtung wie Peilung oder Entfernungsmessung."
    },
    {
        "type": "learn",
        "title_en": "Five Factors of Navigation",
        "content_en": "Navigation relies on five basic factors:\n\n1. COURSE — direction of travel (in degrees from north)\n2. SPEED — how fast (in knots)\n3. TIME — duration of travel\n4. DISTANCE — how far (in nautical miles)\n5. DEPTH — water depth below the keel\n\nInstruments needed:\n• Compass — for course\n• Speedometer/log — for speed and distance\n• Depth sounder — for depth\n• Watch/chronometer — for time\n• Radar / GPS — electronic aids",
        "content_de": "Navigation beruht auf fuenf Grundfaktoren:\n\n1. KURS — Fahrtrichtung (in Grad von Nord)\n2. GESCHWINDIGKEIT — wie schnell (in Knoten)\n3. ZEIT — Fahrtdauer\n4. STRECKE — wie weit (in Seemeilen)\n5. TIEFE — Wassertiefe unter dem Kiel\n\nBeoetigte Instrumente:\n• Kompass, Geschwindigkeitsmesser, Echolot, Uhr, Radar/GPS",
        "image": "p044_img00.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Position Fixing Methods",
        "content_en": "Methods to determine your position:\n\n1. CROSS BEARINGS — take bearings on 2-3 known objects. Plot the bearing lines on the chart — your position is where they cross.\n\n2. BEARING + DISTANCE — one bearing to a known object plus a distance measurement (by radar or estimation).\n\n3. RUNNING FIX — two bearings on the SAME object taken at different times. Transfer the first bearing line forward using course and distance travelled.\n\n4. DEPTH CONTOUR — match echo sounder readings to chart depth contours.\n\nBest fixes use 3 bearings with objects roughly 60° apart.",
        "content_de": "Methoden zur Standortbestimmung:\n\n1. KREUZPEILUNG — 2-3 bekannte Objekte peilen. Peillinien auf der Karte einzeichnen — Position ist der Schnittpunkt.\n\n2. PEILUNG + ENTFERNUNG — eine Peilung plus Entfernungsmessung (Radar oder Schaetzung).\n\n3. VERSETZTE STANDLINIE — zwei Peilungen desselben Objekts zu verschiedenen Zeiten.\n\n4. TIEFENLINIE — Echolot-Werte mit Tiefenlinien auf der Karte abgleichen.",
        "image": "p044_img02.jpeg"
    },
    {
        "type": "quiz",
        "question_en": "What is the minimum number of bearings needed for a reliable position fix?",
        "question_de": "Wie viele Peilungen braucht man mindestens fuer eine zuverlaessige Standortbestimmung?",
        "options": [
            {"text": "1", "correct": False},
            {"text": "2", "correct": True},
            {"text": "4", "correct": False},
            {"text": "5", "correct": False}
        ],
        "explanation_en": "A minimum of 2 lines of position are needed for a fix (where they cross). 3 bearings are preferred as the triangle formed helps identify errors.",
        "explanation_de": "Mindestens 2 Standlinien sind noetig (Schnittpunkt). 3 Peilungen sind bevorzugt, da das entstehende Dreieck Fehler erkennen laesst."
    },
    {
        "type": "quiz_free",
        "question_en": "Explain how dead reckoning works and why it becomes less accurate over time.",
        "question_de": "Erklaere wie Koppelnavigation funktioniert und warum sie mit der Zeit ungenauer wird.",
        "model_answer_en": "Dead reckoning starts from a known position and estimates the current position using course steered, speed, and elapsed time. You plot the course line on the chart and mark the estimated position based on distance travelled. It becomes less accurate over time because it cannot account for wind, current, steering errors, or speed variations. These small errors accumulate, causing the estimated position to drift from the actual position. Regular position fixes are needed to correct DR errors.",
        "model_answer_de": "Koppelnavigation geht von einer bekannten Position aus und schaetzt die aktuelle Position anhand von Kurs, Geschwindigkeit und Zeit. Der Kurslinie wird auf der Karte eingezeichnet. Sie wird mit der Zeit ungenauer, weil Wind, Stroemung, Steuerfehler und Geschwindigkeitsschwankungen nicht beruecksichtigt werden. Diese kleinen Fehler summieren sich. Regelmaessige Standortbestimmungen sind noetig."
    }
]

# ============================================================
# UNIT 1.6a — Radar
# ============================================================
units["unit_1_6a.json"] = [
    {
        "type": "vocab",
        "term_en": "Radar",
        "definition_en": "Radio Detection And Ranging. Sends microwave pulses and measures reflected echoes to detect objects, their distance, and bearing. Works in darkness, fog, rain.",
        "term_de": "Radar",
        "definition_de": "Radio Detection And Ranging. Sendet Mikrowellenimpulse und misst reflektierte Echos um Objekte, deren Entfernung und Richtung zu erkennen. Funktioniert bei Dunkelheit, Nebel, Regen."
    },
    {
        "type": "vocab",
        "term_en": "ARPA",
        "definition_en": "Automatic Radar Plotting Aid. Tracks detected targets automatically, calculates their course, speed, CPA (Closest Point of Approach), and TCPA (Time to CPA). Essential for collision avoidance.",
        "term_de": "ARPA",
        "definition_de": "Automatic Radar Plotting Aid. Verfolgt erkannte Ziele automatisch, berechnet deren Kurs, Geschwindigkeit, CPA (naechster Passierabstand) und TCPA (Zeit bis CPA)."
    },
    {
        "type": "vocab",
        "term_en": "Radar Range / Bearing",
        "definition_en": "Range: distance to a target (from echo delay). Bearing: direction to a target (from antenna position). Together they give the position of any detected object.",
        "term_de": "Radar-Entfernung / -Peilung",
        "definition_de": "Entfernung: Abstand zum Ziel (aus Echoverzoegerung). Peilung: Richtung zum Ziel (aus Antennenstellung). Zusammen ergeben sie die Position des Objekts.",
        "image": "p049_img00.png"
    },
    {
        "type": "learn",
        "title_en": "How Radar Works",
        "content_en": "Radar principle:\n1. Transmitter sends short microwave pulses through rotating antenna\n2. Pulses travel at speed of light, hit objects, reflect back\n3. Receiver picks up echoes\n4. Time delay = distance (range)\n5. Antenna direction = bearing to target\n\nDisplay shows: your vessel at center, objects as bright dots/shapes\n\nTwo frequencies used:\n• X-band (3 cm / 9 GHz) — better resolution, affected by rain\n• S-band (10 cm / 3 GHz) — better in rain, less detail",
        "content_de": "Radar-Prinzip:\n1. Sender schickt kurze Mikrowellenimpulse ueber drehende Antenne\n2. Impulse wandern mit Lichtgeschwindigkeit, treffen Objekte, werden reflektiert\n3. Empfaenger nimmt Echos auf\n4. Zeitverzoegerung = Entfernung\n5. Antennenrichtung = Peilung zum Ziel\n\nZwei Frequenzen:\n• X-Band (3 cm / 9 GHz) — bessere Aufloesung, Regenprobleme\n• S-Band (10 cm / 3 GHz) — besser bei Regen, weniger Detail",
        "image": "p049_img01.png"
    },
    {
        "type": "learn",
        "title_en": "Radar Limitations",
        "content_en": "Radar has limitations:\n• Shadow sectors — blind spots behind mast, funnel\n• Sea clutter — false echoes from waves (worse in rough seas)\n• Rain clutter — echoes from heavy rain\n• Side lobes — false echoes at wrong bearings\n• Small targets — wooden/fiberglass boats reflect poorly\n• Radar horizon — limited by antenna height, about 1.2× √height(m) in NM\n\nNever rely on radar alone! Always maintain visual lookout and use all available means.",
        "content_de": "Radar hat Grenzen:\n• Schattenbereich — tote Winkel hinter Mast, Schornstein\n• Seegang-Clutter — Falschechos von Wellen\n• Regen-Clutter — Echos von starkem Regen\n• Nebenkeulen — Falschechos in falscher Richtung\n• Kleine Ziele — Holz-/GFK-Boote reflektieren schlecht\n• Radarhorizont — begrenzt durch Antennenhoehe\n\nNie nur auf Radar verlassen! Immer visuelle Ausguck halten."
    },
    {
        "type": "quiz",
        "question_en": "What does CPA stand for in radar navigation?",
        "question_de": "Wofuer steht CPA in der Radarnavigation?",
        "options": [
            {"text": "Central Positioning Array", "correct": False},
            {"text": "Course Plot Analysis", "correct": False},
            {"text": "Closest Point of Approach", "correct": True},
            {"text": "Compass Position Angle", "correct": False}
        ],
        "explanation_en": "CPA = Closest Point of Approach — the minimum distance between your vessel and another target. TCPA = Time to Closest Point of Approach. Both are crucial for collision avoidance.",
        "explanation_de": "CPA = Closest Point of Approach — der minimale Abstand zwischen deinem Boot und einem anderen Ziel. TCPA = Zeit bis zum naechsten Passierabstand. Beide sind entscheidend zur Kollisionsvermeidung."
    },
    {
        "type": "quiz_free",
        "question_en": "Name three limitations of radar and explain why visual lookout is still essential.",
        "question_de": "Nenne drei Einschraenkungen von Radar und erklaere warum visueller Ausguck trotzdem wichtig ist.",
        "model_answer_en": "Three radar limitations: 1) Shadow sectors behind the mast create blind spots where targets cannot be detected. 2) Sea clutter from waves creates false echoes that can mask small targets. 3) Small wooden or fiberglass boats reflect radar poorly and may not appear on screen. Visual lookout remains essential because radar cannot see everything — small boats, floating debris, and swimmers are often invisible to radar. COLREGS Rule 5 requires every vessel to maintain a proper lookout by all available means.",
        "model_answer_de": "Drei Radar-Einschraenkungen: 1) Schattenbereiche hinter dem Mast erzeugen tote Winkel. 2) Seegang-Clutter von Wellen erzeugt Falschechos die kleine Ziele verdecken. 3) Kleine Holz-/GFK-Boote reflektieren schlecht. Visueller Ausguck bleibt wichtig weil Radar nicht alles sieht — kleine Boote, treibende Gegenstaende und Schwimmer sind oft unsichtbar."
    }
]

# ============================================================
# UNIT 1.6b — GPS, Echo Sounder, Auto-Pilot
# ============================================================
units["unit_1_6b.json"] = [
    {
        "type": "vocab",
        "term_en": "GPS (Global Positioning System)",
        "definition_en": "Satellite navigation system providing position, speed, and time worldwide. Uses signals from at least 4 satellites. Accuracy about 10-15 meters.",
        "term_de": "GPS (Globales Positionierungssystem)",
        "definition_de": "Satellitennavigationssystem fuer Position, Geschwindigkeit und Zeit weltweit. Nutzt Signale von mindestens 4 Satelliten. Genauigkeit ca. 10-15 Meter.",
        "image": "p056_img00.jpeg"
    },
    {
        "type": "vocab",
        "term_en": "Echo Sounder / Depth Sounder",
        "definition_en": "Electronic device that measures water depth by sending sound pulses to the seabed and measuring the return time. Essential for safe navigation in shallow waters.",
        "term_de": "Echolot / Tiefenmesser",
        "definition_de": "Elektronisches Geraet zur Messung der Wassertiefe durch Senden von Schallimpulsen zum Meeresboden und Messen der Ruecklaufzeit.",
        "image": "p056_img02.jpeg"
    },
    {
        "type": "vocab",
        "term_en": "Autopilot",
        "definition_en": "Electronic system that automatically steers the vessel on a set course. Connected to compass/GPS. The helmsman can set a heading and the autopilot maintains it.",
        "term_de": "Autopilot",
        "definition_de": "Elektronisches System das das Boot automatisch auf einem eingestellten Kurs steuert. Verbunden mit Kompass/GPS. Der Steuermann stellt den Kurs ein."
    },
    {
        "type": "learn",
        "title_en": "GPS Navigation",
        "content_en": "GPS provides:\n• Position (latitude/longitude) — accuracy ~10-15m\n• Speed over ground (SOG)\n• Course over ground (COG)\n• Time (UTC)\n\nWaypoint navigation: enter waypoints (positions), GPS calculates:\n• Bearing to waypoint\n• Distance to waypoint\n• Cross Track Error (XTE) — how far off course\n• Estimated Time of Arrival (ETA)\n\nIMPORTANT: GPS shows position over GROUND. Wind and current can make your course through water different from your track over ground!",
        "content_de": "GPS liefert:\n• Position (Breite/Laenge) — Genauigkeit ~10-15m\n• Geschwindigkeit ueber Grund (SOG)\n• Kurs ueber Grund (COG)\n• Zeit (UTC)\n\nWegpunkt-Navigation: Wegpunkte eingeben, GPS berechnet Peilung, Entfernung, Kursabweichung (XTE), Ankunftszeit (ETA).\n\nWICHTIG: GPS zeigt Position ueber GRUND. Wind und Stroemung koennen den Kurs durchs Wasser vom Kurs ueber Grund abweichen lassen!"
    },
    {
        "type": "learn",
        "title_en": "Speed Measurement at Sea",
        "content_en": "Two types of speed:\n\n1. Speed Through Water (STW) — measured by log/speedometer, shows boat speed relative to water\n2. Speed Over Ground (SOG) — measured by GPS, shows actual speed over the seabed\n\nDifference is caused by current:\n• With current: SOG > STW\n• Against current: SOG < STW\n\nSpeedometer types:\n• Paddle wheel — mechanical, measures STW\n• Pitot tube — measures water pressure = speed\n• GPS — calculates SOG from position changes\n• Doppler log — uses sound waves, very accurate",
        "content_de": "Zwei Geschwindigkeitsarten:\n\n1. Fahrt durchs Wasser (STW) — vom Log/Speedometer gemessen\n2. Fahrt ueber Grund (SOG) — vom GPS gemessen\n\nDer Unterschied entsteht durch Stroemung:\n• Mit Stroemung: SOG > STW\n• Gegen Stroemung: SOG < STW"
    },
    {
        "type": "quiz",
        "question_en": "What is the difference between SOG and STW?",
        "question_de": "Was ist der Unterschied zwischen SOG und STW?",
        "options": [
            {"text": "SOG is speed over ground (GPS), STW is speed through water (log)", "correct": True},
            {"text": "SOG is measured by the speedometer, STW by GPS", "correct": False},
            {"text": "They are the same measurement in different units", "correct": False},
            {"text": "SOG includes wind speed, STW does not", "correct": False}
        ],
        "explanation_en": "SOG (Speed Over Ground) is measured by GPS and shows actual movement over the seabed. STW (Speed Through Water) is measured by a log/speedometer and shows speed relative to the water. The difference is caused by current.",
        "explanation_de": "SOG (Fahrt ueber Grund) wird vom GPS gemessen. STW (Fahrt durchs Wasser) wird vom Log gemessen. Der Unterschied entsteht durch Stroemung."
    },
    {
        "type": "quiz_free",
        "question_en": "Why should you not rely solely on GPS for navigation? What are its limitations?",
        "question_de": "Warum sollte man sich nicht allein auf GPS verlassen? Was sind seine Grenzen?",
        "model_answer_en": "GPS limitations include: signal loss or degradation near cliffs or under bridges, possible satellite failures, position accuracy of only 10-15 meters which is insufficient near dangers, and GPS shows position over ground but not hazards ahead. Chart data may be inaccurate. Electronics can fail due to power loss or water damage. Always use GPS in combination with visual observations, depth sounder, radar, and paper charts as backup.",
        "model_answer_de": "GPS-Einschraenkungen: Signalverlust an Klippen oder unter Bruecken, moegliche Satellitenausfaelle, Genauigkeit nur 10-15m was nahe an Gefahren nicht reicht, zeigt nur Position ueber Grund aber keine Gefahren voraus. Kartendaten koennen ungenau sein. Elektronik kann durch Stromausfall oder Wasser ausfallen. Immer GPS mit visuellen Beobachtungen, Echolot, Radar und Papierkarten kombinieren."
    }
]

# ============================================================
# UNIT 1.7 — Planning a Maritime Voyage
# ============================================================
units["unit_1_7.json"] = [
    {
        "type": "vocab",
        "term_en": "Passage Plan",
        "definition_en": "A detailed plan for a voyage including route, waypoints, weather forecast, tides, fuel requirements, and emergency procedures. Must be prepared before departure.",
        "term_de": "Toernplanung / Reiseplan",
        "definition_de": "Ein detaillierter Plan fuer eine Seereise mit Route, Wegpunkten, Wetterbericht, Gezeiten, Treibstoffbedarf und Notfallverfahren. Muss vor Abfahrt erstellt werden."
    },
    {
        "type": "vocab",
        "term_en": "Waypoint",
        "definition_en": "A specific geographic position (latitude/longitude) along a planned route. Used for GPS navigation and course changes.",
        "term_de": "Wegpunkt",
        "definition_de": "Eine bestimmte geographische Position (Breite/Laenge) entlang einer geplanten Route. Fuer GPS-Navigation und Kurswechsel."
    },
    {
        "type": "learn",
        "title_en": "Voyage Preparation Steps",
        "content_en": "Before departure, prepare:\n\n1. CHARTS — select correct charts, check they are up-to-date (Notices to Mariners)\n2. ROUTE — plot on chart, mark waypoints, note distances and courses for each leg\n3. WEATHER — check forecast for entire voyage period, know wind and sea conditions\n4. TIDES & CURRENTS — check tidal information for departure, arrival, and any narrow passages\n5. FUEL — calculate fuel consumption, ensure enough fuel plus reserve (minimum 1/3 extra)\n6. SAFETY — check all safety equipment, brief crew on emergency procedures\n7. COMMUNICATIONS — test VHF radio, inform someone ashore of your plans\n8. DOCUMENTS — boat registration, insurance, crew list, passports (international waters)",
        "content_de": "Vor der Abfahrt vorbereiten:\n\n1. KARTEN — richtige Karten waehlen, Aktualitaet pruefen\n2. ROUTE — auf der Karte einzeichnen, Wegpunkte markieren\n3. WETTER — Vorhersage fuer die gesamte Reisedauer pruefen\n4. GEZEITEN & STROEMUNGEN — Gezeiteninformationen pruefen\n5. TREIBSTOFF — Verbrauch berechnen, Reserve einplanen (min. 1/3 extra)\n6. SICHERHEIT — alle Sicherheitsausruestung pruefen, Crew einweisen\n7. FUNK — VHF-Radio testen, Person an Land informieren\n8. DOKUMENTE — Registrierung, Versicherung, Crewliste, Paesse"
    },
    {
        "type": "learn",
        "title_en": "Route Selection Criteria",
        "content_en": "When choosing your route, consider:\n\n• SAFETY — avoid dangers (rocks, shallows, traffic separation schemes)\n• WEATHER — choose lee side of islands in strong winds, avoid open crossings in bad conditions\n• DISTANCE — shortest safe route saves fuel and time\n• SHELTER — plan alternative harbors/anchorages along the route in case conditions change\n• TRAFFIC — avoid busy shipping lanes where possible\n• CURRENT — use favorable currents, avoid adverse ones\n• DAYLIGHT — plan to arrive before dark if unfamiliar with the harbor",
        "content_de": "Bei der Routenwahl beachten:\n\n• SICHERHEIT — Gefahren meiden (Felsen, Untiefen, Verkehrstrennungsgebiete)\n• WETTER — bei starkem Wind die Leeseite von Inseln waehlen\n• ENTFERNUNG — kuerzeste sichere Route spart Treibstoff und Zeit\n• SCHUTZ — Alternative Haefen/Ankerplaetze entlang der Route planen\n• VERKEHR — Stark befahrene Schifffahrtswege meiden\n• STROEMUNG — guenstige Stroemungen nutzen\n• TAGESLICHT — bei unbekanntem Hafen vor Dunkelheit ankommen"
    },
    {
        "type": "quiz",
        "question_en": "What is the recommended minimum fuel reserve for a maritime voyage?",
        "question_de": "Wie viel Treibstoffreserve wird mindestens fuer eine Seereise empfohlen?",
        "options": [
            {"text": "10% extra", "correct": False},
            {"text": "20% extra", "correct": False},
            {"text": "33% extra (one-third)", "correct": True},
            {"text": "50% extra", "correct": False}
        ],
        "explanation_en": "The rule of thirds: 1/3 for the outward journey, 1/3 for the return, 1/3 reserve. So you should carry at least 33% more fuel than calculated for the planned voyage.",
        "explanation_de": "Die Drittel-Regel: 1/3 fuer die Hinfahrt, 1/3 fuer die Rueckfahrt, 1/3 Reserve. Mindestens 33% mehr Treibstoff als berechnet mitnehmen."
    },
    {
        "type": "quiz_free",
        "question_en": "List the essential steps for planning a safe maritime voyage.",
        "question_de": "Nenne die wesentlichen Schritte fuer die Planung einer sicheren Seereise.",
        "model_answer_en": "Essential voyage planning steps: 1) Select and check up-to-date charts for the area. 2) Plot the route with waypoints, noting courses and distances for each leg. 3) Check weather forecasts for the entire voyage period. 4) Verify tidal information for departure, arrival and narrow passages. 5) Calculate fuel requirements with a minimum one-third reserve. 6) Inspect all safety equipment and brief the crew on emergency procedures. 7) Test VHF radio and inform someone ashore of your plans. 8) Prepare required documents: registration, insurance, crew list.",
        "model_answer_de": "Wesentliche Schritte: 1) Aktuelle Karten waehlen und pruefen. 2) Route mit Wegpunkten einzeichnen, Kurse und Entfernungen notieren. 3) Wetter fuer die gesamte Reisedauer pruefen. 4) Gezeiten pruefen. 5) Treibstoffbedarf mit mindestens 1/3 Reserve berechnen. 6) Sicherheitsausruestung pruefen, Crew einweisen. 7) VHF-Radio testen, Person an Land informieren. 8) Dokumente vorbereiten."
    }
]

# ============================================================
# UNIT 2.2 — Engine Systems & Maintenance
# ============================================================
units["unit_2_2.json"] = [
    {
        "type": "vocab",
        "term_en": "Cooling System",
        "definition_en": "System to prevent engine overheating. Two types: direct seawater cooling (raw water) or indirect cooling (freshwater circuit cooled by seawater through heat exchanger).",
        "term_de": "Kuehlsystem",
        "definition_de": "System zur Vermeidung von Motorueberhitzung. Zwei Typen: direkte Seekuehlung (Rohwasser) oder indirekte Kuehlung (Suesswasserkreislauf gekuehlt durch Seewasser ueber Waermetauscher)."
    },
    {
        "type": "vocab",
        "term_en": "Impeller",
        "definition_en": "A rubber pump wheel in the seawater cooling pump. Pumps cooling water through the engine. Wears out and should be replaced annually — most common cause of overheating.",
        "term_de": "Impeller",
        "definition_de": "Ein Gummi-Pumpenrad in der Seekuehlwasserpumpe. Pumpt Kuehlwasser durch den Motor. Verschleisst und sollte jaehrlich gewechselt werden — haeufigste Ursache fuer Ueberhitzung."
    },
    {
        "type": "vocab",
        "term_en": "Fuel System",
        "definition_en": "Components that store and deliver fuel: fuel tank, fuel filter/water separator, fuel lines, injection pump, injectors. Diesel engines use compression ignition, petrol engines use spark plugs.",
        "term_de": "Kraftstoffsystem",
        "definition_de": "Komponenten die Treibstoff lagern und liefern: Tank, Kraftstofffilter/Wasserabscheider, Leitungen, Einspritzpumpe, Einspritzduesen."
    },
    {
        "type": "learn",
        "title_en": "Engine Cooling Systems",
        "content_en": "Two cooling methods:\n\n1. DIRECT (raw water) cooling:\n• Seawater pumped directly through engine\n• Simple system\n• Risk: salt deposits, corrosion over time\n\n2. INDIRECT (freshwater) cooling:\n• Closed freshwater circuit cools the engine\n• Seawater cools the freshwater through a heat exchanger\n• Better for the engine, less corrosion\n\nKey parts: seawater intake (with strainer), impeller pump, thermostat, heat exchanger\n\nCheck: water coming out the exhaust? If not = cooling problem!",
        "content_de": "Zwei Kuehlmethoden:\n\n1. DIREKTE (Rohwasser-) Kuehlung:\n• Seewasser wird direkt durch den Motor gepumpt\n• Einfaches System, Risiko: Salzablagerungen, Korrosion\n\n2. INDIREKTE (Suesswasser-) Kuehlung:\n• Geschlossener Suesswasserkreislauf kuehlt den Motor\n• Seewasser kuehlt das Suesswasser ueber Waermetauscher\n\nWichtig: Kommt Wasser aus dem Auspuff? Wenn nicht = Kuehlproblem!",
        "image": "p066_img01.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Pre-Departure Engine Checks",
        "content_en": "Before starting the engine, ALWAYS check:\n\n1. ENGINE OIL — check level with dipstick, top up if low\n2. COOLANT LEVEL — check in expansion tank (indirect) or raw water strainer\n3. FUEL — sufficient fuel, check for water in fuel filter\n4. DRIVE BELTS — proper tension, no cracks\n5. SEAWATER INTAKE — valve open, strainer clean\n6. EXHAUST — check for water flow after starting (cooling working)\n7. BILGE — check for oil or water leaks\n8. GEAR/PROPELLER — check for lines or debris around propeller\n\nAfter starting: check oil pressure, temperature, charging, water exhaust.",
        "content_de": "Vor dem Motorstart IMMER pruefen:\n\n1. MOTOROEL — Fuellstand am Peilstab\n2. KUEHLMITTEL — im Ausgleichsbehaelter pruefen\n3. TREIBSTOFF — genug vorhanden, Wasserabscheider pruefen\n4. KEILRIEMEN — Spannung, keine Risse\n5. SEEKUEHLWASSER — Ventil offen, Seiher sauber\n6. AUSPUFF — nach Start auf Wasserfluss pruefen\n7. BILGE — auf Oel- oder Wasserlecks pruefen\n8. PROPELLER — auf Leinen oder Muell pruefen"
    },
    {
        "type": "quiz",
        "question_en": "What is the most common cause of engine overheating on a boat?",
        "question_de": "Was ist die haeufigste Ursache fuer Motorueberhitzung auf einem Boot?",
        "options": [
            {"text": "Low oil level", "correct": False},
            {"text": "Failed impeller or blocked seawater intake", "correct": True},
            {"text": "Old fuel", "correct": False},
            {"text": "Loose drive belt", "correct": False}
        ],
        "explanation_en": "A worn-out impeller or a blocked seawater intake stops cooling water from flowing through the engine. Check that water is coming out the exhaust after starting. Replace the impeller annually.",
        "explanation_de": "Ein verschlissener Impeller oder verstopfter Seekuehlwassereinlass stoppt den Kuehlwasserfluss. Pruefen ob Wasser aus dem Auspuff kommt. Impeller jaehrlich wechseln."
    },
    {
        "type": "quiz_free",
        "question_en": "What engine checks should you perform before departure?",
        "question_de": "Welche Motorpruefungen solltest du vor der Abfahrt durchfuehren?",
        "model_answer_en": "Before departure: Check engine oil level with the dipstick and top up if needed. Check coolant level in the expansion tank. Ensure sufficient fuel and check the fuel filter for water. Inspect drive belts for proper tension and cracks. Open the seawater intake valve and clean the strainer. After starting, verify cooling water is flowing from the exhaust. Check the bilge for oil or water leaks. Inspect the propeller area for lines or debris. Monitor oil pressure, temperature gauge, and battery charging.",
        "model_answer_de": "Vor der Abfahrt: Motoroel am Peilstab pruefen. Kuehlmittelstand im Ausgleichsbehaelter. Genug Treibstoff, Wasserabscheider pruefen. Keilriemen auf Spannung und Risse pruefen. Seekuehlwasserventil oeffnen, Seiher reinigen. Nach Start Wasserfluss am Auspuff pruefen. Bilge auf Lecks pruefen. Propeller auf Leinen/Muell pruefen. Oeldruck, Temperatur und Ladung ueberwachen."
    }
]

# ============================================================
# UNIT 3.2 — Registration & Documents
# ============================================================
units["unit_3_2.json"] = [
    {
        "type": "vocab",
        "term_en": "Registration Certificate",
        "definition_en": "Official document proving the nationality and ownership of a vessel. Must be carried on board at all times. Issued by the harbor master's office.",
        "term_de": "Registrierungsbescheinigung",
        "definition_de": "Offizielles Dokument das Nationalitaet und Eigentum eines Bootes beweist. Muss immer an Bord sein. Ausgestellt vom Hafenkapitanat."
    },
    {
        "type": "vocab",
        "term_en": "Boat License (Voditelj Brodice)",
        "definition_en": "Croatian boating license, Category C. Required for operating boats up to 30 GT in coastal waters. Oral exam in English covering navigation, safety, rules, and seamanship.",
        "term_de": "Bootsfuehrerschein (Voditelj Brodice)",
        "definition_de": "Kroatischer Bootsfuehrerschein, Kategorie C. Erforderlich fuer Boote bis 30 GT in Kuestengewaessern. Muendliche Pruefung auf Englisch."
    },
    {
        "type": "vocab",
        "term_en": "Vignette (Cruising Permit)",
        "definition_en": "Annual permit for foreign boats cruising in Croatian waters. Must be purchased within 48 hours of arrival. Proves tourist tax and navigation fees are paid.",
        "term_de": "Vignette (Fahrerlaubnis)",
        "definition_de": "Jaehrliche Genehmigung fuer auslaendische Boote in kroatischen Gewaessern. Muss innerhalb von 48 Stunden nach Ankunft gekauft werden."
    },
    {
        "type": "learn",
        "title_en": "Required Documents on Board",
        "content_en": "Every boat in Croatian waters must carry:\n\n1. REGISTRATION CERTIFICATE — boat's official document\n2. BOAT LICENSE — skipper's competence certificate (Voditelj Brodice Cat. C or equivalent)\n3. CREW LIST — names, passport numbers of all persons on board\n4. VIGNETTE — cruising permit for foreign vessels\n5. INSURANCE — third-party liability insurance\n6. VHF RADIO LICENSE — if radio equipment installed\n\nFor Croatian boats also: certificate of seaworthiness, engine certificate.\n\nInspection by harbor police can happen anytime — keep documents accessible!",
        "content_de": "Jedes Boot in kroatischen Gewaessern muss mitfuehren:\n\n1. REGISTRIERUNGSBESCHEINIGUNG\n2. BOOTSFUEHRERSCHEIN (Voditelj Brodice Kat. C oder gleichwertig)\n3. CREWLISTE — Namen, Passnummern aller Personen\n4. VIGNETTE — Fahrerlaubnis fuer auslaendische Boote\n5. VERSICHERUNG — Haftpflichtversicherung\n6. FUNKLIZENZ — wenn Funkgeraet installiert\n\nKontrolle durch Hafenpolizei jederzeit moeglich!"
    },
    {
        "type": "learn",
        "title_en": "Boat Inspections in Croatia",
        "content_en": "Boats must undergo regular inspections:\n\n• Boats up to 20 years old: inspection every 5 years\n• Boats over 20 years old: inspection every 2 years\n• After major repairs or modifications: special inspection required\n\nInspection checks:\n• Hull condition and watertightness\n• Engine and mechanical systems\n• Safety equipment (life jackets, flares, fire extinguisher)\n• Navigation lights and signals\n• Electrical installation\n• Fuel system (no leaks)\n\nThe inspection is recorded in the Registration Certificate.",
        "content_de": "Boote muessen regelmaessig inspiziert werden:\n\n• Boote bis 20 Jahre: alle 5 Jahre\n• Boote ueber 20 Jahre: alle 2 Jahre\n• Nach groesseren Reparaturen: Sonderinspektion\n\nPruefung umfasst: Rumpfzustand, Motor, Sicherheitsausruestung, Navigationslichter, Elektrik, Kraftstoffsystem.",
        "image": "p074_img01.jpeg"
    },
    {
        "type": "quiz",
        "question_en": "Within how many hours must a foreign vessel purchase a vignette (cruising permit) after arriving in Croatian waters?",
        "question_de": "Innerhalb wie vieler Stunden muss ein auslaendisches Boot nach Ankunft in Kroatien eine Vignette kaufen?",
        "options": [
            {"text": "12 hours", "correct": False},
            {"text": "24 hours", "correct": False},
            {"text": "48 hours", "correct": True},
            {"text": "72 hours", "correct": False}
        ],
        "explanation_en": "Foreign vessels must purchase a cruising permit (vignette) within 48 hours of entering Croatian waters. It covers tourist tax and navigation fees for the year.",
        "explanation_de": "Auslaendische Boote muessen innerhalb von 48 Stunden nach Einfahrt in kroatische Gewaesser eine Vignette kaufen."
    },
    {
        "type": "quiz_free",
        "question_en": "What documents must be carried on board when sailing in Croatian waters?",
        "question_de": "Welche Dokumente muessen beim Segeln in kroatischen Gewaessern an Bord sein?",
        "model_answer_en": "Required documents on board in Croatia: 1) Registration certificate proving boat nationality and ownership. 2) Valid boat license — Voditelj Brodice Category C or recognized equivalent. 3) Crew list with names and passport numbers of all persons on board. 4) Vignette or cruising permit for foreign vessels, purchased within 48 hours of arrival. 5) Third-party liability insurance. 6) VHF radio license if radio equipment is installed. All documents must be easily accessible as harbor police can inspect at any time.",
        "model_answer_de": "Erforderliche Dokumente: 1) Registrierungsbescheinigung. 2) Gueltiger Bootsfuehrerschein — Voditelj Brodice Kat. C oder anerkannt. 3) Crewliste mit Namen und Passnummern. 4) Vignette fuer auslaendische Boote, innerhalb 48 Stunden kaufen. 5) Haftpflichtversicherung. 6) Funklizenz wenn Funkgeraet vorhanden. Hafenpolizei kann jederzeit kontrollieren."
    }
]

# ============================================================
# UNIT 4.1 — Boat Types, Equipment & Flags
# ============================================================
units["unit_4_1.json"] = [
    {
        "type": "vocab",
        "term_en": "Displacement Hull",
        "definition_en": "A hull that moves through the water, pushing it aside. Used by sailboats and heavy motorboats. Speed limited by waterline length. More fuel-efficient at lower speeds.",
        "term_de": "Verdraengungsrumpf",
        "definition_de": "Ein Rumpf der sich durch das Wasser bewegt und es verdraengt. Bei Segelbooten und schweren Motorbooten. Geschwindigkeit durch Wasserlinie begrenzt."
    },
    {
        "type": "vocab",
        "term_en": "Planing Hull",
        "definition_en": "A hull that lifts and glides on top of the water at higher speeds. Used by speedboats and small motorboats. Requires more power but can go much faster.",
        "term_de": "Gleitrumpf",
        "definition_de": "Ein Rumpf der bei hoeherer Geschwindigkeit auf dem Wasser gleitet. Bei Schnellbooten und kleinen Motorbooten. Braucht mehr Leistung, ist aber viel schneller."
    },
    {
        "type": "vocab",
        "term_en": "National Flag / Ensign",
        "definition_en": "The flag showing the vessel's nationality. Must be flown from the stern when in foreign waters. In Croatia, display Croatian flag or your country's flag.",
        "term_de": "Nationalflagge",
        "definition_de": "Die Flagge die die Nationalitaet des Bootes zeigt. Muss am Heck gefuehrt werden wenn in fremden Gewaessern.",
        "image": "p083_img00.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Types of Maritime Vessels",
        "content_en": "Vessels are classified by:\n\nBy PURPOSE:\n• Commercial: passenger transport, cargo, fishing\n• Non-commercial: recreation, sports, personal use\n\nBy PROPULSION:\n• Motor vessels — engine powered\n• Sailing vessels — wind powered (may have auxiliary engine)\n• Rowing boats — human powered\n\nBy SIZE (Croatian law):\n• Boat (brodica) — up to 12m length, up to 30 GT\n• Yacht (jahta) — over 12m length or over 30 GT\n• Ship (brod) — over 12m length, commercial use",
        "content_de": "Schiffe werden klassifiziert nach:\n\nNach ZWECK:\n• Gewerblich: Passagiere, Fracht, Fischerei\n• Nicht-gewerblich: Freizeit, Sport, persoenlich\n\nNach ANTRIEB:\n• Motorboote, Segelboote, Ruderboote\n\nNach GROESSE (kroatisches Recht):\n• Boot (brodica) — bis 12m, bis 30 GT\n• Yacht (jahta) — ueber 12m oder ueber 30 GT\n• Schiff (brod) — ueber 12m, gewerblich"
    },
    {
        "type": "learn",
        "title_en": "Required Safety Equipment",
        "content_en": "Minimum equipment for boats in Croatian waters:\n\n• Life jackets — for every person on board\n• Lifebuoy with line — at least one\n• Flares — 6 red hand flares (check expiry!)\n• Fire extinguisher — at least one, appropriate size\n• First aid kit\n• Sound signaling device (horn/whistle)\n• Flashlight / torch\n• Anchor with sufficient rope/chain\n• Bilge pump\n• Navigation lights\n• VHF radio (recommended, required for some categories)\n• Tool kit and spare parts\n\nAll equipment must be accessible and in working condition!",
        "content_de": "Mindestausruestung fuer Boote in Kroatien:\n\n• Rettungswesten — fuer jede Person\n• Rettungsring mit Leine\n• 6 rote Handfackeln (Ablaufdatum pruefen!)\n• Feuerloescher\n• Erste-Hilfe-Kasten\n• Schallsignalgeraet\n• Taschenlampe\n• Anker mit Leine/Kette\n• Lenzpumpe\n• Navigationslichter\n• VHF-Funk (empfohlen/vorgeschrieben)\n• Werkzeug und Ersatzteile",
        "image": "p083_img01.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Flags on Board",
        "content_en": "Important flags:\n\n• NATIONAL FLAG — at stern, shows vessel nationality. Must fly when in foreign waters.\n• COURTESY FLAG — flag of the country you're visiting, flown on starboard spreader\n• Q FLAG (yellow) — 'I request pratique' (health clearance) when entering a country\n• DIVE FLAG (red with white diagonal) — divers in water, keep 50m distance\n• N over C flags — international distress signal\n\nFlag etiquette:\n• Hoist at 0800, lower at sunset\n• Never fly a tattered flag\n• National flag should be largest",
        "content_de": "Wichtige Flaggen:\n\n• NATIONALFLAGGE — am Heck, zeigt Bootsnationalitaet\n• GASTLANDFLAGGE — Flagge des besuchten Landes, an Steuerbord-Saling\n• Q-FLAGGE (gelb) — 'Gesundheitsfreigabe erbeten' bei Einlaufen\n• TAUCHFLAGGE (rot mit weissem Diagonal) — Taucher im Wasser, 50m Abstand\n\nFlaggen-Etikette: Hissen um 08:00, Einholen bei Sonnenuntergang.",
        "image": "p083_img03.jpeg"
    },
    {
        "type": "quiz",
        "question_en": "What is the difference between a displacement hull and a planing hull?",
        "question_de": "Was ist der Unterschied zwischen einem Verdraengungs- und einem Gleitrumpf?",
        "options": [
            {"text": "Displacement hulls are faster", "correct": False},
            {"text": "Planing hulls glide on top of the water at speed", "correct": True},
            {"text": "Displacement hulls are only used for racing", "correct": False},
            {"text": "There is no practical difference", "correct": False}
        ],
        "explanation_en": "A displacement hull pushes through the water and is limited by its waterline length. A planing hull lifts up and glides on the water surface at higher speeds, allowing much greater speed but requiring more engine power.",
        "explanation_de": "Ein Verdraengungsrumpf schiebt sich durchs Wasser, begrenzt durch die Wasserlinienlaenge. Ein Gleitrumpf hebt sich und gleitet bei hoeherer Geschwindigkeit auf der Wasseroberflaeche."
    },
    {
        "type": "quiz_free",
        "question_en": "What safety equipment must be carried on a boat in Croatian waters?",
        "question_de": "Welche Sicherheitsausruestung muss auf einem Boot in kroatischen Gewaessern mitgefuehrt werden?",
        "model_answer_en": "Required safety equipment includes: life jackets for every person on board, at least one lifebuoy with line, six red hand flares within their expiry date, at least one fire extinguisher of appropriate size, a first aid kit, a sound signaling device such as a horn or whistle, a flashlight, an anchor with sufficient rope or chain, a bilge pump, and working navigation lights. A VHF radio is recommended and required for certain vessel categories. All equipment must be accessible and in working order.",
        "model_answer_de": "Erforderliche Sicherheitsausruestung: Rettungswesten fuer jede Person, mindestens ein Rettungsring mit Leine, sechs rote Handfackeln (Ablaufdatum!), Feuerloescher, Erste-Hilfe-Kasten, Schallsignalgeraet, Taschenlampe, Anker mit Leine/Kette, Lenzpumpe, funktionierende Navigationslichter. VHF-Funk empfohlen bzw. vorgeschrieben. Alles muss zugaenglich und funktionsfaehig sein."
    }
]

# ============================================================
# UNIT 7.2 — Clouds, Fog, Tides & Forecasting
# ============================================================
units["unit_7_2.json"] = [
    {
        "type": "vocab",
        "term_en": "Beaufort Scale",
        "definition_en": "Scale from 0 to 12 for classifying wind speed by its effects on the sea. 0=calm, 4=moderate breeze (11-16 kn), 7=near gale (28-33 kn), 10=storm (48-55 kn), 12=hurricane.",
        "term_de": "Beaufort-Skala",
        "definition_de": "Skala von 0 bis 12 zur Klassifizierung der Windstaerke nach ihren Auswirkungen auf die See."
    },
    {
        "type": "vocab",
        "term_en": "Sea State",
        "definition_en": "Description of wave height conditions. Calm (0m), Slight (0.5-1.25m), Moderate (1.25-2.5m), Rough (2.5-4m), Very rough (4-6m), High (6-9m), Phenomenal (>14m).",
        "term_de": "Seegang",
        "definition_de": "Beschreibung der Wellenhoehe. Ruhig (0m), Leicht (0.5-1.25m), Maessig (1.25-2.5m), Rauh (2.5-4m), Sehr rauh (4-6m), Hoch (6-9m).",
        "image": "p103_img01.jpeg"
    },
    {
        "type": "vocab",
        "term_en": "Tide",
        "definition_en": "Regular rise and fall of sea level caused by gravitational forces of the Moon and Sun. High tide (flood) and low tide (ebb) alternate approximately every 6 hours.",
        "term_de": "Gezeiten / Tide",
        "definition_de": "Regelmaessiges Steigen und Fallen des Meeresspiegels durch Gravitationskraefte von Mond und Sonne. Flut (Hochwasser) und Ebbe (Niedrigwasser) wechseln ca. alle 6 Stunden."
    },
    {
        "type": "learn",
        "title_en": "Cloud Types & Weather Prediction",
        "content_en": "Reading clouds helps predict weather:\n\n• CIRRUS (Ci) — high, thin, wispy. Fair weather but can signal approaching warm front (rain in 24-48h)\n• CUMULUS (Cu) — puffy, white. Fair weather if small and separated\n• CUMULONIMBUS (Cb) — towering thunderstorm cloud. DANGER: strong winds, lightning, heavy rain, waterspouts\n• STRATUS (St) — low, gray, flat layer. Drizzle, poor visibility\n• NIMBOSTRATUS (Ns) — thick, dark. Continuous rain or snow\n\nDarkening sky + dropping barometer + increasing wind = deteriorating weather!",
        "content_de": "Wolken helfen bei der Wettervorhersage:\n\n• CIRRUS — hoch, duenn, federartig. Schoenwetter, kann aber Warmfront ankuendigen\n• CUMULUS — aufgetuermte weisse Haufen. Schoenwetter wenn klein\n• CUMULONIMBUS — Gewitterwolke. GEFAHR: Sturmboeen, Blitz, Starkregen\n• STRATUS — tief, grau, flach. Nieselregen, schlechte Sicht\n• NIMBOSTRATUS — dick, dunkel. Dauerregen\n\nVerdunkelnder Himmel + fallender Barometer + zunehmender Wind = Wetterverschlechterung!",
        "image": "p104_img01.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Tides in the Adriatic",
        "content_en": "Tides in the Adriatic Sea are relatively small:\n\n• Average tidal range: 0.3 to 0.5 meters\n• Maximum (spring tides): up to 1 meter in some areas\n• Tides are semi-diurnal: two high and two low tides per day\n\nSpring tides: largest range, during full and new moon (Sun + Moon aligned)\nNeap tides: smallest range, during quarter moons (Sun + Moon at 90°)\n\nTides are important for:\n• Entering shallow harbors or anchorages\n• Calculating under-keel clearance\n• Planning departure/arrival times\n• Tidal currents affect navigation",
        "content_de": "Gezeiten in der Adria sind relativ gering:\n\n• Durchschnittlicher Tidenhub: 0,3 bis 0,5 Meter\n• Maximum (Springtide): bis 1 Meter\n• Halbtagsgezeiten: zweimal Hoch- und Niedrigwasser pro Tag\n\nSpringtide: groesster Hub, bei Voll- und Neumond\nNipptide: kleinster Hub, bei Halbmond\n\nWichtig fuer: flache Haefen, Kielfreiheit, Zeitplanung, Gezeitenstroemungen"
    },
    {
        "type": "learn",
        "title_en": "Weather Forecasts for Mariners",
        "content_en": "Sources for weather information in Croatia:\n\n• VHF Channel 67 & 73 — Croatian coast guard weather broadcasts\n• NAVTEX — automated weather and navigation warnings\n• Internet/apps — GFS, ECMWF models, Windy, PredictWind\n• Barometer — falling pressure = bad weather approaching\n\nKey forecast terms:\n• Gale warning — wind force 8+ expected\n• Storm warning — wind force 10+ expected\n• Variable — wind direction changing\n• Veering — wind shifting clockwise\n• Backing — wind shifting counter-clockwise",
        "content_de": "Wetterquellen in Kroatien:\n\n• VHF Kanal 67 & 73 — Kuestenwache Wetterbericht\n• NAVTEX — automatische Wetter- und Navigationswarnungen\n• Internet/Apps — GFS, ECMWF, Windy, PredictWind\n• Barometer — fallender Druck = Schlechtwetter naht\n\nFachbegriffe: Sturmwarnung, Variable (Richtung wechselnd), Veering (im Uhrzeigersinn), Backing (gegen Uhrzeigersinn)",
        "image": "p105_img01.jpeg"
    },
    {
        "type": "quiz",
        "question_en": "What type of cloud indicates thunderstorm danger?",
        "question_de": "Welcher Wolkentyp zeigt Gewittergefahr an?",
        "options": [
            {"text": "Cirrus", "correct": False},
            {"text": "Stratus", "correct": False},
            {"text": "Cumulonimbus", "correct": True},
            {"text": "Cumulus", "correct": False}
        ],
        "explanation_en": "Cumulonimbus (Cb) is the thunderstorm cloud — towering vertical development with an anvil top. Dangers include strong gusts, lightning, heavy rain, hail, and waterspouts.",
        "explanation_de": "Cumulonimbus (Cb) ist die Gewitterwolke — turmhohe vertikale Entwicklung mit Ambossform. Gefahren: Sturmboeen, Blitz, Starkregen, Hagel, Wasserhosen."
    },
    {
        "type": "quiz",
        "question_en": "When do spring tides occur?",
        "question_de": "Wann treten Springtiden auf?",
        "options": [
            {"text": "Only in spring season", "correct": False},
            {"text": "During quarter moon phases", "correct": False},
            {"text": "During full moon and new moon", "correct": True},
            {"text": "Only during storms", "correct": False}
        ],
        "explanation_en": "Spring tides have the largest tidal range and occur during full moon and new moon when Sun and Moon are aligned and their gravitational forces combine. They have nothing to do with the spring season.",
        "explanation_de": "Springtiden haben den groessten Tidenhub und treten bei Voll- und Neumond auf, wenn Sonne und Mond in einer Linie stehen und ihre Gravitationskraefte sich addieren."
    },
    {
        "type": "quiz_free",
        "question_en": "How can you use clouds and a barometer to predict approaching bad weather?",
        "question_de": "Wie kannst du Wolken und ein Barometer nutzen um schlechtes Wetter vorherzusagen?",
        "model_answer_en": "Approaching bad weather shows several signs: cirrus clouds appearing from the west may indicate a warm front approaching, bringing rain within 24-48 hours. The barometer will start falling — a rapid drop of more than 3 hPa in 3 hours is a strong warning. Clouds lower and thicken from cirrus to cirrostratus to altostratus to nimbostratus. Wind increases and may shift direction. If you see towering cumulonimbus clouds, expect thunderstorms with strong gusts. A falling barometer combined with darkening skies and increasing wind means deteriorating conditions — prepare the boat and consider seeking shelter.",
        "model_answer_de": "Schlechtwetter zeigt sich durch: Cirrus-Wolken aus Westen deuten auf eine Warmfront hin, Regen in 24-48 Stunden. Das Barometer faellt — schneller Abfall von mehr als 3 hPa in 3 Stunden ist eine starke Warnung. Wolken werden tiefer und dicker. Wind nimmt zu. Cumulonimbus bedeutet Gewitter mit Sturmboeen. Fallendes Barometer + verdunkelnder Himmel + zunehmender Wind = Wetterverschlechterung — Boot vorbereiten und Schutz suchen."
    }
]

# ============================================================
# UNIT 9.2 — Navigation Lights & Signals
# ============================================================
units["unit_9_2.json"] = [
    {
        "type": "vocab",
        "term_en": "Navigation Lights",
        "definition_en": "Lights displayed by vessels between sunset and sunrise (and in reduced visibility) to show position, heading, and type of vessel. Required by COLREGS.",
        "term_de": "Navigationslichter / Positionslichter",
        "definition_de": "Lichter die Schiffe zwischen Sonnenuntergang und -aufgang (und bei schlechter Sicht) zeigen. Zeigen Position, Kurs und Schiffstyp."
    },
    {
        "type": "vocab",
        "term_en": "Sidelights",
        "definition_en": "Red light on port (left) side, green light on starboard (right) side. Visible from ahead to 22.5° abaft the beam. Show which side of the vessel you're seeing.",
        "term_de": "Seitenlichter",
        "definition_de": "Rotes Licht an Backbord (links), gruenes Licht an Steuerbord (rechts). Zeigen welche Seite des Schiffes man sieht."
    },
    {
        "type": "vocab",
        "term_en": "Stern Light",
        "definition_en": "White light at the stern, visible from behind over an arc of 135°. Shows that the vessel is moving away from you.",
        "term_de": "Hecklicht",
        "definition_de": "Weisses Licht am Heck, sichtbar von hinten ueber einen Bogen von 135°. Zeigt dass das Schiff sich entfernt."
    },
    {
        "type": "vocab",
        "term_en": "Masthead Light",
        "definition_en": "White light on the mast, visible from ahead over an arc of 225°. Required for power-driven vessels underway. A second higher masthead light is required for vessels over 50m.",
        "term_de": "Topplicht / Mastlicht",
        "definition_de": "Weisses Licht am Mast, sichtbar von vorn ueber 225°. Pflicht fuer Maschinenfahrzeuge in Fahrt. Zweites hoeheres Topplicht fuer Schiffe ueber 50m.",
        "image": "p120_img01.jpeg"
    },
    {
        "type": "learn",
        "title_en": "Power-Driven Vessel Lights",
        "content_en": "A power-driven vessel underway shows:\n\n• MASTHEAD LIGHT — white, forward, 225° arc\n• SIDELIGHTS — red (port), green (starboard), each 112.5°\n• STERN LIGHT — white, aft, 135°\n\nVessels over 50m: two masthead lights (forward one lower)\nVessels under 12m: may combine all lights in one all-round light\n\nWhat you see tells you the situation:\n• Both sidelights + masthead = vessel coming toward you\n• Red sidelight only = vessel crossing from right to left\n• Green sidelight only = vessel crossing from left to right\n• Stern light only = vessel moving away",
        "content_de": "Ein Maschinenfahrzeug in Fahrt zeigt:\n\n• TOPPLICHT — weiss, vorn, 225°\n• SEITENLICHTER — rot (Backbord), gruen (Steuerbord), je 112.5°\n• HECKLICHT — weiss, hinten, 135°\n\nWas du siehst:\n• Beide Seitenlichter + Topplicht = kommt auf dich zu\n• Nur rotes Seitenlicht = kreuzt von rechts nach links\n• Nur gruenes Seitenlicht = kreuzt von links nach rechts\n• Nur Hecklicht = entfernt sich"
    },
    {
        "type": "learn",
        "title_en": "Sailing Vessel & Special Lights",
        "content_en": "SAILING VESSEL under sail only:\n• Sidelights (red + green)\n• Stern light (white)\n• NO masthead light!\n• Optional: red over green at masthead ('red over green, sailing machine')\n\nVESSEL AT ANCHOR:\n• All-round white light (two if over 50m)\n• No sidelights or stern light needed\n\nVESSEL NOT UNDER COMMAND:\n• Two red all-round lights vertically\n\nVESSEL RESTRICTED IN ABILITY TO MANEUVER:\n• Red, white, red all-round lights vertically\n\nVESSEL ENGAGED IN FISHING:\n• Red over white all-round lights (trawling: green over white)",
        "content_de": "SEGELFAHRZEUG nur unter Segeln:\n• Seitenlichter (rot + gruen)\n• Hecklicht (weiss)\n• KEIN Topplicht!\n\nVOR ANKER:\n• Rundumlicht weiss (zwei bei ueber 50m)\n\nMANOEVRIERUNFAEHIG:\n• Zwei rote Rundumlichter uebereinander\n\nBESCHRAENKT MANOEVRIERFAEHIG:\n• Rot, weiss, rot uebereinander\n\nFISCHEND:\n• Rot ueber weiss (Schleppnetz: gruen ueber weiss)"
    },
    {
        "type": "learn",
        "title_en": "Sound Signals",
        "content_en": "Sound signals in restricted visibility and for maneuvering:\n\nShort blast = about 1 second\nProlonged blast = 4-6 seconds\n\nMANEUVERING signals:\n• One short blast — I am turning to starboard\n• Two short blasts — I am turning to port\n• Three short blasts — my engines are going astern\n• Five short blasts — I doubt your intentions / danger!\n\nFOG signals (every 2 minutes):\n• Power vessel making way: one prolonged blast\n• Power vessel stopped: two prolonged blasts\n• Sailing vessel / fishing / towing: one prolonged + two short\n• Vessel at anchor: rapid bell ringing for 5 seconds",
        "content_de": "Schallsignale bei schlechter Sicht und zum Manovrieren:\n\nKurzer Ton = ca. 1 Sekunde\nLanger Ton = 4-6 Sekunden\n\nMANOEVRIER-Signale:\n• Ein kurzer Ton — Ich drehe nach Steuerbord\n• Zwei kurze Toene — Ich drehe nach Backbord\n• Drei kurze Toene — Meine Maschine geht rueckwaerts\n• Fuenf kurze Toene — Ich bezweifle Ihre Absichten / Gefahr!\n\nNEBEL-Signale (alle 2 Minuten):\n• Maschinenfahrzeug in Fahrt: ein langer Ton\n• Maschinenfahrzeug gestoppt: zwei lange Toene\n• Segler/Fischer/Schleppend: ein langer + zwei kurze"
    },
    {
        "type": "quiz",
        "question_en": "At night you see a red sidelight and a masthead light ahead. What does this tell you?",
        "question_de": "Nachts siehst du ein rotes Seitenlicht und ein Topplicht voraus. Was bedeutet das?",
        "options": [
            {"text": "A vessel is moving away from you", "correct": False},
            {"text": "A vessel is crossing from your right to left", "correct": True},
            {"text": "A sailing vessel approaching", "correct": False},
            {"text": "A vessel at anchor", "correct": False}
        ],
        "explanation_en": "Red sidelight + masthead light = a power-driven vessel showing its port (left) side, meaning it's crossing from your right to left. The masthead light confirms it's power-driven (sailing vessels don't show masthead lights).",
        "explanation_de": "Rotes Seitenlicht + Topplicht = ein Maschinenfahrzeug zeigt seine Backbordseite, kreuzt also von rechts nach links. Das Topplicht bestaetigt Maschinenantrieb (Segler zeigen kein Topplicht)."
    },
    {
        "type": "quiz",
        "question_en": "What does five short blasts on the horn mean?",
        "question_de": "Was bedeuten fuenf kurze Toene mit dem Horn?",
        "options": [
            {"text": "I am turning to starboard", "correct": False},
            {"text": "I am going astern", "correct": False},
            {"text": "I am in distress", "correct": False},
            {"text": "I doubt your intentions / danger warning", "correct": True}
        ],
        "explanation_en": "Five or more short blasts is the danger/doubt signal: 'I am unsure of your intentions' or 'You are standing into danger.' One short = starboard turn, two = port turn, three = engines astern.",
        "explanation_de": "Fuenf oder mehr kurze Toene sind das Gefahren-/Zweifelsignal: 'Ich bin unsicher ueber Ihre Absichten.' Ein kurzer = Steuerbord, zwei = Backbord, drei = Maschine rueckwaerts."
    },
    {
        "type": "quiz_free",
        "question_en": "Describe the navigation lights for a power-driven vessel under 50 meters, underway at night.",
        "question_de": "Beschreibe die Navigationslichter eines Maschinenfahrzeugs unter 50 Metern, nachts in Fahrt.",
        "model_answer_en": "A power-driven vessel under 50 meters underway at night must display: one white masthead light forward, visible over an arc of 225 degrees from right ahead to 22.5 degrees abaft the beam on each side. A green sidelight on the starboard side and a red sidelight on the port side, each visible over 112.5 degrees. And a white stern light visible over 135 degrees from astern. Vessels under 12 meters may combine all lights into one all-round white light plus sidelights, or even a single tri-color lantern at the masthead.",
        "model_answer_de": "Ein Maschinenfahrzeug unter 50m zeigt nachts: Ein weisses Topplicht vorn, sichtbar ueber 225 Grad. Ein gruenes Seitenlicht an Steuerbord und ein rotes an Backbord, je 112,5 Grad. Ein weisses Hecklicht ueber 135 Grad von achtern. Boote unter 12m duerfen alle Lichter in einem Rundumlicht kombinieren."
    }
]

# ============================================================
# Write all unit files
# ============================================================
for filename, cards in units.items():
    filepath = os.path.join(UNITS_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)
    print(f"  {filename}: {len(cards)} cards")

print(f"\nTotal: {len(units)} unit files created")
print(f"Total cards: {sum(len(c) for c in units.values())}")
