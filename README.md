# MEMOKI -- AI Memory Game Generator

MEMOKI generates complete, playable Memory card games using generative AI. Users chat with an AI agent to describe their game, and the system produces a full deck of illustrated cards -- with reliably correct image content, exact object counts, and consistent visual style across all cards.

The core challenge: getting generative AI to produce **exactly 7 apples** (not 6, not 8) across 20+ cards in a single session. Anyone who has tried counting tasks with DALL-E or Gemini knows how unreliable this is out of the box. MEMOKI solves this through production-grade prompt engineering.

## What Makes This Project Technically Interesting

### Prompt Engineering That Solves Real Problems

The prompt system is the heart of MEMOKI. The math mode alone (`prompts/math_memory.py`, 320+ lines) contains specialized prompt strategies for:

- **Exact quantity enforcement** -- layout hints force specific grid arrangements ("3 top row, 2 bottom row" for 5 objects) so the model can't silently add or drop items
- **Count verification instructions** -- every prompt includes explicit verification ("IMPORTANT: count all dots -- total must be exactly N, not more, not less")
- **5 distinct rendering strategies** for abstract counting: geometric shapes, dice pip patterns, tally marks, domino tiles, and hand/finger poses -- each with custom prompt logic
- **Anti-morphing constraints** -- Gemini tends to turn inanimate objects into cute characters; the pairs mode prompt explicitly forbids anthropomorphization ("do NOT reshape into an animal, do NOT add faces or eyes")
- **Number card protection** -- themed number cards use constraints to prevent the model from reshaping digits into themed objects

This isn't "generate an image of a cat". It's systematic prompt engineering that makes unreliable AI output reliable and consistent.

### Conversational Agent with Structured Output

The MEMOKI agent (`agents/memoki.py`) orchestrates a guided conversation using Gemini 2.5 Flash:

- Adapts its questions based on the selected game mode (5 different parameter sets)
- Collects theme, art style, and audience through natural conversation
- Outputs a structured JSON action block that triggers the generation pipeline
- No manual form-filling -- the user just chats

### Modular, Production-Ready Architecture

```
User --> Streamlit UI --> MemokiAgent (Gemini Chat)
                              |
                         JSON Action
                              |
              Content Layer (LLM generation or curated knowledge bases)
                              |
                    Mode-specific Prompt Builders
                              |
              Parallel Image Generation (ThreadPoolExecutor, 5 workers)
                  Primary: Gemini 3 Pro | Fallback: Gemini 2.5 Flash
                              |
                     Deck Assembly --> Play or Download
```

- **Clean separation**: agents / prompts / tools / game logic / generators / knowledge bases
- **Abstract generator interface** -- swap image backends without touching game logic
- **Automatic fallback** -- if the primary model (Gemini 3 Pro) fails, falls back to Gemini 2.5 Flash
- **Parallel generation** -- 20-40 images generated concurrently via ThreadPoolExecutor

## Tech Stack

- **Frontend**: Streamlit 1.30+
- **Chat Model**: Google Gemini 2.5 Flash (agent orchestration)
- **Image Model**: Google Gemini 3 Pro (primary) / Gemini 2.5 Flash (fallback)
- **Language**: Python 3.11+
- **Key Libraries**: google-genai, Pillow, python-dotenv

## Game Modes

| Mode | Card A | Card B | Content Source |
|------|--------|--------|----------------|
| **Classic Memory** | Image of object | Identical image | LLM-generated object list |
| **Pairs Memory** | Object A (e.g. pot) | Related object B (e.g. lid) | Curated knowledge base (10 themes, 150+ pairs) |
| **Teekesselchen** | Meaning A of word | Meaning B of same word | Curated knowledge base (132 German homophones) |
| **Math Memory I** | Number (e.g. "5") | 5 abstract shapes | Curated shape definitions (20+ variations) |
| **Math Memory II** | Number (e.g. "5") | 5 real objects | LLM-generated countable objects |

## Quick Start

```bash
git clone https://github.com/leelesemann-sys/memoki-prompt-engine.git
cd memoki-prompt-engine
pip install -r requirements.txt

# Add your Google AI Studio API key
cp .env.example .env
# Edit .env: GOOGLE_API_KEY=your_key_here

streamlit run app.py
```

## Project Structure

```
memoki-prompt-engine/
  app.py                  Streamlit frontend (950 lines) -- UI, game loop, state
  app_test.py             Test/QA mode -- all cards face-up for visual inspection

  agents/
    memoki.py             Conversational agent (Gemini 2.5 Flash, JSON action output)

  prompts/                <-- The core prompt engineering
    math_memory.py        320+ lines: number cards, shapes, dice, tally, domino
    pairs_memory.py       Anti-morphing constraints for object pairs
    teekesselchen.py      Homophone meaning prompts
    classic_memory.py     Standard image prompts

  tools/
    content.py            LLM object generation + knowledge base loaders
    image.py              Style/audience mapping, prompt assembly, image generation

  game/
    card.py               Card data model (pair_id, label, image)
    deck.py               5 deck builders (one per mode), shuffle logic
    session.py            Game state tracking

  generators/
    base.py               Abstract ImageGenerator interface
    nano_banana.py        Gemini 3 Pro implementation

  knowledge/
    teekesselchen_v2.json 132 curated German homophones (DE + EN translations)
    pairs_v2.json         10 themes x 15+ object pairs
    math_shapes.json      20+ shape variations across 5 categories

  config/
    settings.py           API keys, model config, defaults
```

## How It Works

1. **Select a mode** from the sidebar
2. **Chat with MEMOKI** -- the agent asks for theme, style, and audience
3. **Generation pipeline** builds mode-specific prompts and generates images in parallel
4. **Preview** all cards sorted by pair, or **play** a full Memory game in the browser
5. **Download** the complete deck as a ZIP file

For full technical documentation, see [docs/architecture.md](docs/architecture.md).

## Configuration

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Google AI Studio API key (required) |

Reads from `.env` (local) or Streamlit Secrets (cloud deployment).

## Author

Built by [Lee Lesemann](https://github.com/leelesemann-sys) as a portfolio project demonstrating production-grade prompt engineering, LLM agent orchestration, and multi-modal AI integration.
