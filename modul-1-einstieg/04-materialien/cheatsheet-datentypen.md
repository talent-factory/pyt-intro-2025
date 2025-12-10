# Cheatsheet: Datentypen

Schnellreferenz für Python-Datentypen in Modul 1.

## 📊 Übersicht

| Typ | Beschreibung | Beispiel | Verwendung |
|-----|--------------|----------|------------|
| `int` | Ganzzahlen | `42`, `-10`, `0` | Zählen, Indizes |
| `float` | Dezimalzahlen | `3.14`, `-0.5`, `2.0` | Berechnungen, Messungen |
| `str` | Texte (Strings) | `"Hallo"`, `'Python'` | Texte, Namen |
| `bool` | Wahrheitswerte | `True`, `False` | Bedingungen |

## 🔢 int (Integer)

**Ganzzahlen ohne Dezimalstellen**

```python
alter = 25
anzahl = 100
jahr = 2025
temperatur = -5
```

**Operationen:**
```python
10 + 5    # 15 (Addition)
10 - 5    # 5 (Subtraktion)
10 * 5    # 50 (Multiplikation)
10 // 3   # 3 (Ganzzahldivision)
10 % 3    # 1 (Rest/Modulo)
2 ** 3    # 8 (Potenz)
```

## 🔢 float (Floating Point)

**Dezimalzahlen**

```python
preis = 19.99
pi = 3.14159
temperatur = 36.5
```

**Operationen:**
```python
10.5 + 2.3   # 12.8
10.0 / 3.0   # 3.333...
2.5 ** 2     # 6.25
```

**Formatierung:**
```python
preis = 19.99
print(f"{preis:.2f}")  # 19.99 (2 Dezimalstellen)
print(f"{preis:.1f}")  # 20.0 (1 Dezimalstelle)
```

## 📝 str (String)

**Texte in Anführungszeichen**

```python
name = "Anna"
stadt = 'Zürich'
text = "Python macht Spass!"
```

**Operationen:**
```python
"Hallo" + " " + "Welt"  # "Hallo Welt" (Verbinden)
"Ha" * 3                # "HaHaHa" (Wiederholen)
len("Python")           # 6 (Länge)
```

**Methoden:**
```python
text = "python"
text.upper()       # "PYTHON"
text.lower()       # "python"
text.capitalize()  # "Python"
```

**F-Strings:**
```python
name = "Anna"
alter = 25
print(f"{name} ist {alter} Jahre alt")
# Anna ist 25 Jahre alt
```

## ✅ bool (Boolean)

**Wahrheitswerte**

```python
ist_student = True
ist_fertig = False
```

**Verwendung:**
```python
5 > 3      # True
10 == 10   # True
5 < 3      # False
```

## 🔄 Typkonvertierung

**Zwischen Typen wechseln:**

```python
# String zu int
int("42")        # 42
int("3.14")      # Fehler!

# String zu float
float("3.14")    # 3.14
float("42")      # 42.0

# int zu float
float(42)        # 42.0

# float zu int (Nachkommastellen werden abgeschnitten!)
int(3.14)        # 3
int(3.99)        # 3

# Zahl zu String
str(42)          # "42"
str(3.14)        # "3.14"

# String zu bool
bool("Hallo")    # True
bool("")         # False
bool(0)          # False
bool(1)          # True
```

## 🔍 Typ prüfen

```python
type(42)         # <class 'int'>
type(3.14)       # <class 'float'>
type("Hallo")    # <class 'str'>
type(True)       # <class 'bool'>
```

## ⚠️ Häufige Fehler

**Typ-Mismatch:**
```python
# ❌ Fehler
"5" + 5          # TypeError

# ✅ Lösung
int("5") + 5     # 10
"5" + str(5)     # "55"
```

**Division:**
```python
10 / 3    # 3.333... (float)
10 // 3   # 3 (int)
```

## 💡 Tipps

- `int` für Zählen und Indizes
- `float` für Berechnungen mit Dezimalstellen
- `str` für Texte
- `bool` für Ja/Nein-Entscheidungen
- Immer passenden Typ verwenden
- Bei Unsicherheit: `type()` nutzen

