# Quiz: Datentypen und Operatoren

**Dauer:** 15 Minuten
**Bestanden:** 7/10 richtig

## 📝 Anleitung

- Beantworten Sie alle Fragen
- Notieren Sie Ihre Antworten
- Vergleichen Sie mit den Lösungen am Ende
- Wiederholen Sie bei weniger als 7 Punkten den Leseauftrag

## Fragen

### 1. Welche Zuweisung erstellt **keinen** gültigen String?

- [ ] A) `name = "Anna"`
- [ ] B) `name = 'Anna'`
- [ ] C) `name = Anna`
- [ ] D) `name = "Hallo Welt"`

### 2. Was gibt folgender Code aus?

```python
vorname = "Max"
nachname = "Muster"
print(vorname + nachname)
```

- [ ] A) `Max Muster`
- [ ] B) `MaxMuster`
- [ ] C) `Max+Muster`
- [ ] D) Fehler

### 3. Was gibt `"Python"[0]` zurück?

- [ ] A) `"Python"`
- [ ] B) `"P"`
- [ ] C) `"y"`
- [ ] D) `0`

### 4. Was gibt `"Hallo"[1:4]` zurück?

- [ ] A) `"Hal"`
- [ ] B) `"all"`
- [ ] C) `"allo"`
- [ ] D) `"llo"`

### 5. Was gibt `"  Hallo  ".strip()` zurück?

- [ ] A) `"  Hallo  "` (unverändert)
- [ ] B) `"Hallo  "`
- [ ] C) `"  Hallo"`
- [ ] D) `"Hallo"`

### 6. Welcher Code nutzt einen **F-String**, um `Ich bin 25 Jahre alt` auszugeben?

```python
alter = 25
```

- [ ] A) `print("Ich bin " + alter + " Jahre alt")`
- [ ] B) `print(f"Ich bin {alter} Jahre alt")`
- [ ] C) `print("Ich bin {alter} Jahre alt")`
- [ ] D) `print("Ich bin", alter, "Jahre alt")`

### 7. Was gibt `5 == 5` zurück?

- [ ] A) `5`
- [ ] B) `True`
- [ ] C) `False`
- [ ] D) `"True"`

### 8. Was gibt `True and False` zurück?

- [ ] A) `True`
- [ ] B) `False`
- [ ] C) `"True and False"`
- [ ] D) Fehler

### 9. Was gibt folgender Code aus?

```python
zahl = "42"
ergebnis = int(zahl) + 8
print(ergebnis)
```

- [ ] A) `"428"`
- [ ] B) `"50"`
- [ ] C) `50`
- [ ] D) Fehler

### 10. Was gibt `input()` zurück?

- [ ] A) Immer eine Zahl
- [ ] B) Immer einen String
- [ ] C) Immer einen Boolean
- [ ] D) Hängt von der Eingabe ab

## Lösungen

<details>
<summary>Klicken für Lösungen</summary>

1. **C** - Ohne Anführungszeichen sucht Python eine Variable namens `Anna` — kein String, sondern `NameError`. A, B und D sind alle gültige Strings (einfache und doppelte Anführungszeichen sind gleichwertig).
2. **B** - `+` verkettet Strings ohne Leerzeichen. Für ein Leerzeichen: `vorname + " " + nachname`.
3. **B** - Index 0 ist das erste Zeichen, also `"P"`.
4. **B** - `[1:4]` bedeutet von Index 1 (inklusive) bis 4 (exklusive): `"all"`.
5. **D** - `.strip()` entfernt Leerzeichen am Anfang und Ende.
6. **B** - F-Strings beginnen mit `f"..."` und erlauben Variablen in `{}`. Option D gibt zwar denselben Text aus, ist aber kein F-String (`print()` mit Komma-getrennten Argumenten). A scheitert (String + Zahl), C zeigt `{alter}` wörtlich.
7. **B** - `==` ist ein Vergleichsoperator und gibt `True` oder `False` zurück.
8. **B** - `and` gibt nur `True` zurück, wenn beide Werte `True` sind.
9. **C** - `int("42")` konvertiert zu `42`, dann `42 + 8 = 50`.
10. **B** - `input()` gibt **immer** einen String zurück, auch wenn eine Zahl eingegeben wird.

</details>

## ✅ Auswertung

- **10/10:** Perfekt! Sie sind bestens vorbereitet! 🎉
- **7-9/10:** Sehr gut! Sie können starten.
- **4-6/10:** Bitte Leseauftrag nochmals durchgehen.
- **0-3/10:** Bitte Leseauftrag gründlich lesen.

**Weiter zu:** [Präsenzunterricht](../01-praxis/)
