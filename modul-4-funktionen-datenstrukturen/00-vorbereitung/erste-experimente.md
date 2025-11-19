# Erste Experimente

**Dauer:** ca. 60 Minuten

## 🎯 Ziel

Erste praktische Erfahrungen mit Funktionen und Datenstrukturen sammeln.

## 💻 Experiment 1: Erste Funktion (15 Min)

Erstellen Sie `funktion_test.py`:

```python
def quadrat(zahl):
    """Berechnet das Quadrat einer Zahl."""
    return zahl ** 2

# Testen
print(quadrat(5))   # 25
print(quadrat(10))  # 100
```

**Aufgaben:**
1. Funktion erstellen und testen
2. Weitere Funktion `wuerfel(zahl)` hinzufügen
3. Funktion `ist_gerade(zahl)` erstellen (gibt True/False zurück)

## 💻 Experiment 2: Listen (15 Min)

Erstellen Sie `listen_test.py`:

```python
# Liste erstellen
einkaufsliste = ["Apfel", "Banane", "Orange"]

# Ausgeben
print(einkaufsliste)

# Hinzufügen
einkaufsliste.append("Kiwi")

# Entfernen
einkaufsliste.remove("Banane")

# Durchlaufen
for item in einkaufsliste:
    print(f"- {item}")
```

**Aufgaben:**
1. Liste mit 5 Lieblings-Früchten erstellen
2. 2 weitere hinzufügen
3. Erste entfernen
4. Alle ausgeben

## 💻 Experiment 3: Dictionaries (15 Min)

Erstellen Sie `dict_test.py`:

```python
# Person erstellen
person = {
    "name": "Anna Muster",
    "alter": 25,
    "stadt": "Zürich",
    "beruf": "Entwicklerin"
}

# Ausgeben
print(f"{person['name']} ist {person['alter']} Jahre alt")

# Ändern
person["alter"] = 26

# Hinzufügen
person["hobby"] = "Programmieren"

# Alle Schlüssel
for key in person:
    print(f"{key}: {person[key]}")
```

**Aufgaben:**
1. Dictionary für sich selbst erstellen
2. Mindestens 5 Eigenschaften
3. Eine Eigenschaft ändern
4. Zwei neue hinzufügen
5. Alle ausgeben

## 💻 Experiment 4: Kombination (15 Min)

Erstellen Sie `kombination_test.py`:

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste."""
    if len(zahlen) == 0:
        return 0
    return sum(zahlen) / len(zahlen)

# Testen
noten = [5.5, 4.0, 5.0, 6.0, 4.5]
durchschnitt = berechne_durchschnitt(noten)
print(f"Durchschnitt: {durchschnitt:.2f}")

# Liste von Dictionaries
studenten = [
    {"name": "Anna", "note": 5.5},
    {"name": "Bob", "note": 4.0},
    {"name": "Clara", "note": 6.0}
]

# Durchlaufen
for student in studenten:
    print(f"{student['name']}: {student['note']}")
```

**Aufgaben:**
1. Funktion `finde_maximum(zahlen)` erstellen
2. Funktion `finde_minimum(zahlen)` erstellen
3. Liste mit 3 Büchern erstellen (Dictionary pro Buch)
4. Alle Bücher ausgeben

## ✅ Checkliste

- [ ] Experiment 1 abgeschlossen
- [ ] Experiment 2 abgeschlossen
- [ ] Experiment 3 abgeschlossen
- [ ] Experiment 4 abgeschlossen
- [ ] Alle Programme funktionieren

**Weiter zu:** [Quiz](./quiz.md)

