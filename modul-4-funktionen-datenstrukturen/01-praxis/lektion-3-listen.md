# Lektion 3: Listen, Dictionaries & Co.

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

Nach dieser Lektion können Sie:
- Listen-Methoden anwenden
- Dictionaries erstellen und nutzen
- Die richtige Datenstruktur wählen

## 📖 Theorie (15 Min)

### Listen-Methoden (5 Min)

Die wichtigsten Methoden zum Arbeiten mit Listen:

```python
fruechte = ["Apfel", "Banane", "Kirsche"]

# Hinzufügen
fruechte.append("Mango")       # ["Apfel", "Banane", "Kirsche", "Mango"]

# Entfernen
fruechte.remove("Banane")      # ["Apfel", "Kirsche", "Mango"]
letztes = fruechte.pop()       # "Mango" — entfernt und gibt zurück

# Sortieren
zahlen = [3, 1, 4, 1, 5]
zahlen.sort()                  # [1, 1, 3, 4, 5]
```

**Tipp:** Slicing (`liste[1:3]`) kennen Sie bereits aus Modul 3.

### List Comprehensions (Kurzüberblick)

Kompakte Schreibweise zum Erstellen neuer Listen:

```python
quadrate = [x * x for x in range(6)]       # [0, 1, 4, 9, 16, 25]
gerade = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Dictionaries (7 Min)

Dictionaries speichern **Schlüssel-Wert-Paare** — ideal, wenn Sie Daten mit einem Namen ansprechen wollen:

```python
# Erstellen
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}

# Zugriff
print(person["name"])                        # Anna
print(person.get("beruf", "Unbekannt"))      # Unbekannt (kein Fehler)

# Ändern und Hinzufügen
person["alter"] = 26
person["beruf"] = "Entwicklerin"

# Iteration
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")
```

**Wichtig:**
- Schlüssel müssen **eindeutig** sein
- Zugriff mit `[]` löst einen Fehler aus, wenn der Schlüssel fehlt
- Zugriff mit `.get()` gibt stattdessen einen Standardwert zurück

### Vergleichstabelle: Datenstrukturen (3 Min)

| Typ | Veränderbar | Geordnet | Duplikate | Syntax |
|-----|-------------|----------|-----------|--------|
| **Liste** | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| **Tupel** | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| **Set** | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| **Dict** | ✅ | ✅ | Keys: ❌ | `{"a": 1}` |

- **Tupel** sind wie Listen, aber **unveränderbar** — gut für feste Werte wie Koordinaten.
- **Sets** enthalten nur **eindeutige** Elemente — gut zum Entfernen von Duplikaten.

## 💻 Live-Coding (20 Min)

### Beispiel 1: Listen filtern und transformieren

```python
# Einkaufspreise
preise = [12.50, 3.90, 45.00, 8.20, 67.50, 2.10]

# Teure Artikel filtern (über 10 CHF)
teure_artikel = []
for preis in preise:
    if preis > 10:
        teure_artikel.append(preis)

print(f"Teure Artikel: {teure_artikel}")

# Das Gleiche als List Comprehension
teure_artikel = [p for p in preise if p > 10]
print(f"Teure Artikel: {teure_artikel}")

# Preise sortieren
preise.sort()
print(f"Sortiert: {preise}")

# Teuerstes Element entfernen
teuerstes = preise.pop()
print(f"Entfernt: {teuerstes}")
print(f"Übrig: {preise}")
```

### Beispiel 2: Kontakte mit Dictionary

```python
# Kontaktbuch als Dictionary
kontakte = {
    "Anna": {"telefon": "079 123 45 67", "email": "anna@example.ch"},
    "Max": {"telefon": "078 987 65 43", "email": "max@example.ch"},
    "Lisa": {"telefon": "076 555 12 34", "email": "lisa@example.ch"}
}

# Kontakt nachschlagen
name = "Anna"
if name in kontakte:
    daten = kontakte[name]
    print(f"{name}: {daten['telefon']}")

# Neuen Kontakt hinzufügen
kontakte["Tom"] = {"telefon": "077 111 22 33", "email": "tom@example.ch"}

# Alle Kontakte anzeigen
print("=" * 40)
print("Kontaktliste")
print("=" * 40)
for name, daten in kontakte.items():
    print(f"  {name}: {daten['telefon']}")
```

### Beispiel 3: Datenstruktur wählen — gleiches Problem, zwei Lösungen

```python
# Aufgabe: Notenverwaltung für 3 Schüler

# --- Lösung A: Mit Listen ---
namen = ["Anna", "Max", "Lisa"]
noten = [5.5, 4.0, 6.0]

# Note von Max finden
for i in range(len(namen)):
    if namen[i] == "Max":
        print(f"Max hat die Note {noten[i]}")

# --- Lösung B: Mit Dictionary ---
noten_dict = {
    "Anna": 5.5,
    "Max": 4.0,
    "Lisa": 6.0
}

# Note von Max finden
print(f"Max hat die Note {noten_dict['Max']}")

# Fazit: Das Dictionary ist hier übersichtlicher,
# weil wir nach einem Namen suchen.
# Listen sind besser, wenn die Reihenfolge wichtig ist
# oder wir alle Elemente durchgehen wollen.
```

## ✏️ Übungen (15 Min)

- [Übung 5: Listen-Methoden](../02-uebungen/uebung-5-methoden.md)
- [Übung 6: Dictionary-Operationen](../02-uebungen/uebung-6-dict.md)

## 📚 Zusammenfassung

- **Listen-Methoden:** `append`, `remove`, `pop`, `sort`
- **Dictionaries:** `{"key": "value"}` — Zugriff mit `[]` oder `.get()`
- **Datenstruktur wählen:** Liste für Reihenfolge, Dictionary für Zugriff per Name

## 🔗 Weiter

- [Lektion 4: Testing](./lektion-4-testing.md)
