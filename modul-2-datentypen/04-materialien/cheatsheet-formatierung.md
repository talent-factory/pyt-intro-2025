# Cheatsheet: String-Formatierung

## f-Strings (empfohlen)

### Basis
```python
name = "Anna"
alter = 25
print(f"Ich bin {name}, {alter} Jahre alt")
# Ich bin Anna, 25 Jahre alt
```

### Ausdrücke
```python
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
# 5 + 3 = 8

print(f"Doppelt: {a * 2}")
# Doppelt: 10
```

### Methoden aufrufen
```python
name = "anna"
print(f"Hallo {name.upper()}!")
# Hallo ANNA!
```

## Zahlen formatieren

### Dezimalstellen
```python
pi = 3.14159

print(f"{pi:.2f}")    # 3.14 (2 Dezimalstellen)
print(f"{pi:.4f}")    # 3.1416 (4 Dezimalstellen)
print(f"{pi:.0f}")    # 3 (keine Dezimalstellen)
```

### Breite
```python
zahl = 42

print(f"{zahl:5d}")    # '   42' (5 Zeichen breit)
print(f"{zahl:05d}")   # '00042' (mit Nullen auffüllen)
```

### Vorzeichen
```python
zahl = 42

print(f"{zahl:+d}")    # +42 (immer Vorzeichen)
print(f"{zahl: d}")    # ' 42' (Leerzeichen für positive)
```

### Tausender-Trennzeichen
```python
zahl = 1000000

print(f"{zahl:,}")     # 1,000,000
print(f"{zahl:_}")     # 1_000_000
```

### Prozent
```python
anteil = 0.756

print(f"{anteil:.1%}")  # 75.6%
print(f"{anteil:.2%}")  # 75.60%
```

## Ausrichtung

### Links, Rechts, Zentriert
```python
text = "Hallo"

print(f"{text:<10}")   # 'Hallo     ' (links)
print(f"{text:>10}")   # '     Hallo' (rechts)
print(f"{text:^10}")   # '  Hallo   ' (zentriert)
```

### Mit Füllzeichen
```python
text = "Hallo"

print(f"{text:*<10}")  # 'Hallo*****'
print(f"{text:*>10}")  # '*****Hallo'
print(f"{text:*^10}")  # '**Hallo***'
```

## Zahlen-Systeme

```python
zahl = 42

print(f"{zahl:b}")     # 101010 (binär)
print(f"{zahl:o}")     # 52 (oktal)
print(f"{zahl:x}")     # 2a (hexadezimal klein)
print(f"{zahl:X}")     # 2A (hexadezimal gross)
```

## Kombinationen

```python
preis = 19.99

# Breite + Dezimalstellen
print(f"{preis:10.2f}")    # '     19.99'

# Nullen + Dezimalstellen
print(f"{preis:08.2f}")    # '00019.99'

# Rechts + Dezimalstellen
print(f"{preis:>10.2f}")   # '     19.99'
```

## Datum & Zeit

```python
from datetime import datetime

jetzt = datetime.now()

print(f"{jetzt:%Y-%m-%d}")           # 2025-01-19
print(f"{jetzt:%H:%M:%S}")           # 14:30:45
print(f"{jetzt:%d.%m.%Y %H:%M}")     # 19.01.2025 14:30
```

## Spezielle Fälle

### Geschweifte Klammern
```python
print(f"{{Hallo}}")    # {Hallo}
```

### Gleichheitszeichen (Debug)
```python
name = "Anna"
print(f"{name=}")      # name='Anna'
```

### Mehrzeilig
```python
name = "Anna"
alter = 25
text = f"""
Name: {name}
Alter: {alter}
"""
```

## Format-Spezifikation

```
{wert:füllzeichen ausrichtung vorzeichen breite gruppierung .präzision typ}
```

### Beispiele
```python
zahl = 42.123456

f"{zahl:0>10.2f}"
#  │ │ │  │  │ └─ Typ: float
#  │ │ │  │  └─── Präzision: 2 Dezimalstellen
#  │ │ │  └────── Breite: 10 Zeichen
#  │ │ └───────── Vorzeichen: (leer)
#  │ └─────────── Ausrichtung: rechts (>)
#  └───────────── Füllzeichen: 0

# Ergebnis: '0000042.12'
```

## Häufige Muster

```python
# Preis formatieren
preis = 19.99
print(f"CHF {preis:.2f}")  # CHF 19.99

# Prozent
anteil = 0.756
print(f"{anteil:.1%}")     # 75.6%

# Tabelle
for i in range(1, 6):
    print(f"{i:2d} | {i**2:3d} | {i**3:4d}")
# 1 |   1 |    1
# 2 |   4 |    8
# 3 |   9 |   27
# ...

# Fortschrittsbalken
prozent = 0.65
balken = "█" * int(prozent * 20)
print(f"[{balken:<20}] {prozent:.0%}")
# [█████████████       ] 65%
```

## Alte Methoden (nicht empfohlen)

### format()
```python
"Ich bin {}, {} Jahre alt".format("Anna", 25)
"Ich bin {name}, {alter} Jahre alt".format(name="Anna", alter=25)
```

### %-Formatierung
```python
"Ich bin %s, %d Jahre alt" % ("Anna", 25)
"%10.2f" % 19.99
```

## Tipps

✅ **Verwende f-Strings** (ab Python 3.6)
- Lesbarer
- Schneller
- Weniger fehleranfällig

✅ **Formatierung für Ausgabe, nicht für Logik**
```python
# ❌ Schlecht
zahl_str = f"{zahl:.2f}"
zahl_float = float(zahl_str)

# ✅ Gut
print(f"{zahl:.2f}")  # Nur für Ausgabe
```

