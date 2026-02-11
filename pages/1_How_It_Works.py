"""MEMOKI – How it Works: Dokumentation der Architektur und Spielmodi."""

import streamlit as st
import streamlit.components.v1 as components

from i18n import t, get_mode_data, render_lang_selector

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=t("hiw.page_title"),
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
    t("hiw.nav.architecture"),
    t("hiw.nav.classic"),
    t("hiw.nav.paare"),
    t("hiw.nav.teekesselchen"),
    t("hiw.nav.mathe_abstrakt"),
    t("hiw.nav.mathe_konkret"),
    t("hiw.nav.style"),
]

with st.sidebar:
    st.markdown(t("hiw.sidebar_title"))
    st.markdown("---")
    render_lang_selector()
    st.markdown("---")
    selected = st.radio("Navigation", NAV_ITEMS, label_visibility="collapsed")


# ── Mode Data (sprachabhängig) ──────────────────────────────────────────────

MODE_DATA = get_mode_data()


# ── Render Functions ─────────────────────────────────────────────────────────

def render_architecture():
    """Rendert die Architektur-Übersicht."""
    st.markdown(f"""
    <div class="how-header">
        <h1>{t("hiw.arch.header")}</h1>
        <p>{t("hiw.arch.subheader")}</p>
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
    st.markdown(f'<div class="section-head">{t("hiw.arch.kpi_title")}</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-value">5</div>
            <div class="kpi-label">{t("hiw.arch.kpi.modes")}</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-value">10+</div>
            <div class="kpi-label">{t("hiw.arch.kpi.styles")}</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-value">2</div>
            <div class="kpi-label">{t("hiw.arch.kpi.models")}</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-value">3</div>
            <div class="kpi-label">{t("hiw.arch.kpi.knowledge")}</div>
        </div>""", unsafe_allow_html=True)

    # Pipeline
    st.markdown(f'<div class="section-head">{t("hiw.arch.pipeline_title")}</div>', unsafe_allow_html=True)
    steps = [
        (t("hiw.arch.pipeline.chat_agent"), t("hiw.arch.pipeline.chat_agent_desc")),
        (t("hiw.arch.pipeline.content"), t("hiw.arch.pipeline.content_desc")),
        (t("hiw.arch.pipeline.prompt_building"), t("hiw.arch.pipeline.prompt_building_desc")),
        (t("hiw.arch.pipeline.image_gen"), t("hiw.arch.pipeline.image_gen_desc")),
        (t("hiw.arch.pipeline.deck_assembly"), t("hiw.arch.pipeline.deck_assembly_desc")),
    ]
    for label, desc in steps:
        st.markdown(f"""<div class="pipeline-step">
            <b>{label}</b><br>{desc}
        </div>""", unsafe_allow_html=True)

    # Architecture Boxes
    st.markdown(f'<div class="section-head">{t("hiw.arch.structure_title")}</div>', unsafe_allow_html=True)
    boxes = [
        (t("hiw.arch.box.frontend"), t("hiw.arch.box.frontend_desc")),
        (t("hiw.arch.box.agent"), t("hiw.arch.box.agent_desc")),
        (t("hiw.arch.box.generators"), t("hiw.arch.box.generators_desc")),
        (t("hiw.arch.box.prompts"), t("hiw.arch.box.prompts_desc")),
        (t("hiw.arch.box.game_engine"), t("hiw.arch.box.game_engine_desc")),
        (t("hiw.arch.box.knowledge"), t("hiw.arch.box.knowledge_desc")),
    ]
    box_html = '<div class="arch-grid">'
    for title, desc in boxes:
        box_html += f"""<div class="arch-box">
            <h4>{title}</h4>
            {desc}
        </div>"""
    box_html += '</div>'
    st.markdown(box_html, unsafe_allow_html=True)

    # Model Overview
    st.markdown(f'<div class="section-head">{t("hiw.arch.models_title")}</div>', unsafe_allow_html=True)
    st.markdown(t("hiw.arch.models_table"))


def render_mode_page(key: str):
    """Rendert eine Modus-Dokumentationsseite."""
    mode = MODE_DATA[key]

    # Header
    st.markdown(f"""
    <div class="how-header">
        <h1>{mode["icon"]} {mode["title"]}</h1>
        <p>{t("hiw.mode.subheader")}</p>
    </div>
    """, unsafe_allow_html=True)

    # Two-column layout: Was & Wie
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<div class="section-head">{t("hiw.mode.what_title")}</div>', unsafe_allow_html=True)
        st.markdown(mode["what"], unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="section-head">{t("hiw.mode.how_title")}</div>', unsafe_allow_html=True)
        for label, desc in mode["how"]:
            st.markdown(f"""<div class="pipeline-step">
                <b>{label}</b><br>{desc}
            </div>""", unsafe_allow_html=True)

    # Prompt Engineering
    st.markdown(f'<div class="section-head">{t("hiw.mode.pe_title")}</div>', unsafe_allow_html=True)
    for item in mode["prompt_engineering"]:
        st.markdown(f'<div class="info-item">{item}</div>', unsafe_allow_html=True)

    # Challenges
    st.markdown(f'<div class="section-head">{t("hiw.mode.challenges_title")}</div>', unsafe_allow_html=True)
    for title, desc in mode["challenges"]:
        st.markdown(f'<div class="challenge-item"><b>{title}</b> &mdash; {desc}</div>',
                    unsafe_allow_html=True)

    # Learnings
    st.markdown(f'<div class="section-head">{t("hiw.mode.learnings_title")}</div>', unsafe_allow_html=True)
    for item in mode["learnings"]:
        st.markdown(f'<div class="learning-item">{item}</div>', unsafe_allow_html=True)


def render_style_system():
    """Rendert die Stil & Zielgruppen Dokumentation."""
    st.markdown(f"""
    <div class="how-header">
        <h1>{t("hiw.style.header")}</h1>
        <p>{t("hiw.style.subheader")}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<div class="section-head">{t("hiw.style.hybrid_title")}</div>', unsafe_allow_html=True)
        st.markdown(t("hiw.style.hybrid_desc"), unsafe_allow_html=True)

        st.markdown(f"""
        <div class="info-item">
            {t("hiw.style.how_it_works")}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(t("hiw.style.predefined_title"))
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
        st.markdown(f'<div class="section-head">{t("hiw.style.audience_title")}</div>', unsafe_allow_html=True)
        st.markdown(t("hiw.style.audience_desc"), unsafe_allow_html=True)

        audiences = {
            "children": ("👶", t("hiw.style.audience.children"), "cute, friendly, rounded shapes, bright cheerful colors"),
            "teenagers": ("🧑", t("hiw.style.audience.teenagers"), "cool, modern, dynamic, trendy aesthetic"),
            "adults": ("👔", t("hiw.style.audience.adults"), "sophisticated, elegant, refined details"),
        }
        for key_name, (icon, label, desc) in audiences.items():
            st.markdown(f"""<div class="style-card">
                {icon} <b>{label}</b> (<code>{key_name}</code>)<br>
                &rarr; <i>{desc}</i>
            </div>""", unsafe_allow_html=True)

        st.markdown(f'<div class="section-head">{t("hiw.style.freetext_title")}</div>', unsafe_allow_html=True)
        st.markdown(t("hiw.style.freetext_desc"), unsafe_allow_html=True)

        free_styles = [
            ("van Gogh", "van Gogh post-impressionist style, thick swirling brushstrokes, bold vivid colors"),
            ("Bauhaus", "Bauhaus geometric style, primary colors, functional minimalism"),
            ("Jugendstil", "Art Nouveau ornamental style, flowing organic lines, floral patterns"),
        ]
        for user_input, prompt_output in free_styles:
            st.markdown(f"""<div class="info-item">
                {t("hiw.style.user_says", input=user_input)}<br>
                &rarr; {t("hiw.style.prompt_becomes", output=prompt_output)}
            </div>""", unsafe_allow_html=True)

        st.markdown(f'<div class="section-head">{t("hiw.style.learnings_title")}</div>', unsafe_allow_html=True)
        # Style learnings are in MODE_DATA-like structure but kept simple here
        learnings_de = [
            "<b>Hybrides System ist optimal</b> &mdash; Vordefinierte Stile garantieren Qualität, "
            "Freitext ermöglicht Kreativität.",
            "<b>Stil-Konsistenz über Karten</b> &mdash; Der Stil-Prompt muss stark genug sein, "
            "um über 10-20 verschiedene Motive hinweg einen einheitlichen Look zu erzeugen.",
            "<b>Zielgruppe beeinflusst alles</b> &mdash; Nicht nur Farben ändern sich, "
            "sondern auch Formen (runder für Kinder) und Details (feiner für Erwachsene).",
        ]
        learnings_en = [
            "<b>Hybrid system is optimal</b> &mdash; Predefined styles guarantee quality, "
            "free text enables creativity.",
            "<b>Style consistency across cards</b> &mdash; The style prompt must be strong enough "
            "to maintain a consistent look across 10-20 different subjects.",
            "<b>Audience affects everything</b> &mdash; Not just colors change, "
            "but also shapes (rounder for kids) and details (finer for adults).",
        ]
        from i18n import get_lang
        learnings = learnings_en if get_lang() == "en" else learnings_de
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
st.markdown(f"""
<div class="how-footer">
    {t("hiw.footer")}
</div>
""", unsafe_allow_html=True)
