"""MEMOKI -- Deutsche Strings (Standardsprache)."""

# ============================================================================
# Flache Strings fuer t()-Lookups
# ============================================================================

STRINGS: dict[str, str] = {

    # ── Seitentitel / Banner ──────────────────────────────────────────────
    "page.title": "MEMOKI \u2013 KI-Memory-Spiele-Macher",
    "page.title_test": "MEMOKI \u2013 TEST-MODUS",
    "banner.subtitle": "Dein KI-Memory-Spiele-Macher",
    "banner.feat_generate": "\U0001f0cf Karten generieren",
    "banner.feat_play": "\U0001f3ae Direkt spielen",
    "banner.feat_print": "\U0001f5a8\ufe0f Druckvorlage",

    # ── Spielmodi ─────────────────────────────────────────────────────────
    "mode.classic.name": "Klassisches Memory",
    "mode.classic.desc": "2x das gleiche Bildmotiv",
    "mode.paare.name": "Paare-Memory",
    "mode.paare.desc": "Zusammengeh\u00f6rige Objekte (TV & Fernbedienung)",
    "mode.teekesselchen.name": "Teekesselchen-Memory",
    "mode.teekesselchen.desc": "Gleiches Wort, anderes Bild (Eis & Eis)",
    "mode.mathe_abstrakt.name": "Mathe Memory I",
    "mode.mathe_abstrakt.desc": "Zahl \u2194 abstrakte Symbole (5 \u2194 Quadrate)",
    "mode.mathe_konkret.name": "Mathe Memory II",
    "mode.mathe_konkret.desc": "Zahl \u2194 reale Objekte (5 \u2194 Schuhe)",

    # ── Sidebar / Layout ──────────────────────────────────────────────────
    "section.game_mode": "\U0001f3af Spielmodus",
    "section.chat": "\U0001f4ac Sprich mit MEMOKI",
    "footer.text": "MEMOKI \u2013 LLM-Tuning & Prompt Engineering \U0001f9e0",

    # ── Buttons ───────────────────────────────────────────────────────────
    "btn.shuffle_play": "\U0001f3ae Mischen & Spielen",
    "btn.show_cards": "\U0001f441\ufe0f Karten zeigen",
    "btn.download_zip": "\U0001f4e5 Alle Karten herunterladen (ZIP)",
    "btn.new_game": "\U0001f504 Neues Spiel",
    "btn.download_filename": "memoki-karten.zip",

    # ── Vorschau / Spielfeld ──────────────────────────────────────────────
    "preview.title": "\U0001f441\ufe0f Kartenvorschau",
    "preview.pairs_sorted": "{total_pairs} Paare sortiert nach Zugeh\u00f6rigkeit",
    "preview.no_image": "*(kein Bild)*",
    "play.title": "\U0001f3ae Spielfeld",
    "play.pairs_found": "Paare gefunden: <strong>{found}/{total_pairs}</strong>",
    "play.moves": "Z\u00fcge: <strong>{moves}</strong>",
    "play.won": "\U0001f389 Gewonnen! Du hast alle {total_pairs} Paare in {moves} Z\u00fcgen gefunden!",

    # ── Test-Modus ────────────────────────────────────────────────────────
    "test.title": "\U0001f50d TEST-MODUS",
    "test.all_revealed": "Alle {total_pairs} Paare aufgedeckt",
    "test.grouped": "Karten werden nach pair_id gruppiert",

    # ── Chat ──────────────────────────────────────────────────────────────
    "chat.placeholder": "Sag MEMOKI, was Du Dir w\u00fcnschst \u2026",
    "chat.thinking": "MEMOKI denkt nach...",

    # ── Begr\u00fc\u00dfungen ──────────────────────────────────────────────
    "greeting.hello": "Hallo! Ich bin **MEMOKI** \U0001f0cf\n\n",
    "greeting.mode_chosen": "Du hast **{mode_name}** gew\u00e4hlt \u2013 super Wahl!\n\n",
    "greeting.teekesselchen": (
        "Die W\u00f6rter w\u00e4hle ich aus meiner Sammlung von 130 Teekesselchen.\n"
        "Sag mir noch:\n"
        "- Welcher **Stil**? (Cartoon, Foto, Aquarell \u2026)\n"
        "- F\u00fcr **wen**? (Kinder, Teenager, Erwachsene?)"
    ),
    "greeting.mathe_abstrakt": (
        "Die Zahlen 1\u2013{num_pairs} werden automatisch generiert.\n"
        "Sag mir noch:\n"
        "- Welche **Symbole**? (Kreise \u25cf, Sterne \u2605, Herzen \u2665, W\u00fcrfel \u2685, Finger \u270b, \u00dcberraschung \U0001f3b2)\n"
        "- Welcher **Stil**? (Cartoon, Foto, Aquarell \u2026)\n"
        "- F\u00fcr **wen**? (Kinder, Teenager, Erwachsene?)"
    ),
    "greeting.mathe_konkret": (
        "Die Zahlen 1\u2013{num_pairs} werden mit realen Objekten gepaart.\n"
        "Sag mir:\n"
        "- Welches **Thema**? (Sport, Essen, Spielzeug \u2026)\n"
        "  Tipp: Am besten ein Thema mit kleinen, z\u00e4hlbaren Dingen!\n"
        "- Welcher **Stil**? (Cartoon, Foto, Aquarell \u2026)\n"
        "- F\u00fcr **wen**? (Kinder, Teenager, Erwachsene?)"
    ),
    "greeting.paare": (
        "Hier findest du zusammengeh\u00f6rige Paare wie Topf & Deckel.\n"
        "Sag mir:\n"
        "- Welches **Thema**? ({themes_str})\n"
        "- Welcher **Stil**? (Cartoon, Foto, Aquarell \u2026)\n"
        "- F\u00fcr **wen**? (Kinder, Teenager, Erwachsene?)"
    ),
    "greeting.classic": (
        "Erz\u00e4hl mir, was f\u00fcr Karten Du Dir w\u00fcnschst:\n"
        "- Welches **Thema**? (Tiere, Essen, Technik \u2026)\n"
        "- Welcher **Stil**? (Cartoon, Foto, Aquarell \u2026)\n"
        "- F\u00fcr **wen**? (Kinder, Teenager, Erwachsene?)"
    ),

    # ── Generierungs-Pipeline ─────────────────────────────────────────────
    "gen.progress": "Generiere {label}...",
    "gen.image_progress": "Bild {done}/{total}",
    "gen.fallback": "Fallback: {error}",
    "gen.failed": "Fehlgeschlagen: {error}",
    "gen.building_deck": "\U0001f0cf Baue Spielfeld...",
    "gen.error_loading": "Fehler beim Laden: {error}",
    "gen.error_shape": "Fehler beim Shape-Laden: {error}",
    "gen.error_objects": "Fehler bei Objekt-Generierung: {error}",

    # Teekesselchen
    "gen.tk.status": "\U0001f9c6 Generiere {num_pairs} Teekesselchen-Paare...",
    "gen.tk.selecting": "\U0001f4dd W\u00e4hle {num_pairs} Teekesselchen aus 130 W\u00f6rtern...",
    "gen.tk.words_ok": "\u2705 W\u00f6rter: {words}",
    "gen.tk.images": "\U0001f5bc\ufe0f Generiere {count} Bilder parallel (2 pro Wort)...",
    "gen.tk.done": "\u2705 Fertig! Dein Teekesselchen-Memory ist bereit!",
    "gen.tk.complete_msg": "\U0001f389 Dein **Teekesselchen**-Memory mit {num_pairs} Wortpaaren ist fertig! Finde die zwei Bedeutungen!",

    # Mathe Abstrakt
    "gen.ma.status": "\U0001f522 Generiere Mathe-Memory mit {num_pairs} Zahlen...",
    "gen.ma.loading_shape": "\U0001f537 Lade Shape-Stil '{shape_id}'...",
    "gen.ma.shape_ok": "\u2705 Shape: {name} {symbol}",
    "gen.ma.images": "\U0001f5bc\ufe0f Generiere {count} Bilder parallel (Zahl + Shape)...",
    "gen.ma.done": "\u2705 Fertig! Dein Mathe-Memory ist bereit!",
    "gen.ma.complete_msg": "\U0001f389 Dein **Mathe-Memory** mit Zahlen 1\u2013{num_pairs} und **{shape_name}** ist fertig! Finde die passenden Paare!",

    # Mathe Konkret
    "gen.mk.status": "\U0001f3af Generiere Mathe-Memory II mit {num_pairs} Zahlen...",
    "gen.mk.generating_objects": "\U0001f4dd Generiere {num_pairs} z\u00e4hlbare Objekte zum Thema '{theme}'...",
    "gen.mk.objects_ok": "\u2705 Objekte: {objects}",
    "gen.mk.images": "\U0001f5bc\ufe0f Generiere {count} Bilder parallel (Zahl + Objekt)...",
    "gen.mk.done": "\u2705 Fertig! Dein Mathe-Memory II ist bereit!",
    "gen.mk.complete_msg": "\U0001f389 Dein **Mathe-Memory II** zum Thema **{theme}** mit Zahlen 1\u2013{num_pairs} ist fertig! Finde Zahl und passende Objekte!",

    # Paare
    "gen.pa.status": "\U0001f9e9 Generiere {num_pairs} Wortpaare zum Thema '{theme}'...",
    "gen.pa.selecting": "\U0001f4dd W\u00e4hle {num_pairs} Paare zum Thema '{theme}'...",
    "gen.pa.pairs_ok": "\u2705 Paare: {pairs}",
    "gen.pa.images": "\U0001f5bc\ufe0f Generiere {count} Bilder parallel (2 pro Paar)...",
    "gen.pa.done": "\u2705 Fertig! Dein Paare-Memory ist bereit!",
    "gen.pa.complete_msg": "\U0001f389 Dein **Paare-Memory** zum Thema **{theme}** mit {count} Paaren ist fertig! Finde die zusammengeh\u00f6rigen Objekte!",

    # Classic
    "gen.cl.status": "\U0001f3a8 Generiere {num_pairs} Kartenbilder...",
    "gen.cl.generating_objects": "\U0001f4dd Generiere {num_pairs} Objekte zum Thema '{theme}'...",
    "gen.cl.objects_ok": "\u2705 Objekte: {objects}",
    "gen.cl.images": "\U0001f5bc\ufe0f Generiere {num_pairs} Bilder parallel...",
    "gen.cl.done": "\u2705 Fertig! Dein Memory ist bereit!",
    "gen.cl.complete_msg": "\U0001f389 Dein **{theme}**-Memory mit {num_pairs} Paaren ist fertig! Viel Spa\u00df beim Spielen!",

    # ── Card-Labels ───────────────────────────────────────────────────────
    "card.number": "Zahl {num}",
    "card.number_x": "{num}x {name}",

    # ── Agent System Prompt ───────────────────────────────────────────────
    "agent.system_prompt": """\
Du bist MEMOKI, ein freundlicher und kreativer Memory-Spiel-Generator.
Du sprichst Deutsch mit dem User.

## DEINE AUFGABE

Du sammelst die n\u00f6tigen Infos, um ein Memory-Spiel zu erstellen:
- **Variante**: Wird vom Frontend \u00fcbergeben (classic, paare, teekesselchen, mathe_abstrakt, mathe_konkret)
- **Paarzahl**: Wird vom Frontend \u00fcbergeben (10 oder 20)
- **Thema**: Frage den User (z.B. Tiere, Sport, Essen) \u2013 NICHT bei Teekesselchen!
- **Stil**: Frage den User (z.B. Cartoon, foto-realistisch, Aquarell)
- **Zielgruppe**: Frage den User (z.B. Kinder, Teenager, Erwachsene)

## SONDERFALL TEEKESSELCHEN

Bei der Variante "teekesselchen" gibt es KEIN Thema \u2013 die W\u00f6rter kommen aus einer fertigen Wissensbasis.
Frage nur nach **Stil** und **Zielgruppe**. Setze im JSON "theme": "teekesselchen".

## SONDERFALL PAARE

Bei der Variante "paare" w\u00e4hlt der User ein **Thema** aus einer festen Liste.
Die Paare (z.B. Topf & Deckel, Schl\u00fcssel & Schloss) kommen aus einer kuratierten Wissensbasis.

Verf\u00fcgbare Themen: K\u00fcche, B\u00fcro, Sport, Haushalt, Musik, Garten, Bad, Schule, Verkehr, Tiere.

Frage nach **Thema** (aus obiger Liste), **Stil** und **Zielgruppe**.
Im JSON: Setze "theme" auf den deutschen Thema-Namen (z.B. "K\u00fcche", "Sport").

## SONDERFALL MATHE ABSTRAKT

Bei der Variante "mathe_abstrakt" gibt es KEIN Thema. Stattdessen w\u00e4hlt der User einen **Shape-Stil**.
Die Zahlen (1-10 oder 1-20) werden automatisch generiert.

Frage nach **Shape-Stil**, **Bild-Stil** und **Zielgruppe**. Biete diese Optionen an:
- Kreise \u25cf
- Sterne \u2605
- Herzen \u2665
- W\u00fcrfelaugen \u2685
- Finger \u270b
- \u00dcberrasch mich! \U0001f3b2

Im JSON: Setze "theme": "mathe_abstrakt" und f\u00fcge "shape": "<shape_id>" hinzu.
Shape-IDs: "circles", "stars", "hearts", "dice", "fingers", "surprise"

## SONDERFALL MATHE KONKRET

Bei der Variante "mathe_konkret" w\u00e4hlt der User ein **Thema** (z.B. Sport, Tiere, Essen).
Das System generiert dann z\u00e4hlbare Objekte aus diesem Thema (z.B. Tennisb\u00e4lle, Fu\u00dfb\u00e4lle, Schlittschuhe).
Jede Zahl (1-10 oder 1-20) wird mit einem ANDEREN Objekt gepaart.

Frage nach **Thema**, **Stil** und **Zielgruppe**.

WICHTIG: Erkl\u00e4re dem User, dass das Thema gut z\u00e4hlbare, kleine Objekte hergeben sollte.
Beispiele f\u00fcr gute Themen: Sport, Essen, Spielzeug, Natur, S\u00fc\u00dfigkeiten.
Beispiele f\u00fcr schlechte Themen: Weltraum, Landschaften, Geb\u00e4ude (zu gro\u00df/nicht z\u00e4hlbar).

Im JSON: Setze "theme": "<thema>" (wie bei Classic).

## DEIN GESPR\u00c4CHS-FLOW

1. Begr\u00fc\u00dfe den User kurz, nenne die gew\u00e4hlte Variante
2. Je nach Variante:
   - Teekesselchen: Frage nur nach Stil und Zielgruppe
   - Paare: Frage nach Thema (aus der festen Liste!), Stil und Zielgruppe
   - Mathe Abstrakt: Frage nach Shape-Stil, Bild-Stil und Zielgruppe
   - Mathe Konkret: Frage nach Thema (mit Hinweis auf z\u00e4hlbare Objekte!), Stil und Zielgruppe
   - Classic: Frage nach Thema UND Stil. Mache Vorschl\u00e4ge!
3. Sobald du alle Infos hast, fasse kurz zusammen und gib SOFORT den JSON-Block aus (KEINE R\u00fcckfrage!).
   Schreibe die Zusammenfassung und dann DIREKT den JSON-Block. KEINE Ank\u00fcndigung wie "Hier ist dein JSON-Block:" davor!

```json
{"action": "generate", "theme": "...", "style": "...", "audience": "...", "shape": "..."}
```
Hinweis: "shape" nur bei mathe_abstrakt n\u00f6tig, bei anderen Modi weglassen.

## WICHTIGE REGELN

- Sei kurz und freundlich, nicht zu geschw\u00e4tzig
- Biete immer 3-4 konkrete Vorschl\u00e4ge an
- Sobald alle Infos da sind \u2192 direkt JSON ausgeben, NICHT erst nachfragen
- Der JSON-Block MUSS in ```json ... ``` stehen
- Nutze englische Begriffe im JSON (theme, style, audience)
- Standard-Stile: "cartoon", "photorealistic", "watercolor", "minimalist", "artistic", "black-and-white", "pencil", "retro", "pixel", "comic"
- Der User kann auch EIGENE Stile w\u00fcnschen (z.B. "van Gogh", "Bauhaus", "Jugendstil"). In dem Fall: Schreibe eine kurze englische Stil-Beschreibung als style-Wert ins JSON, z.B. "van Gogh post-impressionist style, thick swirling brushstrokes, bold vivid colors"
- Audience-Werte: "children", "teenagers", "adults"
""",

    "agent.context_header": "## AKTUELLER KONTEXT\n- Gew\u00e4hlte Variante: {mode}\n- Paarzahl: {pair_count}\n",

    # ── How-It-Works Seite ────────────────────────────────────────────────
    "hiw.page_title": "MEMOKI \u2013 How it Works",
    "hiw.sidebar_title": "### \U0001f9e0 MEMOKI Docs",
    "hiw.nav.architecture": "\U0001f3d7\ufe0f Architektur-\u00dcbersicht",
    "hiw.nav.classic": "\U0001f0cf Klassisches Memory",
    "hiw.nav.paare": "\U0001f46b Paare-Memory",
    "hiw.nav.teekesselchen": "\U0001f9c6 Teekesselchen",
    "hiw.nav.mathe_abstrakt": "\U0001f522 Mathe I (Abstrakt)",
    "hiw.nav.mathe_konkret": "\U0001f9ee Mathe II (Konkret)",
    "hiw.nav.style": "\U0001f3a8 Stil & Zielgruppen",

    # Architecture page
    "hiw.arch.header": "\U0001f3d7\ufe0f Architektur-\u00dcbersicht",
    "hiw.arch.subheader": "Wie MEMOKI unter der Haube funktioniert",
    "hiw.arch.kpi_title": "\U0001f4ca Auf einen Blick",
    "hiw.arch.kpi.modes": "Spielmodi",
    "hiw.arch.kpi.styles": "Bildstile",
    "hiw.arch.kpi.models": "Gemini-Modelle",
    "hiw.arch.kpi.knowledge": "Wissensbasen",
    "hiw.arch.pipeline_title": "\U0001f504 Die MEMOKI-Pipeline",
    "hiw.arch.structure_title": "\U0001f4c1 Projekt-Struktur",
    "hiw.arch.models_title": "\U0001f9e0 KI-Modelle im Einsatz",

    # Mode page
    "hiw.mode.subheader": "Spielmodus-Dokumentation &mdash; Wie es funktioniert und was wir gelernt haben",
    "hiw.mode.what_title": "\U0001f3af Was es macht",
    "hiw.mode.how_title": "\u2699\ufe0f Wie es funktioniert",
    "hiw.mode.pe_title": "\u270d\ufe0f Prompt Engineering",
    "hiw.mode.challenges_title": "\U0001f527 Herausforderungen & L\u00f6sungen",
    "hiw.mode.learnings_title": "\U0001f4a1 Learnings",

    # Style page
    "hiw.style.header": "\U0001f3a8 Stil & Zielgruppen",
    "hiw.style.subheader": "Das hybride Stil-System und die Zielgruppen-Anpassung",
    "hiw.style.hybrid_title": "\U0001f58c\ufe0f Das Hybrid-Stil-System",
    "hiw.style.hybrid_desc": (
        "MEMOKI verwendet ein **hybrides** Stil-System: 10 vordefinierte Stile "
        "mit optimierten Prompt-Fragmenten **plus** die M\u00f6glichkeit, beliebige "
        "Freitext-Stile einzugeben."
    ),
    "hiw.style.how_it_works": (
        '<b>Wie es funktioniert:</b> Die Funktion <code>resolve_style(style)</code> pr\u00fcft, '
        'ob der Stil in der <code>STYLE_MAP</code> existiert. Wenn ja, wird das optimierte '
        'Prompt-Fragment verwendet. Wenn nein, wird der Freitext direkt als Stil-Beschreibung '
        'in den Prompt eingef\u00fcgt.'
    ),
    "hiw.style.predefined_title": "**Vordefinierte Stile:**",
    "hiw.style.audience_title": "\U0001f3af Zielgruppen-Anpassung",
    "hiw.style.audience_desc": (
        "Jeder Bild-Prompt wird automatisch mit zielgruppenspezifischen "
        "Attributen angereichert:"
    ),
    "hiw.style.audience.children": "Kinder",
    "hiw.style.audience.teenagers": "Teenager",
    "hiw.style.audience.adults": "Erwachsene",
    "hiw.style.freetext_title": "\U0001f196 Freitext-Stile",
    "hiw.style.freetext_desc": (
        "Neben den vordefinierten Stilen k\u00f6nnen User beliebige Stile eingeben. "
        "Der MEMOKI-Agent formuliert diese als englische Stil-Beschreibung:"
    ),
    "hiw.style.user_says": 'User sagt: <b>"{input}"</b>',
    "hiw.style.prompt_becomes": "Prompt wird: <code>{output}</code>",
    "hiw.style.learnings_title": "\U0001f4a1 Learnings",

    # Architecture page content
    "hiw.arch.pipeline.chat_agent": "\U0001f5e3\ufe0f Chat-Agent",
    "hiw.arch.pipeline.chat_agent_desc": (
        "Der MEMOKI-Agent (Gemini 2.5 Flash) f\u00fchrt den User durch "
        "die Konfiguration: Modus, Thema, Stil, Zielgruppe."
    ),
    "hiw.arch.pipeline.content": "\U0001f4cb Content-Generierung",
    "hiw.arch.pipeline.content_desc": (
        "Je nach Modus werden Objekte per LLM generiert oder "
        "aus kuratierten Wissensbasen geladen (Teekesselchen, Paare, Shapes)."
    ),
    "hiw.arch.pipeline.prompt_building": "\u270d\ufe0f Prompt-Building",
    "hiw.arch.pipeline.prompt_building_desc": (
        "Spezialisierte Prompt-Builder erzeugen optimierte Bild-Prompts "
        "mit Stil, Zielgruppe und modus-spezifischen Anpassungen."
    ),
    "hiw.arch.pipeline.image_gen": "\U0001f3a8 Bild-Generierung",
    "hiw.arch.pipeline.image_gen_desc": (
        "Gemini 3 Pro (Qualit\u00e4t) oder Gemini 2.5 Flash (Schnell) "
        "generiert die Kartenbilder parallel via ThreadPoolExecutor."
    ),
    "hiw.arch.pipeline.deck_assembly": "\U0001f0cf Deck-Assembly",
    "hiw.arch.pipeline.deck_assembly_desc": (
        "Die Bilder werden zu Card-Objekten, das Deck wird gemischt, "
        "und die interaktive Spieloberfl\u00e4che wird gerendert."
    ),

    "hiw.arch.box.frontend": "\U0001f3ad Frontend",
    "hiw.arch.box.frontend_desc": (
        "<code>app.py</code> &mdash; Streamlit-UI mit Custom CSS, Chat-Interface, "
        "Mode-Selector, Kartenraster und Spiellogik. Nunito-Font, Gradient-Background, "
        "interaktive Mode-Cards."
    ),
    "hiw.arch.box.agent": "\U0001f916 Agent",
    "hiw.arch.box.agent_desc": (
        "<code>agents/memoki.py</code> &mdash; Chat-Orchestrierung mit Gemini. "
        "System-Prompt mit Modus-spezifischen Regeln, JSON-Action-Block-Erkennung, "
        "Gespr\u00e4chshistorie."
    ),
    "hiw.arch.box.generators": "\U0001f5bc\ufe0f Generatoren",
    "hiw.arch.box.generators_desc": (
        "<code>tools/image.py</code> &mdash; Bildgenerierung via Gemini mit "
        "Stil-Mapping und Zielgruppen-Anpassung.<br>"
        "<code>tools/content.py</code> &mdash; Content-Generierung per LLM."
    ),
    "hiw.arch.box.prompts": "\u270d\ufe0f Prompts",
    "hiw.arch.box.prompts_desc": (
        "<code>prompts/</code> &mdash; Spezialisierte Prompt-Builder pro Modus: "
        "Classic, Paare, Teekesselchen, Mathe I, Mathe II. Jeder mit eigenen "
        "Optimierungen und Sonderf\u00e4llen."
    ),
    "hiw.arch.box.game_engine": "\U0001f3ae Game Engine",
    "hiw.arch.box.game_engine_desc": (
        "<code>game/</code> &mdash; Card (Dataclass), Deck (Mischen, Verwalten), "
        "GameSession (Spielzustand, Flip-Logik, Match-Erkennung)."
    ),
    "hiw.arch.box.knowledge": "\U0001f4da Wissensbasen",
    "hiw.arch.box.knowledge_desc": (
        "<code>knowledge/</code> &mdash; Kuratierte JSON-Dateien: "
        "Teekesselchen (Homonyme mit 2 Bedeutungen), Paare (logisch zusammengeh\u00f6rige "
        "Objekte), Math-Shapes (abstrakte Formen)."
    ),

    "hiw.arch.models_table": """\
| Modell | Aufgabe | Warum dieses Modell? |
|--------|---------|---------------------|
| Gemini 2.5 Flash | Chat-Agent, Objekt-Generierung | Schnell, g\u00fcnstig, gutes Sprachverst\u00e4ndnis |
| Gemini 3 Pro | Bildgenerierung (Standard) | Beste Bildqualit\u00e4t, kreative Stile |
| Gemini 2.5 Flash Image | Bildgenerierung (Schnell) | Schneller und g\u00fcnstiger f\u00fcr einfachere Motive |
""",

    # Footer
    "hiw.footer": "MEMOKI &mdash; KI-Memory-Spiele-Macher | Built with Streamlit & Google Gemini",
}


# ============================================================================
# MODE_DATA fuer How-It-Works Seite (verschachtelte Struktur)
# ============================================================================

MODE_DATA = {
    "classic": {
        "icon": "\U0001f0cf",
        "title": "Klassisches Memory",
        "what": (
            "Im klassischen Modus generiert MEMOKI Bildpaare zu einem frei "
            "w\u00e4hlbaren Thema. Der User nennt ein Thema (z.B. *Tiere*, *Fahrzeuge*, "
            "*Weltraum*), und das System erzeugt passende Motive als identische Kartenpaare.\n\n"
            "Jedes Paar besteht aus zwei identischen Karten mit demselben Motiv. "
            "Die Spieler decken Karten auf und suchen die passenden Paare."
        ),
        "how": [
            ("1. Thema w\u00e4hlen", "Der MEMOKI-Agent fragt nach Thema, Stil und Zielgruppe."),
            ("2. Objekte generieren", "Gemini 2.5 Flash generiert eine Liste passender Objekte per LLM-Call."),
            ("3. Prompts bauen", "<code>build_image_prompt()</code> erstellt f\u00fcr jedes Objekt einen optimierten Bild-Prompt."),
            ("4. Bilder erzeugen", "Gemini 3 Pro generiert die Kartenbilder parallel (ThreadPoolExecutor)."),
            ("5. Deck erstellen", "Jedes Bild wird verdoppelt, gemischt und als spielbares Deck ausgegeben."),
        ],
        "prompt_engineering": [
            "<b>Objekt-Generierung</b> &mdash; Der Content-Prompt fordert visuell unterscheidbare, "
            "konkrete Objekte. Abstrakte Konzepte und Synonyme werden explizit ausgeschlossen.",
            "<b>Stil-Anpassung</b> &mdash; Das Hybrid-System l\u00f6st bekannte Stil-Keys (z.B. <code>cartoon</code>) "
            "in detaillierte Prompt-Fragmente auf, l\u00e4sst aber auch Freitext durch (z.B. <code>van Gogh</code>).",
            "<b>Zielgruppen-Tuning</b> &mdash; Je nach Audience werden Attribute wie <code>cute, friendly</code> "
            "(Kinder) oder <code>sophisticated, elegant</code> (Erwachsene) erg\u00e4nzt.",
            "<b>Wei\u00dfer Hintergrund</b> &mdash; Alle Prompts enden mit <code>pure white background, no text, "
            "square format</code> f\u00fcr konsistente Kartenlayouts.",
        ],
        "challenges": [
            ("Objekt-Qualit\u00e4t", "Der LLM generiert manchmal zu \u00e4hnliche oder zu abstrakte Objekte. "
             "Gel\u00f6st durch detaillierte Beispiele und Negativbeispiele im Prompt."),
            ("Stil-Konsistenz", "Verschiedene Objekte im selben Stil halten &mdash; der Stil-Prompt "
             "muss stark genug sein, um den Look \u00fcber alle Karten hinweg einheitlich zu halten."),
        ],
        "learnings": [
            "<b>Few-Shot-Beispiele wirken</b> &mdash; Gute und schlechte Beispiele im Content-Prompt "
            "verbessern die Objekt-Qualit\u00e4t drastisch.",
            "<b>Parallelisierung lohnt sich</b> &mdash; 10 Bilder parallel statt sequenziell spart "
            "erheblich Zeit bei der Generierung.",
        ],
    },

    "paare": {
        "icon": "\U0001f46b",
        "title": "Paare-Memory",
        "what": (
            "Im Paare-Modus bestehen die Kartenpaare aus zwei *zusammengeh\u00f6rigen* "
            "aber *unterschiedlichen* Motiven. Zum Beispiel: Hund & Knochen, "
            "Schl\u00fcssel & Schloss, Nadel & Faden.\n\n"
            "Die Spieler m\u00fcssen erkennen, welche zwei verschiedenen Bilder "
            "logisch zusammengeh\u00f6ren &mdash; eine anspruchsvollere Variante als identische Paare."
        ),
        "how": [
            ("1. Thema w\u00e4hlen", "Der Agent fragt nach Thema, Stil und Zielgruppe."),
            ("2. Paare laden", "Zusammengeh\u00f6rige Objekt-Paare werden aus der <code>pairs_v2.json</code> Wissensbasis geladen."),
            ("3. Prompts bauen", "F\u00fcr jedes Objekt wird ein eigener Bild-Prompt erstellt (Objekt A und Objekt B getrennt)."),
            ("4. Bilder erzeugen", "Beide Bilder eines Paares werden parallel generiert."),
            ("5. Deck erstellen", "Die Karten werden gemischt, jedes Paar hat eine gemeinsame <code>pair_id</code>."),
        ],
        "prompt_engineering": [
            "<b>Paar-Koh\u00e4renz</b> &mdash; Beide Objekte eines Paares m\u00fcssen im selben Stil generiert werden, "
            "damit sie visuell als zusammengeh\u00f6rig erkennbar sind.",
            "<b>Eindeutigkeit</b> &mdash; Jedes Objekt muss eindeutig dargestellt werden &mdash; "
            "ein Schl\u00fcssel darf nicht wie ein Schloss aussehen und umgekehrt.",
            "<b>Wissensbasis-Kuratierung</b> &mdash; Die Paare in <code>pairs_v2.json</code> sind manuell kuratiert, "
            "um sicherzustellen, dass die Zuordnung f\u00fcr die Zielgruppe klar ist.",
            "<b>Anti-Morphing</b> &mdash; Der Bild-Prompt verbietet explizit Anthropomorphismus: "
            "<code>do NOT reshape it into an animal, do NOT add faces, eyes, or animal features</code>. "
            "Ohne diese Regel verwandelt Gemini Alltagsobjekte gerne in niedliche Charaktere.",
        ],
        "challenges": [
            ("Paar-Erkennung", "Die logische Verbindung muss auch visuell erkennbar sein. "
             "Zu abstrakte Paare (z.B. Ursache & Wirkung) funktionieren als Bild nicht."),
            ("Schwierigkeitsbalance", "Paare m\u00fcssen herausfordernd genug sein, aber nicht zu obskur &mdash; "
             "besonders f\u00fcr Kinder eine Gratwanderung."),
        ],
        "learnings": [
            "<b>Kuratierte Wissensbasis > LLM-Generierung</b> &mdash; F\u00fcr Paare ist eine "
            "handgepflegte JSON-Datei zuverl\u00e4ssiger als LLM-generierte Zuordnungen.",
            "<b>Kulturelle Sensibilit\u00e4t</b> &mdash; Manche Paare sind kulturabh\u00e4ngig "
            "(z.B. Brezel & Bier funktioniert in DE, aber nicht \u00fcberall).",
        ],
    },

    "teekesselchen": {
        "icon": "\U0001f9c6",
        "title": "Teekesselchen",
        "what": (
            "Teekesselchen sind W\u00f6rter mit mehreren Bedeutungen (Homonyme). "
            "Zum Beispiel: *Bank* (Sitzbank vs. Geldinstitut), *Birne* (Obst vs. Gl\u00fchbirne), "
            "*Schloss* (Geb\u00e4ude vs. T\u00fcrschloss).\n\n"
            "Karte A zeigt die eine Bedeutung als Bild, Karte B die andere Bedeutung. "
            "Die Spieler m\u00fcssen erkennen, dass beide Bilder dasselbe Wort darstellen."
        ),
        "how": [
            ("1. Kein Thema n\u00f6tig", "Teekesselchen kommen aus der kuratierten Wissensbasis <code>teekesselchen_v2.json</code>."),
            ("2. W\u00f6rter ausw\u00e4hlen", "<code>load_teekesselchen()</code> w\u00e4hlt zuf\u00e4llig N Eintr\u00e4ge mit beiden Bedeutungen."),
            ("3. Prompts bauen", "F\u00fcr jede Bedeutung wird ein separater Bild-Prompt erstellt, der die spezifische Bedeutung klar darstellt."),
            ("4. Bilder erzeugen", "Beide Bedeutungen werden als separate Karten generiert."),
            ("5. R\u00e4tsel-Deck", "Die Karten werden gemischt &mdash; das R\u00e4tsel: Welche zwei Bilder geh\u00f6ren zum selben Wort?"),
        ],
        "prompt_engineering": [
            "<b>Bedeutungs-Disambiguierung</b> &mdash; Der Prompt muss unmissverst\u00e4ndlich klarmachen, "
            "WELCHE Bedeutung gemeint ist. <code>\"A wooden park bench in a park\"</code> statt nur <code>\"Bank\"</code>.",
            "<b>Englische Bild-Prompts</b> &mdash; Die Bildgenerierung arbeitet auf Englisch, "
            "die Bedeutungen werden in der Wissensbasis bereits als englische Prompts gespeichert.",
            "<b>Keine Texthinweise</b> &mdash; Die Bilder d\u00fcrfen keinen Text enthalten, der das Wort verr\u00e4t. "
            "Nur die visuelle Darstellung z\u00e4hlt.",
        ],
        "challenges": [
            ("Homonym-Qualit\u00e4t", "Nicht jedes Homonym eignet sich &mdash; beide Bedeutungen m\u00fcssen "
             "gut als Bild darstellbar sein. <code>Ton</code> (Klang vs. Erde) ist z.B. schwierig."),
            ("Schwierigkeitsgrad", "Die beiden Bilder d\u00fcrfen sich nicht zu \u00e4hnlich sehen "
             "(sonst zu leicht) und nicht zu unterschiedlich (sonst geraten)."),
            ("Wissensbasis-Pflege", "Jeder Eintrag braucht zwei sorgf\u00e4ltig formulierte englische "
             "Bild-Beschreibungen &mdash; aufwendig, aber notwendig f\u00fcr Qualit\u00e4t."),
        ],
        "learnings": [
            "<b>JSON-Struktur entscheidend</b> &mdash; Jedes Teekesselchen hat <code>meaning_a</code> und "
            "<code>meaning_b</code> mit je einer deutschen Bezeichnung und einem englischen Bild-Prompt.",
            "<b>Kuratierung ist King</b> &mdash; LLMs k\u00f6nnen Teekesselchen vorschlagen, aber die "
            "finale Auswahl und Prompt-Formulierung braucht menschliches Urteil.",
        ],
    },

    "mathe_abstrakt": {
        "icon": "\U0001f522",
        "title": "Mathe I (Abstrakt)",
        "what": (
            "Mathe Memory I trainiert Zahlenverst\u00e4ndnis durch abstrakte Darstellungen. "
            "Karte A zeigt eine Zahl (z.B. **5**), Karte B zeigt die entsprechende Menge "
            "als abstrakte Formen (z.B. 5 Kreise, 5 Sterne, 5 Herzen).\n\n"
            "Der User w\u00e4hlt einen **Shape-Stil** (Kreise, Sterne, Herzen, W\u00fcrfelaugen, "
            "Finger oder \u00dcberraschung). Die Zahlen 1&ndash;10 oder 1&ndash;20 werden automatisch generiert."
        ),
        "how": [
            ("1. Shape w\u00e4hlen", "Der Agent bietet 6 Shape-Optionen an: Kreise, Sterne, Herzen, W\u00fcrfelaugen, Finger, \u00dcberraschung."),
            ("2. Shape laden", "<code>load_math_shape()</code> l\u00e4dt die Shape-Definition aus <code>math_shapes.json</code>."),
            ("3. Zahl-Prompts", "<code>build_number_prompt()</code> erzeugt Prompts f\u00fcr die Zahlenkarten (gro\u00dfe, klare Ziffer)."),
            ("4. Shape-Prompts", "<code>build_shapes_prompt()</code> erzeugt Prompts f\u00fcr die Shape-Karten (N Objekte, klar z\u00e4hlbar)."),
            ("5. Parallel generieren", "Alle Karten werden parallel via ThreadPoolExecutor generiert."),
        ],
        "prompt_engineering": [
            "<b>Z\u00e4hlbarkeit</b> &mdash; Der Shape-Prompt betont <code>clearly countable, well-spaced</code> &mdash; "
            "die Formen m\u00fcssen einzeln abz\u00e4hlbar sein, nicht ineinander verschmelzen.",
            "<b>Finger-Sonderlogik</b> &mdash; Zahlen 1&ndash;5 zeigen eine Hand, 6&ndash;10 zeigen zwei H\u00e4nde. "
            "Der Prompt beschreibt explizit <code>left hand 5 fingers + right hand N fingers</code>.",
            "<b>Zahlen-Klarheit</b> &mdash; Zahlenkarten betonen <code>clean standard shape, instantly recognizable</code> "
            "und verbieten explizit Dekorationen, die die Lesbarkeit beeintr\u00e4chtigen.",
            "<b>Konsistente Shapes</b> &mdash; Die <code>image_prompt_en</code> aus der JSON-Datei definiert das "
            "exakte Aussehen jeder Form f\u00fcr konsistente Ergebnisse.",
            "<b>Layout-Hints</b> &mdash; <code>_layout_hint(n)</code> gibt f\u00fcr jede Zahl eine explizite "
            "Grid-Anordnung vor (z.B. <code>3 top row, 2 bottom row</code> f\u00fcr 5), damit die KI "
            "die korrekte Anzahl nicht zuf\u00e4llig verteilt, sondern strukturiert anordnet.",
            "<b>W\u00fcrfelaugen-Prompts</b> &mdash; <code>_dice_prompt(n)</code> beschreibt exakte Pip-Positionen "
            "pro W\u00fcrfelseite. Ab 7 werden mehrere W\u00fcrfel nebeneinander dargestellt (z.B. 6+1 f\u00fcr 7).",
            "<b>Strichlisten-Prompts</b> &mdash; <code>_tally_prompt(n)</code> nutzt das klassische System: "
            "4 senkrechte Striche + 1 diagonaler = 5. Gruppen werden getrennt dargestellt.",
            "<b>Domino-Prompts</b> &mdash; <code>_domino_prompt(n)</code> teilt die Zahl optimal auf zwei "
            "H\u00e4lften auf (max 6 pro H\u00e4lfte). Ab 13 werden zwei Dominosteine verwendet.",
        ],
        "challenges": [
            ("Zahlen-Styling vs. Lesbarkeit", "Wenn ein Thema gew\u00e4hlt wird, d\u00fcrfen Farben sich anpassen, "
             "aber die Ziffernform muss sauber bleiben. Gel\u00f6st durch explizites <code>Do NOT reshape the number</code>."),
            ("Finger-Darstellung", "LLMs haben Schwierigkeiten mit korrekter Finger-Anzahl. "
             "Gel\u00f6st durch sehr explizite Hand-Beschreibungen im Prompt."),
            ("Hohe Zahlen z\u00e4hlen", "Bei 15+ Objekten wird das Z\u00e4hlen im Bild schwierig. "
             "Reihen/Grid-Anordnung und gro\u00dfz\u00fcgiger Abstand helfen."),
        ],
        "learnings": [
            "<b>Shape-Datenbank statt Freitext</b> &mdash; Vordefinierte Shapes mit getesteten "
            "Prompt-Fragmenten liefern konsistentere Ergebnisse als freie Beschreibungen.",
            "<b>Negative Prompts wirken</b> &mdash; <code>no borders, no frames, no black edges</code> "
            "verhindert unerw\u00fcnschte visuelle Artefakte bei den Zahlenkarten.",
        ],
    },

    "mathe_konkret": {
        "icon": "\U0001f9ee",
        "title": "Mathe II (Konkret)",
        "what": (
            "Mathe Memory II verwendet **reale Objekte** statt abstrakter Formen. "
            "Karte A zeigt eine Zahl, Karte B zeigt die entsprechende Menge "
            "realer Gegenst\u00e4nde (z.B. 3 Tennisb\u00e4lle, 7 Cupcakes).\n\n"
            "Der User w\u00e4hlt ein **Thema** (z.B. Sport, Essen, Spielzeug), und das "
            "System generiert per LLM passende, z\u00e4hlbare Objekte. Jede Zahl wird "
            "mit einem *anderen* Objekt gepaart."
        ),
        "how": [
            ("1. Thema w\u00e4hlen", "Der Agent fragt nach einem Thema und erkl\u00e4rt, dass es gut z\u00e4hlbare Objekte hergeben muss."),
            ("2. Objekte generieren", "<code>generate_countable_objects()</code> nutzt Gemini Flash, um N z\u00e4hlbare Objekte zum Thema zu finden."),
            ("3. Zahl-Prompts", "<code>build_number_prompt()</code> erstellt Zahlenkarten mit optionalem Thema-Einfluss auf Farben."),
            ("4. Objekt-Prompts", "<code>build_real_objects_prompt()</code> erstellt Karten mit exakt N identischen Objekten."),
            ("5. Generieren & Paaren", "Zahl 1 &harr; Objekt A, Zahl 2 &harr; Objekt B, etc. Parallel generiert."),
        ],
        "prompt_engineering": [
            "<b>Z\u00e4hlbare Objekte erzwingen</b> &mdash; Der Content-Prompt hat strenge Regeln: "
            "Objekte m\u00fcssen diskret, klein und einzeln z\u00e4hlbar sein. Elefanten oder Schwimmb\u00e4der sind verboten.",
            "<b>Die Sache selbst, nicht Zubeh\u00f6r</b> &mdash; Wichtigste Regel im Prompt: Bei Thema <code>Schuhe</code> "
            "Schuhtypen generieren (Sneaker, Stiefel), NICHT Schuh-Zubeh\u00f6r (Schn\u00fcrsenkel, Schuhschnalle).",
            "<b>Anti-Cropping</b> &mdash; Explizite Anweisung: <code>all objects fully visible and not cropped or "
            "cut off at the edges</code> mit <code>generous margin</code> verhindert abgeschnittene Objekte.",
            "<b>Identische Objekte</b> &mdash; Der Prompt betont <code>identical</code> und <code>same type</code> &mdash; "
            "5 Tennisb\u00e4lle sollen 5 gleiche Tennisb\u00e4lle sein, nicht 3 Tennisb\u00e4lle und 2 Fu\u00dfb\u00e4lle.",
            "<b>Thema-Kontext f\u00fcr Mehrdeutigkeiten</b> &mdash; <code>(in the context of {theme})</code> hilft dem "
            "Bildgenerator bei mehrdeutigen W\u00f6rtern (z.B. <code>mouse</code> bei Thema Technik vs. Tiere).",
            "<b>Layout-Hints</b> &mdash; Auch bei realen Objekten nutzt <code>build_real_objects_prompt()</code> "
            "die <code>_layout_hint(n)</code>-Funktion f\u00fcr strukturierte Grid-Anordnungen, damit die "
            "exakte Anzahl klar z\u00e4hlbar bleibt.",
        ],
        "challenges": [
            ("Objekt-Auswahl-Qualit\u00e4t", "LLMs generierten Zubeh\u00f6r statt der Sache selbst "
             "(Schuhschnallen statt Schuhe). Gel\u00f6st durch explizite Regel und Positiv-/Negativ-Beispiele."),
            ("Objekt-Cropping", "Bei 7+ Objekten wurden Teile am Bildrand abgeschnitten. "
             "Gel\u00f6st durch <code>generous margin</code> und explizite Anti-Cropping-Anweisung."),
            ("Zahlenkarten-Deformation", "Zahlen wurden thematisch verformt (6 sah aus wie ein Schuh). "
             "Gel\u00f6st durch explizites <code>Do NOT reshape the number to look like objects from the theme</code>."),
            ("Schwarze R\u00e4nder", "Manche Zahlenkarten hatten unerw\u00fcnschte schwarze Rahmen. "
             "Gel\u00f6st durch <code>no borders, no frames, no black edges</code> im Prompt."),
        ],
        "learnings": [
            "<b>Iteratives Prompt-Engineering</b> &mdash; Die Prompts wurden durch mehrere Test-Runden "
            "schrittweise verbessert. Jeder Testlauf offenbarte neue Edge Cases.",
            "<b>Negative Anweisungen sind m\u00e4chtig</b> &mdash; Explizite Verbote (<code>Do NOT reshape</code>, "
            "<code>no borders</code>) wirken oft besser als positive Anweisungen allein.",
            "<b>Beispiel-basiertes Prompting</b> &mdash; Gute und schlechte Beispiele im Content-Prompt "
            "verbessern die LLM-Objekt-Auswahl massiv (Schuhe, Getr\u00e4nke).",
        ],
    },
}
