# Übung 8: KI-Grenzen testen

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐⭐⭐ Schwer

## 📝 Aufgabe

Stellen Sie Claude Code bewusst **schwierige oder mehrdeutige Aufgaben** und beobachten Sie, wo die KI an ihre Grenzen stösst. Dokumentieren Sie Ihre Erkenntnisse.

### Schritt 1: Vage Prompts testen

Geben Sie Claude Code diese absichtlich unklaren Anweisungen:

| # | Vager Prompt | Beobachtung |
|---|-------------|-------------|
| 1 | "Mach den Code schöner" | Was versteht die KI unter "schöner"? |
| 2 | "Optimiere das" | Optimiert sie Geschwindigkeit? Lesbarkeit? Speicher? |
| 3 | "Was meinst du dazu?" | Kann die KI eine Meinung haben? |

Verwenden Sie als Grundlage den Code aus [`../05-beispiele/ki_grenzen.py`](../05-beispiele/ki_grenzen.py).

### Schritt 2: Widersprüchliche Anforderungen testen

Geben Sie Claude Code Aufgaben mit widersprüchlichen Anforderungen:

```
Schreibe eine Funktion, die möglichst kurz ist UND
ausführlich kommentiert UND für Anfänger verständlich.
```

### Schritt 3: Fachlich anspruchsvolle Fragen stellen

Stellen Sie Fragen, bei denen es keine eindeutige Antwort gibt:

- "Ist mein Code gut genug?"
- "Welche Architektur soll ich verwenden?"
- "Wird dieses Programm in der Praxis funktionieren?"

### Schritt 4: Ergebnisse dokumentieren

| Kategorie | Prompt | KI-Reaktion | Grenzen erkannt? |
|-----------|--------|-------------|-----------------|
| Vage | "Mach es besser" | ... | Ja / Nein |
| Widersprüchlich | "Kurz und ausführlich" | ... | Ja / Nein |
| Subjektiv | "Ist der Code gut?" | ... | Ja / Nein |

## 💡 Erkenntnisse

Typische Grenzen von KI-Assistenten:

- **Vage Anweisungen:** KI trifft eigene Annahmen, die nicht immer passen
- **Fehlender Kontext:** Ohne Projektinformationen fehlt der Bezugsrahmen
- **Subjektive Fragen:** KI kann keine echten Meinungen oder Präferenzen haben
- **Aktualität:** KI-Wissen hat einen Stichtag und kennt neueste Entwicklungen nicht
- **Domänenwissen:** Spezifisches Fachwissen kann fehlen oder veraltet sein

## ✅ Checkliste

- [ ] Mindestens 3 vage Prompts getestet
- [ ] Widersprüchliche Anforderungen getestet
- [ ] Fachlich anspruchsvolle Fragen gestellt
- [ ] Ergebnisse dokumentiert
- [ ] Eigene Erkenntnisse über KI-Grenzen formuliert
