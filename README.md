# MEMOKI -- AI Memory Game Generator

MEMOKI is an AI-powered Memory card game generator built with Streamlit and Google Gemini. Users chat with an AI agent to describe their desired game, and MEMOKI generates custom card decks with AI-created images -- ready to preview or play directly in the browser.

## Tech Stack

- **Frontend**: Streamlit 1.30+
- **Chat LLM**: Google Gemini 2.5 Flash
- **Image Generation**: Google Gemini 3 Pro (primary) / Gemini 2.5 Flash (fallback)
- **Language**: Python 3.11+

## Game Modes

| Mode | Description |
|------|-------------|
| Classic Memory | Identical image pairs on a freely chosen theme |
| Pairs Memory | Related objects form a pair (e.g. pot & lid) |
| Teekesselchen Memory | Same German word, two different meanings (homophones) |
| Math Memory I (Abstract) | Number card matched to abstract shapes (e.g. 5 & five circles) |
| Math Memory II (Concrete) | Number card matched to real objects (e.g. 5 & five tennis balls) |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/leelesemann-sys/memoki-prompt-engine.git
cd memoki-prompt-engine

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your Google AI Studio API key:
# GOOGLE_API_KEY=your_key_here

# Run the app
streamlit run app.py
```

## Project Structure

```
memoki-prompt-engine/
  app.py                  Main Streamlit application
  app_test.py             Test mode (all cards face-up for QA)
  requirements.txt        Python dependencies
  .env / .env.example     API key configuration

  agents/
    memoki.py             Chat agent (Gemini 2.5 Flash orchestration)

  config/
    settings.py           Centralized configuration (models, keys, defaults)

  game/
    card.py               Card data model
    deck.py               Deck builder (5 build methods, one per mode)
    session.py            Game session state

  generators/
    base.py               Abstract image generator interface
    nano_banana.py        Gemini 3 Pro image generator

  tools/
    content.py            LLM object generation + knowledge base loaders
    image.py              Image prompt builder + generate_card_image()

  prompts/
    classic_memory.py     Classic mode prompt builder
    pairs_memory.py       Pairs mode prompt builder
    teekesselchen.py      Teekesselchen mode prompt builder
    math_memory.py        Math mode prompt builders (numbers, shapes, dice, tally, domino)

  knowledge/
    teekesselchen_v2.json 132 curated German homophones (DE + EN)
    pairs_v2.json         10 themes x 15+ object pairs
    math_shapes.json      20+ shape variations for counting

  pages/
    1_How_It_Works.py     Streamlit info page

  docs/
    architecture.md       Technical architecture documentation
    ...                   Design artifacts and session reports
```

## How It Works

1. **Select a mode** from the sidebar
2. **Chat with MEMOKI** -- the AI agent asks for theme, style, and audience
3. **Cards are generated** in parallel using Gemini image generation
4. **Preview** all cards sorted by pair, or **play** a full Memory game
5. **Download** the generated deck as a ZIP file

For detailed technical documentation, see [docs/architecture.md](docs/architecture.md).

## Configuration

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Google AI Studio API key (required) |

The app reads secrets from `.env` (local) or Streamlit Secrets (cloud deployment).

## License

This project was created by Lee Lesemann as a portfolio project demonstrating prompt engineering, LLM agent orchestration, and multi-modal AI integration.
