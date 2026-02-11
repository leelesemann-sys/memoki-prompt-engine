"""MEMOKI i18n -- Internationalisierung.

Stellt eine t(key, **kwargs)-Funktion bereit, die Strings
in der aktuellen Sprache liefert. Sprache wird in
st.session_state.lang gespeichert (Default: "de").

Neue Sprache hinzufuegen:
1. i18n/fr.py anlegen (Kopie von en.py, uebersetzen)
2. Hier registrieren: from i18n import fr  +  LANGUAGES["fr"] = fr.STRINGS
3. LANG_OPTIONS um Flagge ergaenzen
"""

import streamlit as st

from i18n import de, en

# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
LANGUAGES: dict[str, dict] = {
    "de": de.STRINGS,
    "en": en.STRINGS,
}

LANG_OPTIONS = [
    ("de", "DE"),
    ("en", "EN"),
]

DEFAULT_LANG = "de"


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def get_lang() -> str:
    """Gibt die aktuelle Sprache zurueck (Default: 'de')."""
    return st.session_state.get("lang", DEFAULT_LANG)


def set_lang(lang: str) -> None:
    """Setzt die aktuelle Sprache."""
    st.session_state.lang = lang


def t(key: str, **kwargs) -> str:
    """Uebersetzt einen Key in die aktuelle Sprache.

    Falls kwargs uebergeben werden, werden sie via .format()
    in den String eingesetzt.

    Gibt bei fehlendem Key den Key selbst zurueck (fuer Debugging).
    """
    lang = get_lang()
    strings = LANGUAGES.get(lang, LANGUAGES[DEFAULT_LANG])
    text = strings.get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass  # Fehlende Platzhalter still ignorieren
    return text


def get_mode_data() -> dict:
    """Gibt die MODE_DATA-Struktur in der aktuellen Sprache zurueck."""
    lang = get_lang()
    if lang == "en":
        return en.MODE_DATA
    return de.MODE_DATA


def render_lang_selector():
    """Rendert einen Sprachumschalter in der Sidebar."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG

    cols = st.columns(len(LANG_OPTIONS))
    for i, (code, label) in enumerate(LANG_OPTIONS):
        with cols[i]:
            is_active = get_lang() == code
            btn_type = "primary" if is_active else "secondary"
            if st.button(label, key=f"lang_{code}", type=btn_type, use_container_width=True):
                set_lang(code)
                st.rerun()
