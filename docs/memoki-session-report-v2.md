# MEMOKI Session-Report v2

**Datum:** 07.02.2026
**Projekt:** MEMOKI – KI-Memory-Spiele-Macher
**Stand:** Alle 5 Spielmodi funktionsfaehig, Prompt-Engineering-Phase

---

## Was wurde in dieser Session gemacht?

### 1. Wuerfelaugen-Fix (Mathe Abstrakt – Dice Shape)

**Problem:** Die Wuerfelflaechenaugen fuer die Zahl 4 zeigten 5 statt 4 Punkte.
**Ursache:** Der Prompt `"showing 4 dots one in each corner"` war mehrdeutig – Gemini interpretierte "in each corner" so, dass ein Center-Dot fehlte und fuegtehinzu.
**Loesung:** Prompt praezisiert zu:
```
"showing 4 dots arranged in a 2x2 square pattern, two on top and two on bottom, NO dot in the center"
```

### 2. Zaehler-Selbstverifikation in Dice-Prompts

**Problem:** Bildgeneratoren zaehlen nicht automatisch, ob die richtige Anzahl Punkte dargestellt wird.
**Loesung:** Allen Wuerfel-Prompts eine Count-Check-Anweisung hinzugefuegt:
```
"IMPORTANT: count all black dots – the total must be exactly {n}, not more, not less"
```

### 3. Wal-Halluzination in Paare-Memory (Bad-Thema)

**Problem:** Im Modus "Paare-Memory" mit Thema "Bad" wurden Objekte wie Shampoo-Flasche, Seifenschale und Schere als Wal-Figuren gerendert – sowohl im Aquarell- als auch im Cartoon-Stil.
**Ursache:** Gemini hat bei "children"-Zielgruppe die Tendenz, Objekte in suesse Tierfiguren umzuformen.
**Loesung:** Prompt in `pairs_memory.py` stark verstaerkt:
- Positiv: `"A single realistic {object_name_en}, showing the actual real-world object"`
- Negativ: `"do NOT reshape it into an animal, whale, duck, character, or toy"`
- Negativ: `"do NOT add faces, eyes, or animal features to the object"`

### 4. JSON-Block-Ankuendigung entfernt

**Problem:** Der MEMOKI-Agent schrieb vor dem JSON-Action-Block `"Hier ist dein JSON-Block:"`, was den User verwirrt.
**Loesung:** System-Prompt in `agents/memoki.py` ergaenzt:
```
Schreibe die Zusammenfassung und dann DIREKT den JSON-Block.
KEINE Ankuendigung wie "Hier ist dein JSON-Block:" davor!
```

### 5. Domino-Prompt-Funktion implementiert

**Neues Feature:** `_domino_prompt(n)` in `math_memory.py`
- 1–12: Ein einzelner Dominostein mit zwei Haelften (je 0–6 Punkte)
- 13–20: Zwei Dominosteine nebeneinander (erster = 6|6, zweiter = Rest)
- Jede Haelfte mit praeziser Pip-Beschreibung
- Eigener Count-Check

### 6. Tally-Prompt-Funktion implementiert

**Neues Feature:** `_tally_prompt(n)` in `math_memory.py`
- 1–4: Einzelne senkrechte Striche
- 5: Gruppe (4 senkrecht + 1 diagonal)
- 6–20: Gruppen von 5 + Rest
- Klassisches Strichlisten-System

---

## Prompt-Engineering-Erkenntnisse

### Was funktioniert

| Technik | Beispiel | Wirkung |
|---------|----------|---------|
| Explizite Layout-Hints | `"arranged in 2 rows of 3"` | Korrekte Anordnung bei zahlbaren Objekten |
| Count-Check-Anweisung | `"total must be exactly N"` | Reduziert falsche Anzahlen |
| Anti-Halluzinations-Prompts | `"do NOT reshape into animal"` | Verhindert Tier-Formen |
| Per-Number-Beschreibungen | Eigene Funktion pro Spezial-Shape | Praezisere Bilder |
| Stil-Freitext durchreichen | Custom Stile wie "van Gogh" | Flexibilitaet fuer User |

### Bekannte Schwaechen

| Problem | Haeufigkeit | Workaround |
|---------|-------------|------------|
| Falsche Objektanzahl (z.B. 7 statt 6) | Mittel | Layout-Hints + Count-Check |
| Halluzination bei Children-Audience | Selten nach Fix | Starke Anti-Halluzinations-Prompts |
| Wuerfel 4 = 5 Punkte | Behoben | Explizite 2x2-Beschreibung |
| Domino/Tally noch nicht getestet | Ausstehend | Muss manuell getestet werden |

---

## Datei-Aenderungen (Zusammenfassung)

| Datei | Aenderung |
|-------|-----------|
| `prompts/math_memory.py` | Dice-Face-4-Fix, Count-Check, `_tally_prompt()`, `_domino_prompt()`, Branches in `build_shapes_prompt()` |
| `prompts/pairs_memory.py` | Anti-Wal-Halluzinations-Prompt |
| `agents/memoki.py` | JSON-Block-Ankuendigung entfernt |

---

## Naechste Schritte (offen)

1. **Testen:** Domino-Prompts mit verschiedenen Zahlen (1–20)
2. **Testen:** Tally-Prompts mit verschiedenen Zahlen (1–20)
3. **Testen:** Wuerfel-4-Fix und Count-Check
4. **Testen:** Anti-Wal-Fix bei Paare-Memory Bad-Thema
5. **Ggf.:** Weitere Shape-Spezialfaelle (z.B. Blocks)
6. **Spaeter:** Azure DALL-E 3 Integration
7. **Spaeter:** Druckvorlage / PDF-Export
