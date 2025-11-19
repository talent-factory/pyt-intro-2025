# Lektion 2: Boolsche Werte und Vergleiche

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Boolsche Werte (`True`/`False`) verstehen
- Vergleichsoperatoren anwenden
- Logische Operatoren nutzen
- Wahrheitswerte anderer Typen kennen

---

## 📖 Teil 1: Theorie (15 Min)

### 1.1 Boolsche Werte

**Boolean** kann nur zwei Werte haben: `True` oder `False`

```python
ist_student = True
ist_rentner = False
```

**Wichtig:** Gross-/Kleinschreibung beachten!

### 1.2 Vergleichsoperatoren

| Operator | Bedeutung | Beispiel | Ergebnis |
|----------|-----------|----------|----------|
| `==` | Gleich | `5 == 5` | `True` |
| `!=` | Ungleich | `5 != 3` | `True` |
| `<` | Kleiner | `3 < 5` | `True` |
| `>` | Grösser | `5 > 3` | `True` |
| `<=` | Kleiner/gleich | `5 <= 5` | `True` |
| `>=` | Grösser/gleich | `3 >= 5` | `False` |

```python
alter = 18
ist_volljaehrig = alter >= 18  # True

temperatur = 25
ist_warm = temperatur > 20     # True
```

### 1.3 Logische Operatoren

**`and`** - Beide müssen wahr sein:
```python
alter = 25
hat_fuehrerschein = True
darf_fahren = alter >= 18 and hat_fuehrerschein  # True
```

**`or`** - Mindestens eine muss wahr sein:
```python
ist_wochenende = True
ist_feiertag = False
ist_frei = ist_wochenende or ist_feiertag  # True
```

**`not`** - Negation:
```python
ist_regen = False
ist_trocken = not ist_regen  # True
```

### 1.4 Wahrheitswerte

Andere Typen haben auch Wahrheitswerte:

```python
bool(1)      # True
bool(0)      # False
bool("")     # False (leerer String)
bool("Hi")   # True
bool([])     # False (leere Liste)
bool([1])    # True
```

---

## 💻 Teil 2: Live-Coding (20 Min)

### Beispiel 1: Alterscheck

```python
"""
Alterscheck
Prüft verschiedene Altersgrenzen
"""

alter = 20

# Einzelne Prüfungen
ist_volljaehrig = alter >= 18
ist_senior = alter >= 65
ist_kind = alter < 12

print(f"Alter: {alter}")
print(f"Volljährig: {ist_volljaehrig}")
print(f"Senior: {ist_senior}")
print(f"Kind: {ist_kind}")

# Kombinierte Prüfungen
ist_erwachsen_nicht_senior = alter >= 18 and alter < 65
print(f"Erwachsen (nicht Senior): {ist_erwachsen_nicht_senior}")
```

### Beispiel 2: Zugangskontrolle

```python
"""
Zugangskontrolle
Prüft ob Zugang erlaubt ist
"""

alter = 25
hat_ticket = True
ist_mitglied = False

# Zugang erlaubt wenn:
# - Alter >= 18 UND Ticket vorhanden
# - ODER Mitglied
zugang_erlaubt = (alter >= 18 and hat_ticket) or ist_mitglied

print(f"Alter: {alter}")
print(f"Ticket: {hat_ticket}")
print(f"Mitglied: {ist_mitglied}")
print(f"Zugang erlaubt: {zugang_erlaubt}")
```

### Beispiel 3: String-Vergleiche

```python
"""
String-Vergleiche
Vergleicht Texte
"""

name1 = "Anna"
name2 = "anna"
name3 = "Anna"

print(f"'{name1}' == '{name2}': {name1 == name2}")  # False
print(f"'{name1}' == '{name3}': {name1 == name3}")  # True

# Case-insensitive Vergleich
print(f"Gleich (ignoriert Gross/Klein): {name1.lower() == name2.lower()}")

# Weitere Vergleiche
text = "Python"
print(f"Beginnt mit 'Py': {text.startswith('Py')}")
print(f"Endet mit 'on': {text.endswith('on')}")
print(f"Enthält 'th': {'th' in text}")
```

---

## ✏️ Teil 3: Übung (15 Min)

### Übung 2: Vergleiche und Bedingungen

Siehe [02-uebungen/uebung-2-vergleiche.md](../02-uebungen/uebung-2-vergleiche.md)

**Aufgabe:**

Erstellen Sie ein Programm, das:

1. Variablen für Alter, Temperatur und Name definiert
2. Verschiedene Vergleiche durchführt
3. Logische Operatoren verwendet
4. Die Ergebnisse ausgibt

**Beispiel:**

```python
alter = 20
temperatur = 25
name = "Max"

# Vergleiche
print(f"Volljährig: {alter >= 18}")
print(f"Warm: {temperatur > 20}")
print(f"Name ist Max: {name == 'Max'}")

# Kombiniert
print(f"Volljährig UND warm: {alter >= 18 and temperatur > 20}")
```

---

## 📝 Zusammenfassung

- **Boolean:** `True` oder `False`
- **Vergleiche:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logisch:** `and`, `or`, `not`
- **Wahrheitswerte:** Andere Typen haben auch bool-Werte

## 🎯 Lernzielkontrolle

- ✅ Boolsche Werte verstehen?
- ✅ Vergleichsoperatoren anwenden?
- ✅ Logische Operatoren nutzen?

