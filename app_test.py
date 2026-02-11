"""MEMOKI – TEST-MODUS (alle Karten aufgedeckt).

Kopie von app.py zum schnellen Testen. Karten werden sofort
aufgedeckt und nach pair_id sortiert angezeigt (Paare nebeneinander).
Starten mit: streamlit run app_test.py
"""

import io
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from i18n import t, get_lang, render_lang_selector
from agents.memoki import MemokiAgent
from tools.content import generate_objects, generate_countable_objects, load_teekesselchen, load_math_shape, load_pairs, load_pairs_themes
from tools.image import build_image_prompt, generate_card_image
from prompts.math_memory import build_number_prompt, build_shapes_prompt, build_real_objects_prompt
from prompts.pairs_memory import build_pair_object_prompt
from game.card import Card
from game.deck import Deck

# --- Page Config ---
st.set_page_config(
    page_title=t("page.title_test"),
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fdf6f0 0%, #e8f4f8 50%, #f0e6f6 100%);
    }

    .block-container {
        padding-top: 1rem !important;
    }

    /* --- Header-Banner --- */
    .memoki-banner {
        background: white;
        border-radius: 18px;
        padding: 0.8rem 1.5rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 3px 15px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.8rem;
    }

    .memoki-brand {
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    .memoki-title {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ff6b6b, #ffa502, #2ed573, #1e90ff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        letter-spacing: 2px;
    }

    .memoki-subtitle {
        font-size: 0.85rem;
        color: #6b7280;
        font-weight: 600;
    }

    .memoki-features {
        display: flex;
        gap: 1.2rem;
        flex-wrap: wrap;
    }

    .memoki-feat {
        font-size: 0.8rem;
        color: #4a5568;
        font-weight: 600;
    }

    /* --- Mode-Karten --- */
    .mode-card {
        border-radius: 12px;
        padding: 0.55rem 0.9rem;
        margin-bottom: 0.4rem;
        cursor: pointer;
        border: 2px solid transparent;
        transition: transform 0.15s, box-shadow 0.15s;
    }

    .mode-card:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 14px rgba(0,0,0,0.1);
    }

    /* Transparenter Button-Overlay auf Mode-Karten */
    [data-testid="stVerticalBlock"] > div:has(.mode-card) + div {
        margin-top: -3.6rem;
        height: 3.6rem;
        position: relative;
        z-index: 10;
        overflow: hidden;
    }
    [data-testid="stVerticalBlock"] > div:has(.mode-card) + div button {
        width: 100% !important;
        height: 3.6rem !important;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        box-shadow: none !important;
        cursor: pointer !important;
    }
    [data-testid="stVerticalBlock"] > div:has(.mode-card) + div button:hover {
        background: rgba(255,255,255,0.18) !important;
        border-radius: 12px !important;
    }

    .mode-classic    { background: linear-gradient(135deg, #dfe6e9, #b2bec3); border-color: #636e72; }
    .mode-paare      { background: linear-gradient(135deg, #ffeaa7, #fdcb6e); border-color: #f39c12; }
    .mode-teekessel  { background: linear-gradient(135deg, #c7ecee, #7ed6df); border-color: #22a6b3; }
    .mode-mathe1     { background: linear-gradient(135deg, #f8c9d4, #e17055); border-color: #d63031; }
    .mode-mathe2     { background: linear-gradient(135deg, #d5aee4, #a29bfe); border-color: #6c5ce7; }

    .mode-card .mode-name {
        font-size: 0.88rem;
        font-weight: 700;
        color: #2d3436;
    }

    .mode-card .mode-desc {
        font-size: 0.75rem;
        color: #2d3436;
        opacity: 0.8;
    }

    /* --- Chat-Input --- */
    .stChatMessage {
        font-size: 0.92rem;
    }

    .stChatInput {
        background: white;
        border: 2px solid #2ed573;
        border-radius: 18px;
        padding: 0.5rem;
        box-shadow: 0 3px 15px rgba(46, 213, 115, 0.15);
    }

    .stChatInput > div {
        border-radius: 14px !important;
        border: none !important;
    }

    .stChatInput textarea {
        min-height: 80px !important;
        font-size: 0.95rem !important;
        font-family: 'Nunito', sans-serif !important;
    }

    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        font-family: 'Nunito', sans-serif;
    }

    .mini-divider {
        text-align: center;
        font-size: 0.8rem;
        letter-spacing: 5px;
        margin: 0.4rem 0;
        opacity: 0.35;
    }

    .section-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #2d3436;
        margin: 0.3rem 0 0.4rem;
    }

    .footer {
        text-align: center;
        color: #b2bec3;
        font-size: 0.7rem;
        padding-top: 0.4rem;
    }

    /* --- Memory-Spielfeld --- */
    .memory-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
        gap: 10px;
        padding: 10px;
    }

    .memory-card {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        width: 100%;
        max-height: 140px;
    }

    .memory-card img {
        width: 100%;
        height: 140px;
        object-fit: contain;
        display: block;
    }

    /* Button-Karten gleich groß wie aufgedeckte */
    .stColumn .stButton > button {
        height: 140px !important;
        font-size: 1.5rem !important;
    }

    .progress-box {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

</style>
""", unsafe_allow_html=True)

# ── Sidebar-Fixes per JS ─────────────────────────────────────────────────────
components.html("""
<script>
(function fix() {
    const doc = window.parent.document;
    const sidebar = doc.querySelector('section[data-testid="stSidebar"]');
    if (!sidebar) { setTimeout(fix, 300); return; }

    const walker = document.createTreeWalker(sidebar, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
        const node = walker.currentNode;
        if (node.textContent.includes('keyboard_double')) {
            let el = node.parentElement;
            while (el && el !== sidebar) {
                if (el.tagName === 'BUTTON' || el.getAttribute('role') === 'button') {
                    el.style.display = 'none';
                    break;
                }
                el = el.parentElement;
            }
            if (el === sidebar) node.parentElement.style.display = 'none';
        }
    }

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


# ============================
# HELPER: PIL Image → base64
# ============================
def img_to_base64(img: Image.Image) -> str:
    """Konvertiert PIL Image zu base64-String für HTML."""
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


# ============================
# MODE-MAPPING (internal keys)
# ============================
GAME_MODES = {
    "classic": {"icon": "🖼️", "css": "mode-classic"},
    "paare": {"icon": "🧩", "css": "mode-paare"},
    "teekesselchen": {"icon": "🫖", "css": "mode-teekessel"},
    "mathe_abstrakt": {"icon": "🔢", "css": "mode-mathe1"},
    "mathe_konkret": {"icon": "🎯", "css": "mode-mathe2"},
}


# ============================
# HEADER-BANNER
# ============================
st.markdown(f"""
<div class="memoki-banner">
    <div class="memoki-brand">
        <div>
            <div class="memoki-title">🎴 MEMOKI</div>
            <div class="memoki-subtitle">{t("banner.subtitle")}</div>
        </div>
    </div>
    <div class="memoki-features">
        <span class="memoki-feat">{t("banner.feat_generate")}</span>
        <span class="memoki-feat">{t("banner.feat_play")}</span>
        <span class="memoki-feat">{t("banner.feat_print")}</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================
# 2-SPALTEN-LAYOUT
# ============================
left_col, right_col = st.columns([1, 2], gap="large")


# --- LINKE SPALTE ---
with left_col:
    # Language selector
    render_lang_selector()

    st.markdown(f'<div class="section-title">{t("section.game_mode")}</div>', unsafe_allow_html=True)

    # Mode-Auswahl: bunte Karte + transparenter Button als Overlay
    mode_keys = list(GAME_MODES.keys())
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = mode_keys[0]

    def _select_mode(mode_key):
        st.session_state.selected_mode = mode_key

    for mk, mode_info in GAME_MODES.items():
        is_selected = mk == st.session_state.selected_mode
        style_attr = "border-width: 3px; box-shadow: 0 4px 14px rgba(0,0,0,0.12);" if is_selected else "opacity: 0.6;"
        check = " ✓" if is_selected else ""
        mode_name = t(f"mode.{mk}.name")
        mode_desc = t(f"mode.{mk}.desc")
        st.markdown(f"""
        <div class="mode-card {mode_info['css']}" style="{style_attr}">
            <div class="mode-name">{mode_info['icon']} {mode_name}{check}</div>
            <div class="mode-desc">{mode_desc}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button(
            mode_name,
            key=f"mode_{mk}",
            use_container_width=True,
            on_click=_select_mode,
            args=(mk,),
        )

    selected_mode = st.session_state.selected_mode

    st.markdown('<div class="mini-divider">🟡 🔵 🟢 🟣 🔴</div>', unsafe_allow_html=True)

    num_pairs = 8  # TEST: weniger Paare für schnelleres Testen

    st.markdown(f'<div class="footer">{t("footer.text")}</div>', unsafe_allow_html=True)


# ============================
# SESSION STATE INIT
# ============================
mode_key = selected_mode
lang = get_lang()

# Agent neu erstellen bei Modus/Paarzahl/Sprach-Wechsel
if (
    "agent" not in st.session_state
    or st.session_state.get("current_mode") != mode_key
    or st.session_state.get("current_pairs") != num_pairs
    or st.session_state.get("current_lang") != lang
):
    st.session_state.agent = MemokiAgent(mode=mode_key, pair_count=num_pairs, lang=lang)
    st.session_state.current_mode = mode_key
    st.session_state.current_pairs = num_pairs
    st.session_state.current_lang = lang
    st.session_state.messages = []
    st.session_state.deck = None
    st.session_state.generating = False
    st.session_state.flipped = set()
    st.session_state.matched = set()
    st.session_state.first_pick = None
    st.session_state.pending_flip_back = None
    st.session_state.moves = 0

# Erste Begrüßung
if not st.session_state.messages:
    mode_display_name = t(f"mode.{mode_key}.name")
    hello = t("greeting.hello") + t("greeting.mode_chosen", mode_name=mode_display_name)

    if mode_key == "teekesselchen":
        hello += t("greeting.teekesselchen")
    elif mode_key == "mathe_abstrakt":
        hello += t("greeting.mathe_abstrakt", num_pairs=num_pairs)
    elif mode_key == "mathe_konkret":
        hello += t("greeting.mathe_konkret", num_pairs=num_pairs)
    elif mode_key == "paare":
        available_themes = load_pairs_themes(lang=lang)
        themes_str = ", ".join(available_themes)
        hello += t("greeting.paare", themes_str=themes_str)
    else:
        hello += t("greeting.classic")

    st.session_state.messages.append({
        "role": "assistant",
        "content": hello,
    })


# ============================
# RECHTE SPALTE: Chat + Spiel
# ============================
with right_col:
    # Wenn Deck vorhanden → Spielfeld anzeigen
    if st.session_state.deck is not None:
        deck = st.session_state.deck

        # TEST-MODUS: Alle Karten aufgedeckt (kein Spiellogik)
        total_pairs = len(deck.cards) // 2
        st.markdown(f"""
        <div class="progress-box">
            <strong>{t("test.title")}</strong> &nbsp;|&nbsp;
            {t("test.all_revealed", total_pairs=total_pairs)} &nbsp;|&nbsp;
            {t("test.grouped")}
        </div>
        """, unsafe_allow_html=True)

        # Karten nach pair_id sortieren, damit Paare nebeneinander stehen
        sorted_cards = sorted(deck.cards, key=lambda c: (c.pair_id, c.label))

        cols_per_row = 5 if total_pairs <= 10 else 8
        cols = st.columns(cols_per_row)

        for idx, card in enumerate(sorted_cards):
            col = cols[idx % cols_per_row]
            with col:
                if card.image is not None:
                    b64 = img_to_base64(card.image)
                    st.markdown(
                        f'<div class="memory-card" style="border: 2px solid #ddd;">'
                        f'<img src="data:image/png;base64,{b64}" />'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(t("preview.no_image"))
                st.caption(f"#{card.pair_id} – {card.label}")

        if st.button(t("btn.new_game")):
            st.session_state.deck = None
            st.session_state.messages = []
            st.session_state.flipped = set()
            st.session_state.matched = set()
            st.session_state.first_pick = None
            st.session_state.pending_flip_back = None
            st.session_state.moves = 0
            st.session_state.agent = MemokiAgent(mode=mode_key, pair_count=num_pairs, lang=lang)
            st.rerun()

        st.markdown("---")

    # Chat-Interface
    st.markdown(f'<div class="section-title">{t("section.chat")}</div>', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        avatar = "🎴" if msg["role"] == "assistant" else "🙋"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    if prompt := st.chat_input(t("chat.placeholder")):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🙋"):
            st.markdown(prompt)

        # Agent-Antwort
        with st.chat_message("assistant", avatar="🎴"):
            with st.spinner(t("chat.thinking")):
                response = st.session_state.agent.chat(prompt)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

        # Prüfe ob Agent einen Action-Block ausgegeben hat
        action = MemokiAgent.parse_action(response)
        if action and action.get("action") == "generate":
            st.session_state.generating = True
            st.session_state.gen_action = action
            st.rerun()

    # Generierungs-Pipeline
    if st.session_state.get("generating"):
        action = st.session_state.get("gen_action", {})
        style = action.get("style", "cartoon")
        audience = action.get("audience", "children")

        def _gen_one_img(idx_and_prompt):
            """Generiert ein Bild mit Fallback."""
            idx, label, prompt = idx_and_prompt
            try:
                return idx, label, generate_card_image(prompt), None
            except Exception as e:
                try:
                    return idx, label, generate_card_image(prompt, use_fast=True), t("gen.fallback", error=e)
                except Exception as e2:
                    return idx, label, None, t("gen.failed", error=e2)

        def _parallel_images(jobs, total_label=""):
            """Generiert Bilder parallel und zeigt Fortschritt."""
            results = [None] * len(jobs)
            done = 0
            total = len(jobs)
            progress = st.progress(0, text=t("gen.progress", label=total_label))
            with ThreadPoolExecutor(max_workers=5) as pool:
                futures = {pool.submit(_gen_one_img, j): j[0] for j in jobs}
                for future in as_completed(futures):
                    idx, label, img, warn = future.result()
                    results[idx] = img
                    done += 1
                    if warn:
                        st.warning(f"⚠️ {label}: {warn}")
                    else:
                        st.write(f"✅ {label}")
                    progress.progress(done / total, text=t("gen.image_progress", done=done, total=total))
            return results

        # === TEEKESSELCHEN ===
        if mode_key == "teekesselchen":
            with st.status(t("gen.tk.status", num_pairs=num_pairs), expanded=True) as status:
                st.write(t("gen.tk.selecting", num_pairs=num_pairs))
                try:
                    tk_list = load_teekesselchen(num_pairs, lang=lang)
                    words = [tk["word"] for tk in tk_list]
                    st.write(t("gen.tk.words_ok", words=", ".join(words)))
                except Exception as e:
                    st.error(t("gen.error_loading", error=e))
                    st.session_state.generating = False
                    st.stop()

                jobs = []
                for i, tk in enumerate(tk_list):
                    prompt_a = build_image_prompt(tk["meaning_a"], style, audience)
                    prompt_b = build_image_prompt(tk["meaning_b"], style, audience)
                    jobs.append((i * 2, f"{tk['word']} ({tk['label_a']})", prompt_a))
                    jobs.append((i * 2 + 1, f"{tk['word']} ({tk['label_b']})", prompt_b))

                st.write(t("gen.tk.images", count=len(jobs)))
                all_images = _parallel_images(jobs, f"{len(jobs)}")

                images_a = [all_images[i * 2] for i in range(num_pairs)]
                images_b = [all_images[i * 2 + 1] for i in range(num_pairs)]

                st.write(t("gen.building_deck"))
                deck = Deck.build_teekesselchen(tk_list, images_a, images_b)

                st.session_state.deck = deck
                st.session_state.generating = False
                status.update(label=t("gen.tk.done"), state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": t("gen.tk.complete_msg", num_pairs=num_pairs),
            })
            st.rerun()

        # === MATHE ABSTRAKT ===
        elif mode_key == "mathe_abstrakt":
            shape_id = action.get("shape", "surprise")
            with st.status(t("gen.ma.status", num_pairs=num_pairs), expanded=True) as status:
                st.write(t("gen.ma.loading_shape", shape_id=shape_id))
                try:
                    shape = load_math_shape(shape_id)
                    shape_name = shape.get(f"name_{lang}", shape["name_de"])
                    st.write(t("gen.ma.shape_ok", name=shape_name, symbol=shape.get("symbol", "")))
                except Exception as e:
                    st.error(t("gen.error_shape", error=e))
                    st.session_state.generating = False
                    st.stop()

                numbers = list(range(1, num_pairs + 1))
                jobs = []
                for i, num in enumerate(numbers):
                    num_prompt = build_number_prompt(num, style, audience, theme=shape["name_en"])
                    shape_prompt = build_shapes_prompt(num, shape, style, audience)
                    jobs.append((i * 2, t("card.number", num=num), num_prompt))
                    jobs.append((i * 2 + 1, t("card.number_x", num=num, name=shape_name), shape_prompt))

                st.write(t("gen.ma.images", count=len(jobs)))
                all_images = _parallel_images(jobs, f"{len(jobs)}")

                number_images = [all_images[i * 2] for i in range(num_pairs)]
                shape_images = [all_images[i * 2 + 1] for i in range(num_pairs)]

                st.write(t("gen.building_deck"))
                deck = Deck.build_mathe_abstrakt(numbers, shape_name, number_images, shape_images, lang=lang)

                st.session_state.deck = deck
                st.session_state.generating = False
                status.update(label=t("gen.ma.done"), state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": t("gen.ma.complete_msg", num_pairs=num_pairs, shape_name=shape_name),
            })
            st.rerun()

        # === MATHE KONKRET ===
        elif mode_key == "mathe_konkret":
            theme = action.get("theme", "toys")
            with st.status(t("gen.mk.status", num_pairs=num_pairs), expanded=True) as status:
                st.write(t("gen.mk.generating_objects", num_pairs=num_pairs, theme=theme))
                try:
                    objects = generate_countable_objects(
                        theme=theme,
                        count=num_pairs,
                        audience=audience,
                    )
                    st.write(t("gen.mk.objects_ok", objects=", ".join(objects)))
                except Exception as e:
                    st.error(t("gen.error_objects", error=e))
                    st.session_state.generating = False
                    st.stop()

                numbers = list(range(1, num_pairs + 1))
                jobs = []
                for i, (num, obj) in enumerate(zip(numbers, objects)):
                    num_prompt = build_number_prompt(num, style, audience, theme=theme)
                    obj_prompt = build_real_objects_prompt(num, obj, style, audience, theme=theme)
                    jobs.append((i * 2, t("card.number", num=num), num_prompt))
                    jobs.append((i * 2 + 1, f"{num}x {obj}", obj_prompt))

                st.write(t("gen.mk.images", count=len(jobs)))
                all_images = _parallel_images(jobs, f"{len(jobs)}")

                number_images = [all_images[i * 2] for i in range(num_pairs)]
                object_images = [all_images[i * 2 + 1] for i in range(num_pairs)]

                st.write(t("gen.building_deck"))
                deck = Deck.build_mathe_konkret(numbers, objects, number_images, object_images, lang=lang)

                st.session_state.deck = deck
                st.session_state.generating = False
                status.update(label=t("gen.mk.done"), state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": t("gen.mk.complete_msg", theme=theme, num_pairs=num_pairs),
            })
            st.rerun()

        # === PAARE-MEMORY ===
        elif mode_key == "paare":
            theme = action.get("theme", "Küche")
            with st.status(t("gen.pa.status", num_pairs=num_pairs, theme=theme), expanded=True) as status:
                st.write(t("gen.pa.selecting", num_pairs=num_pairs, theme=theme))
                try:
                    pairs = load_pairs(theme, num_pairs, lang=lang)
                    pair_labels = [f"{p['a_label']} & {p['b_label']}" for p in pairs]
                    st.write(t("gen.pa.pairs_ok", pairs=", ".join(pair_labels)))
                except Exception as e:
                    st.error(t("gen.error_loading", error=e))
                    st.session_state.generating = False
                    st.stop()

                jobs = []
                for i, pair in enumerate(pairs):
                    prompt_a = build_pair_object_prompt(pair["a_en"], style, audience)
                    prompt_b = build_pair_object_prompt(pair["b_en"], style, audience)
                    jobs.append((i * 2, pair["a_label"], prompt_a))
                    jobs.append((i * 2 + 1, pair["b_label"], prompt_b))

                st.write(t("gen.pa.images", count=len(jobs)))
                all_images = _parallel_images(jobs, f"{len(jobs)}")

                images_a = [all_images[i * 2] for i in range(len(pairs))]
                images_b = [all_images[i * 2 + 1] for i in range(len(pairs))]

                st.write(t("gen.building_deck"))
                deck = Deck.build_paare(pairs, images_a, images_b)

                st.session_state.deck = deck
                st.session_state.generating = False
                status.update(label=t("gen.pa.done"), state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": t("gen.pa.complete_msg", theme=theme, count=len(pairs)),
            })
            st.rerun()

        # === CLASSIC ===
        else:
            theme = action.get("theme", "animals")
            with st.status(t("gen.cl.status", num_pairs=num_pairs), expanded=True) as status:
                st.write(t("gen.cl.generating_objects", num_pairs=num_pairs, theme=theme))
                try:
                    objects = generate_objects(
                        theme=theme,
                        count=num_pairs,
                        audience=audience,
                        style=style,
                    )
                    st.write(t("gen.cl.objects_ok", objects=", ".join(objects)))
                except Exception as e:
                    st.error(t("gen.error_objects", error=e))
                    st.session_state.generating = False
                    st.stop()

                st.write(t("gen.cl.images", num_pairs=num_pairs))
                jobs = [
                    (i, obj, build_image_prompt(obj, style, audience))
                    for i, obj in enumerate(objects)
                ]
                images = _parallel_images(jobs)

                st.write(t("gen.building_deck"))
                deck = Deck.build_classic(objects, images)

                st.session_state.deck = deck
                st.session_state.generating = False
                status.update(label=t("gen.cl.done"), state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": t("gen.cl.complete_msg", theme=theme, num_pairs=num_pairs),
            })
            st.rerun()
