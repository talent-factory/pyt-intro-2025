# Quiz Modul 2: Datentypen und Operatoren

**Zeitaufwand:** 15-20 Minuten  
**Bestehensgrenze:** 7 von 10 Punkten

## 📝 Anleitung

- Beantworten Sie alle Fragen
- Notieren Sie Ihre Antworten
- Vergleichen Sie mit den Lösungen am Ende
- Wiederholen Sie bei weniger als 7 Punkten den Leseauftrag

---

## Frage 1: String-Erstellung (1 Punkt)

Welche der folgenden Zeilen erstellt einen gültigen String?

A) `name = Anna`  
B) `name = "Anna"`  
C) `name = 'Anna'`  
D) Nur B ist korrekt  
E) B und C sind korrekt

---

## Frage 2: String-Konkatenation (1 Punkt)

Was gibt folgender Code aus?

```python
vorname = "Max"
nachname = "Muster"
print(vorname + nachname)
```

A) `Max Muster`  
B) `MaxMuster`  
C) `Max+Muster`  
D) Fehler

---

## Frage 3: String-Indexierung (1 Punkt)

Was gibt `"Python"[0]` zurück?

A) `"Python"`  
B) `"P"`  
C) `"y"`  
D) `0`

---

## Frage 4: String-Slicing (1 Punkt)

Was gibt `"Hallo"[1:4]` zurück?

A) `"Hal"`  
B) `"all"`  
C) `"allo"`  
D) `"llo"`

---

## Frage 5: String-Methoden (1 Punkt)

Was gibt `"  Hallo  ".strip()` zurück?

A) `"  Hallo  "` (unverändert)  
B) `"Hallo  "`  
C) `"  Hallo"`  
D) `"Hallo"`

---

## Frage 6: F-Strings (1 Punkt)

Welcher Code gibt `"Ich bin 25 Jahre alt"` aus?

```python
alter = 25
```

A) `print("Ich bin " + alter + " Jahre alt")`  
B) `print(f"Ich bin {alter} Jahre alt")`  
C) `print("Ich bin {alter} Jahre alt")`  
D) `print("Ich bin", alter, "Jahre alt")`

---

## Frage 7: Vergleichsoperatoren (1 Punkt)

Was gibt `5 == 5` zurück?

A) `5`  
B) `True`  
C) `False`  
D) `"True"`

---

## Frage 8: Logische Operatoren (1 Punkt)

Was gibt `True and False` zurück?

A) `True`  
B) `False`  
C) `"True and False"`  
D) Fehler

---

## Frage 9: Typkonvertierung (1 Punkt)

Was gibt folgender Code aus?

```python
zahl = "42"
ergebnis = int(zahl) + 8
print(ergebnis)
```

A) `"428"`  
B) `"50"`  
C) `50`  
D) Fehler

---

## Frage 10: Input-Funktion (1 Punkt)

Was gibt `input()` zurück?

A) Immer eine Zahl  
B) Immer einen String  
C) Immer einen Boolean  
D) Hängt von der Eingabe ab

---

## 🔍 Lösungen

<details>
<summary>Klicken Sie hier für die Lösungen (erst nach dem Lösen!)</summary>

### Frage 1: E
**Erklärung:** Sowohl einfache (`'...'`) als auch doppelte (`"..."`) Anführungszeichen sind gültig.

### Frage 2: B
**Erklärung:** `+` verkettet Strings ohne Leerzeichen. Für ein Leerzeichen: `vorname + " " + nachname`

### Frage 3: B
**Erklärung:** Index 0 ist das erste Zeichen, also `"P"`.

### Frage 4: B
**Erklärung:** `[1:4]` bedeutet von Index 1 (inklusive) bis 4 (exklusive): `"all"`.

### Frage 5: D
**Erklärung:** `.strip()` entfernt Leerzeichen am Anfang und Ende.

### Frage 6: B
**Erklärung:** F-Strings (`f"..."`) erlauben Variablen in `{}`. Option A funktioniert nicht (String + Zahl).

### Frage 7: B
**Erklärung:** `==` ist ein Vergleichsoperator und gibt `True` oder `False` zurück.

### Frage 8: B
**Erklärung:** `and` gibt nur `True` zurück, wenn beide Werte `True` sind.

### Frage 9: C
**Erklärung:** `int("42")` konvertiert zu `42`, dann `42 + 8 = 50`.

### Frage 10: B
**Erklärung:** `input()` gibt **immer** einen String zurück, auch wenn eine Zahl eingegeben wird.

</details>

---

## 📊 Auswertung

Zählen Sie Ihre richtigen Antworten:

- **10 Punkte:** Perfekt! Sie sind bestens vorbereitet 🌟
- **8-9 Punkte:** Sehr gut! Kleine Lücken schliessen 👍
- **7 Punkte:** Bestanden! Wiederholen Sie unsichere Themen ✅
- **< 7 Punkte:** Wiederholen Sie den Leseauftrag und Experimente 📚

## 💡 Nächste Schritte

- **10 Punkte:** Sie sind bereit für den Präsenztag!
- **7-9 Punkte:** Wiederholen Sie die Experimente
- **< 7 Punkte:** Lesen Sie den Leseauftrag nochmals und machen Sie die Experimente

## 🆘 Hilfe

Falls Sie Schwierigkeiten haben:

1. Wiederholen Sie den [Leseauftrag](./leseauftrag.md)
2. Machen Sie die [Experimente](./erste-experimente.md) nochmals
3. Schauen Sie sich die Beispiele in [05-beispiele](../05-beispiele/) an
4. Fragen Sie im Kurs nach

Viel Erfolg! 🚀

