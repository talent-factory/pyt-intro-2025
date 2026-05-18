# Lektion 2: Python Shell & erste Schritte

**Dauer:** 50 Minuten  
**Format:** Theorie (15 Min.) + Live-Coding (20 Min.) + Übung (15 Min.)

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Die Python Shell (REPL) effektiv nutzen
- Verschiedene Datentypen unterscheiden
- Mit Variablen arbeiten
- Einfache Fehler erkennen und beheben

---

## 📖 Theorie (15 Min.)

### 1. Was ist REPL?

**REPL** = Read-Eval-Print-Loop

1. **Read:** Python liest Ihre Eingabe
2. **Eval:** Python wertet aus (evaluiert)
3. **Print:** Python zeigt das Ergebnis
4. **Loop:** Zurück zu Schritt 1

**Perfekt für:**
- Experimente
- Schnelle Tests
- Lernen
- Debugging

### 2. Datentypen

Python kennt verschiedene **Arten von Daten**:

```python
# int - Ganzzahlen
alter = 25
anzahl = 100

# float - Dezimalzahlen
preis = 19.99
temperatur = 36.5

# str - Texte (Strings)
name = "Anna"
stadt = "Zürich"

# bool - Wahrheitswerte
ist_student = True
ist_fertig = False
```

**Typ herausfinden:**

```python
>>> type(42)
<class 'int'>

>>> type(3.14)
<class 'float'>

>>> type("Hallo")
<class 'str'>
```

### 3. Operatoren

**Arithmetische Operatoren:**

```python
+   # Addition
-   # Subtraktion
*   # Multiplikation
/   # Division
//  # Ganzzahldivision
%   # Modulo (Rest)
**  # Potenz
```

**Beispiele:**

```python
>>> 10 + 5    # 15
>>> 10 - 5    # 5
>>> 10 * 5    # 50
>>> 10 / 5    # 2.0
>>> 10 // 3   # 3 (ohne Rest)
>>> 10 % 3    # 1 (nur Rest)
>>> 2 ** 3    # 8 (2 hoch 3)
```

---

## 💻 Live-Coding (20 Min.)

### Demo 1: Datentypen erkunden (7 Min.)

```python
>>> # Ganzzahlen
>>> x = 42
>>> type(x)
<class 'int'>

>>> # Dezimalzahlen
>>> pi = 3.14159
>>> type(pi)
<class 'float'>

>>> # Strings
>>> name = "Python"
>>> type(name)
<class 'str'>

>>> # Booleans
>>> ist_wahr = True
>>> type(ist_wahr)
<class 'bool'>
```

**Erklären:**
- Jeder Wert hat einen Typ
- Python erkennt Typ automatisch
- `type()` zeigt den Typ

### Demo 2: Rechnen mit Variablen (7 Min.)

```python
>>> # Einfache Berechnungen
>>> a = 10
>>> b = 3
>>> summe = a + b
>>> summe
13

>>> differenz = a - b
>>> differenz
7

>>> produkt = a * b
>>> produkt
30

>>> # Praktisches Beispiel: Rechteck-Fläche
>>> laenge = 5
>>> breite = 3
>>> flaeche = laenge * breite
>>> print(f"Die Fläche beträgt {flaeche} Quadratmeter")
Die Fläche beträgt 15 Quadratmeter
```

### Demo 3: String-Operationen (6 Min.)

```python
>>> # Strings verbinden
>>> vorname = "Anna"
>>> nachname = "Müller"
>>> vollname = vorname + " " + nachname
>>> vollname
'Anna Müller'

>>> # String wiederholen
>>> "Ha" * 3
'HaHaHa'

>>> # String-Länge
>>> len("Python")
6

>>> # String-Methoden
>>> text = "python"
>>> text.upper()
'PYTHON'
>>> text.capitalize()
'Python'
```

---

## ✏️ Übung (15 Min.)

### [Übung 2: Einfacher Taschenrechner](../02-uebungen/uebung-2-taschenrechner.md)

**Aufgaben:**

1. Verschiedene Berechnungen durchführen
2. Variablen für Berechnungen nutzen
3. Ergebnisse mit `print()` ausgeben
4. Mit Strings experimentieren

**Dozent:**
- Herumgehen und unterstützen
- Auf häufige Fehler hinweisen
- Erfolge loben

---

## 🐛 Häufige Fehler

### Fehler 1: Variablenname vergessen

```python
>>> print(xyz)
NameError: name 'xyz' is not defined
```

**Lösung:** Variable erst definieren:
```python
>>> xyz = 10
>>> print(xyz)
10
```

### Fehler 2: Typ-Mismatch

```python
>>> "5" + 5
TypeError: can only concatenate str (not "int") to str
```

**Lösung:** Typen angleichen:
```python
>>> int("5") + 5  # 10
>>> "5" + str(5)  # "55"
```

### Fehler 3: Division durch Null

```python
>>> 10 / 0
ZeroDivisionError: division by zero
```

**Lösung:** Prüfen vor Division:
```python
>>> if b != 0:
...     ergebnis = a / b
```

---

## 📝 Zusammenfassung

**Wichtigste Punkte:**

1. REPL = Interaktive Python-Umgebung
2. Datentypen: int, float, str, bool
3. Operatoren: +, -, *, /, //, %, **
4. Variablen speichern Werte
5. `type()` zeigt Datentyp

**Ausblick auf Lektion 3:**
- VS Code als professioneller Editor
- Python-Dateien erstellen
- Programme speichern und ausführen

---

## 🎓 Für Dozenten

### Tipps

- **Live-Coding:** Fehler machen und korrigieren
- **Interaktiv:** Studierende raten lassen
- **Tempo:** Langsam genug für Mitschreiben
- **Wiederholung:** Wichtige Konzepte mehrfach zeigen

### Zeitmanagement

- Theorie: 15 Min. (nicht überziehen!)
- Demo: 20 Min. (wichtigster Teil)
- Übung: 15 Min. (Zeit für Fragen lassen)

---

**Nächste Lektion:** [Lektion 3: VS Code](./lektion-3-vscode.md)

