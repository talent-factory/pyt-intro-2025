# Lektion 3: Typkonvertierung und Input/Output

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Datentypen ermitteln
- Zwischen Typen konvertieren
- Benutzereingaben mit `input()` verarbeiten
- Fehler bei Konvertierung verstehen

---

## 📖 Teil 1: Theorie (15 Min)

### 1.1 Datentypen ermitteln

Mit `type()` den Typ ermitteln:

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hallo")   # <class 'str'>
type(True)      # <class 'bool'>
```

### 1.2 Typkonvertierung

**String zu Zahl:**
```python
alter_str = "25"
alter_int = int(alter_str)      # 25
preis_str = "19.99"
preis_float = float(preis_str)  # 19.99
```

**Zahl zu String:**
```python
zahl = 42
text = str(zahl)  # "42"
```

**Zu Boolean:**
```python
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("Hi")   # True
```

**Achtung:** Nicht alle Konvertierungen funktionieren:
```python
int("Hallo")  # ValueError!
```

### 1.3 Input/Output

**`input()` liest Benutzereingaben:**

```python
name = input("Wie heissen Sie? ")
print(f"Hallo {name}!")
```

**Wichtig:** `input()` gibt **immer einen String** zurück!

```python
alter = input("Alter: ")  # String!
print(type(alter))        # <class 'str'>

# Für Berechnungen konvertieren:
alter = int(input("Alter: "))
naechstes_jahr = alter + 1
```

**`print()` mit mehreren Werten:**

```python
print("Hallo", "Welt")  # Hallo Welt
print("Summe:", 5 + 3)  # Summe: 8

# Mit Parametern:
print("A", "B", "C", sep="-")  # A-B-C
print("Zeile 1", end=" ")
print("Zeile 2")  # Zeile 1 Zeile 2
```

---

## 💻 Teil 2: Live-Coding (20 Min)

### Beispiel 1: Einfacher Rechner

```python
"""
Einfacher Rechner
Addiert zwei Zahlen
"""

print("=== Einfacher Rechner ===")

# Eingabe (als String!)
zahl1_str = input("Erste Zahl: ")
zahl2_str = input("Zweite Zahl: ")

# Konvertierung
zahl1 = float(zahl1_str)
zahl2 = float(zahl2_str)

# Berechnung
summe = zahl1 + zahl2
differenz = zahl1 - zahl2
produkt = zahl1 * zahl2
quotient = zahl1 / zahl2

# Ausgabe
print(f"\nErgebnisse:")
print(f"{zahl1} + {zahl2} = {summe}")
print(f"{zahl1} - {zahl2} = {differenz}")
print(f"{zahl1} * {zahl2} = {produkt}")
print(f"{zahl1} / {zahl2} = {quotient:.2f}")
```

### Beispiel 2: Personalisierte Begrüssung

```python
"""
Personalisierte Begrüssung
Sammelt Informationen und gibt sie formatiert aus
"""

print("=== Willkommen ===\n")

# Eingaben
vorname = input("Vorname: ")
nachname = input("Nachname: ")
alter = int(input("Alter: "))
stadt = input("Stadt: ")

# Verarbeitung
vollname = f"{vorname} {nachname}"
geburtsjahr = 2025 - alter

# Ausgabe
print("\n" + "=" * 40)
print(f"Name:        {vollname}")
print(f"Alter:       {alter} Jahre")
print(f"Geburtsjahr: ca. {geburtsjahr}")
print(f"Wohnort:     {stadt}")
print("=" * 40)
```

### Beispiel 3: Typ-Demonstrator

```python
"""
Typ-Demonstrator
Zeigt Typkonvertierungen
"""

# Original-Werte
zahl_int = 42
zahl_float = 3.14
text = "100"
wahrheit = True

print("=== Original-Typen ===")
print(f"{zahl_int} ist {type(zahl_int)}")
print(f"{zahl_float} ist {type(zahl_float)}")
print(f"{text} ist {type(text)}")
print(f"{wahrheit} ist {type(wahrheit)}")

print("\n=== Konvertierungen ===")

# Int zu anderen Typen
print(f"int zu float: {float(zahl_int)}")
print(f"int zu str: '{str(zahl_int)}'")
print(f"int zu bool: {bool(zahl_int)}")

# String zu Zahl
print(f"str zu int: {int(text)}")
print(f"str zu float: {float(text)}")

# Bool zu anderen
print(f"bool zu int: {int(wahrheit)}")
print(f"bool zu str: '{str(wahrheit)}'")
```

---

## ✏️ Teil 3: Übung (15 Min)

### Übung 3: Benutzereingaben verarbeiten

Siehe [02-uebungen/uebung-3-input.md](../02-uebungen/uebung-3-input.md)

**Aufgabe:**

Erstellen Sie ein Programm, das:

1. Nach Name, Alter und Lieblingsfarbe fragt
2. Das Geburtsjahr berechnet
3. Alle Informationen formatiert ausgibt

**Beispiel-Ausgabe:**

```
=== Persönliche Daten ===

Name: Max Muster
Alter: 25 Jahre
Geburtsjahr: ca. 2000
Lieblingsfarbe: Blau

Nächstes Jahr sind Sie 26 Jahre alt!
```

---

## 📝 Zusammenfassung

- **`type()`** ermittelt den Datentyp
- **Konvertierung:** `int()`, `float()`, `str()`, `bool()`
- **`input()`** gibt immer String zurück
- **Konvertierung nötig** für Berechnungen
- **Fehlerbehandlung** bei ungültigen Werten

## 🎯 Lernzielkontrolle

- ✅ Datentypen ermitteln?
- ✅ Typkonvertierung durchführen?
- ✅ `input()` nutzen?
- ✅ Eingaben verarbeiten?

