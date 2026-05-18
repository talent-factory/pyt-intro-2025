# Quiz: Kontrollstrukturen

**Dauer:** 15 Minuten
**Bestanden:** 7/10 richtig

## 📝 Anleitung

- Beantworten Sie alle Fragen
- Notieren Sie Ihre Antworten
- Vergleichen Sie mit den Lösungen am Ende
- Wiederholen Sie bei weniger als 7 Punkten den Leseauftrag

## Fragen

### 1. Was gibt dieser Code aus?

```python
if 10 > 5:
    print("A")
```

- [ ] A) A
- [ ] B) Nichts
- [ ] C) 10
- [ ] D) Fehler

### 2. Welcher Operator prüft auf Gleichheit?

- [ ] A) `=`
- [ ] B) `==`
- [ ] C) `!=`
- [ ] D) `<>`

### 3. Was gibt folgender Code aus?

```python
alter = 16
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

- [ ] A) Volljährig
- [ ] B) Minderjährig
- [ ] C) Beides
- [ ] D) Nichts

### 4. Wofür verwendet man `elif`?

- [ ] A) Für eine weitere Bedingung nach `if`
- [ ] B) Um eine Schleife zu beenden
- [ ] C) Um eine Funktion zu definieren
- [ ] D) Um einen Fehler abzufangen

### 5. Wie oft wird folgende Schleife ausgeführt?

```python
zaehler = 0
while zaehler < 3:
    print(zaehler)
    zaehler += 1
```

- [ ] A) 2 Mal
- [ ] B) 3 Mal
- [ ] C) 4 Mal
- [ ] D) Endlos

### 6. Was gibt `for i in range(5):` zurück?

- [ ] A) Die Zahlen 1, 2, 3, 4, 5
- [ ] B) Die Zahlen 0, 1, 2, 3, 4
- [ ] C) Die Zahlen 0, 1, 2, 3, 4, 5
- [ ] D) Nur die Zahl 5

### 7. Was macht `break` in einer Schleife?

- [ ] A) Überspringt eine Iteration
- [ ] B) Beendet die Schleife vorzeitig
- [ ] C) Startet die Schleife neu
- [ ] D) Pausiert die Schleife

### 8. Was gibt folgender Code aus?

```python
namen = ["Anna", "Max", "Lisa"]
for name in namen:
    print(name)
```

- [ ] A) `namen`
- [ ] B) `Anna Max Lisa` in einer Zeile
- [ ] C) `Anna`, `Max`, `Lisa` in drei Zeilen
- [ ] D) `["Anna", "Max", "Lisa"]`

### 9. Was ist in Python besonders wichtig bei Kontrollstrukturen?

- [ ] A) Semikolons am Zeilenende
- [ ] B) Geschweifte Klammern `{}`
- [ ] C) Die korrekte Einrückung (Indentation)
- [ ] D) Grossbuchstaben

### 10. Was macht `continue` in einer Schleife?

- [ ] A) Beendet die Schleife
- [ ] B) Springt zur nächsten Iteration
- [ ] C) Wiederholt die aktuelle Iteration
- [ ] D) Gibt einen Wert zurück

## Lösungen

<details>
<summary>Klicken für Lösungen</summary>

1. **A** - A (die Bedingung `10 > 5` ist wahr)
2. **B** - `==` (`=` ist Zuweisung, `==` ist Vergleich)
3. **B** - Minderjährig (16 ist nicht `>= 18`)
4. **A** - Für eine weitere Bedingung nach `if`
5. **B** - 3 Mal (Werte 0, 1, 2)
6. **B** - Die Zahlen 0, 1, 2, 3, 4 (`range(5)` startet bei 0, endet vor 5)
7. **B** - Beendet die Schleife vorzeitig
8. **C** - `Anna`, `Max`, `Lisa` in drei Zeilen
9. **C** - Die korrekte Einrückung (Indentation)
10. **B** - Springt zur nächsten Iteration

</details>

## ✅ Auswertung

- **10/10:** Perfekt! Sie sind bestens vorbereitet! 🎉
- **7-9/10:** Sehr gut! Sie können starten.
- **4-6/10:** Bitte Leseauftrag nochmals durchgehen.
- **0-3/10:** Bitte Leseauftrag gründlich lesen.

**Weiter zu:** [Präsenzunterricht](../01-praxis/)
