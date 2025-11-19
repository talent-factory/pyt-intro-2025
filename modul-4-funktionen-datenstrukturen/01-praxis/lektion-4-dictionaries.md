# Lektion 4: Dictionaries

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Dictionaries erstellen und verwenden
- Auf Werte zugreifen
- Dictionaries manipulieren
- Über Dictionaries iterieren

## 📖 Theorie (15 Min)

### Was sind Dictionaries?

Dictionaries speichern **Schlüssel-Wert-Paare**:

```python
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}
```

### Zugriff auf Werte

```python
# Mit Schlüssel
print(person["name"])  # Anna

# Mit get() (sicherer)
print(person.get("alter"))  # 25
print(person.get("beruf", "Unbekannt"))  # Unbekannt
```

### Werte ändern und hinzufügen

```python
# Ändern
person["alter"] = 26

# Hinzufügen
person["beruf"] = "Entwicklerin"

# Löschen
del person["stadt"]
```

### Dictionary-Methoden

```python
# Alle Schlüssel
keys = person.keys()

# Alle Werte
values = person.values()

# Alle Paare
items = person.items()
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Kontaktverwaltung

```python
kontakt = {
    "name": "Max Muster",
    "email": "max@example.com",
    "telefon": "079 123 45 67"
}

print("=" * 40)
print("KONTAKT")
print("=" * 40)
for key, value in kontakt.items():
    print(f"{key.capitalize()}: {value}")
```

### Beispiel 2: Wörterbuch

```python
woerterbuch = {
    "hello": "hallo",
    "world": "welt",
    "python": "python"
}

def uebersetze(wort):
    """Übersetzt ein englisches Wort ins Deutsche."""
    return woerterbuch.get(wort.lower(), "Nicht gefunden")

print(uebersetze("hello"))  # hallo
print(uebersetze("test"))   # Nicht gefunden
```

### Beispiel 3: Verschachtelte Dictionaries

```python
studenten = {
    "anna": {
        "alter": 20,
        "noten": [5.5, 6.0, 5.0]
    },
    "max": {
        "alter": 22,
        "noten": [4.5, 5.0, 5.5]
    }
}

# Zugriff
print(studenten["anna"]["alter"])  # 20
print(studenten["max"]["noten"])   # [4.5, 5.0, 5.5]

# Durchschnitt berechnen
for name, daten in studenten.items():
    durchschnitt = sum(daten["noten"]) / len(daten["noten"])
    print(f"{name}: {durchschnitt:.2f}")
```

## ✏️ Übungen (15 Min)

- [Übung 6: Dictionary-Operationen](../02-uebungen/uebung-6-dict.md)

## 📚 Zusammenfassung

- Dictionaries: `{"key": "value"}`
- Zugriff: `dict["key"]` oder `dict.get("key")`
- Methoden: keys(), values(), items()
- Iteration: `for key, value in dict.items():`

## 🔗 Weiter

- [Lektion 5: Tupel & Sets](./lektion-5-tupel-sets.md)

