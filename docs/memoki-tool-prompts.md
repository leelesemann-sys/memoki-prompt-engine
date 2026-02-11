# MEMOKI Tool Prompts (Few-Shot)

---

## 1. generate_objects

**Zweck:** Generiert zählbare Objekte für Mathe Konkret Memory

```python
GENERATE_OBJECTS_PROMPT = """
Du generierst eine Liste von Objekten, die sich gut zählen und als Bild darstellen lassen.

AUFGABE:
Generiere {count} verschiedene, konkrete Objekte zum Thema "{theme}".
Die Objekte sollen für {audience} geeignet sein.

ANFORDERUNGEN:
- Objekte müssen visuell klar unterscheidbar sein
- Objekte müssen sich gut zählen lassen (keine abstrakten Konzepte)
- Objekte müssen als {style} darstellbar sein
- Jedes Objekt nur einmal verwenden

GUTE BEISPIELE:

Thema: "Tiere", Zielgruppe: "Kinder"
→ ["cat", "elephant", "fish", "rabbit", "butterfly", "dog", "horse", "bird", "frog", "turtle"]

Thema: "Essen", Zielgruppe: "Erwachsene"  
→ ["apple", "croissant", "sushi roll", "pizza slice", "cupcake", "pretzel", "taco", "donut", "grape bunch", "cheese wheel"]

Thema: "Fahrzeuge", Zielgruppe: "Kinder"
→ ["car", "airplane", "boat", "bicycle", "train", "helicopter", "bus", "motorcycle", "rocket", "tractor"]

SCHLECHTE BEISPIELE (vermeide):
- "love", "happiness" ← abstrakt, nicht zählbar
- "water", "sand" ← Masse, nicht einzeln zählbar
- "car" und "automobile" ← Duplikate/Synonyme
- "microscopic bacteria" ← nicht klar darstellbar

AUSGABE:
Antworte NUR mit einem JSON-Array von Strings, keine Erklärung.
["object1", "object2", ...]
"""
```

---

## 2. generate_pairs

**Zweck:** Generiert zusammengehörige Objektpaare für Paare Memory

```python
GENERATE_PAIRS_PROMPT = """
Du generierst Paare von Objekten, die logisch zusammengehören.

AUFGABE:
Generiere {count} Paare von zusammengehörigen Objekten zum Thema "{theme}".
Die Objekte sollen für {audience} geeignet sein.

ARTEN VON GUTEN PAAREN:
1. Objekt + Zubehör: (Kamera, Stativ), (Gitarre, Plektrum)
2. Objekt + Behälter: (Brief, Briefumschlag), (Wein, Weinglas)
3. Gerät + Energiequelle: (Taschenlampe, Batterie), (Auto, Tankstelle)
4. Werkzeug + Material: (Pinsel, Farbe), (Nadel, Faden)
5. Schutz + Geschütztes: (Regenschirm, Person im Regen), (Helm, Kopf)

GUTE BEISPIELE:

Thema: "Haushalt"
→ [
    {"a": "key", "b": "lock"},
    {"a": "toothbrush", "b": "toothpaste"},
    {"a": "pot", "b": "lid"},
    {"a": "broom", "b": "dustpan"},
    {"a": "lamp", "b": "light bulb"}
  ]

Thema: "Büro"
→ [
    {"a": "pen", "b": "paper"},
    {"a": "stapler", "b": "staples"},
    {"a": "computer", "b": "mouse"},
    {"a": "envelope", "b": "stamp"},
    {"a": "scissors", "b": "tape"}
  ]

Thema: "Sport"
→ [
    {"a": "tennis racket", "b": "tennis ball"},
    {"a": "bow", "b": "arrow"},
    {"a": "golf club", "b": "golf ball"},
    {"a": "fishing rod", "b": "fish hook"},
    {"a": "ski", "b": "ski pole"}
  ]

SCHLECHTE BEISPIELE (vermeide):
- {"a": "dog", "b": "cat"} ← keine logische Zugehörigkeit, nur gleiche Kategorie
- {"a": "car", "b": "bus"} ← beide sind Fahrzeuge, aber gehören nicht zusammen
- {"a": "sun", "b": "moon"} ← Gegensätze, aber keine funktionale Verbindung
- {"a": "apple", "b": "banana"} ← gleiche Kategorie, keine Zugehörigkeit

AUSGABE:
Antworte NUR mit einem JSON-Array, keine Erklärung.
[{"a": "object_a", "b": "object_b"}, ...]
"""
```

---

## 3. get_homonymes

**Zweck:** Generiert Teekesselchen (Homonyme) für Teekesselchen Memory

```python
GET_HOMONYMES_PROMPT = """
Du generierst deutsche Teekesselchen (Homonyme): Wörter mit mehreren, völlig unterschiedlichen Bedeutungen.

AUFGABE:
Generiere {count} deutsche Teekesselchen.
Beide Bedeutungen müssen sich gut als Bild darstellen lassen.

WAS IST EIN GUTES TEEKESSELCHEN:
- GLEICHES Wort, VERSCHIEDENE Bedeutungen
- Beide Bedeutungen sind visuell darstellbar
- Bedeutungen kommen aus unterschiedlichen Kontexten

GUTE BEISPIELE:

[
  {
    "word": "Bank",
    "meaning_a": "wooden park bench for sitting",
    "meaning_b": "financial institution building"
  },
  {
    "word": "Eis", 
    "meaning_a": "ice cream cone with scoops",
    "meaning_b": "frozen ice on a winter lake"
  },
  {
    "word": "Birne",
    "meaning_a": "pear fruit on a tree",
    "meaning_b": "glowing light bulb"
  },
  {
    "word": "Hahn",
    "meaning_a": "rooster on a farm",
    "meaning_b": "water faucet in a kitchen"
  },
  {
    "word": "Schloss",
    "meaning_a": "door lock with keyhole",
    "meaning_b": "fairy tale castle palace"
  },
  {
    "word": "Ton",
    "meaning_a": "musical note or sound wave",
    "meaning_b": "clay pottery material"
  },
  {
    "word": "Ball",
    "meaning_a": "round sports ball",
    "meaning_b": "elegant dance ball event"
  },
  {
    "word": "Blatt",
    "meaning_a": "green leaf on a tree",
    "meaning_b": "sheet of paper"
  },
  {
    "word": "Decke",
    "meaning_a": "cozy blanket on a bed",
    "meaning_b": "ceiling of a room"
  },
  {
    "word": "Fliege",
    "meaning_a": "flying insect",
    "meaning_b": "bow tie for formal wear"
  }
]

SCHLECHTE BEISPIELE (vermeide):
- "laufen" / "rennen" ← Synonyme, NICHT Homonyme
- "Bank" nur als Sitzbank ← zweite Bedeutung fehlt
- "cool" (englisch slang) ← Fremdwort, kein deutsches Homonym
- "Liebe" ← abstrakt, schwer als Bild darstellbar
- "Tau" (Morgentau / Schiffstau) ← Schiffstau schwer erkennbar als Bild

AUSGABE:
Antworte NUR mit einem JSON-Array, keine Erklärung.
[{"word": "...", "meaning_a": "... (English description for image prompt)", "meaning_b": "..."}, ...]
"""
```

---

## 4. generate_image

**Zweck:** Baut den finalen Prompt für DALL-E / Nano Banana

```python
GENERATE_IMAGE_PROMPT = """
Du erstellst präzise Bild-Prompts für Memory-Spielkarten.

AUFGABE:
Erstelle einen Bild-Prompt für: "{subject}"
Stil: {style}
Zielgruppe: {audience}

ANFORDERUNGEN AN MEMORY-KARTEN:
- Weißer oder einfarbiger Hintergrund
- Objekt zentriert und klar erkennbar
- Kein Text im Bild
- Konsistenter Stil über alle Karten
- Quadratisches Format optimiert

STIL-ÜBERSETZUNGEN:

"foto-realistisch" → "photorealistic, high detail, professional photography, soft studio lighting"
"Zeichentrick" → "cartoon style, bold outlines, vibrant colors, Disney-Pixar inspired"
"künstlerisch" → "artistic, painterly, impressionist style, soft brushstrokes"
"minimalistisch" → "minimalist, simple shapes, flat design, limited color palette"
"Aquarell" → "watercolor painting, soft edges, pastel colors, artistic"

ZIELGRUPPEN-ANPASSUNG:

"Kinder" → "cute, friendly, rounded shapes, bright cheerful colors, non-threatening"
"Teenager" → "cool, modern, dynamic, trendy aesthetic"
"Erwachsene" → "sophisticated, elegant, refined details"

GUTE PROMPT-BEISPIELE:

Subject: "elephant", Style: "Zeichentrick", Audience: "Kinder"
→ "A cute cartoon elephant, Disney-Pixar inspired style, friendly expression, big eyes, rounded shapes, bright cheerful colors. Centered on pure white background. No text. Square format."

Subject: "coffee cup", Style: "foto-realistisch", Audience: "Erwachsene"  
→ "A photorealistic coffee cup with steam rising, professional product photography, soft studio lighting, elegant and sophisticated. Centered on pure white background. No text. Square format."

Subject: "the number 5", Style: "Zeichentrick", Audience: "Kinder"
→ "The number 5 as a large, bold, friendly cartoon digit, bright blue color, cute face on the number, cheerful style. Centered on pure white background. No text except the number. Square format."

Subject: "exactly 5 red apples arranged in a row", Style: "Zeichentrick", Audience: "Kinder"
→ "Exactly 5 red cartoon apples arranged in a clear horizontal row, easy to count, cute style with small highlights, bright colors. Centered on pure white background. No text. Square format."

SCHLECHTE PROMPTS (vermeide):
- "an elephant" ← zu vage, kein Stil, kein Hintergrund definiert
- "beautiful amazing incredible elephant" ← Füllwörter ohne Mehrwert
- "elephant with text saying ELEPHANT" ← kein Text im Bild!
- "elephant in a jungle scene" ← zu komplexer Hintergrund

AUSGABE:
Antworte NUR mit dem fertigen Prompt-String, keine Erklärung.
"""
```

---

## 5. Bonus: validate_pair (für Spiellogik)

**Zweck:** Prüft ob zwei aufgedeckte Karten ein gültiges Paar sind

```python
VALIDATE_PAIR_PROMPT = """
Du prüfst, ob zwei Memory-Karten ein gültiges Paar bilden.

SPIELMODUS: {game_mode}

REGELN JE MODUS:

mathe_abstrakt:
- Karte A zeigt Zahl N
- Karte B zeigt N geometrische Formen
- Paar wenn: Zahl = Anzahl Formen

mathe_konkret:
- Karte A zeigt Zahl N  
- Karte B zeigt N Objekte
- Paar wenn: Zahl = Anzahl Objekte

classic:
- Beide Karten zeigen identisches Motiv
- Paar wenn: gleiches Motiv

paare:
- Karte A zeigt Objekt X
- Karte B zeigt zugehöriges Objekt Y
- Paar wenn: X und Y gehören logisch zusammen (aus pair_definition)

teekesselchen:
- Karte A zeigt Bedeutung 1 von Wort W
- Karte B zeigt Bedeutung 2 von Wort W
- Paar wenn: beide Karten gehören zum selben Homonym

EINGABE:
card_a: {card_a_id}
card_b: {card_b_id}
pair_definitions: {pair_definitions}

AUSGABE:
{"is_match": true/false, "pair_id": "..." oder null}
"""
```

---

## Zusammenfassung

| Tool | Few-Shot | Komplexität |
|------|----------|-------------|
| generate_objects | ✅ 3 Beispiele + Anti-Patterns | Mittel |
| generate_pairs | ✅ 3 Beispiele + 5 Paar-Typen | Hoch |
| get_homonymes | ✅ 10 Beispiele + Anti-Patterns | Hoch |
| generate_image | ✅ 4 Beispiele + Stil-Mapping | Mittel |
| validate_pair | ✅ Regel-basiert | Niedrig |
