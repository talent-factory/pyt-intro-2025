# Lektion 4: Dictionaries, Tupel & Sets

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Dictionaries erstellen und verwenden
- Tupel und Sets verstehen
- Unterschiede zwischen Datenstrukturen kennen
- Richtige Datenstruktur wählen

## 📖 Theorie (15 Min)

### Dictionaries

**Schlüssel-Wert-Paare:**

```python
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}

# Zugriff
print(person["name"])  # Anna
print(person.get("beruf", "Unbekannt"))  # Unbekannt

# Ändern/Hinzufügen
person["alter"] = 26
person["beruf"] = "Entwicklerin"

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

### Tupel

**Unveränderbare** Sequenzen:

```python
koordinaten = (10, 20)
person = ("Anna", 25, "Zürich")

# Zugriff wie bei Listen
print(koordinaten[0])  # 10

# NICHT möglich:
# koordinaten[0] = 15  # Fehler!

# Mehrere Rückgabewerte
def statistik(zahlen):
    return min(zahlen), max(zahlen), sum(zahlen)/len(zahlen)

min_wert, max_wert, avg = statistik([1, 2, 3, 4, 5])
```

### Sets

**Eindeutige** Elemente, **ungeordnet**:

```python
zahlen = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Mengenoperationen
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Vereinigung: {1, 2, 3, 4, 5, 6}
print(a & b)  # Schnittmenge: {3, 4}
print(a - b)  # Differenz: {1, 2}
```

### Vergleich

| Typ | Veränderbar | Geordnet | Duplikate | Syntax |
|-----|-------------|----------|-----------|--------|
| Liste | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| Tupel | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| Set | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| Dict | ✅ | ✅ | Keys: ❌ | `{"a": 1}` |

## 💻 Live-Coding (20 Min)

### Beispiel 1: Kontakte mit Dictionary

```python
studenten = {
    "anna": {"alter": 20, "noten": [5.5, 6.0, 5.0]},
    "max": {"alter": 22, "noten": [4.5, 5.0, 5.5]}
}

for name, daten in studenten.items():
    durchschnitt = sum(daten["noten"]) / len(daten["noten"])
    print(f"{name}: {durchschnitt:.2f}")
```

### Beispiel 2: Tupel für Koordinaten

```python
def berechne_distanz(punkt1, punkt2):
    """Berechnet Distanz zwischen zwei Punkten."""
    x1, y1 = punkt1
    x2, y2 = punkt2
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

p1 = (0, 0)
p2 = (3, 4)
print(f"Distanz: {berechne_distanz(p1, p2)}")  # 5.0
```

### Beispiel 3: Sets für Duplikate

```python
def eindeutige_woerter(text):
    """Findet alle eindeutigen Wörter."""
    return set(text.lower().split())

text = "Python ist toll Python macht Spass"
eindeutig = eindeutige_woerter(text)
print(f"Eindeutige Wörter: {eindeutig}")

# Teilnehmer in zwei Kursen
kurs_a = {"Anna", "Max", "Lisa"}
kurs_b = {"Lisa", "Tom", "Sara"}

print(f"In beiden: {kurs_a & kurs_b}")  # {'Lisa'}
print(f"Alle: {kurs_a | kurs_b}")
```

## ✏️ Übungen (15 Min)

- [Übung 6: Dictionary-Operationen](../02-uebungen/uebung-6-dict.md)
- [Übung 7: Verschachtelte Daten](../02-uebungen/uebung-7-verschachtelt.md)
- [Übung 8: Datenverarbeitung](../02-uebungen/uebung-8-verarbeitung.md)

## 📚 Zusammenfassung

- **Dictionaries:** `{"key": "value"}` - Schlüssel-Wert-Paare
- **Tupel:** `(1, 2, 3)` - Unveränderbar, geordnet
- **Sets:** `{1, 2, 3}` - Eindeutig, ungeordnet
- Wählen Sie die passende Datenstruktur für Ihren Anwendungsfall

## 🎉 Modul abgeschlossen!

Sie haben gelernt:

- ✅ Funktionen definieren
- ✅ Parameter und Return
- ✅ Listen, Dictionaries, Tupel, Sets
- ✅ Code modular strukturieren

**Weiter:** [Hausaufgaben](../03-nachbearbeitung/)
