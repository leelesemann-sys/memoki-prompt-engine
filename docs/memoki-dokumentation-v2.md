# MEMOKI – Projekt-Dokumentation v2

**Stand:** 07.02.2026
**Version:** 0.2 (Prompt-Engineering-Phase)

---

## 1. Projektuebersicht

**MEMOKI** ist ein KI-Memory-Spiele-Macher: Eine Streamlit-Web-App, in der User per Chat mit einem KI-Agenten personalisierte Memory-Spiele erstellen. Die Bilder werden in Echtzeit von Google Gemini generiert.

**Lernziele:** LLM-Tuning, Prompt Engineering, Agentenorchestrierung, Web-Entwicklung mit Python.

---

## 2. Spielmodi

| Modus | Key | Kartenstruktur | Wissensbasis |
|-------|-----|---------------|--------------|
| **Klassisches Memory** | `classic` | A = B (identische Bilder) | LLM generiert Objekte |
| **Paare-Memory** | `paare` | A ↔ B (zusammengehoerige Objekte) | `pairs_v2.json` (10 Themen) |
| **Teekesselchen** | `teekesselchen` | A ↔ B (zwei Bedeutungen eines Wortes) | `teekesselchen_v2.json` (130 Eintraege) |
| **Mathe I (Abstrakt)** | `mathe_abstrakt` | Zahl ↔ abstrakte Symbole | `math_shapes.json` (20 Shapes) |
| **Mathe II (Konkret)** | `mathe_konkret` | Zahl ↔ reale Objekte | LLM generiert Objekte |

---

## 3. Architektur

```
llm-semantic-memory/
│
├── app.py                          # Streamlit-Frontend (2-Spalten-Layout, Chat, Spielfeld)
│
├── agents/
│   └── memoki.py                   # MEMOKI Chat-Agent (Gemini 2.5 Flash)
│
├── config/
│   └── settings.py                 # Zentrale Konfig (.env, Model-Strings)
│
├── generators/
│   ├── base.py                     # ImageGenerator ABC
│   └── nano_banana.py              # Gemini-Bildgenerator (3 Pro / 2.5 Flash)
│
├── tools/
│   ├── image.py                    # Bild-Prompt-Builder + generate_card_image()
│   └── content.py                  # Content-Tools (Objekte, Paare, Teekesselchen, Shapes)
│
├── prompts/
│   ├── classic_memory.py           # Prompt-Builder: Classic
│   ├── pairs_memory.py             # Prompt-Builder: Paare (Anti-Halluzination)
│   ├── teekesselchen.py            # Prompt-Builder: Teekesselchen
│   └── math_memory.py              # Prompt-Builder: Mathe I + II (Shapes, Dice, Domino, Tally)
│
├── game/
│   ├── card.py                     # Card Dataclass (pair_id, label, image, is_revealed)
│   ├── deck.py                     # Deck-Builder (5 build_*-Methoden, shuffle)
│   └── session.py                  # GameSession (Spielzustand)
│
├── knowledge/
│   ├── pairs_v2.json               # 10 Themen × ~15 Paare
│   ├── teekesselchen_v2.json       # 130 Homonyme (Deutsch, 2 Bedeutungen pro Wort)
│   └── math_shapes.json            # 20 Shapes in 5 Kategorien
│
└── docs/
    ├── llm-semantic-memory-briefing.md   # Original-Briefing (v1)
    ├── memoki-agent-system-prompt.md     # Agent-System-Prompt-Doku (v1)
    ├── memoki-tool-prompts.md            # Tool-Prompt-Doku (v1)
    ├── memoki-session-report-v2.md       # Session-Bericht v2 (aktuell)
    └── memoki-dokumentation-v2.md        # Diese Datei
```

---

## 4. Tech-Stack

| Komponente | Technologie | Details |
|------------|-------------|---------|
| Frontend | Streamlit | Custom CSS (Nunito Font, Gradient-BG, Mode-Cards) |
| Chat-Agent | Google Gemini 2.5 Flash | System-Prompt, Multi-Turn-Chat |
| Bildgenerierung (Standard) | Google Gemini 3 Pro | `gemini-3-pro-image-preview` |
| Bildgenerierung (Fallback) | Google Gemini 2.5 Flash | `gemini-2.5-flash-image` |
| Sprache | Python 3.12 | Windows, VS Code |
| Config | python-dotenv | `.env` fuer API-Keys |

### Geplant (noch nicht implementiert)
- Azure DALL-E 3 als alternativer Bildgenerator
- Azure AI Search fuer Knowledge-Retrieval
- PDF-Export / Druckvorlage

---

## 5. Datenfluss

```
User waehlt Modus → MEMOKI-Agent (Chat) → sammelt Infos (Thema, Stil, Zielgruppe)
    → Agent gibt JSON-Action-Block aus
    → app.py erkennt Action → startet Generierungs-Pipeline

Generierungs-Pipeline:
    1. Content laden/generieren (JSON oder LLM)
    2. Prompts bauen (modusabhaengig)
    3. Bilder parallel generieren (ThreadPoolExecutor, 5 Workers)
    4. Deck bauen (Card + Deck Klassen)
    5. Spielfeld anzeigen (Memory-Grid mit Flip-Logik)
```

### Agent-Kommunikation

Der MEMOKI-Agent kommuniziert ueber einen JSON-Action-Block:

```json
{"action": "generate", "theme": "Sport", "style": "cartoon", "audience": "children"}
```

Bei Mathe Abstrakt zusaetzlich: `"shape": "dice"` (oder circles, stars, hearts, fingers, surprise)

---

## 6. Prompt-Architektur

### 6.1 Generische Prompts (`tools/image.py`)

Fuer Classic und Teekesselchen:
```
"A {subject}, {style_desc}, {audience_desc}.
 High contrast, ensure the subject stands out clearly against the background.
 Centered on pure white background. No text. Square format."
```

**10 vordefinierte Stile:** cartoon, photorealistic, watercolor, minimalist, artistic, black-and-white, pencil, retro, pixel, comic.
**Custom-Stile:** Werden als Freitext durchgereicht (z.B. "van Gogh post-impressionist style").

### 6.2 Paare-Memory-Prompts (`prompts/pairs_memory.py`)

Spezieller Anti-Halluzinations-Prompt:
```
"A single realistic {object_name_en}, showing the actual real-world object,
 the object must keep its normal real shape –
 do NOT reshape it into an animal, whale, duck, character, or toy,
 do NOT add faces, eyes, or animal features to the object, ..."
```

**Hintergrund:** Gemini hat bei Children-Audience die Tendenz, Objekte in suesse Tierfiguren umzuformen (Wal-Halluzination bei Bad-Thema).

### 6.3 Mathe-Prompts (`prompts/math_memory.py`)

#### Zahlenkarten
```
"A single digit showing only the number {number}, displayed very large and bold..."
```
Mit optionalem Theme-Hint fuer Farben (aber NICHT Form-Aenderung der Ziffer).

#### Standard-Shapes (Kreise, Sterne, Herzen etc.)
```
"Exactly {number} {shape_desc}, {layout_hint}, clearly countable, well-spaced..."
```
Mit expliziten Layout-Hints pro Zahl (z.B. "arranged in 2 rows of 3" fuer 6).

#### Spezial-Shapes

| Shape | Funktion | Besonderheiten |
|-------|----------|----------------|
| **Finger** | Inline-Logik | 1–5: eine Hand, 6–10: zwei Haende |
| **Wuerfelaugen** | `_dice_prompt(n)` | 1–6: ein Wuerfel, 7–12: zwei, 13–18: drei, 19–20: vier. Per-Face-Beschreibung. Count-Check. |
| **Dominosteine** | `_domino_prompt(n)` | 1–12: ein Stein (zwei Haelften, 0–6 Dots), 13–20: zwei Steine. |
| **Strichliste** | `_tally_prompt(n)` | 1–4: einzelne Striche, 5er-Gruppen (4 senkrecht + 1 diagonal). |

#### Reale Objekte (Mathe II)
```
"Exactly {number} identical {plural}, nothing else in the image.
 All {number} objects must be the same type of {object_name}..."
```
Mit Layout-Hints und Theme-Context fuer Mehrdeutigkeiten.

---

## 7. Wissensbasen

### 7.1 `knowledge/pairs_v2.json`

10 Themen mit je ~15 Paaren (Deutsch + Englisch):
Kueche, Buero, Sport, Haushalt, Musik, Garten, Bad, Schule, Verkehr, Tiere.

Struktur:
```json
{"a": {"de": "Topf", "en": "cooking pot"}, "b": {"de": "Deckel", "en": "pot lid"}}
```

### 7.2 `knowledge/teekesselchen_v2.json`

130 deutsche Homonyme mit je 2 visuell darstellbaren Bedeutungen (DE + EN):
```json
{"word": "Bank", "meaning_a": {"de": "Sitzbank", "en": "wooden park bench..."}, "meaning_b": {"de": "Geldinstitut", "en": "bank building..."}}
```

### 7.3 `knowledge/math_shapes.json`

20 Shapes in 5 Kategorien:
- **Geometrisch:** Kreise, Quadrate, Dreiecke, Rauten, Sechsecke
- **Natur:** Sterne, Blumen, Blaetter, Tropfen, Sonnen
- **Objekte:** Herzen, Knoepfe, Muenzen, Edelsteine, Luftballons
- **Haende & Wuerfel:** Finger, Wuerfelaugen, Dominosteine
- **Strichlisten & Bloecke:** Strichliste, Baukloetze

Jeder Shape hat: `id`, `name_de`, `name_en`, `symbol`, `image_prompt_en`, `colors`.
Spezial-Shapes haben `special_handling`.

---

## 8. Frontend

### Layout
- **2-Spalten-Layout:** Links Modus-Auswahl, Rechts Chat + Spielfeld
- **Header-Banner:** MEMOKI-Branding mit Gradient-Titel
- **Mode-Cards:** 5 farbige Karten mit CSS-Hover-Effekten
- **Chat-Interface:** Streamlit chat_message mit Custom-Avatars
- **Memory-Grid:** Responsive Grid mit Flip-Logik (Click → Reveal → Match-Check)

### Spiellogik
- Karten werden als Button (verdeckt) oder Bild (aufgedeckt) gerendert
- Match-Pruefung ueber `pair_id` auf dem `Card`-Objekt
- Nicht-Paare werden beim naechsten Click zurueckgedreht
- Gewonnen-Screen mit Zuege-Zaehler

### Bildgenerierung
- Parallel mit `ThreadPoolExecutor` (5 Worker)
- Fallback: Gemini 3 Pro → Gemini 2.5 Flash
- Fortschrittsanzeige mit `st.progress()`

---

## 9. MEMOKI Chat-Agent

### Modell
Google Gemini 2.5 Flash (`gemini-2.5-flash`) – schnell und guenstig fuer Chat.

### System-Prompt
- Spricht Deutsch mit dem User
- Kennt alle 5 Spielmodi mit Sonderregeln
- Sammelt: Thema, Stil, Zielgruppe (modusabhaengig)
- Gibt JSON-Action-Block aus sobald alle Infos da sind
- Bietet 3–4 Vorschlaege an
- Keine Rueckfragen nach Zusammenfassung

### Sonderregeln pro Modus

| Modus | Thema | Besonderes |
|-------|-------|------------|
| Classic | User waehlt | – |
| Paare | Aus fester Liste (10 Themen) | – |
| Teekesselchen | Kein Thema | Aus Wissensbasis |
| Mathe Abstrakt | Kein Thema | Shape-Stil waehlen |
| Mathe Konkret | User waehlt | Hinweis: zaehlbare Objekte |

---

## 10. Prompt-Engineering-Learnings

### Funktioniert gut
1. **Layout-Hints:** Explizite Anordnungsbeschreibungen ("arranged in 2 rows of 3") verbessern die Zaehlung
2. **Count-Check:** "IMPORTANT: total must be exactly N" als Self-Verification
3. **Anti-Halluzination:** Sowohl positive ("show the actual real-world object") als auch negative ("do NOT reshape") Anweisungen noetig
4. **Per-Number-Prompts:** Spezial-Shapes wie Wuerfel, Domino, Tally brauchen eigene Funktionen mit exakten Beschreibungen pro Zahl
5. **Stil-Durchreichung:** Custom-Stile als Freitext ermoeglichen maximale Flexibilitaet

### Bekannte Schwaechen
1. **Anzahl-Fehler:** Bildgeneratoren haben Schwierigkeiten, exakt N Objekte zu zaehlen (besonders >6)
2. **Children-Halluzination:** Bei Zielgruppe "Kinder" tendieren Modelle dazu, Objekte zu vermenschlichen/vertieren
3. **Stil-Konsistenz:** Ueber ein Deck hinweg kann der Stil variieren (verschiedene API-Calls)

---

## 11. Konfiguration

### Model-Strings (`config/settings.py`)
```python
GOOGLE_CHAT_MODEL = "gemini-2.5-flash"           # Agent-Chat
GOOGLE_IMAGE_MODEL = "gemini-3-pro-image-preview" # Bildgenerierung (Standard)
GOOGLE_IMAGE_MODEL_FAST = "gemini-2.5-flash-image" # Bildgenerierung (Fallback)
```

### Umgebungsvariablen (`.env`)
```
GOOGLE_API_KEY=...   # Google AI Studio API Key
```

---

## 12. Abhaengigkeiten

```
streamlit
google-genai
python-dotenv
pillow
```

---

## 13. Offene Punkte / Roadmap

### Kurzfristig (naechste Sessions)
- [ ] Domino-Prompts testen (1–20)
- [ ] Tally-Prompts testen (1–20)
- [ ] Wuerfel-4-Fix verifizieren
- [ ] Anti-Wal-Fix bei Paare-Memory verifizieren
- [ ] Blocks-Shape implementieren (ggf. eigene Funktion)

### Mittelfristig
- [ ] Azure DALL-E 3 als alternativer Generator
- [ ] Generator-Vergleich (Side-by-Side)
- [ ] PDF-Export / Druckvorlage
- [ ] Paarzahl variabel machen (aktuell fix 10)

### Langfristig
- [ ] Azure AI Search fuer Knowledge-Retrieval
- [ ] Azure Hosting
- [ ] Spielstand speichern
- [ ] Multiplayer
