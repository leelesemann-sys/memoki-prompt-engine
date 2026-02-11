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
    ("de", "Deutsch"),
    ("en", "English"),
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


def _on_lang_change():
    """Callback fuer Sprachwechsel via pills."""
    _code_map = {label: code for code, label in LANG_OPTIONS}
    selected_label = st.session_state.get("lang_pills")
    if selected_label and selected_label in _code_map:
        new_code = _code_map[selected_label]
        if new_code != get_lang():
            set_lang(new_code)


def render_lang_selector():
    """Rendert einen kompakten Sprachumschalter (DE | EN) als Pills."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG

    labels = [label for _, label in LANG_OPTIONS]
    current = get_lang()
    default_label = dict(LANG_OPTIONS).get(current, labels[0])

    st.pills(
        label="🌐",
        options=labels,
        default=default_label,
        key="lang_pills",
        on_change=_on_lang_change,
    )
