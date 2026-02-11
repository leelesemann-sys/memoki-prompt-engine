"""MEMOKI -- English strings."""

# ============================================================================
# Flat strings for t() lookups
# ============================================================================

STRINGS: dict[str, str] = {

    # -- Page title / Banner -----------------------------------------------
    "page.title": "MEMOKI \u2013 AI Memory Game Maker",
    "page.title_test": "MEMOKI \u2013 TEST MODE",
    "banner.subtitle": "Your AI Memory Game Maker",
    "banner.feat_generate": "\U0001f0cf Generate cards",
    "banner.feat_play": "\U0001f3ae Play instantly",
    "banner.feat_print": "\U0001f5a8\ufe0f Print template",

    # -- Game modes --------------------------------------------------------
    "mode.classic.name": "Classic Memory",
    "mode.classic.desc": "2x the same image",
    "mode.paare.name": "Pairs Memory",
    "mode.paare.desc": "Related objects (TV & Remote)",
    "mode.teekesselchen.name": "Teapot Memory",
    "mode.teekesselchen.desc": "Same word, different picture (Bat & Bat)",
    "mode.mathe_abstrakt.name": "Math Memory I",
    "mode.mathe_abstrakt.desc": "Number \u2194 abstract shapes (5 \u2194 squares)",
    "mode.mathe_konkret.name": "Math Memory II",
    "mode.mathe_konkret.desc": "Number \u2194 real objects (5 \u2194 shoes)",

    # -- Sidebar / Layout --------------------------------------------------
    "section.game_mode": "\U0001f3af Game Mode",
    "section.chat": "\U0001f4ac Chat with MEMOKI",
    "footer.text": "MEMOKI \u2013 LLM Tuning & Prompt Engineering \U0001f9e0",

    # -- Buttons -----------------------------------------------------------
    "btn.shuffle_play": "\U0001f3ae Shuffle & Play",
    "btn.show_cards": "\U0001f441\ufe0f Show Cards",
    "btn.download_zip": "\U0001f4e5 Download All Cards (ZIP)",
    "btn.new_game": "\U0001f504 New Game",
    "btn.download_filename": "memoki-cards.zip",

    # -- Preview / Play field ----------------------------------------------
    "preview.title": "\U0001f441\ufe0f Card Preview",
    "preview.pairs_sorted": "{total_pairs} pairs sorted by match",
    "preview.no_image": "*(no image)*",
    "play.title": "\U0001f3ae Game Board",
    "play.pairs_found": "Pairs found: <strong>{found}/{total_pairs}</strong>",
    "play.moves": "Moves: <strong>{moves}</strong>",
    "play.won": "\U0001f389 You won! You found all {total_pairs} pairs in {moves} moves!",

    # -- Test mode ---------------------------------------------------------
    "test.title": "\U0001f50d TEST MODE",
    "test.all_revealed": "All {total_pairs} pairs revealed",
    "test.grouped": "Cards grouped by pair_id",

    # -- Chat --------------------------------------------------------------
    "chat.placeholder": "Tell MEMOKI what you\u2019d like \u2026",
    "chat.thinking": "MEMOKI is thinking...",

    # -- Greetings ---------------------------------------------------------
    "greeting.hello": "Hello! I\u2019m **MEMOKI** \U0001f0cf\n\n",
    "greeting.mode_chosen": "You chose **{mode_name}** \u2013 great choice!\n\n",
    "greeting.teekesselchen": (
        "I\u2019ll pick the words from my collection of 119 homonyms.\n"
        "Just tell me:\n"
        "- What **style**? (Cartoon, Photo, Watercolor \u2026)\n"
        "- For **whom**? (Kids, Teenagers, Adults?)"
    ),
    "greeting.mathe_abstrakt": (
        "Numbers 1\u2013{num_pairs} are generated automatically.\n"
        "Just tell me:\n"
        "- Which **shapes**? (Circles \u25cf, Stars \u2605, Hearts \u2665, Dice \u2685, Fingers \u270b, Surprise \U0001f3b2)\n"
        "- What **style**? (Cartoon, Photo, Watercolor \u2026)\n"
        "- For **whom**? (Kids, Teenagers, Adults?)"
    ),
    "greeting.mathe_konkret": (
        "Numbers 1\u2013{num_pairs} will be paired with real objects.\n"
        "Tell me:\n"
        "- What **theme**? (Sports, Food, Toys \u2026)\n"
        "  Tip: Pick a theme with small, countable things!\n"
        "- What **style**? (Cartoon, Photo, Watercolor \u2026)\n"
        "- For **whom**? (Kids, Teenagers, Adults?)"
    ),
    "greeting.paare": (
        "Here you\u2019ll find matching pairs like Pot & Lid.\n"
        "Tell me:\n"
        "- What **theme**? ({themes_str})\n"
        "- What **style**? (Cartoon, Photo, Watercolor \u2026)\n"
        "- For **whom**? (Kids, Teenagers, Adults?)"
    ),
    "greeting.classic": (
        "Tell me what kind of cards you\u2019d like:\n"
        "- What **theme**? (Animals, Food, Technology \u2026)\n"
        "- What **style**? (Cartoon, Photo, Watercolor \u2026)\n"
        "- For **whom**? (Kids, Teenagers, Adults?)"
    ),

    # -- Generation pipeline -----------------------------------------------
    "gen.progress": "Generating {label}...",
    "gen.image_progress": "Image {done}/{total}",
    "gen.fallback": "Fallback: {error}",
    "gen.failed": "Failed: {error}",
    "gen.building_deck": "\U0001f0cf Building game board...",
    "gen.error_loading": "Error loading: {error}",
    "gen.error_shape": "Error loading shape: {error}",
    "gen.error_objects": "Error generating objects: {error}",

    # Teekesselchen
    "gen.tk.status": "\U0001f9c6 Generating {num_pairs} homonym pairs...",
    "gen.tk.selecting": "\U0001f4dd Picking {num_pairs} homonyms from 119 words...",
    "gen.tk.words_ok": "\u2705 Words: {words}",
    "gen.tk.images": "\U0001f5bc\ufe0f Generating {count} images in parallel (2 per word)...",
    "gen.tk.done": "\u2705 Done! Your Teapot Memory is ready!",
    "gen.tk.complete_msg": "\U0001f389 Your **Teapot Memory** with {num_pairs} word pairs is ready! Find the two meanings!",

    # Math Abstract
    "gen.ma.status": "\U0001f522 Generating Math Memory with {num_pairs} numbers...",
    "gen.ma.loading_shape": "\U0001f537 Loading shape style '{shape_id}'...",
    "gen.ma.shape_ok": "\u2705 Shape: {name} {symbol}",
    "gen.ma.images": "\U0001f5bc\ufe0f Generating {count} images in parallel (Number + Shape)...",
    "gen.ma.done": "\u2705 Done! Your Math Memory is ready!",
    "gen.ma.complete_msg": "\U0001f389 Your **Math Memory** with numbers 1\u2013{num_pairs} and **{shape_name}** is ready! Find the matching pairs!",

    # Math Concrete
    "gen.mk.status": "\U0001f3af Generating Math Memory II with {num_pairs} numbers...",
    "gen.mk.generating_objects": "\U0001f4dd Generating {num_pairs} countable objects for theme '{theme}'...",
    "gen.mk.objects_ok": "\u2705 Objects: {objects}",
    "gen.mk.images": "\U0001f5bc\ufe0f Generating {count} images in parallel (Number + Object)...",
    "gen.mk.done": "\u2705 Done! Your Math Memory II is ready!",
    "gen.mk.complete_msg": "\U0001f389 Your **Math Memory II** on theme **{theme}** with numbers 1\u2013{num_pairs} is ready! Match numbers and objects!",

    # Pairs
    "gen.pa.status": "\U0001f9e9 Generating {num_pairs} pairs for theme '{theme}'...",
    "gen.pa.selecting": "\U0001f4dd Picking {num_pairs} pairs for theme '{theme}'...",
    "gen.pa.pairs_ok": "\u2705 Pairs: {pairs}",
    "gen.pa.images": "\U0001f5bc\ufe0f Generating {count} images in parallel (2 per pair)...",
    "gen.pa.done": "\u2705 Done! Your Pairs Memory is ready!",
    "gen.pa.complete_msg": "\U0001f389 Your **Pairs Memory** on theme **{theme}** with {count} pairs is ready! Find the matching objects!",

    # Classic
    "gen.cl.status": "\U0001f3a8 Generating {num_pairs} card images...",
    "gen.cl.generating_objects": "\U0001f4dd Generating {num_pairs} objects for theme '{theme}'...",
    "gen.cl.objects_ok": "\u2705 Objects: {objects}",
    "gen.cl.images": "\U0001f5bc\ufe0f Generating {num_pairs} images in parallel...",
    "gen.cl.done": "\u2705 Done! Your Memory is ready!",
    "gen.cl.complete_msg": "\U0001f389 Your **{theme}** Memory with {num_pairs} pairs is ready! Have fun playing!",

    # -- Card labels -------------------------------------------------------
    "card.number": "Number {num}",
    "card.number_x": "{num}x {name}",

    # -- Agent System Prompt -----------------------------------------------
    "agent.system_prompt": """\
You are MEMOKI, a friendly and creative Memory card game generator.
You speak English with the user.

## YOUR TASK

You collect the information needed to create a Memory card game:
- **Mode**: Provided by the frontend (classic, paare, teekesselchen, mathe_abstrakt, mathe_konkret)
- **Pair count**: Provided by the frontend (10 or 20)
- **Theme**: Ask the user (e.g. Animals, Sports, Food) -- NOT for Homonyms!
- **Style**: Ask the user (e.g. Cartoon, Photorealistic, Watercolor)
- **Audience**: Ask the user (e.g. Kids, Teenagers, Adults)

## SPECIAL CASE: HOMONYMS (Teekesselchen)

For the "teekesselchen" mode there is NO theme -- the words come from a curated knowledge base.
Only ask for **style** and **audience**. Set "theme": "teekesselchen" in the JSON.

## SPECIAL CASE: PAIRS

For the "paare" mode the user picks a **theme** from a fixed list.
The pairs (e.g. Pot & Lid, Key & Lock) come from a curated knowledge base.

Available themes: Kitchen, Office, Sports, Household, Music, Garden, Bathroom, School, Traffic, Animals.

Ask for **theme** (from the list above), **style** and **audience**.
In JSON: Set "theme" to the English theme name (e.g. "Kitchen", "Sports").

## SPECIAL CASE: MATH ABSTRACT

For the "mathe_abstrakt" mode there is NO theme. Instead the user picks a **shape style**.
Numbers (1-10 or 1-20) are generated automatically.

Ask for **shape style**, **image style** and **audience**. Offer these options:
- Circles \u25cf
- Stars \u2605
- Hearts \u2665
- Dice pips \u2685
- Fingers \u270b
- Surprise me! \U0001f3b2

In JSON: Set "theme": "mathe_abstrakt" and add "shape": "<shape_id>".
Shape IDs: "circles", "stars", "hearts", "dice", "fingers", "surprise"

## SPECIAL CASE: MATH CONCRETE

For the "mathe_konkret" mode the user picks a **theme** (e.g. Sports, Animals, Food).
The system generates countable objects from that theme (e.g. tennis balls, soccer balls, ice skates).
Each number (1-10 or 1-20) is paired with a DIFFERENT object.

Ask for **theme**, **style** and **audience**.

IMPORTANT: Tell the user that the theme should have small, countable objects.
Good theme examples: Sports, Food, Toys, Nature, Candy.
Bad theme examples: Space, Landscapes, Buildings (too large / not countable).

In JSON: Set "theme": "<theme>" (same as Classic).

## YOUR CONVERSATION FLOW

1. Briefly greet the user and mention the chosen mode
2. Depending on mode:
   - Homonyms: Only ask for style and audience
   - Pairs: Ask for theme (from the fixed list!), style and audience
   - Math Abstract: Ask for shape style, image style and audience
   - Math Concrete: Ask for theme (mention countable objects!), style and audience
   - Classic: Ask for theme AND style. Make suggestions!
3. Once you have all info, briefly summarize and output the JSON block IMMEDIATELY (NO confirmation question!).
   Write the summary then DIRECTLY the JSON block. NO announcement like "Here is your JSON:" before it!

```json
{"action": "generate", "theme": "...", "style": "...", "audience": "...", "shape": "..."}
```
Note: "shape" only needed for mathe_abstrakt, omit for other modes.

## IMPORTANT RULES

- Be brief and friendly, not too chatty
- Always offer 3-4 concrete suggestions
- Once all info is collected -> output JSON immediately, do NOT ask for confirmation
- The JSON block MUST be wrapped in ```json ... ```
- Use English terms in JSON (theme, style, audience)
- Standard styles: "cartoon", "photorealistic", "watercolor", "minimalist", "artistic", "black-and-white", "pencil", "retro", "pixel", "comic"
- The user can also request CUSTOM styles (e.g. "van Gogh", "Bauhaus", "Art Nouveau"). In that case: Write a short English style description as the style value in JSON, e.g. "van Gogh post-impressionist style, thick swirling brushstrokes, bold vivid colors"
- Audience values: "children", "teenagers", "adults"
""",

    "agent.context_header": "## CURRENT CONTEXT\n- Selected mode: {mode}\n- Pair count: {pair_count}\n",

    # -- How-It-Works page -------------------------------------------------
    "hiw.page_title": "MEMOKI \u2013 How it Works",
    "hiw.sidebar_title": "### \U0001f9e0 MEMOKI Docs",
    "hiw.nav.architecture": "\U0001f3d7\ufe0f Architecture Overview",
    "hiw.nav.classic": "\U0001f0cf Classic Memory",
    "hiw.nav.paare": "\U0001f46b Pairs Memory",
    "hiw.nav.teekesselchen": "\U0001f9c6 Teapot Memory",
    "hiw.nav.mathe_abstrakt": "\U0001f522 Math I (Abstract)",
    "hiw.nav.mathe_konkret": "\U0001f9ee Math II (Concrete)",
    "hiw.nav.style": "\U0001f3a8 Style & Audience",
    "hiw.nav.i18n": "\U0001f310 Languages (i18n)",

    # Architecture page
    "hiw.arch.header": "\U0001f3d7\ufe0f Architecture Overview",
    "hiw.arch.subheader": "How MEMOKI works under the hood",
    "hiw.arch.kpi_title": "\U0001f4ca At a Glance",
    "hiw.arch.kpi.modes": "Game Modes",
    "hiw.arch.kpi.styles": "Image Styles",
    "hiw.arch.kpi.models": "Gemini Models",
    "hiw.arch.kpi.knowledge": "Knowledge Bases",
    "hiw.arch.pipeline_title": "\U0001f504 The MEMOKI Pipeline",
    "hiw.arch.structure_title": "\U0001f4c1 Project Structure",
    "hiw.arch.models_title": "\U0001f9e0 AI Models in Use",

    # Mode page
    "hiw.mode.subheader": "Game Mode Documentation &mdash; How it works and what we learned",
    "hiw.mode.what_title": "\U0001f3af What it does",
    "hiw.mode.how_title": "\u2699\ufe0f How it works",
    "hiw.mode.pe_title": "\u270d\ufe0f Prompt Engineering",
    "hiw.mode.challenges_title": "\U0001f527 Challenges & Solutions",
    "hiw.mode.learnings_title": "\U0001f4a1 Learnings",

    # Style page
    "hiw.style.header": "\U0001f3a8 Style & Audience",
    "hiw.style.subheader": "The hybrid style system and audience adaptation",
    "hiw.style.hybrid_title": "\U0001f58c\ufe0f The Hybrid Style System",
    "hiw.style.hybrid_desc": (
        "MEMOKI uses a **hybrid** style system: 10 predefined styles "
        "with optimized prompt fragments **plus** the ability to enter "
        "any free-text style."
    ),
    "hiw.style.how_it_works": (
        '<b>How it works:</b> The function <code>resolve_style(style)</code> checks '
        'if the style exists in the <code>STYLE_MAP</code>. If yes, the optimized '
        'prompt fragment is used. If not, the free text is inserted directly as '
        'the style description in the prompt.'
    ),
    "hiw.style.predefined_title": "**Predefined Styles:**",
    "hiw.style.audience_title": "\U0001f3af Audience Adaptation",
    "hiw.style.audience_desc": (
        "Every image prompt is automatically enriched with "
        "audience-specific attributes:"
    ),
    "hiw.style.audience.children": "Kids",
    "hiw.style.audience.teenagers": "Teenagers",
    "hiw.style.audience.adults": "Adults",
    "hiw.style.freetext_title": "\U0001f196 Free-Text Styles",
    "hiw.style.freetext_desc": (
        "Besides the predefined styles, users can enter any style they like. "
        "The MEMOKI agent formulates these as English style descriptions:"
    ),
    "hiw.style.user_says": 'User says: <b>"{input}"</b>',
    "hiw.style.prompt_becomes": "Prompt becomes: <code>{output}</code>",
    "hiw.style.learnings_title": "\U0001f4a1 Learnings",

    # Architecture page content
    "hiw.arch.pipeline.chat_agent": "\U0001f5e3\ufe0f Chat Agent",
    "hiw.arch.pipeline.chat_agent_desc": (
        "The MEMOKI agent (Gemini 2.5 Flash) guides the user through "
        "the configuration: mode, theme, style, audience."
    ),
    "hiw.arch.pipeline.content": "\U0001f4cb Content Generation",
    "hiw.arch.pipeline.content_desc": (
        "Depending on the mode, objects are generated via LLM or "
        "loaded from curated knowledge bases (Homonyms, Pairs, Shapes)."
    ),
    "hiw.arch.pipeline.prompt_building": "\u270d\ufe0f Prompt Building",
    "hiw.arch.pipeline.prompt_building_desc": (
        "Specialized prompt builders create optimized image prompts "
        "with style, audience and mode-specific adjustments."
    ),
    "hiw.arch.pipeline.image_gen": "\U0001f3a8 Image Generation",
    "hiw.arch.pipeline.image_gen_desc": (
        "Gemini 3 Pro (quality) or Gemini 2.5 Flash (fast) "
        "generates card images in parallel via ThreadPoolExecutor."
    ),
    "hiw.arch.pipeline.deck_assembly": "\U0001f0cf Deck Assembly",
    "hiw.arch.pipeline.deck_assembly_desc": (
        "Images become Card objects, the deck is shuffled, "
        "and the interactive game board is rendered."
    ),

    "hiw.arch.box.frontend": "\U0001f3ad Frontend",
    "hiw.arch.box.frontend_desc": (
        "<code>app.py</code> &mdash; Streamlit UI with custom CSS, chat interface, "
        "mode selector, card grid and game logic. Nunito font, gradient background, "
        "interactive mode cards."
    ),
    "hiw.arch.box.agent": "\U0001f916 Agent",
    "hiw.arch.box.agent_desc": (
        "<code>agents/memoki.py</code> &mdash; Chat orchestration with Gemini. "
        "System prompt with mode-specific rules, JSON action block detection, "
        "conversation history."
    ),
    "hiw.arch.box.generators": "\U0001f5bc\ufe0f Generators",
    "hiw.arch.box.generators_desc": (
        "<code>tools/image.py</code> &mdash; Image generation via Gemini with "
        "style mapping and audience adaptation.<br>"
        "<code>tools/content.py</code> &mdash; Content generation via LLM."
    ),
    "hiw.arch.box.prompts": "\u270d\ufe0f Prompts",
    "hiw.arch.box.prompts_desc": (
        "<code>prompts/</code> &mdash; Specialized prompt builders per mode: "
        "Classic, Pairs, Homonyms, Math I, Math II. Each with its own "
        "optimizations and special cases."
    ),
    "hiw.arch.box.game_engine": "\U0001f3ae Game Engine",
    "hiw.arch.box.game_engine_desc": (
        "<code>game/</code> &mdash; Card (dataclass), Deck (shuffle, manage), "
        "GameSession (game state, flip logic, match detection)."
    ),
    "hiw.arch.box.knowledge": "\U0001f4da Knowledge Bases",
    "hiw.arch.box.knowledge_desc": (
        "<code>knowledge/</code> &mdash; Curated JSON files: "
        "Homonyms (words with 2 meanings), Pairs (logically related "
        "objects), Math Shapes (abstract forms)."
    ),

    "hiw.arch.models_table": """\
| Model | Task | Why this model? |
|-------|------|-----------------|
| Gemini 2.5 Flash | Chat agent, object generation | Fast, affordable, good language understanding |
| Gemini 3 Pro | Image generation (standard) | Best image quality, creative styles |
| Gemini 2.5 Flash Image | Image generation (fast) | Faster and cheaper for simpler subjects |
""",

    # Footer
    "hiw.footer": "MEMOKI &mdash; AI Memory Game Maker | Built with Streamlit & Google Gemini",
}


# ============================================================================
# MODE_DATA for How-It-Works page (nested structure)
# ============================================================================

MODE_DATA = {
    "classic": {
        "icon": "\U0001f0cf",
        "title": "Classic Memory",
        "what": (
            "In classic mode, MEMOKI generates image pairs for any theme you choose. "
            "The user names a theme (e.g. *Animals*, *Vehicles*, *Space*), and the system "
            "creates matching images as identical card pairs.\n\n"
            "Each pair consists of two identical cards with the same image. "
            "Players flip cards and look for matching pairs."
        ),
        "how": [
            ("1. Choose theme", "The MEMOKI agent asks for theme, style and audience."),
            ("2. Generate objects", "Gemini 2.5 Flash generates a list of matching objects via LLM call."),
            ("3. Build prompts", "<code>build_image_prompt()</code> creates an optimized image prompt for each object."),
            ("4. Generate images", "Gemini 3 Pro generates the card images in parallel (ThreadPoolExecutor)."),
            ("5. Build deck", "Each image is duplicated, shuffled and presented as a playable deck."),
        ],
        "prompt_engineering": [
            "<b>Object generation</b> &mdash; The content prompt requires visually distinguishable, "
            "concrete objects. Abstract concepts and synonyms are explicitly excluded.",
            "<b>Style adaptation</b> &mdash; The hybrid system resolves known style keys (e.g. <code>cartoon</code>) "
            "into detailed prompt fragments, but also passes through free text (e.g. <code>van Gogh</code>).",
            "<b>Audience tuning</b> &mdash; Depending on audience, attributes like <code>cute, friendly</code> "
            "(kids) or <code>sophisticated, elegant</code> (adults) are added.",
            "<b>White background</b> &mdash; All prompts end with <code>pure white background, no text, "
            "square format</code> for consistent card layouts.",
        ],
        "challenges": [
            ("Object quality", "The LLM sometimes generates objects that are too similar or too abstract. "
             "Solved with detailed examples and negative examples in the prompt."),
            ("Style consistency", "Keeping different objects in the same style &mdash; the style prompt "
             "must be strong enough to maintain a consistent look across all cards."),
        ],
        "learnings": [
            "<b>Few-shot examples work</b> &mdash; Good and bad examples in the content prompt "
            "drastically improve object quality.",
            "<b>Parallelization pays off</b> &mdash; 10 images in parallel instead of sequential saves "
            "significant generation time.",
        ],
    },

    "paare": {
        "icon": "\U0001f46b",
        "title": "Pairs Memory",
        "what": (
            "In Pairs mode, card pairs consist of two *related* but *different* images. "
            "For example: Dog & Bone, Key & Lock, Needle & Thread.\n\n"
            "Players must identify which two different images belong together "
            "&mdash; a more challenging variant than identical pairs."
        ),
        "how": [
            ("1. Choose theme", "The agent asks for theme, style and audience."),
            ("2. Load pairs", "Related object pairs are loaded from the <code>pairs_v2.json</code> knowledge base."),
            ("3. Build prompts", "A separate image prompt is created for each object (Object A and Object B separately)."),
            ("4. Generate images", "Both images of a pair are generated in parallel."),
            ("5. Build deck", "Cards are shuffled, each pair shares a common <code>pair_id</code>."),
        ],
        "prompt_engineering": [
            "<b>Pair coherence</b> &mdash; Both objects of a pair must be generated in the same style "
            "so they are visually recognizable as belonging together.",
            "<b>Distinctness</b> &mdash; Each object must be clearly depicted &mdash; "
            "a key must not look like a lock and vice versa.",
            "<b>Knowledge base curation</b> &mdash; The pairs in <code>pairs_v2.json</code> are manually curated "
            "to ensure the association is clear for the target audience.",
            "<b>Anti-morphing</b> &mdash; The image prompt explicitly forbids anthropomorphism: "
            "<code>do NOT reshape it into an animal, do NOT add faces, eyes, or animal features</code>. "
            "Without this rule, Gemini tends to turn everyday objects into cute characters.",
        ],
        "challenges": [
            ("Pair recognition", "The logical connection must also be visually recognizable. "
             "Too abstract pairs (e.g. Cause & Effect) don\u2019t work as images."),
            ("Difficulty balance", "Pairs must be challenging enough but not too obscure &mdash; "
             "especially for kids, a fine line to walk."),
        ],
        "learnings": [
            "<b>Curated knowledge base > LLM generation</b> &mdash; For pairs, a "
            "hand-maintained JSON file is more reliable than LLM-generated associations.",
            "<b>Cultural sensitivity</b> &mdash; Some pairs are culture-dependent "
            "(e.g. Pretzel & Beer works in Germany, but not everywhere).",
        ],
    },

    "teekesselchen": {
        "icon": "\U0001f9c6",
        "title": "Teapot Memory",
        "what": (
            "Homonyms are words with multiple meanings. "
            "For example: *Bank* (park bench vs. financial institution), *Bat* (animal vs. sports equipment), "
            "*Trunk* (tree trunk vs. elephant trunk).\n\n"
            "Card A shows one meaning as an image, Card B shows the other meaning. "
            "Players must recognize that both images represent the same word."
        ),
        "how": [
            ("1. No theme needed", "Homonyms come from the curated, language-specific knowledge base (<code>teekesselchen_en.json</code> / <code>teekesselchen_de.json</code>)."),
            ("2. Select words", "<code>load_teekesselchen()</code> randomly selects N entries with both meanings."),
            ("3. Build prompts", "A separate image prompt is created for each meaning, clearly depicting the specific interpretation."),
            ("4. Generate images", "Both meanings are generated as separate cards."),
            ("5. Puzzle deck", "Cards are shuffled &mdash; the puzzle: Which two images belong to the same word?"),
        ],
        "prompt_engineering": [
            "<b>Meaning disambiguation</b> &mdash; The prompt must unambiguously clarify "
            "WHICH meaning is intended. <code>\"A wooden park bench in a park\"</code> instead of just <code>\"Bank\"</code>.",
            "<b>English image prompts</b> &mdash; Image generation works in English, "
            "the meanings are already stored as English prompts in the knowledge base.",
            "<b>No text hints</b> &mdash; The images must not contain text that reveals the word. "
            "Only the visual representation counts.",
        ],
        "challenges": [
            ("Homonym quality", "Not every homonym is suitable &mdash; both meanings must be "
             "easy to depict as images. <code>Tone</code> (sound vs. clay) is tricky, for example."),
            ("Difficulty level", "The two images must not look too similar "
             "(too easy) nor too different (just guessing)."),
            ("Knowledge base maintenance", "Each entry needs two carefully crafted English "
             "image descriptions &mdash; labor-intensive but necessary for quality."),
        ],
        "learnings": [
            "<b>JSON structure is key</b> &mdash; Each homonym has <code>meaning_a</code> and "
            "<code>meaning_b</code> with a German label and an English image prompt each.",
            "<b>Curation is king</b> &mdash; LLMs can suggest homonyms, but the "
            "final selection and prompt formulation needs human judgment.",
        ],
    },

    "mathe_abstrakt": {
        "icon": "\U0001f522",
        "title": "Math I (Abstract)",
        "what": (
            "Math Memory I trains number understanding through abstract representations. "
            "Card A shows a number (e.g. **5**), Card B shows the corresponding quantity "
            "as abstract shapes (e.g. 5 circles, 5 stars, 5 hearts).\n\n"
            "The user picks a **shape style** (Circles, Stars, Hearts, Dice pips, "
            "Fingers or Surprise). Numbers 1&ndash;10 or 1&ndash;20 are generated automatically."
        ),
        "how": [
            ("1. Choose shape", "The agent offers 6 shape options: Circles, Stars, Hearts, Dice pips, Fingers, Surprise."),
            ("2. Load shape", "<code>load_math_shape()</code> loads the shape definition from <code>math_shapes.json</code>."),
            ("3. Number prompts", "<code>build_number_prompt()</code> creates prompts for number cards (large, clear digit)."),
            ("4. Shape prompts", "<code>build_shapes_prompt()</code> creates prompts for shape cards (N objects, clearly countable)."),
            ("5. Parallel generation", "All cards are generated in parallel via ThreadPoolExecutor."),
        ],
        "prompt_engineering": [
            "<b>Countability</b> &mdash; The shape prompt emphasizes <code>clearly countable, well-spaced</code> &mdash; "
            "shapes must be individually countable, not merging into each other.",
            "<b>Finger special logic</b> &mdash; Numbers 1&ndash;5 show one hand, 6&ndash;10 show two hands. "
            "The prompt explicitly describes <code>left hand 5 fingers + right hand N fingers</code>.",
            "<b>Number clarity</b> &mdash; Number cards emphasize <code>clean standard shape, instantly recognizable</code> "
            "and explicitly forbid decorations that impair readability.",
            "<b>Consistent shapes</b> &mdash; The <code>image_prompt_en</code> from the JSON file defines the "
            "exact appearance of each shape for consistent results.",
            "<b>Layout hints</b> &mdash; <code>_layout_hint(n)</code> provides an explicit "
            "grid arrangement for each number (e.g. <code>3 top row, 2 bottom row</code> for 5), so the AI "
            "arranges the correct count in a structured way instead of randomly.",
            "<b>Dice pip prompts</b> &mdash; <code>_dice_prompt(n)</code> describes exact pip positions "
            "per die face. From 7 onward, multiple dice are shown side by side (e.g. 6+1 for 7).",
            "<b>Tally mark prompts</b> &mdash; <code>_tally_prompt(n)</code> uses the classic system: "
            "4 vertical strokes + 1 diagonal = 5. Groups are displayed separately.",
            "<b>Domino prompts</b> &mdash; <code>_domino_prompt(n)</code> optimally splits the number across two "
            "halves (max 6 per half). From 13 onward, two domino tiles are used.",
        ],
        "challenges": [
            ("Number styling vs. readability", "When a theme is chosen, colors may adapt, "
             "but the digit shape must stay clean. Solved with explicit <code>Do NOT reshape the number</code>."),
            ("Finger representation", "LLMs struggle with correct finger counts. "
             "Solved with very explicit hand descriptions in the prompt."),
            ("Counting high numbers", "With 15+ objects, counting in the image gets difficult. "
             "Row/grid arrangements and generous spacing help."),
        ],
        "learnings": [
            "<b>Shape database over free text</b> &mdash; Predefined shapes with tested "
            "prompt fragments deliver more consistent results than free descriptions.",
            "<b>Negative prompts work</b> &mdash; <code>no borders, no frames, no black edges</code> "
            "prevents unwanted visual artifacts on number cards.",
        ],
    },

    "mathe_konkret": {
        "icon": "\U0001f9ee",
        "title": "Math II (Concrete)",
        "what": (
            "Math Memory II uses **real objects** instead of abstract shapes. "
            "Card A shows a number, Card B shows the corresponding quantity "
            "of real objects (e.g. 3 tennis balls, 7 cupcakes).\n\n"
            "The user picks a **theme** (e.g. Sports, Food, Toys), and the "
            "system generates matching countable objects via LLM. Each number is "
            "paired with a *different* object."
        ),
        "how": [
            ("1. Choose theme", "The agent asks for a theme and explains that it should have countable objects."),
            ("2. Generate objects", "<code>generate_countable_objects()</code> uses Gemini Flash to find N countable objects for the theme."),
            ("3. Number prompts", "<code>build_number_prompt()</code> creates number cards with optional theme-influenced colors."),
            ("4. Object prompts", "<code>build_real_objects_prompt()</code> creates cards with exactly N identical objects."),
            ("5. Generate & pair", "Number 1 &harr; Object A, Number 2 &harr; Object B, etc. Generated in parallel."),
        ],
        "prompt_engineering": [
            "<b>Enforce countable objects</b> &mdash; The content prompt has strict rules: "
            "objects must be discrete, small and individually countable. Elephants or swimming pools are forbidden.",
            "<b>The thing itself, not accessories</b> &mdash; Most important prompt rule: For theme <code>Shoes</code>, "
            "generate shoe types (sneaker, boot), NOT shoe accessories (shoelace, shoe buckle).",
            "<b>Anti-cropping</b> &mdash; Explicit instruction: <code>all objects fully visible and not cropped or "
            "cut off at the edges</code> with <code>generous margin</code> prevents cut-off objects.",
            "<b>Identical objects</b> &mdash; The prompt emphasizes <code>identical</code> and <code>same type</code> &mdash; "
            "5 tennis balls should be 5 identical tennis balls, not 3 tennis balls and 2 soccer balls.",
            "<b>Theme context for ambiguities</b> &mdash; <code>(in the context of {theme})</code> helps the "
            "image generator with ambiguous words (e.g. <code>mouse</code> for Technology vs. Animals).",
            "<b>Layout hints</b> &mdash; Real objects also use <code>build_real_objects_prompt()</code> with "
            "the <code>_layout_hint(n)</code> function for structured grid arrangements, keeping "
            "the exact count clearly countable.",
        ],
        "challenges": [
            ("Object selection quality", "LLMs generated accessories instead of the thing itself "
             "(shoe buckles instead of shoes). Solved with explicit rule and positive/negative examples."),
            ("Object cropping", "With 7+ objects, parts were cut off at image edges. "
             "Solved with <code>generous margin</code> and explicit anti-cropping instruction."),
            ("Number card deformation", "Numbers were thematically deformed (6 looked like a shoe). "
             "Solved with explicit <code>Do NOT reshape the number to look like objects from the theme</code>."),
            ("Black borders", "Some number cards had unwanted black frames. "
             "Solved with <code>no borders, no frames, no black edges</code> in the prompt."),
        ],
        "learnings": [
            "<b>Iterative prompt engineering</b> &mdash; Prompts were improved step by step through "
            "multiple test runs. Each test revealed new edge cases.",
            "<b>Negative instructions are powerful</b> &mdash; Explicit prohibitions (<code>Do NOT reshape</code>, "
            "<code>no borders</code>) often work better than positive instructions alone.",
            "<b>Example-based prompting</b> &mdash; Good and bad examples in the content prompt "
            "massively improve LLM object selection (shoes, beverages).",
        ],
    },

    "i18n": {
        "icon": "\U0001f310",
        "title": "Languages (i18n)",
        "what": (
            "MEMOKI supports multiple languages \u2013 currently **German** and **English**. "
            "The language system (internationalization, short *i18n*) is designed so that "
            "new languages can be added with minimal effort.\n\n"
            "All UI texts, greetings, status messages, and even the "
            "game mode documentation live in separate language files. "
            "The knowledge base (Teapot Memory) is also language-specific: "
            "German homonyms (Bank, Birne, Schloss) and English homonyms "
            "(Bat, Crane, Trunk) are stored in separate JSON files."
        ),
        "how": [
            ("1. Language files", "Each language has its own Python file: "
             "<code>i18n/de.py</code> and <code>i18n/en.py</code> with a "
             "<code>STRINGS</code> dict and a <code>MODE_DATA</code> structure."),
            ("2. t() function", "<code>t(key, **kwargs)</code> returns the string "
             "in the current language. Placeholders are replaced via <code>.format()</code>. "
             "Missing keys return the key itself (for debugging)."),
            ("3. Language switch", "A compact <code>st.pills</code> selector (Deutsch | English) "
             "in the sidebar stores the choice in <code>st.session_state.lang</code>."),
            ("4. Language-specific knowledge base", "<code>load_teekesselchen(count, lang)</code> "
             "automatically loads <code>teekesselchen_{lang}.json</code> \u2013 "
             "with fallback to the German file."),
            ("5. Image prompts stay English", "Regardless of the UI language, all "
             "image prompts in the JSON are English (<code>prompt</code> field), "
             "since image generation works best in English."),
        ],
        "prompt_engineering": [
            "<b>Flat key structure</b> &mdash; All strings use flat, "
            "dot-notated keys like <code>greeting.hello</code>, <code>gen.tk.status</code>. "
            "This avoids nested dicts and makes search/replace easy.",
            "<b>Placeholder convention</b> &mdash; Dynamic values are inserted via "
            "<code>{num_pairs}</code>, <code>{mode_name}</code> etc. "
            "The <code>t()</code> function silently ignores missing placeholders.",
            "<b>Prompt vs. label separation</b> &mdash; In the Teapot Memory JSON, "
            "each entry has three fields: <code>de</code> (German label), "
            "<code>en</code> (English label), and <code>prompt</code> "
            "(detailed image prompt in English).",
            "<b>Agent prompts are language-independent</b> &mdash; The system prompts "
            "for the LLM agent are in English, as the agent always works "
            "internally in English. Only the UI texts are translated.",
        ],
        "challenges": [
            ("Homonyms are language-specific",
             "\"Schloss\" (castle/door lock) has no English equivalent, "
             "\"Bat\" (animal/baseball bat) has no German one. "
             "Solution: Separate JSON files per language instead of one universal file."),
            ("Streamlit version on Cloud",
             "<code>st.pills</code> (compact language selector) requires Streamlit &ge;1.39.0. "
             "Streamlit Cloud installed older versions. "
             "Solution: Pinned <code>requirements.txt</code> to <code>&ge;1.39.0</code>."),
            ("Count consistency",
             "Greeting texts and status messages mention the number of homonyms "
             "(e.g. \"119 homonyms\"). Every time entries are added, "
             "these numbers must be updated in both languages."),
        ],
        "learnings": [
            "<b>Separate knowledge base > translation</b> &mdash; Homonyms cannot be "
            "translated \u2013 they must be curated per language. "
            "The separate JSON structure (<code>teekesselchen_de.json</code> / "
            "<code>teekesselchen_en.json</code>) was the right decision.",
            "<b>Flat strings scale better</b> &mdash; A flat dict with "
            "dot-notated keys is easier to maintain than nested "
            "language trees. New keys can be added quickly.",
            "<b>New language in 3 steps</b> &mdash; (1) Copy and translate a language file, "
            "(2) register it in <code>i18n/__init__.py</code>, "
            "(3) optionally create a language-specific knowledge base. "
            "The system is designed for extensibility.",
        ],
    },
}
