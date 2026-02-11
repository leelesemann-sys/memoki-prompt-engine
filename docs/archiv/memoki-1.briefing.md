# LLM Semantic Memory - Projekt-Briefing für Claude Code

## Projekt-Übersicht

**Projektname:** llm-semantic-memory  
**Zielordner:** `C:\Users\Lee Chr. Lesemann\OneDrive - LL\__dringend_solides 2. Standbein finanziell\_Praxis-Projekte als Referenzarbeiten\llm-semantic-memory`

**Projektziel:**  
Web-App zum Lernen von LLM-Tuning, AI Search-Konfiguration und Agentenorchestrierung. Gleichzeitig Portfolio-Projekt.

**User-Hintergrund:**  
- Azure AI Engineer
- Unerfahren mit Web-App-Entwicklung
- Arbeitet mit Windows, Python 3.11, VS Code

---

## Was die App tun soll

Ein **Memory-Spiel-Generator**, bei dem der User per Chat mit einem LLM den Spielmodus konfiguriert. Das LLM generiert dann die Kartenpaare mit Bildern.

### 4 Spielmodi:

1. **Mathe Memory**  
   - Karte A: Zahl (z.B. "5")  
   - Karte B: Bild mit 5 Objekten/Symbolen

2. **Classic Memory**  
   - Beide Karten zeigen identisches Motiv

3. **Paare Memory**  
   - Zusammengehörige Objekte (z.B. TV & Fernbedienung, Schuh & Schnürsenkel)

4. **Teekesselchen Memory**  
   - Homonyme: 2 Bilder, gleiches Wort (z.B. "Eis" zum Essen + "Eis" im Winter)

---

## Tech-Stack

| Komponente | Technologie |
|------------|-------------|
| Frontend | Streamlit (einfach, Python-basiert) |
| Hosting | Azure |
| Bildgeneratoren | Azure DALL-E 3 + Google Nano Banana Pro |
| Knowledge Base | JSON-Dateien (für Teekesselchen, Paare) |
| Später | Azure AI Search für Retrieval |

### Bildgenerator-Details:

**Azure DALL-E 3:**  
- Über Azure OpenAI Endpoint

**Google Nano Banana Pro:**  
- Model-String: `gemini-3-pro-image-preview`
- Zugang über Google AI Studio API (aistudio.google.com)
- User hat Gemini-Abo (20€/Monat)

---

## Projekt-Struktur (anzulegen)

```
llm-semantic-memory/
│
├── app.py                     # Streamlit Hauptanwendung
├── requirements.txt           # Dependencies
├── .env                       # API Keys (nicht ins Git!)
├── .gitignore
├── README.md
│
├── config/
│   └── settings.py            # Zentrale Konfiguration (Models, Endpoints)
│
├── generators/
│   ├── __init__.py
│   ├── base.py                # Abstract Base Class für Bildgeneratoren
│   ├── dalle.py               # Azure DALL-E 3 Implementierung
│   └── nano_banana.py         # Google Nano Banana Pro Implementierung
│
├── prompts/
│   ├── __init__.py
│   ├── math_memory.py         # Prompt-Logik: Zahl ↔ Menge
│   ├── classic_memory.py      # Prompt-Logik: identische Paare
│   ├── pairs_memory.py        # Prompt-Logik: zusammengehörige Objekte
│   └── teekesselchen.py       # Prompt-Logik: Homonyme
│
├── game/
│   ├── __init__.py
│   ├── card.py                # Card Datenmodell
│   ├── deck.py                # Deck-Generierung & Verwaltung
│   └── session.py             # Spielzustand
│
└── knowledge/
    ├── __init__.py
    ├── homonyme.json          # Wissensbasis: deutsche Teekesselchen
    └── pairs.json             # Wissensbasis: zusammengehörige Objektpaare
```

---

## Logik-Komponenten (zu implementieren)

| Komponente | Verantwortung |
|------------|---------------|
| **ModeSelector** | User wählt Spielmodus (Math/Classic/Pairs/Teekesselchen) |
| **PromptBuilder** | Baut modusabhängig den Bildgenerierungs-Prompt |
| **PairGenerator** | Erzeugt die Kartenpaare (inkl. Abruf aus Knowledge Base) |
| **ImageGenerator** | Interface zu DALL-E / Nano Banana – gibt Bild zurück |
| **CardRenderer** | Zeigt Karten im Frontend (verdeckt/aufgedeckt) |
| **MatchValidator** | Prüft ob 2 aufgedeckte Karten ein Paar sind |
| **GameStateManager** | Verwaltet: Züge, Paare gefunden, Spielende |
| **GeneratorComparator** | (Optional) Side-by-side Vergleich der Bildgeneratoren |

---

## Nächste Schritte

1. **Projekt-Skelett anlegen** (alle Ordner + Dateien mit Docstrings)
2. **API-Verbindungen testen** (DALL-E + Nano Banana)
3. **Ersten Spielmodus implementieren** (vermutlich Classic Memory als einfachsten)

---

## Arbeitsweise

- Beratend, immer nur 1-2 Schritte auf einmal
- User will lernen, nicht nur fertigen Code bekommen
- Fokus auf LLM-Tuning und Prompt Engineering
- Frontend soll minimal bleiben (nicht das Lernziel)
