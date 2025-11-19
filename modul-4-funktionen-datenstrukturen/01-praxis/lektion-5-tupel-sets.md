# Lektion 5: Tupel & Sets

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Tupel erstellen und verwenden
- Sets verstehen und anwenden
- Unterschiede zwischen Datenstrukturen kennen
- Richtige Datenstruktur wählen

## 📖 Theorie (15 Min)

### Tupel

**Unveränderbare** Sequenzen:

```python
koordinaten = (10, 20)
person = ("Anna", 25, "Zürich")

# Zugriff wie bei Listen
print(koordinaten[0])  # 10

# NICHT möglich:
# koordinaten[0] = 15  # Fehler!
```

**Verwendung:**
- Feste Datenstrukturen
- Rückgabe mehrerer Werte
- Dictionary-Keys

### Sets

**Eindeutige** Elemente, **ungeordnet**:

```python
zahlen = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
```

**Mengenoperationen:**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Vereinigung
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Schnittmenge
print(a & b)  # {3, 4}

# Differenz
print(a - b)  # {1, 2}
```

### Vergleich

| Typ | Veränderbar | Geordnet | Duplikate | Syntax |
|-----|-------------|----------|-----------|--------|
| Liste | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| Tupel | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| Set | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| Dict | ✅ | ✅* | Keys: ❌ | `{"a": 1}` |

*Ab Python 3.7

## 💻 Live-Coding (20 Min)

### Beispiel 1: Tupel für Koordinaten

```python
def berechne_distanz(punkt1, punkt2):
    """Berechnet Distanz zwischen zwei Punkten."""
    x1, y1 = punkt1
    x2, y2 = punkt2
    
    dx = x2 - x1
    dy = y2 - y1
    distanz = (dx**2 + dy**2) ** 0.5
    
    return distanz

p1 = (0, 0)
p2 = (3, 4)
d = berechne_distanz(p1, p2)
print(f"Distanz: {d}")  # 5.0
```

### Beispiel 2: Mehrere Rückgabewerte

```python
def statistik(zahlen):
    """Berechnet Min, Max und Durchschnitt."""
    minimum = min(zahlen)
    maximum = max(zahlen)
    durchschnitt = sum(zahlen) / len(zahlen)
    
    return minimum, maximum, durchschnitt  # Tupel!

werte = [1, 2, 3, 4, 5]
min_wert, max_wert, avg = statistik(werte)

print(f"Min: {min_wert}")
print(f"Max: {max_wert}")
print(f"Durchschnitt: {avg}")
```

### Beispiel 3: Sets für Duplikate entfernen

```python
def eindeutige_woerter(text):
    """Findet alle eindeutigen Wörter."""
    woerter = text.lower().split()
    return set(woerter)

text = "Python ist toll Python macht Spass"
eindeutig = eindeutige_woerter(text)
print(f"Eindeutige Wörter: {eindeutig}")
print(f"Anzahl: {len(eindeutig)}")
```

### Beispiel 4: Set-Operationen

```python
kurs_a = {"Anna", "Max", "Lisa", "Tom"}
kurs_b = {"Lisa", "Tom", "Sara", "Ben"}

# Beide Kurse
alle = kurs_a | kurs_b
print(f"Alle Teilnehmer: {alle}")

# Beide Kurse besuchen
beide = kurs_a & kurs_b
print(f"In beiden Kursen: {beide}")

# Nur Kurs A
nur_a = kurs_a - kurs_b
print(f"Nur Kurs A: {nur_a}")
```

## ✏️ Übungen (15 Min)

- [Übung 7: Verschachtelte Daten](../02-uebungen/uebung-7-verschachtelt.md)
- [Übung 8: Datenverarbeitung](../02-uebungen/uebung-8-verarbeitung.md)

## 📚 Zusammenfassung

- **Tupel:** Unveränderbar, geordnet `(1, 2, 3)`
- **Sets:** Eindeutig, ungeordnet `{1, 2, 3}`
- Tupel für feste Daten, Sets für Eindeutigkeit
- Mengenoperationen: `|`, `&`, `-`

## 🎉 Modul abgeschlossen!

Sie haben gelernt:
- ✅ Funktionen definieren
- ✅ Parameter und Return
- ✅ Listen, Dictionaries, Tupel, Sets
- ✅ Code modular strukturieren

**Weiter:** [Hausaufgaben](../03-nachbearbeitung/)

