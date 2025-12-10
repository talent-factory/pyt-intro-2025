# Erste Schritte mit Python

**Zeitaufwand:** 60 Minuten  
**Voraussetzung:** Python installiert oder Codespaces eingerichtet

## 🎯 Ziele

Nach dieser Übung können Sie:

- Die Python Shell (REPL) starten und nutzen
- Einfache Berechnungen durchführen
- Variablen erstellen und verwenden
- Erste Python-Befehle ausführen

---

## 1. Python Shell starten

### Was ist die Python Shell?

Die **Python Shell** (auch **REPL** genannt: Read-Eval-Print-Loop) ist eine **interaktive Umgebung**, in der Sie Python-Code direkt eingeben und sofort das Ergebnis sehen.

### Shell öffnen

**Terminal/Kommandozeile öffnen:**

- **Windows:** `cmd` oder `PowerShell`
- **macOS:** `Terminal`
- **Linux:** `Terminal`
- **Codespaces:** Terminal ist bereits offen (unten)

**Python starten:**

```bash
python  # Windows
python3 # macOS/Linux
```

Sie sehen jetzt:

```python
Python 3.12.x (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Der `>>>` ist der **Prompt** - hier können Sie Code eingeben!

---

## 2. Erste Berechnungen

### Einfache Mathematik

Tippen Sie folgende Befehle ein (drücken Sie nach jedem Enter):

```python
>>> 2 + 2
4

>>> 10 - 3
7

>>> 5 * 4
20

>>> 15 / 3
5.0

>>> 2 ** 3
8
```

**Erklärung:**

- `+` Addition
- `-` Subtraktion
- `*` Multiplikation
- `/` Division
- `**` Potenz (2³ = 8)

### Weitere Operatoren

```python
>>> 17 // 5
3

>>> 17 % 5
2

>>> (2 + 3) * 4
20
```

**Erklärung:**

- `//` Ganzzahldivision (ohne Rest)
- `%` Modulo (nur der Rest)
- `()` Klammern für Reihenfolge

---

## 3. Variablen

### Variablen erstellen

```python
>>> x = 10
>>> x
10

>>> name = "Python"
>>> name
'Python'

>>> preis = 19.99
>>> preis
19.99
```

**Wichtig:** Variablennamen sollten **aussagekräftig** sein!

### Mit Variablen rechnen

```python
>>> a = 5
>>> b = 3
>>> summe = a + b
>>> summe
8

>>> a * b
15
```

### Variablen ändern

```python
>>> x = 10
>>> x
10

>>> x = 20
>>> x
20

>>> x = x + 5
>>> x
25
```

---

## 4. Strings (Texte)

### Strings erstellen

```python
>>> vorname = "Anna"
>>> nachname = "Müller"
>>> vorname
'Anna'
```

### Strings verbinden

```python
>>> vollname = vorname + " " + nachname
>>> vollname
'Anna Müller'

>>> begruessung = "Hallo, " + vorname + "!"
>>> begruessung
'Hallo, Anna!'
```

### String-Operationen

```python
>>> text = "Python"
>>> text * 3
'PythonPythonPython'

>>> len(text)
6

>>> text.upper()
'PYTHON'

>>> text.lower()
'python'
```

---

## 5. Der print() Befehl

### Ausgabe erzeugen

```python
>>> print("Hello, World!")
Hello, World!

>>> print(42)
42

>>> x = 10
>>> print(x)
10

>>> print("Der Wert ist:", x)
Der Wert ist: 10
```

### Mehrere Werte ausgeben

```python
>>> name = "Max"
>>> alter = 25
>>> print(name, "ist", alter, "Jahre alt")
Max ist 25 Jahre alt
```

### F-Strings (modern)

```python
>>> name = "Lisa"
>>> alter = 30
>>> print(f"{name} ist {alter} Jahre alt")
Lisa ist 30 Jahre alt

>>> preis = 19.99
>>> print(f"Der Preis beträgt {preis} Euro")
Der Preis beträgt 19.99 Euro
```

---

## 6. Praktische Übungen

### Übung 1: Taschenrechner

Berechnen Sie:

```python
>>> # Ihre Lösung hier
>>> 15 + 27

>>> 100 - 37

>>> 12 * 8

>>> 144 / 12
```

### Übung 2: Variablen

Erstellen Sie Variablen für:

```python
>>> # Ihr Name
>>> mein_name = "..."

>>> # Ihr Alter
>>> mein_alter = ...

>>> # Ihre Stadt
>>> meine_stadt = "..."

>>> # Ausgabe
>>> print(f"Ich bin {mein_name}, {mein_alter} Jahre alt und wohne in {meine_stadt}")
```

### Übung 3: Berechnungen

```python
>>> # Berechnen Sie die Fläche eines Rechtecks
>>> laenge = 10
>>> breite = 5
>>> flaeche = laenge * breite
>>> print(f"Die Fläche beträgt {flaeche} Quadratmeter")

>>> # Berechnen Sie den Durchschnitt von 3 Zahlen
>>> zahl1 = 10
>>> zahl2 = 20
>>> zahl3 = 30
>>> durchschnitt = (zahl1 + zahl2 + zahl3) / 3
>>> print(f"Der Durchschnitt ist {durchschnitt}")
```

---

## 7. Fehler verstehen

### Häufige Fehler

**Syntaxfehler:**

```python
>>> print("Hallo"
  File "<stdin>", line 1
    print("Hallo"
                 ^
SyntaxError: '(' was never closed
```

**Lösung:** Klammer schliessen: `print("Hallo")`

**NameError:**

```python
>>> print(xyz)
NameError: name 'xyz' is not defined
```

**Lösung:** Variable erst definieren: `xyz = 10`

**TypeError:**

```python
>>> "5" + 5
TypeError: can only concatenate str (not "int") to str
```

**Lösung:** Typ konvertieren: `int("5") + 5` oder `"5" + str(5)`

---

## 8. Shell beenden

```python
>>> exit()
```

Oder: `Ctrl+D` (macOS/Linux) / `Ctrl+Z` dann Enter (Windows)

---

## ✅ Checkliste

Nach diesen ersten Schritten sollten Sie:

- [ ] Die Python Shell starten können
- [ ] Einfache Berechnungen durchführen können
- [ ] Variablen erstellen und verwenden können
- [ ] Strings verbinden können
- [ ] `print()` nutzen können
- [ ] Einfache Fehler verstehen

---

## 💡 Tipps

- **Experimentieren Sie!** Die Shell ist perfekt zum Ausprobieren
- **Fehler sind okay!** Sie können nichts kaputt machen
- **Pfeiltaste hoch:** Zeigt vorherige Befehle
- **Tab-Taste:** Auto-Vervollständigung (manchmal)

---

## 📚 Nächste Schritte

Sie sind jetzt bereit für den **Präsenztag**!

Am Präsenztag werden wir:

- VS Code als Editor nutzen
- Richtige Python-Dateien erstellen
- Komplexere Programme schreiben
- Viel üben!

---

**Gut gemacht! Sie haben Ihre ersten Schritte mit Python gemeistert! 🎉**

