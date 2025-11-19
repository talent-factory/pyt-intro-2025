# Lektion 4: Variablen und Zahlen

**Dauer:** 50 Minuten  
**Format:** Theorie (15 Min.) + Live-Demo (20 Min.) + Übung (15 Min.)

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Variablen sinnvoll benennen
- Mit int und float arbeiten
- Alle arithmetischen Operatoren nutzen
- Typkonvertierung durchführen
- Best Practices anwenden

---

## 📖 Theorie (15 Min.)

### 1. Variablen richtig benennen

**Regeln:**

```python
# ✅ Gut
alter = 25
vorname = "Anna"
ist_student = True
max_punkte = 100

# ❌ Schlecht
a = 25  # Nicht aussagekräftig
1name = "Anna"  # Beginnt mit Zahl
ist-student = True  # Bindestrich nicht erlaubt
class = "Python"  # Reserviertes Wort
```

**Konventionen (PEP 8):**
- Kleinbuchstaben
- Wörter mit Unterstrich trennen: `mein_name`
- Aussagekräftige Namen
- Englisch oder Deutsch (konsistent bleiben)

### 2. int vs. float

**int (Integer) - Ganzzahlen:**

```python
alter = 25
anzahl_studenten = 30
jahr = 2025
```

**float (Floating Point) - Dezimalzahlen:**

```python
preis = 19.99
temperatur = 36.5
pi = 3.14159
```

**Automatische Erkennung:**

```python
>>> type(42)
<class 'int'>

>>> type(42.0)
<class 'float'>

>>> type(3.14)
<class 'float'>
```

### 3. Operatoren-Übersicht

```python
+   # Addition:          5 + 3 = 8
-   # Subtraktion:       5 - 3 = 2
*   # Multiplikation:    5 * 3 = 15
/   # Division:          5 / 2 = 2.5
//  # Ganzzahldivision:  5 // 2 = 2
%   # Modulo (Rest):     5 % 2 = 1
**  # Potenz:            5 ** 2 = 25
```

**Operator-Reihenfolge (wie Mathematik):**

```python
>>> 2 + 3 * 4
14  # Erst 3*4, dann +2

>>> (2 + 3) * 4
20  # Klammern zuerst
```

---

## 💻 Live-Demo (20 Min.)

### Demo 1: Variablen-Best-Practices (5 Min.)

```python
# Schlechtes Beispiel
a = 10
b = 5
c = a * b
print(c)

# Gutes Beispiel
laenge = 10
breite = 5
flaeche = laenge * breite
print(f"Die Fläche beträgt {flaeche} Quadratmeter")
```

**Erklären:**
- Aussagekräftige Namen helfen beim Verstehen
- Code wird selbst-dokumentierend
- Andere (und Sie selbst später) verstehen den Code besser

### Demo 2: Rechnen mit int und float (7 Min.)

```python
# Ganzzahlen
anzahl_aepfel = 10
preis_pro_apfel = 2
gesamtpreis = anzahl_aepfel * preis_pro_apfel
print(f"Gesamtpreis: {gesamtpreis} Euro")

# Dezimalzahlen
radius = 5.0
pi = 3.14159
umfang = 2 * pi * radius
print(f"Umfang: {umfang:.2f} cm")  # .2f = 2 Dezimalstellen

# Mischung int und float
stunden = 8
stundenlohn = 25.50
gehalt = stunden * stundenlohn
print(f"Gehalt: {gehalt} Euro")
```

### Demo 3: Alle Operatoren (4 Min.)

```python
a = 17
b = 5

print(f"{a} + {b} = {a + b}")    # 22
print(f"{a} - {b} = {a - b}")    # 12
print(f"{a} * {b} = {a * b}")    # 85
print(f"{a} / {b} = {a / b}")    # 3.4
print(f"{a} // {b} = {a // b}")  # 3 (Ganzzahldivision)
print(f"{a} % {b} = {a % b}")    # 2 (Rest)
print(f"{a} ** 2 = {a ** 2}")    # 289 (17²)
```

### Demo 4: Typkonvertierung (4 Min.)

```python
# String zu int
alter_str = "25"
alter_int = int(alter_str)
print(alter_int + 5)  # 30

# int zu float
zahl = 10
zahl_float = float(zahl)
print(zahl_float)  # 10.0

# float zu int (Nachkommastellen werden abgeschnitten!)
preis = 19.99
preis_int = int(preis)
print(preis_int)  # 19

# Zahl zu String
alter = 25
text = "Ich bin " + str(alter) + " Jahre alt"
print(text)
```

---

## ✏️ Übung (15 Min.)

### [Übung 4: Temperaturumrechner](../02-uebungen/uebung-4-temperatur.md)

**Aufgabe:**

Erstellen Sie `temperatur.py`:

```python
# Celsius zu Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit zu Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

**Erweitern Sie:**
- Verschiedene Temperaturen testen
- Kelvin-Umrechnung hinzufügen
- Ausgabe schön formatieren

---

## 💡 Best Practices

### 1. Aussagekräftige Namen

```python
# ❌ Schlecht
x = 100
y = 0.19
z = x * y

# ✅ Gut
preis_netto = 100
mehrwertsteuer_satz = 0.19
mehrwertsteuer = preis_netto * mehrwertsteuer_satz
```

### 2. Konstanten

```python
# Konstanten in GROSSBUCHSTABEN
PI = 3.14159
MEHRWERTSTEUER = 0.19
MAX_VERSUCHE = 3
```

### 3. Kommentare

```python
# Berechne Kreisfläche
radius = 5
flaeche = PI * radius ** 2  # A = π * r²
```

### 4. Formatierung

```python
# Zahlen formatieren
preis = 19.99
print(f"Preis: {preis:.2f} Euro")  # 19.99 Euro

zahl = 1234567
print(f"Zahl: {zahl:,}")  # 1,234,567
```

---

## 📝 Zusammenfassung

**Wichtigste Punkte:**

1. Variablen: Aussagekräftige Namen verwenden
2. int = Ganzzahlen, float = Dezimalzahlen
3. Operatoren: +, -, *, /, //, %, **
4. Typkonvertierung: int(), float(), str()
5. Best Practices: Lesbarkeit ist wichtig

**Was Sie jetzt können:**
- ✅ Python Shell nutzen
- ✅ VS Code bedienen
- ✅ Python-Dateien erstellen
- ✅ Mit Variablen und Zahlen arbeiten

**Nächste Schritte:**
- Hausaufgaben bearbeiten
- Üben, üben, üben!
- Vorbereitung auf Modul 2

---

## 🎓 Für Dozenten

### Abschluss des Tages

**Zusammenfassung (5 Min.):**
- Was haben wir gelernt?
- Fragen klären
- Hausaufgaben erklären

**Motivation:**
- Erfolge betonen
- Ermutigen zum Üben
- Ausblick auf Modul 2

### Hausaufgaben-Briefing

- [Nachbearbeitung](../03-nachbearbeitung/) erklären
- Deadline nennen
- Fragen beantworten

---

**Glückwunsch! Sie haben Modul 1 abgeschlossen! 🎉**

**Nächstes Modul:** Modul 2: Grundlegende Datentypen und Operatoren

