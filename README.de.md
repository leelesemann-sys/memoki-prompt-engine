# MEMOKI -- KI Memory-Spiel-Generator

> **Sprache:** [English](README.md) | Deutsch

**[▶ Live-Demo](https://memoki-prompt-engine.streamlit.app/)**

MEMOKI generiert vollständige, spielbare Memory-Kartenspiele mit generativer KI. Nutzer chatten mit einem KI-Agenten, um ihr Spiel zu beschreiben, und das System produziert ein komplettes Kartendeck mit illustrierten Karten -- mit zuverlässig korrektem Bildinhalt, exakten Objektanzahlen und konsistentem visuellen Stil über alle Karten hinweg.

**Zweisprachig** (Deutsch/Englisch) mit sprachspezifischen Wissensdatenbanken und einem vollständigen i18n-System.

Die zentrale Herausforderung: generative KI dazu zu bringen, **exakt 7 Äpfel** zu produzieren (nicht 6, nicht 8) über 20+ Karten in einer einzigen Sitzung. Jeder, der Zählaufgaben mit DALL-E oder Gemini ausprobiert hat, weiß, wie unzuverlässig das standardmäßig ist. MEMOKI löst dies durch produktionsreifes Prompt Engineering.

## Was dieses Projekt technisch interessant macht

### Prompt Engineering, das echte Probleme löst

Das Prompt-System ist das Herzstück von MEMOKI. Allein der Mathe-Modus (`prompts/math_memory.py`, 320+ Zeilen) enthält spezialisierte Prompt-Strategien für:

- **Exakte Mengenerzwingung** -- Layout-Hinweise erzwingen bestimmte Rasteranordnungen ("3 obere Reihe, 2 untere Reihe" für 5 Objekte), sodass das Modell nicht stillschweigend Elemente hinzufügen oder weglassen kann
- **Zählverifizierungsanweisungen** -- jeder Prompt enthält explizite Verifizierung ("WICHTIG: zähle alle Punkte -- Summe muss exakt N sein, nicht mehr, nicht weniger")
- **5 verschiedene Darstellungsstrategien** für abstraktes Zählen: geometrische Formen, Würfelaugen-Muster, Strichlisten, Dominosteine und Hand-/Fingerposen -- jeweils mit eigener Prompt-Logik
- **Anti-Morphing-Einschränkungen** -- Gemini neigt dazu, unbelebte Objekte in niedliche Figuren zu verwandeln; der Paare-Modus-Prompt verbietet explizit Vermenschlichung ("NICHT in ein Tier umformen, KEINE Gesichter oder Augen hinzufügen")
- **Zahlenkartenschutz** -- thematische Zahlenkarten verwenden Einschränkungen, um zu verhindern, dass das Modell Ziffern in thematische Objekte umformt

Das ist kein "generiere ein Bild von einer Katze". Es ist systematisches Prompt Engineering, das unzuverlässige KI-Ausgaben zuverlässig und konsistent macht.

### Konversationsagent mit strukturierter Ausgabe

Der MEMOKI-Agent (`agents/memoki.py`) orchestriert ein geführtes Gespräch mit Gemini 2.5 Flash:

- Passt seine Fragen basierend auf dem gewählten Spielmodus an (5 verschiedene Parameter-Sets)
- Sammelt Thema, Kunststil und Zielgruppe durch natürliche Konversation
- Gibt einen strukturierten JSON-Aktionsblock aus, der die Generierungs-Pipeline auslöst
- Kein manuelles Formularausfüllen -- der Nutzer chattet einfach

### Modulare, produktionsreife Architektur

```
User --> Streamlit UI --> MemokiAgent (Gemini Chat)
                              |
                         JSON Action
                              |
              Content Layer (LLM-Generierung oder kuratierte Wissensdatenbanken)
                              |
                    Modus-spezifische Prompt Builder
                              |
              Parallele Bildgenerierung (ThreadPoolExecutor, 5 Worker)
                  Primär: Gemini 3 Pro | Fallback: Gemini 2.5 Flash
                              |
                     Deck-Zusammenstellung --> Spielen oder Herunterladen
```

- **Saubere Trennung**: agents / prompts / tools / game logic / generators / knowledge bases / i18n
- **Abstraktes Generator-Interface** -- Bild-Backends austauschen ohne Spiellogik anzufassen
- **Automatischer Fallback** -- wenn das primäre Modell (Gemini 3 Pro) fehlschlägt, Rückfall auf Gemini 2.5 Flash
- **Parallele Generierung** -- 20-40 Bilder gleichzeitig generiert via ThreadPoolExecutor
- **Vollständiges i18n** -- zweisprachige UI mit sprachspezifischen Homonym-Wissensdatenbanken

## Tech Stack

- **Frontend**: Streamlit 1.39+
- **Chat-Modell**: Google Gemini 2.5 Flash (Agenten-Orchestrierung)
- **Bildmodell**: Google Gemini 3 Pro (primär) / Gemini 2.5 Flash (Fallback)
- **Sprache**: Python 3.11+
- **i18n**: Deutsch & Englisch (erweiterbar)
- **Wichtige Bibliotheken**: google-genai, Pillow, python-dotenv

## Spielmodi

| Modus | Karte A | Karte B | Inhaltsquelle |
|-------|---------|---------|---------------|
| **Klassisches Memory** | Bild eines Objekts | Identisches Bild | LLM-generierte Objektliste |
| **Paare-Memory** | Objekt A (z.B. Topf) | Verwandtes Objekt B (z.B. Deckel) | Kuratierte Wissensdatenbank (10 Themen, 150+ Paare) |
| **Teekesselchen-Memory** | Bedeutung A eines Wortes | Bedeutung B desselben Wortes | Kuratierte Wissensdatenbank (DE: 130 Homonyme, EN: 119 Homonyme) |
| **Mathe-Memory I** | Zahl (z.B. "5") | 5 abstrakte Formen | Kuratierte Formdefinitionen (20+ Variationen) |
| **Mathe-Memory II** | Zahl (z.B. "5") | 5 reale Objekte | LLM-generierte zählbare Objekte |

## Schnellstart

```bash
git clone https://github.com/leelesemann-sys/memoki-prompt-engine.git
cd memoki-prompt-engine
pip install -r requirements.txt

# Google AI Studio API-Schlüssel hinzufügen
cp .env.example .env
# .env bearbeiten: GOOGLE_API_KEY=your_key_here

streamlit run app.py
```

## Projektstruktur

```
memoki-prompt-engine/
  app.py                  Streamlit Frontend (950 Zeilen) -- UI, Spielschleife, State
  app_test.py             Test/QA-Modus -- alle Karten aufgedeckt zur visuellen Prüfung

  agents/
    memoki.py             Konversationsagent (Gemini 2.5 Flash, JSON-Aktionsausgabe)

  prompts/                <-- Das Kern-Prompt-Engineering
    math_memory.py        320+ Zeilen: Zahlenkarten, Formen, Würfel, Strichlisten, Domino
    pairs_memory.py       Anti-Morphing-Einschränkungen für Objektpaare
    teekesselchen.py      Homophon-Bedeutungsprompts
    classic_memory.py     Standard-Bildprompts

  tools/
    content.py            LLM-Objektgenerierung + Wissensdatenbank-Loader
    image.py              Stil/Zielgruppen-Mapping, Prompt-Zusammenstellung, Bildgenerierung

  game/
    card.py               Karten-Datenmodell (pair_id, label, image)
    deck.py               5 Deck-Builder (einer pro Modus), Mischlogik
    session.py            Spielstatus-Tracking

  generators/
    base.py               Abstraktes ImageGenerator Interface
    nano_banana.py        Gemini 3 Pro Implementierung

  knowledge/
    teekesselchen_de.json 130 kuratierte deutsche Homonyme
    teekesselchen_en.json 119 kuratierte englische Homonyme
    pairs_v2.json         10 Themen x 15+ Objektpaare
    math_shapes.json      20+ Formvariationen in 5 Kategorien

  i18n/
    __init__.py           Sprachregistrierung, t() Hilfsfunktion
    de.py                 Deutsche Strings + How-It-Works-Inhalte
    en.py                 Englische Strings + How-It-Works-Inhalte

  config/
    settings.py           API-Schlüssel, Modellkonfiguration, Standardwerte

  pages/
    1_How_It_Works.py     Interaktive Dokumentation (7 Modus-Seiten + Architektur)
```

## So funktioniert es

1. **Sprache wählen** (Deutsch / English) in der Seitenleiste
2. **Modus auswählen** in der Seitenleiste
3. **Mit MEMOKI chatten** -- der Agent fragt nach Thema, Stil und Zielgruppe
4. **Generierungs-Pipeline** erstellt modusspezifische Prompts und generiert Bilder parallel
5. **Vorschau** aller Karten sortiert nach Paar, oder ein vollständiges Memory-Spiel im Browser **spielen**
6. **Herunterladen** des kompletten Decks als ZIP-Datei

Die vollständige technische Dokumentation finden Sie unter [docs/architecture.md](docs/architecture.md).

## Konfiguration

| Variable | Beschreibung |
|----------|-------------|
| `GOOGLE_API_KEY` | Google AI Studio API-Schlüssel (erforderlich) |

Liest aus `.env` (lokal) oder Streamlit Secrets (Cloud-Deployment).

## Autor

Erstellt von [Lee Lesemann](https://github.com/leelesemann-sys) als Portfolio-Projekt zur Demonstration von produktionsreifem Prompt Engineering, LLM-Agenten-Orchestrierung und multimodaler KI-Integration.
