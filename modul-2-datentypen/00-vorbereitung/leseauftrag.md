# Leseauftrag Modul 2: Datentypen und Operatoren

**Zeitaufwand:** 60-90 Minuten

## 1. Strings - Texte in Python

### Was sind Strings?

Ein **String** (Zeichenkette) ist eine Folge von Zeichen. In Python können Strings mit einfachen (`'`) oder doppelten (`"`) Anführungszeichen erstellt werden:

```python
name = "Anna"
stadt = 'Zürich'
```

Beide Varianten sind gleichwertig. Für mehrzeilige Strings verwenden Sie dreifache Anführungszeichen:

```python
text = """Dies ist ein
mehrzeiliger
Text"""
```

### String-Operationen

**Konkatenation** (Verkettung) mit `+`:

```python
vorname = "Max"
nachname = "Muster"
vollname = vorname + " " + nachname  # "Max Muster"
```

**Multiplikation** mit `*`:

```python
linie = "-" * 20  # "--------------------"
```

**Länge** mit `len()`:

```python
text = "Hallo"
laenge = len(text)  # 5
```

### String-Indexierung

Strings sind **indexiert** - jedes Zeichen hat eine Position (beginnend bei 0):

```python
wort = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5

erster = wort[0]   # "P"
zweiter = wort[1]  # "y"
letzter = wort[-1] # "n" (negativ zählt von hinten)
```

### String-Slicing

Mit **Slicing** können Sie Teilstrings extrahieren:

```python
text = "Python Programmierung"
# text[start:end]  # end ist exklusiv!

text[0:6]   # "Python"
text[7:20]  # "Programmierung"
text[:6]    # "Python" (von Anfang)
text[7:]    # "Programmierung" (bis Ende)
text[::2]   # "Pto rgamern" (jedes 2. Zeichen)
```

### String-Methoden

Strings haben viele nützliche **Methoden**:

```python
text = "  Hallo Welt  "

text.upper()        # "  HALLO WELT  "
text.lower()        # "  hallo welt  "
text.strip()        # "Hallo Welt" (Leerzeichen entfernen)
text.replace("Hallo", "Hi")  # "  Hi Welt  "
text.split()        # ["Hallo", "Welt"] (Liste!)
```

**Wichtig:** String-Methoden ändern den Original-String **nicht**, sondern geben einen neuen String zurück!

```python
name = "anna"
name.upper()  # Gibt "ANNA" zurück
print(name)   # Ausgabe: "anna" (unverändert!)

# Korrekt:
name = name.upper()  # Neuen Wert zuweisen
print(name)          # Ausgabe: "ANNA"
```

### String-Formatierung mit f-Strings

**F-Strings** (ab Python 3.6) sind die moderne Art, Strings zu formatieren:

```python
name = "Anna"
alter = 25

# Alt (nicht empfohlen):
text = "Ich heisse " + name + " und bin " + str(alter) + " Jahre alt."

# Modern (empfohlen):
text = f"Ich heisse {name} und bin {alter} Jahre alt."
```

F-Strings können auch Ausdrücke enthalten:

```python
a = 10
b = 20
print(f"Die Summe von {a} und {b} ist {a + b}")
# Ausgabe: Die Summe von 10 und 20 ist 30
```

## 2. Boolsche Werte

### True und False

**Boolsche Werte** (Boolean) können nur zwei Werte haben: `True` oder `False`.

```python
ist_student = True
ist_rentner = False
```

**Wichtig:** Gross-/Kleinschreibung beachten! `true` funktioniert nicht, nur `True`.

### Vergleichsoperatoren

Vergleiche ergeben immer einen boolschen Wert:

| Operator | Bedeutung | Beispiel | Ergebnis |
|----------|-----------|----------|----------|
| `==` | Gleich | `5 == 5` | `True` |
| `!=` | Ungleich | `5 != 3` | `True` |
| `<` | Kleiner | `3 < 5` | `True` |
| `>` | Grösser | `5 > 3` | `True` |
| `<=` | Kleiner oder gleich | `5 <= 5` | `True` |
| `>=` | Grösser oder gleich | `3 >= 5` | `False` |

**Beispiele:**

```python
alter = 18
ist_volljaehrig = alter >= 18  # True

temperatur = 25
ist_warm = temperatur > 20     # True

name = "Anna"
ist_anna = name == "Anna"      # True
```

### Logische Operatoren

Boolsche Werte können mit **logischen Operatoren** verknüpft werden:

**`and`** - Beide Bedingungen müssen wahr sein:

```python
alter = 25
hat_fuehrerschein = True

darf_fahren = alter >= 18 and hat_fuehrerschein  # True
```

**`or`** - Mindestens eine Bedingung muss wahr sein:

```python
ist_wochenende = True
ist_feiertag = False

ist_frei = ist_wochenende or ist_feiertag  # True
```

**`not`** - Negation (Umkehrung):

```python
ist_regen = False
ist_trocken = not ist_regen  # True
```

## 3. Typkonvertierung

### Datentypen ermitteln

Mit `type()` können Sie den Typ einer Variable ermitteln:

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hallo")   # <class 'str'>
type(True)      # <class 'bool'>
```

### Konvertierung zwischen Typen

Python kann Werte zwischen verschiedenen Typen konvertieren:

```python
# String zu Zahl
alter_str = "25"
alter_int = int(alter_str)      # 25 (Integer)
preis_str = "19.99"
preis_float = float(preis_str)  # 19.99 (Float)

# Zahl zu String
zahl = 42
text = str(zahl)  # "42"

# Zu Boolean
bool(1)      # True
bool(0)      # False
bool("")     # False (leerer String)
bool("Hi")   # True (nicht-leerer String)
```

**Achtung:** Nicht alle Konvertierungen funktionieren:

```python
int("Hallo")  # ValueError: invalid literal for int()
```

## 4. Input/Output

### Benutzereingaben mit input()

Die `input()` Funktion liest Benutzereingaben ein:

```python
name = input("Wie heissen Sie? ")
print(f"Hallo {name}!")
```

**Wichtig:** `input()` gibt **immer einen String** zurück!

```python
alter = input("Wie alt sind Sie? ")
print(type(alter))  # <class 'str'>

# Für Berechnungen konvertieren:
alter = int(input("Wie alt sind Sie? "))
naechstes_jahr = alter + 1
print(f"Nächstes Jahr sind Sie {naechstes_jahr}")
```

### Ausgabe mit print()

`print()` kann mehrere Werte ausgeben:

```python
print("Hallo", "Welt")  # Hallo Welt
print("Summe:", 5 + 3)  # Summe: 8

# Mit sep und end Parameter:
print("A", "B", "C", sep="-")  # A-B-C
print("Zeile 1", end=" ")
print("Zeile 2")  # Zeile 1 Zeile 2
```

## 📝 Zusammenfassung

- **Strings** sind Zeichenketten in `"..."` oder `'...'`
- **String-Methoden** wie `.upper()`, `.lower()`, `.strip()` sind sehr nützlich
- **F-Strings** (`f"..."`) sind die moderne Art der Formatierung
- **Boolsche Werte** sind `True` oder `False`
- **Vergleichsoperatoren** (`==`, `!=`, `<`, `>`, etc.) ergeben Boolean
- **Logische Operatoren** (`and`, `or`, `not`) verknüpfen Bedingungen
- **Typkonvertierung** mit `int()`, `float()`, `str()`, `bool()`
- **`input()`** liest Benutzereingaben (immer als String!)

## ✅ Selbsttest

Können Sie diese Fragen beantworten?

1. Was ist der Unterschied zwischen `'...'` und `"..."`?
2. Wie verketten Sie zwei Strings?
3. Was gibt `"Python"[0]` zurück?
4. Was ist der Unterschied zwischen `=` und `==`?
5. Was gibt `5 > 3 and 2 < 1` zurück?
6. Wie konvertieren Sie den String `"42"` zu einer Zahl?
7. Was gibt `input()` zurück?

Wenn Sie alle Fragen beantworten können, sind Sie bereit für die Experimente!

