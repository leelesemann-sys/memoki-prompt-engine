"""MEMOKI – KI-Memory-Spiele-Macher.

Streamlit-Frontend für den Memory-Spiel-Generator mit KI-generierten Bildern.
2-Spalten-Layout: Links Konfiguration, Rechts Chat + Spielfeld.
"""

import io
import base64
import random
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from agents.memoki import MemokiAgent
from tools.content import generate_objects, generate_countable_objects, load_teekesselchen, load_math_shape, load_pairs, load_pairs_themes
from tools.image import build_image_prompt, generate_card_image
from prompts.math_memory import build_number_prompt, build_shapes_prompt, build_real_objects_prompt
from prompts.pairs_memory import build_pair_object_prompt
from game.card import Card
from game.deck import Deck

# --- Page Config ---
st.set_page_config(
    page_title="MEMOKI – KI-Memory-Spiele-Macher",
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="expanded",
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
        if (span && /^app2?$/i.test(span.textContent.trim())) {
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
# MODE-MAPPING
# ============================
GAME_MODES = {
    "Klassisches Memory": {
        "icon": "🖼️",
        "css": "mode-classic",
        "desc": "2x das gleiche Bildmotiv",
        "key": "classic",
    },
    "Paare-Memory": {
        "icon": "🧩",
        "css": "mode-paare",
        "desc": "Zusammengehörige Objekte (TV & Fernbedienung)",
        "key": "paare",
    },
    "Teekesselchen-Memory": {
        "icon": "🫖",
        "css": "mode-teekessel",
        "desc": "Gleiches Wort, anderes Bild (Eis & Eis)",
        "key": "teekesselchen",
    },
    "Mathe Memory I": {
        "icon": "🔢",
        "css": "mode-mathe1",
        "desc": "Zahl ↔ abstrakte Symbole (5 ↔ Quadrate)",
        "key": "mathe_abstrakt",
    },
    "Mathe Memory II": {
        "icon": "🎯",
        "css": "mode-mathe2",
        "desc": "Zahl ↔ reale Objekte (5 ↔ Schuhe)",
        "key": "mathe_konkret",
    },
}


# ============================
# HEADER-BANNER
# ============================
st.markdown("""
<div class="memoki-banner">
    <div class="memoki-brand">
        <div>
            <div class="memoki-title">🎴 MEMOKI</div>
            <div class="memoki-subtitle">Dein KI-Memory-Spiele-Macher</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================
# 2-SPALTEN-LAYOUT
# ============================
left_col, right_col = st.columns([1, 2], gap="large")


# --- LINKE SPALTE ---
with left_col:
    st.markdown('<div class="section-title">🎯 Spielmodus</div>', unsafe_allow_html=True)

    # Mode-Auswahl: bunte Karte + transparenter Button als Overlay
    mode_names = list(GAME_MODES.keys())
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = mode_names[0]

    def _select_mode(mode):
        st.session_state.selected_mode = mode

    for mode_name, mode_info in GAME_MODES.items():
        is_selected = mode_name == st.session_state.selected_mode
        style_attr = "border-width: 3px; box-shadow: 0 4px 14px rgba(0,0,0,0.12);" if is_selected else "opacity: 0.6;"
        check = " ✓" if is_selected else ""
        st.markdown(f"""
        <div class="mode-card {mode_info['css']}" style="{style_attr}">
            <div class="mode-name">{mode_info['icon']} {mode_name}{check}</div>
            <div class="mode-desc">{mode_info['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button(
            mode_name,
            key=f"mode_{mode_name}",
            use_container_width=True,
            on_click=_select_mode,
            args=(mode_name,),
        )

    selected_mode = st.session_state.selected_mode

    st.markdown('<div class="mini-divider">🟡 🔵 🟢 🟣 🔴</div>', unsafe_allow_html=True)

    num_pairs = 10

    st.markdown('<div class="footer">MEMOKI – LLM-Tuning & Prompt Engineering 🧠</div>', unsafe_allow_html=True)


# ============================
# SESSION STATE INIT
# ============================
mode_key = GAME_MODES[selected_mode]["key"]

# Agent neu erstellen bei Modus/Paarzahl-Wechsel
if (
    "agent" not in st.session_state
    or st.session_state.get("current_mode") != mode_key
    or st.session_state.get("current_pairs") != num_pairs
):
    st.session_state.agent = MemokiAgent(mode=mode_key, pair_count=num_pairs)
    st.session_state.current_mode = mode_key
    st.session_state.current_pairs = num_pairs
    st.session_state.messages = []
    st.session_state.deck = None
    st.session_state.generating = False
    st.session_state.flipped = set()
    st.session_state.matched = set()
    st.session_state.first_pick = None
    st.session_state.pending_flip_back = None
    st.session_state.moves = 0
    st.session_state.view_mode = "preview"

# Erste Begrüßung (hübsch formatiert, nicht vom Agent)
if not st.session_state.messages:
    if mode_key == "teekesselchen":
        greeting = (
            f"Hallo! Ich bin **MEMOKI** 🎴\n\n"
            f"Du hast **{selected_mode}** gewählt – super Wahl!\n\n"
            "Die Wörter wähle ich aus meiner Sammlung von 130 Teekesselchen.\n"
            "Sag mir noch:\n"
            "- Welcher **Stil**? (Cartoon, Foto, Aquarell …)\n"
            "- Für **wen**? (Kinder, Teenager, Erwachsene?)"
        )
    elif mode_key == "mathe_abstrakt":
        greeting = (
            f"Hallo! Ich bin **MEMOKI** 🎴\n\n"
            f"Du hast **{selected_mode}** gewählt – super Wahl!\n\n"
            f"Die Zahlen 1–{num_pairs} werden automatisch generiert.\n"
            "Sag mir noch:\n"
            "- Welche **Symbole**? (Kreise ●, Sterne ★, Herzen ♥, Würfel ⚅, Finger ✋, Überraschung 🎲)\n"
            "- Welcher **Stil**? (Cartoon, Foto, Aquarell …)\n"
            "- Für **wen**? (Kinder, Teenager, Erwachsene?)"
        )
    elif mode_key == "mathe_konkret":
        greeting = (
            f"Hallo! Ich bin **MEMOKI** 🎴\n\n"
            f"Du hast **{selected_mode}** gewählt – super Wahl!\n\n"
            f"Die Zahlen 1–{num_pairs} werden mit realen Objekten gepaart.\n"
            "Sag mir:\n"
            "- Welches **Thema**? (Sport, Essen, Spielzeug …)\n"
            "  Tipp: Am besten ein Thema mit kleinen, zählbaren Dingen!\n"
            "- Welcher **Stil**? (Cartoon, Foto, Aquarell …)\n"
            "- Für **wen**? (Kinder, Teenager, Erwachsene?)"
        )
    elif mode_key == "paare":
        available_themes = load_pairs_themes()
        themes_str = ", ".join(available_themes)
        greeting = (
            f"Hallo! Ich bin **MEMOKI** 🎴\n\n"
            f"Du hast **{selected_mode}** gewählt – super Wahl!\n\n"
            "Hier findest du zusammengehörige Paare wie Topf & Deckel.\n"
            "Sag mir:\n"
            f"- Welches **Thema**? ({themes_str})\n"
            "- Welcher **Stil**? (Cartoon, Foto, Aquarell …)\n"
            "- Für **wen**? (Kinder, Teenager, Erwachsene?)"
        )
    else:
        greeting = (
            f"Hallo! Ich bin **MEMOKI** 🎴\n\n"
            f"Du hast **{selected_mode}** gewählt – super Wahl!\n\n"
            "Erzähl mir, was für Karten Du Dir wünschst:\n"
            "- Welches **Thema**? (Tiere, Essen, Technik …)\n"
            "- Welcher **Stil**? (Cartoon, Foto, Aquarell …)\n"
            "- Für **wen**? (Kinder, Teenager, Erwachsene?)"
        )
    st.session_state.messages.append({
        "role": "assistant",
        "content": greeting,
    })


# ============================
# RECHTE SPALTE: Chat + Spiel
# ============================
with right_col:
    # Wenn Deck vorhanden → Spielfeld anzeigen
    if st.session_state.deck is not None:
        deck = st.session_state.deck
        total_pairs = len(deck.cards) // 2

        # --- Modus-Buttons ---
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("👁️ Karten zeigen", use_container_width=True):
                st.session_state.view_mode = "preview"
                st.rerun()
        with btn_col2:
            if st.button("🎮 Mischen & Spielen", use_container_width=True):
                random.shuffle(deck.cards)
                st.session_state.flipped = set()
                st.session_state.matched = set()
                st.session_state.first_pick = None
                st.session_state.pending_flip_back = None
                st.session_state.moves = 0
                st.session_state.view_mode = "play"
                st.rerun()

        # === PREVIEW-MODUS ===
        if st.session_state.view_mode == "preview":
            st.markdown(f"""
            <div class="progress-box">
                <strong>👁️ Kartenvorschau</strong> &nbsp;|&nbsp;
                {total_pairs} Paare sortiert nach Zugehörigkeit
            </div>
            """, unsafe_allow_html=True)

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
                        st.markdown("*(kein Bild)*")
                    st.caption(f"#{card.pair_id} – {card.label}")

            # --- ZIP-Download ---
            zip_buf = io.BytesIO()
            with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_DEFLATED) as zf:
                for card in sorted_cards:
                    if card.image is not None:
                        img_buf = io.BytesIO()
                        card.image.save(img_buf, format="PNG")
                        safe_label = card.label.replace(" ", "_").replace("/", "-")
                        zf.writestr(f"Paar{card.pair_id:02d}_{safe_label}.png", img_buf.getvalue())
            st.download_button(
                "📥 Alle Karten herunterladen (ZIP)",
                data=zip_buf.getvalue(),
                file_name="memoki-karten.zip",
                mime="application/zip",
                use_container_width=True,
            )

        # === SPIEL-MODUS ===
        else:
            found = len(st.session_state.matched)
            st.markdown(f"""
            <div class="progress-box">
                <strong>🎮 Spielfeld</strong> &nbsp;|&nbsp;
                Paare gefunden: <strong>{found}/{total_pairs}</strong> &nbsp;|&nbsp;
                Züge: <strong>{st.session_state.moves}</strong>
            </div>
            """, unsafe_allow_html=True)

            # Callback: Karte anklicken (läuft VOR dem Rendering)
            def _on_card_click(idx):
                # Vorheriges Nicht-Paar zurückdrehen
                if st.session_state.pending_flip_back:
                    a, b = st.session_state.pending_flip_back
                    st.session_state.flipped.discard(a)
                    st.session_state.flipped.discard(b)
                    st.session_state.pending_flip_back = None

                if st.session_state.first_pick is None:
                    # Erste Karte aufdecken
                    st.session_state.first_pick = idx
                    st.session_state.flipped.add(idx)
                else:
                    # Zweite Karte aufdecken + prüfen
                    first = st.session_state.first_pick
                    st.session_state.flipped.add(idx)
                    st.session_state.moves += 1

                    deck = st.session_state.deck
                    if deck.cards[first].pair_id == deck.cards[idx].pair_id:
                        st.session_state.matched.add(deck.cards[idx].pair_id)
                    else:
                        st.session_state.pending_flip_back = (first, idx)

                    st.session_state.first_pick = None

            # Karten als Grid
            cols_per_row = 5 if total_pairs <= 10 else 8
            cols = st.columns(cols_per_row)

            for idx, card in enumerate(deck.cards):
                col = cols[idx % cols_per_row]
                with col:
                    is_matched = card.pair_id in st.session_state.matched
                    is_flipped = idx in st.session_state.flipped or is_matched

                    if is_flipped and card.image is not None:
                        b64 = img_to_base64(card.image)
                        border = "3px solid #2ed573" if is_matched else "2px solid #ddd"
                        st.markdown(
                            f'<div class="memory-card" style="border: {border};">'
                            f'<img src="data:image/png;base64,{b64}" />'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.button(
                            "🎴", key=f"card_{idx}",
                            use_container_width=True,
                            on_click=_on_card_click, args=(idx,),
                        )

            # Spiel gewonnen?
            if found == total_pairs:
                st.success(f"🎉 Gewonnen! Du hast alle {total_pairs} Paare in {st.session_state.moves} Zügen gefunden!")
                if st.button("🔄 Neues Spiel"):
                    st.session_state.deck = None
                    st.session_state.messages = []
                    st.session_state.flipped = set()
                    st.session_state.matched = set()
                    st.session_state.first_pick = None
                    st.session_state.pending_flip_back = None
                    st.session_state.moves = 0
                    st.session_state.view_mode = "preview"
                    st.session_state.agent = MemokiAgent(mode=mode_key, pair_count=num_pairs)
                    st.rerun()

        st.markdown("---")

    # Chat-Interface
    st.markdown('<div class="section-title">💬 Sprich mit MEMOKI</div>', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        avatar = "🎴" if msg["role"] == "assistant" else "🙋"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Auto-Scroll: nach dem Rendern der Nachrichten ans Ende scrollen
    components.html("""
    <script>
        setTimeout(function() {
            const doc = window.parent.document;
            // Versuche verschiedene Streamlit-Container
            const targets = [
                doc.querySelector('[data-testid="stAppViewContainer"]'),
                doc.querySelector('section.main'),
                doc.querySelector('.main'),
            ];
            for (const el of targets) {
                if (el) {
                    el.scrollTo({top: el.scrollHeight, behavior: 'smooth'});
                }
            }
            // Fallback: ganzes Fenster scrollen
            window.parent.scrollTo({top: doc.body.scrollHeight, behavior: 'smooth'});
        }, 200);
    </script>
    """, height=1)

    if prompt := st.chat_input("Sag MEMOKI, was Du Dir wünschst …"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🙋"):
            st.markdown(prompt)

        # Agent-Antwort
        with st.chat_message("assistant", avatar="🎴"):
            with st.spinner("MEMOKI denkt nach..."):
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
                    return idx, label, generate_card_image(prompt, use_fast=True), f"Fallback: {e}"
                except Exception as e2:
                    return idx, label, None, f"Fehlgeschlagen: {e2}"

        def _parallel_images(jobs, total_label="Bilder"):
            """Generiert Bilder parallel und zeigt Fortschritt."""
            results = [None] * len(jobs)
            done = 0
            total = len(jobs)
            progress = st.progress(0, text=f"Generiere {total_label}...")
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
                    progress.progress(done / total, text=f"Bild {done}/{total}")
            return results

        # === TEEKESSELCHEN ===
        if mode_key == "teekesselchen":
            with st.status(f"🫖 Generiere {num_pairs} Teekesselchen-Paare...", expanded=True) as status:
                # Schritt 1: Teekesselchen aus JSON laden
                st.write(f"📝 Wähle {num_pairs} Teekesselchen aus 130 Wörtern...")
                try:
                    tk_list = load_teekesselchen(num_pairs)
                    words = [tk["word"] for tk in tk_list]
                    st.write(f"✅ Wörter: {', '.join(words)}")
                except Exception as e:
                    st.error(f"Fehler beim Laden: {e}")
                    st.session_state.generating = False
                    st.stop()

                # Schritt 2: Bild-Prompts bauen (2 pro Wort)
                jobs = []
                for i, tk in enumerate(tk_list):
                    prompt_a = build_image_prompt(tk["meaning_a"], style, audience)
                    prompt_b = build_image_prompt(tk["meaning_b"], style, audience)
                    jobs.append((i * 2, f"{tk['word']} ({tk['label_a']})", prompt_a))
                    jobs.append((i * 2 + 1, f"{tk['word']} ({tk['label_b']})", prompt_b))

                st.write(f"🖼️ Generiere {len(jobs)} Bilder parallel (2 pro Wort)...")
                all_images = _parallel_images(jobs, f"{len(jobs)} Bilder")

                # Bilder aufteilen: gerade=A, ungerade=B
                images_a = [all_images[i * 2] for i in range(num_pairs)]
                images_b = [all_images[i * 2 + 1] for i in range(num_pairs)]

                # Schritt 3: Deck bauen
                st.write("🃏 Baue Spielfeld...")
                deck = Deck.build_teekesselchen(tk_list, images_a, images_b)

                st.session_state.deck = deck
                st.session_state.generating = False
                st.session_state.view_mode = "preview"
                status.update(label="✅ Fertig! Dein Teekesselchen-Memory ist bereit!", state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"🎉 Dein **Teekesselchen**-Memory mit {num_pairs} Wortpaaren ist fertig! Finde die zwei Bedeutungen!"
            })
            st.rerun()

        # === MATHE ABSTRAKT ===
        elif mode_key == "mathe_abstrakt":
            shape_id = action.get("shape", "surprise")
            with st.status(f"🔢 Generiere Mathe-Memory mit {num_pairs} Zahlen...", expanded=True) as status:
                # Schritt 1: Shape laden
                st.write(f"🔷 Lade Shape-Stil '{shape_id}'...")
                try:
                    shape = load_math_shape(shape_id)
                    st.write(f"✅ Shape: {shape['name_de']} {shape.get('symbol', '')}")
                except Exception as e:
                    st.error(f"Fehler beim Shape-Laden: {e}")
                    st.session_state.generating = False
                    st.stop()

                # Schritt 2: Zahlen + Prompts vorbereiten
                numbers = list(range(1, num_pairs + 1))
                jobs = []
                for i, num in enumerate(numbers):
                    num_prompt = build_number_prompt(num, style, audience, theme=shape["name_en"])
                    shape_prompt = build_shapes_prompt(num, shape, style, audience)
                    jobs.append((i * 2, f"Zahl {num}", num_prompt))
                    jobs.append((i * 2 + 1, f"{num}x {shape['name_de']}", shape_prompt))

                # Schritt 3: Bilder parallel generieren (2 pro Zahl)
                st.write(f"🖼️ Generiere {len(jobs)} Bilder parallel (Zahl + Shape)...")
                all_images = _parallel_images(jobs, f"{len(jobs)} Bilder")

                # Bilder aufteilen: gerade=Zahlen, ungerade=Shapes
                number_images = [all_images[i * 2] for i in range(num_pairs)]
                shape_images = [all_images[i * 2 + 1] for i in range(num_pairs)]

                # Schritt 4: Deck bauen
                st.write("🃏 Baue Spielfeld...")
                deck = Deck.build_mathe_abstrakt(numbers, shape["name_de"], number_images, shape_images)

                st.session_state.deck = deck
                st.session_state.generating = False
                st.session_state.view_mode = "preview"
                status.update(label="✅ Fertig! Dein Mathe-Memory ist bereit!", state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"🎉 Dein **Mathe-Memory** mit Zahlen 1–{num_pairs} und **{shape['name_de']}** ist fertig! Finde die passenden Paare!"
            })
            st.rerun()

        # === MATHE KONKRET ===
        elif mode_key == "mathe_konkret":
            theme = action.get("theme", "toys")
            with st.status(f"🎯 Generiere Mathe-Memory II mit {num_pairs} Zahlen...", expanded=True) as status:
                # Schritt 1: Zählbare Objekte generieren
                st.write(f"📝 Generiere {num_pairs} zählbare Objekte zum Thema '{theme}'...")
                try:
                    objects = generate_countable_objects(
                        theme=theme,
                        count=num_pairs,
                        audience=audience,
                    )
                    st.write(f"✅ Objekte: {', '.join(objects)}")
                except Exception as e:
                    st.error(f"Fehler bei Objekt-Generierung: {e}")
                    st.session_state.generating = False
                    st.stop()

                # Schritt 2: Zahlen + Prompts vorbereiten
                numbers = list(range(1, num_pairs + 1))
                jobs = []
                for i, (num, obj) in enumerate(zip(numbers, objects)):
                    num_prompt = build_number_prompt(num, style, audience, theme=theme)
                    obj_prompt = build_real_objects_prompt(num, obj, style, audience, theme=theme)
                    jobs.append((i * 2, f"Zahl {num}", num_prompt))
                    jobs.append((i * 2 + 1, f"{num}x {obj}", obj_prompt))

                # Schritt 3: Bilder parallel generieren (2 pro Zahl)
                st.write(f"🖼️ Generiere {len(jobs)} Bilder parallel (Zahl + Objekt)...")
                all_images = _parallel_images(jobs, f"{len(jobs)} Bilder")

                # Bilder aufteilen: gerade=Zahlen, ungerade=Objekte
                number_images = [all_images[i * 2] for i in range(num_pairs)]
                object_images = [all_images[i * 2 + 1] for i in range(num_pairs)]

                # Schritt 4: Deck bauen
                st.write("🃏 Baue Spielfeld...")
                deck = Deck.build_mathe_konkret(numbers, objects, number_images, object_images)

                st.session_state.deck = deck
                st.session_state.generating = False
                st.session_state.view_mode = "preview"
                status.update(label="✅ Fertig! Dein Mathe-Memory II ist bereit!", state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"🎉 Dein **Mathe-Memory II** zum Thema **{theme}** mit Zahlen 1–{num_pairs} ist fertig! Finde Zahl und passende Objekte!"
            })
            st.rerun()

        # === PAARE-MEMORY ===
        elif mode_key == "paare":
            theme = action.get("theme", "Küche")
            with st.status(f"🧩 Generiere {num_pairs} Wortpaare zum Thema '{theme}'...", expanded=True) as status:
                # Schritt 1: Paare aus JSON laden
                st.write(f"📝 Wähle {num_pairs} Paare zum Thema '{theme}'...")
                try:
                    pairs = load_pairs(theme, num_pairs)
                    pair_labels = [f"{p['a_de']} & {p['b_de']}" for p in pairs]
                    st.write(f"✅ Paare: {', '.join(pair_labels)}")
                except Exception as e:
                    st.error(f"Fehler beim Laden: {e}")
                    st.session_state.generating = False
                    st.stop()

                # Schritt 2: Bild-Prompts bauen (2 pro Paar: Objekt A + Objekt B)
                jobs = []
                for i, pair in enumerate(pairs):
                    prompt_a = build_pair_object_prompt(pair["a_en"], style, audience)
                    prompt_b = build_pair_object_prompt(pair["b_en"], style, audience)
                    jobs.append((i * 2, pair["a_de"], prompt_a))
                    jobs.append((i * 2 + 1, pair["b_de"], prompt_b))

                st.write(f"🖼️ Generiere {len(jobs)} Bilder parallel (2 pro Paar)...")
                all_images = _parallel_images(jobs, f"{len(jobs)} Bilder")

                # Bilder aufteilen: gerade=A, ungerade=B
                images_a = [all_images[i * 2] for i in range(len(pairs))]
                images_b = [all_images[i * 2 + 1] for i in range(len(pairs))]

                # Schritt 3: Deck bauen
                st.write("🃏 Baue Spielfeld...")
                deck = Deck.build_paare(pairs, images_a, images_b)

                st.session_state.deck = deck
                st.session_state.generating = False
                st.session_state.view_mode = "preview"
                status.update(label="✅ Fertig! Dein Paare-Memory ist bereit!", state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"🎉 Dein **Paare-Memory** zum Thema **{theme}** mit {len(pairs)} Paaren ist fertig! Finde die zusammengehörigen Objekte!"
            })
            st.rerun()

        # === CLASSIC (und vorerst alle anderen Modi) ===
        else:
            theme = action.get("theme", "animals")
            with st.status(f"🎨 Generiere {num_pairs} Kartenbilder...", expanded=True) as status:
                # Schritt 1: Objekte generieren
                st.write(f"📝 Generiere {num_pairs} Objekte zum Thema '{theme}'...")
                try:
                    objects = generate_objects(
                        theme=theme,
                        count=num_pairs,
                        audience=audience,
                        style=style,
                    )
                    st.write(f"✅ Objekte: {', '.join(objects)}")
                except Exception as e:
                    st.error(f"Fehler bei Objekt-Generierung: {e}")
                    st.session_state.generating = False
                    st.stop()

                # Schritt 2: Bilder parallel generieren
                st.write(f"🖼️ Generiere {num_pairs} Bilder parallel...")
                jobs = [
                    (i, obj, build_image_prompt(obj, style, audience))
                    for i, obj in enumerate(objects)
                ]
                images = _parallel_images(jobs)

                # Schritt 3: Deck bauen
                st.write("🃏 Baue Spielfeld...")
                deck = Deck.build_classic(objects, images)

                st.session_state.deck = deck
                st.session_state.generating = False
                st.session_state.view_mode = "preview"
                status.update(label="✅ Fertig! Dein Memory ist bereit!", state="complete")

            st.session_state.messages.append({
                "role": "assistant",
                "content": f"🎉 Dein **{theme}**-Memory mit {num_pairs} Paaren ist fertig! Viel Spaß beim Spielen!"
            })
            st.rerun()
