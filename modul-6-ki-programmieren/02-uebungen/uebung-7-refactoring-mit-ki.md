# Übung 7: Refactoring mit KI

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐⭐⭐ Schwer

## 📝 Aufgabe

Lassen Sie Claude Code bestehenden Code aus Modul 3 oder 4 refactoren. Analysieren Sie die Änderungen kritisch und entscheiden Sie, welche Sie übernehmen würden.

### Ausgangslage

In der Datei [`../05-beispiele/refactoring_beispiel.py`](../05-beispiele/refactoring_beispiel.py) finden Sie Code, der funktioniert, aber verbessert werden kann. Alternativ können Sie eigenen Code aus Modul 3 oder 4 verwenden.

### Schritt 1: Code analysieren

Schauen Sie sich den Ausgangscode an und notieren Sie, was Ihnen auffällt:

- Gibt es Wiederholungen?
- Sind die Funktionen zu lang?
- Sind die Variablennamen aussagekräftig?
- Fehlen Kommentare oder Docstrings?

### Schritt 2: KI um Refactoring bitten

Geben Sie den Code an Claude Code mit einem klaren Auftrag:

```
Refactore diesen Code. Verbessere:
- Lesbarkeit und Struktur
- Wiederverwendbarkeit
- Fehlerbehandlung
- Dokumentation (Docstrings und Kommentare)
Behalte die gleiche Funktionalität bei.
```

### Schritt 3: Änderungen analysieren

Füllen Sie die Bewertungstabelle aus:

| Änderung | Was wurde geändert? | Verbessert? | Verschlechtert? | Übernehmen? |
|----------|-------------------|-------------|-----------------|-------------|
| 1 | z.B. Funktion aufgeteilt | Lesbarkeit | - | Ja |
| 2 | z.B. List Comprehension | Kompaktheit | Verständlichkeit | Nein |
| 3 | ... | ... | ... | ... |

## 💡 Reflexionsfragen

- Was hat sich durch das Refactoring verbessert?
- Gibt es Änderungen, die den Code schwerer verständlich machen?
- Würden Sie alle Änderungen übernehmen oder nur bestimmte?
- Hätten Sie das Refactoring selbst so gemacht?

## ✅ Checkliste

- [ ] Ausgangscode analysiert
- [ ] Claude Code um Refactoring gebeten
- [ ] Änderungen in der Tabelle dokumentiert
- [ ] Reflexionsfragen beantwortet
- [ ] Entscheidung getroffen: Was wird übernommen?
