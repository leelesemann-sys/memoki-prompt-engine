"""MEMOKI – How it Works: Dokumentation der Architektur und Spielmodi."""

import streamlit as st
import streamlit.components.v1 as components

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MEMOKI – How it Works",
    page_icon="🧠",
    layout="wide",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    /* ── Globals ── */
    .stApp {
        background: linear-gradient(135deg, #e0f2f1 0%, #e0f7fa 50%, #e8eaf6 100%);
        font-family: 'Nunito', sans-serif;
    }
    h1, h2, h3, h4, h5, h6, p, li, td, th, label, .stMarkdown {
        font-family: 'Nunito', sans-serif !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #00695c 0%, #00796b 40%, #00897b 100%);
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
        font-family: 'Nunito', sans-serif !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: rgba(255,255,255,0.9) !important;
        font-size: 0.95rem;
        padding: 4px 0;
    }
    section[data-testid="stSidebar"] .stRadio label:hover {
        color: #b2dfdb !important;
    }
    section[data-testid="stSidebar"] .stRadio [data-testid="stWidgetLabel"] {
        display: none;
    }

    /* ── Header ── */
    .how-header {
        background: linear-gradient(135deg, #00695c 0%, #00838f 50%, #1565c0 100%);
        color: white;
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }
    .how-header h1 {
        color: white !important;
        font-size: 2rem;
        font-weight: 800;
        margin: 0 0 0.3rem 0;
    }
    .how-header p {
        color: rgba(255,255,255,0.85) !important;
        font-size: 1.05rem;
        margin: 0;
    }

    /* ── Section Headers ── */
    .section-head {
        font-size: 1.3rem;
        font-weight: 700;
        color: #00695c;
        margin: 1.5rem 0 0.8rem 0;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #b2dfdb;
    }

    /* ── Tech Badges ── */
    .tech-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 3px 4px 3px 0;
    }
    .tech-badge.gemini { background: #e8f5e9; color: #2e7d32; border: 1px solid #a5d6a7; }
    .tech-badge.azure { background: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }
    .tech-badge.streamlit { background: #fce4ec; color: #c62828; border: 1px solid #ef9a9a; }
    .tech-badge.python { background: #fff8e1; color: #f57f17; border: 1px solid #ffe082; }
    .tech-badge.prompt { background: #f3e5f5; color: #7b1fa2; border: 1px solid #ce93d8; }

    /* ── Pipeline Steps ── */
    .pipeline-step {
        background: white;
        border-left: 4px solid #00897b;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .pipeline-step b {
        color: #00695c;
    }

    /* ── Architecture Grid ── */
    .arch-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin: 1rem 0;
    }
    .arch-box {
        background: white;
        border-radius: 12px;
        padding: 1.2rem;
        border-top: 4px solid #00897b;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    }
    .arch-box h4 {
        color: #00695c !important;
        margin: 0 0 0.5rem 0;
    }

    /* ── Info Items ── */
    .info-item {
        background: linear-gradient(135deg, #e0f2f1 0%, #ffffff 100%);
        border-left: 3px solid #26a69a;
        padding: 0.7rem 1rem;
        margin: 0.4rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
    }

    /* ── Challenge Items ── */
    .challenge-item {
        background: linear-gradient(135deg, #fff3e0 0%, #ffffff 100%);
        border-left: 3px solid #ff9800;
        padding: 0.7rem 1rem;
        margin: 0.4rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
    }

    /* ── Learning Items ── */
    .learning-item {
        background: linear-gradient(135deg, #e8eaf6 0%, #ffffff 100%);
        border-left: 3px solid #5c6bc0;
        padding: 0.7rem 1rem;
        margin: 0.4rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
    }

    /* ── KPI Cards ── */
    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border-top: 3px solid #00897b;
    }
    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #00695c;
    }
    .kpi-label {
        font-size: 0.85rem;
        color: #666;
        margin-top: 0.2rem;
    }

    /* ── Style Preview Cards ── */
    .style-card {
        background: white;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin: 0.3rem 0;
        box-shadow: 0 1px 6px rgba(0,0,0,0.05);
        border-left: 3px solid #00897b;
    }
    .style-card code {
        background: #e0f2f1;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.85rem;
    }

    /* ── Footer ── */
    .how-footer {
        text-align: center;
        padding: 1.5rem;
        color: #78909c;
        font-size: 0.85rem;
        margin-top: 2rem;
        border-top: 1px solid #b2dfdb;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar-Fixes per JS (CSS-Selektoren greifen nicht zuverlässig) ──────────
components.html("""
<script>
(function fix() {
    const doc = window.parent.document;
    const sidebar = doc.querySelector('section[data-testid="stSidebar"]');
    if (!sidebar) { setTimeout(fix, 300); return; }

    // 1) "keyboard_double_..." Text finden und verstecken
    const walker = document.createTreeWalker(
        sidebar, NodeFilter.SHOW_TEXT, null, false
    );
    while (walker.nextNode()) {
        const node = walker.currentNode;
        if (node.textContent.includes('keyboard_double')) {
            let el = node.parentElement;
            while (el && el !== sidebar) {
                if (el.tagName === 'BUTTON' || el.tagName === 'A' || el.getAttribute('role') === 'button') {
                    el.style.display = 'none';
                    break;
                }
                el = el.parentElement;
            }
            if (el === sidebar) node.parentElement.style.display = 'none';
        }
    }

    // 2) Ersten Nav-Link umbenennen (app / app_test → MEMOKI-App)
    const navLinks = sidebar.querySelectorAll('a[href]');
    for (const link of navLinks) {
        const span = link.querySelector('span');
        if (span && /^app(_test)?$/i.test(span.textContent.trim())) {
            span.textContent = 'MEMOKI-App';
        }
    }
})();
</script>
""", height=0)

# ── Navigation ───────────────────────────────────────────────────────────────

NAV_ITEMS = [
    "🏗️ Architektur-Übersicht",
    "🎴 Klassisches Memory",
    "👫 Paare-Memory",
    "🫖 Teekesselchen",
    "🔢 Mathe I (Abstrakt)",
    "🧮 Mathe II (Konkret)",
    "🎨 Stil & Zielgruppen",
]

with st.sidebar:
    st.markdown("### 🧠 MEMOKI Docs")
    st.markdown("---")
    selected = st.radio("Navigation", NAV_ITEMS, label_visibility="collapsed")


# ── Mode Data ────────────────────────────────────────────────────────────────

MODE_DATA = {
    "classic": {
        "icon": "🎴",
        "title": "Klassisches Memory",
        "what": (
            "Im klassischen Modus generiert MEMOKI Bildpaare zu einem frei "
            "wählbaren Thema. Der User nennt ein Thema (z.B. *Tiere*, *Fahrzeuge*, "
            "*Weltraum*), und das System erzeugt passende Motive als identische Kartenpaare.\n\n"
            "Jedes Paar besteht aus zwei identischen Karten mit demselben Motiv. "
            "Die Spieler decken Karten auf und suchen die passenden Paare."
        ),
        "how": [
            ("1. Thema wählen", "Der MEMOKI-Agent fragt nach Thema, Stil und Zielgruppe."),
            ("2. Objekte generieren", "Gemini 2.5 Flash generiert eine Liste passender Objekte per LLM-Call."),
            ("3. Prompts bauen", "<code>build_image_prompt()</code> erstellt für jedes Objekt einen optimierten Bild-Prompt."),
            ("4. Bilder erzeugen", "Gemini 3 Pro generiert die Kartenbilder parallel (ThreadPoolExecutor)."),
            ("5. Deck erstellen", "Jedes Bild wird verdoppelt, gemischt und als spielbares Deck ausgegeben."),
        ],
        "prompt_engineering": [
            "<b>Objekt-Generierung</b> &mdash; Der Content-Prompt fordert visuell unterscheidbare, "
            "konkrete Objekte. Abstrakte Konzepte und Synonyme werden explizit ausgeschlossen.",
            "<b>Stil-Anpassung</b> &mdash; Das Hybrid-System löst bekannte Stil-Keys (z.B. <code>cartoon</code>) "
            "in detaillierte Prompt-Fragmente auf, lässt aber auch Freitext durch (z.B. <code>van Gogh</code>).",
            "<b>Zielgruppen-Tuning</b> &mdash; Je nach Audience werden Attribute wie <code>cute, friendly</code> "
            "(Kinder) oder <code>sophisticated, elegant</code> (Erwachsene) ergänzt.",
            "<b>Weißer Hintergrund</b> &mdash; Alle Prompts enden mit <code>pure white background, no text, "
            "square format</code> für konsistente Kartenlayouts.",
        ],
        "challenges": [
            ("Objekt-Qualität", "Der LLM generiert manchmal zu ähnliche oder zu abstrakte Objekte. "
             "Gelöst durch detaillierte Beispiele und Negativbeispiele im Prompt."),
            ("Stil-Konsistenz", "Verschiedene Objekte im selben Stil halten &mdash; der Stil-Prompt "
             "muss stark genug sein, um den Look über alle Karten hinweg einheitlich zu halten."),
        ],
        "learnings": [
            "<b>Few-Shot-Beispiele wirken</b> &mdash; Gute und schlechte Beispiele im Content-Prompt "
            "verbessern die Objekt-Qualität drastisch.",
            "<b>Parallelisierung lohnt sich</b> &mdash; 10 Bilder parallel statt sequenziell spart "
            "erheblich Zeit bei der Generierung.",
        ],
    },

    "paare": {
        "icon": "👫",
        "title": "Paare-Memory",
        "what": (
            "Im Paare-Modus bestehen die Kartenpaare aus zwei *zusammengehörigen* "
            "aber *unterschiedlichen* Motiven. Zum Beispiel: Hund & Knochen, "
            "Schlüssel & Schloss, Nadel & Faden.\n\n"
            "Die Spieler müssen erkennen, welche zwei verschiedenen Bilder "
            "logisch zusammengehören &mdash; eine anspruchsvollere Variante als identische Paare."
        ),
        "how": [
            ("1. Thema wählen", "Der Agent fragt nach Thema, Stil und Zielgruppe."),
            ("2. Paare laden", "Zusammengehörige Objekt-Paare werden aus der <code>pairs_v2.json</code> Wissensbasis geladen."),
            ("3. Prompts bauen", "Für jedes Objekt wird ein eigener Bild-Prompt erstellt (Objekt A und Objekt B getrennt)."),
            ("4. Bilder erzeugen", "Beide Bilder eines Paares werden parallel generiert."),
            ("5. Deck erstellen", "Die Karten werden gemischt, jedes Paar hat eine gemeinsame <code>pair_id</code>."),
        ],
        "prompt_engineering": [
            "<b>Paar-Kohärenz</b> &mdash; Beide Objekte eines Paares müssen im selben Stil generiert werden, "
            "damit sie visuell als zusammengehörig erkennbar sind.",
            "<b>Eindeutigkeit</b> &mdash; Jedes Objekt muss eindeutig dargestellt werden &mdash; "
            "ein Schlüssel darf nicht wie ein Schloss aussehen und umgekehrt.",
            "<b>Wissensbasis-Kuratierung</b> &mdash; Die Paare in <code>pairs_v2.json</code> sind manuell kuratiert, "
            "um sicherzustellen, dass die Zuordnung für die Zielgruppe klar ist.",
            "<b>Anti-Morphing</b> &mdash; Der Bild-Prompt verbietet explizit Anthropomorphismus: "
            "<code>do NOT reshape it into an animal, do NOT add faces, eyes, or animal features</code>. "
            "Ohne diese Regel verwandelt Gemini Alltagsobjekte gerne in niedliche Charaktere.",
        ],
        "challenges": [
            ("Paar-Erkennung", "Die logische Verbindung muss auch visuell erkennbar sein. "
             "Zu abstrakte Paare (z.B. Ursache & Wirkung) funktionieren als Bild nicht."),
            ("Schwierigkeitsbalance", "Paare müssen herausfordernd genug sein, aber nicht zu obskur &mdash; "
             "besonders für Kinder eine Gratwanderung."),
        ],
        "learnings": [
            "<b>Kuratierte Wissensbasis > LLM-Generierung</b> &mdash; Für Paare ist eine "
            "handgepflegte JSON-Datei zuverlässiger als LLM-generierte Zuordnungen.",
            "<b>Kulturelle Sensibilität</b> &mdash; Manche Paare sind kulturabhängig "
            "(z.B. Brezel & Bier funktioniert in DE, aber nicht überall).",
        ],
    },

    "teekesselchen": {
        "icon": "🫖",
        "title": "Teekesselchen",
        "what": (
            "Teekesselchen sind Wörter mit mehreren Bedeutungen (Homonyme). "
            "Zum Beispiel: *Bank* (Sitzbank vs. Geldinstitut), *Birne* (Obst vs. Glühbirne), "
            "*Schloss* (Gebäude vs. Türschloss).\n\n"
            "Karte A zeigt die eine Bedeutung als Bild, Karte B die andere Bedeutung. "
            "Die Spieler müssen erkennen, dass beide Bilder dasselbe Wort darstellen."
        ),
        "how": [
            ("1. Kein Thema nötig", "Teekesselchen kommen aus der kuratierten Wissensbasis <code>teekesselchen_v2.json</code>."),
            ("2. Wörter auswählen", "<code>load_teekesselchen()</code> wählt zufällig N Einträge mit beiden Bedeutungen."),
            ("3. Prompts bauen", "Für jede Bedeutung wird ein separater Bild-Prompt erstellt, der die spezifische Bedeutung klar darstellt."),
            ("4. Bilder erzeugen", "Beide Bedeutungen werden als separate Karten generiert."),
            ("5. Rätsel-Deck", "Die Karten werden gemischt &mdash; das Rätsel: Welche zwei Bilder gehören zum selben Wort?"),
        ],
        "prompt_engineering": [
            "<b>Bedeutungs-Disambiguierung</b> &mdash; Der Prompt muss unmissverständlich klarmachen, "
            "WELCHE Bedeutung gemeint ist. <code>\"A wooden park bench in a park\"</code> statt nur <code>\"Bank\"</code>.",
            "<b>Englische Bild-Prompts</b> &mdash; Die Bildgenerierung arbeitet auf Englisch, "
            "die Bedeutungen werden in der Wissensbasis bereits als englische Prompts gespeichert.",
            "<b>Keine Texthinweise</b> &mdash; Die Bilder dürfen keinen Text enthalten, der das Wort verrät. "
            "Nur die visuelle Darstellung zählt.",
        ],
        "challenges": [
            ("Homonym-Qualität", "Nicht jedes Homonym eignet sich &mdash; beide Bedeutungen müssen "
             "gut als Bild darstellbar sein. <code>Ton</code> (Klang vs. Erde) ist z.B. schwierig."),
            ("Schwierigkeitsgrad", "Die beiden Bilder dürfen sich nicht zu ähnlich sehen "
             "(sonst zu leicht) und nicht zu unterschiedlich (sonst geraten)."),
            ("Wissensbasis-Pflege", "Jeder Eintrag braucht zwei sorgfältig formulierte englische "
             "Bild-Beschreibungen &mdash; aufwendig, aber notwendig für Qualität."),
        ],
        "learnings": [
            "<b>JSON-Struktur entscheidend</b> &mdash; Jedes Teekesselchen hat <code>meaning_a</code> und "
            "<code>meaning_b</code> mit je einer deutschen Bezeichnung und einem englischen Bild-Prompt.",
            "<b>Kuratierung ist King</b> &mdash; LLMs können Teekesselchen vorschlagen, aber die "
            "finale Auswahl und Prompt-Formulierung braucht menschliches Urteil.",
        ],
    },

    "mathe_abstrakt": {
        "icon": "🔢",
        "title": "Mathe I (Abstrakt)",
        "what": (
            "Mathe Memory I trainiert Zahlenverständnis durch abstrakte Darstellungen. "
            "Karte A zeigt eine Zahl (z.B. **5**), Karte B zeigt die entsprechende Menge "
            "als abstrakte Formen (z.B. 5 Kreise, 5 Sterne, 5 Herzen).\n\n"
            "Der User wählt einen **Shape-Stil** (Kreise, Sterne, Herzen, Würfelaugen, "
            "Finger oder Überraschung). Die Zahlen 1&ndash;10 oder 1&ndash;20 werden automatisch generiert."
        ),
        "how": [
            ("1. Shape wählen", "Der Agent bietet 6 Shape-Optionen an: Kreise, Sterne, Herzen, Würfelaugen, Finger, Überraschung."),
            ("2. Shape laden", "<code>load_math_shape()</code> lädt die Shape-Definition aus <code>math_shapes.json</code>."),
            ("3. Zahl-Prompts", "<code>build_number_prompt()</code> erzeugt Prompts für die Zahlenkarten (große, klare Ziffer)."),
            ("4. Shape-Prompts", "<code>build_shapes_prompt()</code> erzeugt Prompts für die Shape-Karten (N Objekte, klar zählbar)."),
            ("5. Parallel generieren", "Alle Karten werden parallel via ThreadPoolExecutor generiert."),
        ],
        "prompt_engineering": [
            "<b>Zählbarkeit</b> &mdash; Der Shape-Prompt betont <code>clearly countable, well-spaced</code> &mdash; "
            "die Formen müssen einzeln abzählbar sein, nicht ineinander verschmelzen.",
            "<b>Finger-Sonderlogik</b> &mdash; Zahlen 1&ndash;5 zeigen eine Hand, 6&ndash;10 zeigen zwei Hände. "
            "Der Prompt beschreibt explizit <code>left hand 5 fingers + right hand N fingers</code>.",
            "<b>Zahlen-Klarheit</b> &mdash; Zahlenkarten betonen <code>clean standard shape, instantly recognizable</code> "
            "und verbieten explizit Dekorationen, die die Lesbarkeit beeinträchtigen.",
            "<b>Konsistente Shapes</b> &mdash; Die <code>image_prompt_en</code> aus der JSON-Datei definiert das "
            "exakte Aussehen jeder Form für konsistente Ergebnisse.",
            "<b>Layout-Hints</b> &mdash; <code>_layout_hint(n)</code> gibt für jede Zahl eine explizite "
            "Grid-Anordnung vor (z.B. <code>3 top row, 2 bottom row</code> für 5), damit die KI "
            "die korrekte Anzahl nicht zufällig verteilt, sondern strukturiert anordnet.",
            "<b>Würfelaugen-Prompts</b> &mdash; <code>_dice_prompt(n)</code> beschreibt exakte Pip-Positionen "
            "pro Würfelseite. Ab 7 werden mehrere Würfel nebeneinander dargestellt (z.B. 6+1 für 7).",
            "<b>Strichlisten-Prompts</b> &mdash; <code>_tally_prompt(n)</code> nutzt das klassische System: "
            "4 senkrechte Striche + 1 diagonaler = 5. Gruppen werden getrennt dargestellt.",
            "<b>Domino-Prompts</b> &mdash; <code>_domino_prompt(n)</code> teilt die Zahl optimal auf zwei "
            "Hälften auf (max 6 pro Hälfte). Ab 13 werden zwei Dominosteine verwendet.",
        ],
        "challenges": [
            ("Zahlen-Styling vs. Lesbarkeit", "Wenn ein Thema gewählt wird, dürfen Farben sich anpassen, "
             "aber die Ziffernform muss sauber bleiben. Gelöst durch explizites <code>Do NOT reshape the number</code>."),
            ("Finger-Darstellung", "LLMs haben Schwierigkeiten mit korrekter Finger-Anzahl. "
             "Gelöst durch sehr explizite Hand-Beschreibungen im Prompt."),
            ("Hohe Zahlen zählen", "Bei 15+ Objekten wird das Zählen im Bild schwierig. "
             "Reihen/Grid-Anordnung und großzügiger Abstand helfen."),
        ],
        "learnings": [
            "<b>Shape-Datenbank statt Freitext</b> &mdash; Vordefinierte Shapes mit getesteten "
            "Prompt-Fragmenten liefern konsistentere Ergebnisse als freie Beschreibungen.",
            "<b>Negative Prompts wirken</b> &mdash; <code>no borders, no frames, no black edges</code> "
            "verhindert unerwünschte visuelle Artefakte bei den Zahlenkarten.",
        ],
    },

    "mathe_konkret": {
        "icon": "🧮",
        "title": "Mathe II (Konkret)",
        "what": (
            "Mathe Memory II verwendet **reale Objekte** statt abstrakter Formen. "
            "Karte A zeigt eine Zahl, Karte B zeigt die entsprechende Menge "
            "realer Gegenstände (z.B. 3 Tennisbälle, 7 Cupcakes).\n\n"
            "Der User wählt ein **Thema** (z.B. Sport, Essen, Spielzeug), und das "
            "System generiert per LLM passende, zählbare Objekte. Jede Zahl wird "
            "mit einem *anderen* Objekt gepaart."
        ),
        "how": [
            ("1. Thema wählen", "Der Agent fragt nach einem Thema und erklärt, dass es gut zählbare Objekte hergeben muss."),
            ("2. Objekte generieren", "<code>generate_countable_objects()</code> nutzt Gemini Flash, um N zählbare Objekte zum Thema zu finden."),
            ("3. Zahl-Prompts", "<code>build_number_prompt()</code> erstellt Zahlenkarten mit optionalem Thema-Einfluss auf Farben."),
            ("4. Objekt-Prompts", "<code>build_real_objects_prompt()</code> erstellt Karten mit exakt N identischen Objekten."),
            ("5. Generieren & Paaren", "Zahl 1 &harr; Objekt A, Zahl 2 &harr; Objekt B, etc. Parallel generiert."),
        ],
        "prompt_engineering": [
            "<b>Zählbare Objekte erzwingen</b> &mdash; Der Content-Prompt hat strenge Regeln: "
            "Objekte müssen diskret, klein und einzeln zählbar sein. Elefanten oder Schwimmbäder sind verboten.",
            "<b>Die Sache selbst, nicht Zubehör</b> &mdash; Wichtigste Regel im Prompt: Bei Thema <code>Schuhe</code> "
            "Schuhtypen generieren (Sneaker, Stiefel), NICHT Schuh-Zubehör (Schnürsenkel, Schuhschnalle).",
            "<b>Anti-Cropping</b> &mdash; Explizite Anweisung: <code>all objects fully visible and not cropped or "
            "cut off at the edges</code> mit <code>generous margin</code> verhindert abgeschnittene Objekte.",
            "<b>Identische Objekte</b> &mdash; Der Prompt betont <code>identical</code> und <code>same type</code> &mdash; "
            "5 Tennisbälle sollen 5 gleiche Tennisbälle sein, nicht 3 Tennisbälle und 2 Fußbälle.",
            "<b>Thema-Kontext für Mehrdeutigkeiten</b> &mdash; <code>(in the context of {theme})</code> hilft dem "
            "Bildgenerator bei mehrdeutigen Wörtern (z.B. <code>mouse</code> bei Thema Technik vs. Tiere).",
            "<b>Layout-Hints</b> &mdash; Auch bei realen Objekten nutzt <code>build_real_objects_prompt()</code> "
            "die <code>_layout_hint(n)</code>-Funktion für strukturierte Grid-Anordnungen, damit die "
            "exakte Anzahl klar zählbar bleibt.",
        ],
        "challenges": [
            ("Objekt-Auswahl-Qualität", "LLMs generierten Zubehör statt der Sache selbst "
             "(Schuhschnallen statt Schuhe). Gelöst durch explizite Regel und Positiv-/Negativ-Beispiele."),
            ("Objekt-Cropping", "Bei 7+ Objekten wurden Teile am Bildrand abgeschnitten. "
             "Gelöst durch <code>generous margin</code> und explizite Anti-Cropping-Anweisung."),
            ("Zahlenkarten-Deformation", "Zahlen wurden thematisch verformt (6 sah aus wie ein Schuh). "
             "Gelöst durch explizites <code>Do NOT reshape the number to look like objects from the theme</code>."),
            ("Schwarze Ränder", "Manche Zahlenkarten hatten unerwünschte schwarze Rahmen. "
             "Gelöst durch <code>no borders, no frames, no black edges</code> im Prompt."),
        ],
        "learnings": [
            "<b>Iteratives Prompt-Engineering</b> &mdash; Die Prompts wurden durch mehrere Test-Runden "
            "schrittweise verbessert. Jeder Testlauf offenbarte neue Edge Cases.",
            "<b>Negative Anweisungen sind mächtig</b> &mdash; Explizite Verbote (<code>Do NOT reshape</code>, "
            "<code>no borders</code>) wirken oft besser als positive Anweisungen allein.",
            "<b>Beispiel-basiertes Prompting</b> &mdash; Gute und schlechte Beispiele im Content-Prompt "
            "verbessern die LLM-Objekt-Auswahl massiv (Schuhe, Getränke).",
        ],
    },
}


# ── Render Functions ─────────────────────────────────────────────────────────

def render_architecture():
    """Rendert die Architektur-Übersicht."""
    st.markdown("""
    <div class="how-header">
        <h1>🏗️ Architektur-Übersicht</h1>
        <p>Wie MEMOKI unter der Haube funktioniert</p>
    </div>
    """, unsafe_allow_html=True)

    # Tech Stack Badges
    st.markdown("""
    <span class="tech-badge streamlit">Streamlit</span>
    <span class="tech-badge gemini">Gemini 2.5 Flash</span>
    <span class="tech-badge gemini">Gemini 3 Pro</span>
    <span class="tech-badge python">Python 3.11+</span>
    <span class="tech-badge prompt">Prompt Engineering</span>
    """, unsafe_allow_html=True)

    # KPI Cards
    st.markdown('<div class="section-head">📊 Auf einen Blick</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="kpi-card">
            <div class="kpi-value">5</div>
            <div class="kpi-label">Spielmodi</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="kpi-card">
            <div class="kpi-value">10+</div>
            <div class="kpi-label">Bildstile</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="kpi-card">
            <div class="kpi-value">2</div>
            <div class="kpi-label">Gemini-Modelle</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="kpi-card">
            <div class="kpi-value">3</div>
            <div class="kpi-label">Wissensbasen</div>
        </div>""", unsafe_allow_html=True)

    # Pipeline
    st.markdown('<div class="section-head">🔄 Die MEMOKI-Pipeline</div>', unsafe_allow_html=True)
    steps = [
        ("🗣️ Chat-Agent", "Der MEMOKI-Agent (Gemini 2.5 Flash) führt den User durch "
         "die Konfiguration: Modus, Thema, Stil, Zielgruppe."),
        ("📋 Content-Generierung", "Je nach Modus werden Objekte per LLM generiert oder "
         "aus kuratierten Wissensbasen geladen (Teekesselchen, Paare, Shapes)."),
        ("✍️ Prompt-Building", "Spezialisierte Prompt-Builder erzeugen optimierte Bild-Prompts "
         "mit Stil, Zielgruppe und modus-spezifischen Anpassungen."),
        ("🎨 Bild-Generierung", "Gemini 3 Pro (Qualität) oder Gemini 2.5 Flash (Schnell) "
         "generiert die Kartenbilder parallel via ThreadPoolExecutor."),
        ("🃏 Deck-Assembly", "Die Bilder werden zu Card-Objekten, das Deck wird gemischt, "
         "und die interaktive Spieloberfläche wird gerendert."),
    ]
    for label, desc in steps:
        st.markdown(f"""<div class="pipeline-step">
            <b>{label}</b><br>{desc}
        </div>""", unsafe_allow_html=True)

    # Architecture Boxes
    st.markdown('<div class="section-head">📁 Projekt-Struktur</div>', unsafe_allow_html=True)
    st.markdown("""<div class="arch-grid">
        <div class="arch-box">
            <h4>🎭 Frontend</h4>
            <code>app.py</code> &mdash; Streamlit-UI mit Custom CSS, Chat-Interface,
            Mode-Selector, Kartenraster und Spiellogik. Nunito-Font, Gradient-Background,
            interaktive Mode-Cards.
        </div>
        <div class="arch-box">
            <h4>🤖 Agent</h4>
            <code>agents/memoki.py</code> &mdash; Chat-Orchestrierung mit Gemini.
            System-Prompt mit Modus-spezifischen Regeln, JSON-Action-Block-Erkennung,
            Gesprächshistorie.
        </div>
        <div class="arch-box">
            <h4>🖼️ Generatoren</h4>
            <code>tools/image.py</code> &mdash; Bildgenerierung via Gemini mit
            Stil-Mapping und Zielgruppen-Anpassung.<br>
            <code>tools/content.py</code> &mdash; Content-Generierung per LLM.
        </div>
        <div class="arch-box">
            <h4>✍️ Prompts</h4>
            <code>prompts/</code> &mdash; Spezialisierte Prompt-Builder pro Modus:
            Classic, Paare, Teekesselchen, Mathe I, Mathe II. Jeder mit eigenen
            Optimierungen und Sonderfällen.
        </div>
        <div class="arch-box">
            <h4>🎮 Game Engine</h4>
            <code>game/</code> &mdash; Card (Dataclass), Deck (Mischen, Verwalten),
            GameSession (Spielzustand, Flip-Logik, Match-Erkennung).
        </div>
        <div class="arch-box">
            <h4>📚 Wissensbasen</h4>
            <code>knowledge/</code> &mdash; Kuratierte JSON-Dateien:
            Teekesselchen (Homonyme mit 2 Bedeutungen), Paare (logisch zusammengehörige
            Objekte), Math-Shapes (abstrakte Formen).
        </div>
    </div>""", unsafe_allow_html=True)

    # Model Overview
    st.markdown('<div class="section-head">🧠 KI-Modelle im Einsatz</div>', unsafe_allow_html=True)
    st.markdown("""
| Modell | Aufgabe | Warum dieses Modell? |
|--------|---------|---------------------|
| Gemini 2.5 Flash | Chat-Agent, Objekt-Generierung | Schnell, günstig, gutes Sprachverständnis |
| Gemini 3 Pro | Bildgenerierung (Standard) | Beste Bildqualität, kreative Stile |
| Gemini 2.5 Flash Image | Bildgenerierung (Schnell) | Schneller und günstiger für einfachere Motive |
    """)


def render_mode_page(key: str):
    """Rendert eine Modus-Dokumentationsseite."""
    mode = MODE_DATA[key]

    # Header
    st.markdown(f"""
    <div class="how-header">
        <h1>{mode["icon"]} {mode["title"]}</h1>
        <p>Spielmodus-Dokumentation &mdash; Wie es funktioniert und was wir gelernt haben</p>
    </div>
    """, unsafe_allow_html=True)

    # Two-column layout: Was & Wie
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-head">🎯 Was es macht</div>', unsafe_allow_html=True)
        st.markdown(mode["what"], unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-head">⚙️ Wie es funktioniert</div>', unsafe_allow_html=True)
        for label, desc in mode["how"]:
            st.markdown(f"""<div class="pipeline-step">
                <b>{label}</b><br>{desc}
            </div>""", unsafe_allow_html=True)

    # Prompt Engineering
    st.markdown('<div class="section-head">✍️ Prompt Engineering</div>', unsafe_allow_html=True)
    for item in mode["prompt_engineering"]:
        st.markdown(f'<div class="info-item">{item}</div>', unsafe_allow_html=True)

    # Challenges
    st.markdown('<div class="section-head">🔧 Herausforderungen & Lösungen</div>', unsafe_allow_html=True)
    for title, desc in mode["challenges"]:
        st.markdown(f'<div class="challenge-item"><b>{title}</b> &mdash; {desc}</div>',
                    unsafe_allow_html=True)

    # Learnings
    st.markdown('<div class="section-head">💡 Learnings</div>', unsafe_allow_html=True)
    for item in mode["learnings"]:
        st.markdown(f'<div class="learning-item">{item}</div>', unsafe_allow_html=True)


def render_style_system():
    """Rendert die Stil & Zielgruppen Dokumentation."""
    st.markdown("""
    <div class="how-header">
        <h1>🎨 Stil & Zielgruppen</h1>
        <p>Das hybride Stil-System und die Zielgruppen-Anpassung</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-head">🖌️ Das Hybrid-Stil-System</div>', unsafe_allow_html=True)
        st.markdown(
            "MEMOKI verwendet ein **hybrides** Stil-System: 10 vordefinierte Stile "
            "mit optimierten Prompt-Fragmenten **plus** die Möglichkeit, beliebige "
            "Freitext-Stile einzugeben.",
            unsafe_allow_html=True,
        )

        st.markdown("""
        <div class="info-item">
            <b>Wie es funktioniert:</b> Die Funktion <code>resolve_style(style)</code> prüft,
            ob der Stil in der <code>STYLE_MAP</code> existiert. Wenn ja, wird das optimierte
            Prompt-Fragment verwendet. Wenn nein, wird der Freitext direkt als Stil-Beschreibung
            in den Prompt eingefügt.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Vordefinierte Stile:**")
        styles = {
            "cartoon": "Bold outlines, vibrant colors, Disney-Pixar inspired",
            "photorealistic": "High detail, professional photography, soft studio lighting",
            "watercolor": "Soft edges, pastel colors, artistic",
            "minimalist": "Simple shapes, flat design, limited color palette",
            "artistic": "Painterly, impressionist style, soft brushstrokes",
            "black-and-white": "Grayscale, monochrome, pencil sketch style",
            "pencil": "Hand-sketched, graphite on paper",
            "retro": "Vintage style, muted warm tones, 1970s aesthetic",
            "pixel": "8-bit retro game aesthetic, blocky shapes",
            "comic": "Bold ink outlines, halftone dots, dynamic",
        }
        for key_name, desc in styles.items():
            st.markdown(f"""<div class="style-card">
                <code>{key_name}</code> &rarr; {desc}
            </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-head">🎯 Zielgruppen-Anpassung</div>', unsafe_allow_html=True)
        st.markdown(
            "Jeder Bild-Prompt wird automatisch mit zielgruppenspezifischen "
            "Attributen angereichert:",
            unsafe_allow_html=True,
        )

        audiences = {
            "children": ("👶", "Kinder", "cute, friendly, rounded shapes, bright cheerful colors"),
            "teenagers": ("🧑", "Teenager", "cool, modern, dynamic, trendy aesthetic"),
            "adults": ("👔", "Erwachsene", "sophisticated, elegant, refined details"),
        }
        for key_name, (icon, label, desc) in audiences.items():
            st.markdown(f"""<div class="style-card">
                {icon} <b>{label}</b> (<code>{key_name}</code>)<br>
                &rarr; <i>{desc}</i>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-head">🆓 Freitext-Stile</div>', unsafe_allow_html=True)
        st.markdown(
            "Neben den vordefinierten Stilen können User beliebige Stile eingeben. "
            "Der MEMOKI-Agent formuliert diese als englische Stil-Beschreibung:",
            unsafe_allow_html=True,
        )

        free_styles = [
            ("van Gogh", "van Gogh post-impressionist style, thick swirling brushstrokes, bold vivid colors"),
            ("Bauhaus", "Bauhaus geometric style, primary colors, functional minimalism"),
            ("Jugendstil", "Art Nouveau ornamental style, flowing organic lines, floral patterns"),
        ]
        for user_input, prompt_output in free_styles:
            st.markdown(f"""<div class="info-item">
                User sagt: <b>"{user_input}"</b><br>
                &rarr; Prompt wird: <code>{prompt_output}</code>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-head">💡 Learnings</div>', unsafe_allow_html=True)
        learnings = [
            "<b>Hybrides System ist optimal</b> &mdash; Vordefinierte Stile garantieren Qualität, "
            "Freitext ermöglicht Kreativität.",
            "<b>Stil-Konsistenz über Karten</b> &mdash; Der Stil-Prompt muss stark genug sein, "
            "um über 10-20 verschiedene Motive hinweg einen einheitlichen Look zu erzeugen.",
            "<b>Zielgruppe beeinflusst alles</b> &mdash; Nicht nur Farben ändern sich, "
            "sondern auch Formen (runder für Kinder) und Details (feiner für Erwachsene).",
        ]
        for item in learnings:
            st.markdown(f'<div class="learning-item">{item}</div>', unsafe_allow_html=True)


# ── Routing ──────────────────────────────────────────────────────────────────

NAV_TO_KEY = {
    NAV_ITEMS[1]: "classic",
    NAV_ITEMS[2]: "paare",
    NAV_ITEMS[3]: "teekesselchen",
    NAV_ITEMS[4]: "mathe_abstrakt",
    NAV_ITEMS[5]: "mathe_konkret",
}

if selected == NAV_ITEMS[0]:
    render_architecture()
elif selected == NAV_ITEMS[6]:
    render_style_system()
else:
    mode_key = NAV_TO_KEY.get(selected)
    if mode_key:
        render_mode_page(mode_key)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="how-footer">
    MEMOKI &mdash; KI-Memory-Spiele-Macher | Built with Streamlit & Google Gemini
</div>
""", unsafe_allow_html=True)
