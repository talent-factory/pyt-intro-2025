# Handout: Python Basics

Zusammenfassung aller Grundlagen aus Modul 1.

## 📚 Inhaltsverzeichnis

1. [Was ist Programmieren?](#was-ist-programmieren)
2. [Python Shell](#python-shell)
3. [VS Code](#vs-code)
4. [Variablen](#variablen)
5. [Datentypen](#datentypen)
6. [Operatoren](#operatoren)
7. [Ein-/Ausgabe](#ein-ausgabe)

---

## Was ist Programmieren?

**Definition:** Programmieren = Einem Computer präzise Anweisungen geben

**Wichtig:**
- Computer sind dumm aber schnell
- Jedes Zeichen zählt
- Fehler sind normal und hilfreich

**Warum Python?**
- Einfache Syntax
- Vielseitig einsetzbar
- Große Community

---

## Python Shell

**REPL** = Read-Eval-Print-Loop

**Starten:**
```bash
python    # Windows
python3   # macOS/Linux
```

**Beenden:**
```python
>>> exit()
```

**Verwendung:**
- Experimente
- Schnelle Tests
- Lernen

---

## VS Code

**Professioneller Code-Editor**

**Wichtige Bereiche:**
- Explorer (links): Dateien
- Editor (Mitte): Code schreiben
- Terminal (unten): Befehle

**Python-Datei erstellen:**
1. `File` → `New File`
2. Speichern als `.py`
3. Code schreiben
4. Ausführen (▶️)

---

## Variablen

**Speicherplätze mit Namen**

```python
name = "Anna"
alter = 25
preis = 19.99
```

**Regeln:**
- Kleinbuchstaben
- Unterstriche für Wörter: `mein_name`
- Aussagekräftige Namen
- Keine Zahlen am Anfang
- Keine Leerzeichen

**Beispiele:**
```python
# ✅ Gut
vorname = "Max"
anzahl_studenten = 30
ist_student = True

# ❌ Schlecht
x = "Max"  # Nicht aussagekräftig
1name = "Max"  # Beginnt mit Zahl
ist-student = True  # Bindestrich
```

---

## Datentypen

### int (Ganzzahlen)

```python
alter = 25
anzahl = 100
jahr = 2025
```

### float (Dezimalzahlen)

```python
preis = 19.99
pi = 3.14159
temperatur = 36.5
```

### str (Strings/Texte)

```python
name = "Anna"
stadt = "Zürich"
text = "Python macht Spaß!"
```

### bool (Wahrheitswerte)

```python
ist_student = True
ist_fertig = False
```

**Typ prüfen:**
```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hallo")   # <class 'str'>
```

---

## Operatoren

### Arithmetische Operatoren

```python
+   # Addition:          5 + 3 = 8
-   # Subtraktion:       5 - 3 = 2
*   # Multiplikation:    5 * 3 = 15
/   # Division:          5 / 2 = 2.5
//  # Ganzzahldivision:  5 // 2 = 2
%   # Modulo (Rest):     5 % 2 = 1
**  # Potenz:            5 ** 2 = 25
```

### Reihenfolge

```python
2 + 3 * 4      # 14 (erst *, dann +)
(2 + 3) * 4    # 20 (Klammern zuerst)
```

---

## Ein-/Ausgabe

### Ausgabe mit print()

```python
print("Hallo")
print(42)
print(name)
```

### Mehrere Werte

```python
print("Name:", name, "Alter:", alter)
```

### F-Strings (modern)

```python
name = "Anna"
alter = 25
print(f"{name} ist {alter} Jahre alt")
```

### Formatierung

```python
preis = 19.99
print(f"Preis: {preis:.2f} Euro")  # 19.99 Euro
```

---

## Typkonvertierung

```python
# String zu int
int("42")        # 42

# String zu float
float("3.14")    # 3.14

# int zu float
float(42)        # 42.0

# float zu int (Nachkommastellen weg!)
int(3.99)        # 3

# Zahl zu String
str(42)          # "42"
```

---

## Häufige Fehler

### SyntaxError

```python
# Fehler
print("Hallo"

# Lösung
print("Hallo")
```

### NameError

```python
# Fehler
print(xyz)

# Lösung
xyz = 10
print(xyz)
```

### TypeError

```python
# Fehler
"5" + 5

# Lösung
int("5") + 5  # 10
```

---

## Best Practices

1. **Aussagekräftige Namen:** `alter` statt `a`
2. **Kommentare:** Erklären Sie Ihr Code
3. **Konstanten:** GROSSBUCHSTABEN für feste Werte
4. **Formatierung:** Lesbarkeit ist wichtig
5. **Testen:** Verschiedene Werte ausprobieren

---

## Beispiel-Programm

```python
# Rechteck-Fläche berechnen

# Eingabewerte
laenge = 10
breite = 5

# Berechnung
flaeche = laenge * breite
umfang = 2 * (laenge + breite)

# Ausgabe
print("=== Rechteck-Berechnung ===")
print(f"Länge: {laenge} m")
print(f"Breite: {breite} m")
print(f"Fläche: {flaeche} m²")
print(f"Umfang: {umfang} m")
```

---

## Nächste Schritte

**Modul 2:** Grundlegende Datentypen und Operatoren
- Strings vertiefen
- Booleans und Vergleiche
- Type Conversion
- Input/Output

**Üben Sie:**
- Schreiben Sie eigene Programme
- Experimentieren Sie
- Machen Sie Fehler und lernen Sie daraus

---

**Viel Erfolg mit Python! 🐍**

