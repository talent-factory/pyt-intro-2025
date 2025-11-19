# Lektion 1: Strings - Texte verarbeiten

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Strings erstellen und verketten
- String-Indexierung und Slicing anwenden
- String-Methoden nutzen
- F-Strings für moderne Formatierung verwenden

---

## 📖 Teil 1: Theorie (15 Min)

### 1.1 Was sind Strings?

Ein **String** ist eine Folge von Zeichen (Text). In Python können Strings mit einfachen oder doppelten Anführungszeichen erstellt werden:

```python
name = "Anna"
stadt = 'Zürich'
text = """Mehrzeiliger
Text"""
```

### 1.2 String-Operationen

**Konkatenation** (Verkettung):
```python
vorname = "Max"
nachname = "Muster"
vollname = vorname + " " + nachname  # "Max Muster"
```

**Multiplikation**:
```python
linie = "=" * 30  # "=============================="
```

**Länge**:
```python
text = "Hallo"
laenge = len(text)  # 5
```

### 1.3 String-Indexierung

Jedes Zeichen hat eine Position (Index), beginnend bei 0:

```python
wort = "Python"
#      012345

wort[0]   # "P" (erstes Zeichen)
wort[5]   # "n" (letztes Zeichen)
wort[-1]  # "n" (von hinten)
wort[-2]  # "o" (vorletztes)
```

### 1.4 String-Slicing

Teilstrings extrahieren:

```python
text = "Python Programmierung"

text[0:6]    # "Python"
text[7:20]   # "Programmierung"
text[:6]     # "Python" (von Anfang)
text[7:]     # "Programmierung" (bis Ende)
text[::2]    # "Pto rgamern" (jedes 2. Zeichen)
text[::-1]   # "gnureimmargorP nohtyP" (rückwärts)
```

### 1.5 String-Methoden

Strings haben viele nützliche Methoden:

```python
text = "  Hallo Welt  "

text.upper()         # "  HALLO WELT  "
text.lower()         # "  hallo welt  "
text.strip()         # "Hallo Welt"
text.replace("Hallo", "Hi")  # "  Hi Welt  "
text.split()         # ["Hallo", "Welt"]
```

**Wichtig:** Methoden ändern den Original-String nicht!

```python
name = "anna"
name.upper()  # Gibt "ANNA" zurück
print(name)   # Ausgabe: "anna" (unverändert!)

# Korrekt:
name = name.upper()
```

### 1.6 F-Strings (Modern!)

F-Strings sind die moderne Art der String-Formatierung:

```python
name = "Anna"
alter = 25

# Alt (nicht empfohlen):
text = "Ich heisse " + name + " und bin " + str(alter)

# Modern (empfohlen):
text = f"Ich heisse {name} und bin {alter}"
```

Mit Berechnungen:
```python
a = 10
b = 20
print(f"Die Summe von {a} und {b} ist {a + b}")
```

---

## 💻 Teil 2: Live-Coding (20 Min)

### Beispiel 1: Namensschild-Generator

```python
"""
Namensschild-Generator
Erstellt ein formatiertes Namensschild
"""

# Eingabe
vorname = "Max"
nachname = "Muster"
firma = "Python AG"

# Verarbeitung
vollname = vorname + " " + nachname
linie = "=" * 40

# Ausgabe
print(linie)
print(f"Name:  {vollname}")
print(f"Firma: {firma}")
print(linie)
```

### Beispiel 2: Text-Analyse

```python
"""
Einfache Text-Analyse
Analysiert einen Text
"""

text = "Python ist eine tolle Programmiersprache"

# Informationen
print(f"Text: {text}")
print(f"Länge: {len(text)} Zeichen")
print(f"Grossbuchstaben: {text.upper()}")
print(f"Kleinbuchstaben: {text.lower()}")
print(f"Wörter: {text.split()}")
print(f"Anzahl Wörter: {len(text.split())}")

# Prüfungen
print(f"Beginnt mit 'Python': {text.startswith('Python')}")
print(f"Enthält 'tolle': {'tolle' in text}")
```

### Beispiel 3: String-Manipulation

```python
"""
String-Manipulation
Verschiedene String-Operationen
"""

# Original
text = "  Python Programmierung  "
print(f"Original: '{text}'")

# Leerzeichen entfernen
sauber = text.strip()
print(f"Ohne Leerzeichen: '{sauber}'")

# Ersetzen
neu = sauber.replace("Programmierung", "Kurs")
print(f"Ersetzt: '{neu}'")

# Aufteilen
woerter = sauber.split()
print(f"Wörter: {woerter}")

# Zusammenfügen
verbunden = "-".join(woerter)
print(f"Verbunden: '{verbunden}'")
```

---

## ✏️ Teil 3: Übung (15 Min)

### Übung 1: Textformatierung

Siehe [02-uebungen/uebung-1-textformatierung.md](../02-uebungen/uebung-1-textformatierung.md)

**Aufgabe:**

Erstellen Sie ein Programm, das:

1. Einen Namen in Variablen speichert
2. Den Namen in verschiedenen Formaten ausgibt:
   - Grossbuchstaben
   - Kleinbuchstaben
   - Nur erster Buchstabe gross
3. Die Länge des Namens ausgibt
4. Die ersten 3 Buchstaben extrahiert

**Beispiel-Ausgabe:**

```
Name: Max Muster
Grossbuchstaben: MAX MUSTER
Kleinbuchstaben: max muster
Titel-Format: Max Muster
Länge: 10 Zeichen
Erste 3 Buchstaben: Max
```

---

## 📝 Zusammenfassung

- **Strings** sind Zeichenketten in `"..."` oder `'...'`
- **Konkatenation** mit `+`, **Multiplikation** mit `*`
- **Indexierung** mit `[0]`, **Slicing** mit `[start:end]`
- **Methoden** wie `.upper()`, `.lower()`, `.strip()`, `.split()`
- **F-Strings** (`f"..."`) für moderne Formatierung
- **Wichtig:** String-Methoden ändern den Original nicht!

## 🎯 Lernzielkontrolle

Können Sie:

- ✅ Strings erstellen und verketten?
- ✅ String-Indexierung und Slicing anwenden?
- ✅ String-Methoden nutzen?
- ✅ F-Strings verwenden?

## 📚 Weiterführende Ressourcen

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Beispielcode](../05-beispiele/strings.py)
- [Cheatsheet](../04-materialien/cheatsheet-strings.md)

