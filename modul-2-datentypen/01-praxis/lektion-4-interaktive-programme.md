# Lektion 4: Interaktive Programme & Vertiefung

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 25 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Alle Konzepte kombinieren
- Benutzerfreundliche Programme erstellen
- Eingaben validieren
- Erweiterte String-Methoden anwenden
- Fehlerbehandlung verstehen

---

## 📖 Teil 1: Theorie (10 Min)

### 1.1 Best Practices für interaktive Programme

**1. Klare Anweisungen:**

```python
# Schlecht:
name = input()

# Gut:
name = input("Bitte geben Sie Ihren Namen ein: ")
```

**2. Formatierte Ausgaben:**

```python
# Schlecht:
print(name, alter, stadt)

# Gut:
print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")
```

**3. Visuelle Trennung:**

```python
print("=" * 40)
print("Titel")
print("=" * 40)
```

### 1.2 Eingabe-Validierung & Fehlerbehandlung

```python
# Mit String-Methoden
alter_str = input("Alter: ")
if alter_str.isdigit():
    alter = int(alter_str)
else:
    print("Ungültige Eingabe!")

# Mit try-except
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Ungültige Eingabe!")
    alter = 0
```

### 1.3 Programm-Struktur

```python
# 1. Titel/Begrüssung
print("=== Programm-Titel ===\n")

# 2. Eingaben sammeln
name = input("Name: ")
alter = int(input("Alter: "))

# 3. Verarbeitung
ergebnis = alter + 1

# 4. Ausgabe
print(f"\nErgebnis: {ergebnis}")
```

---

## 💻 Teil 2: Live-Coding (25 Min)

### Beispiel 1: BMI-Rechner (10 Min)

```python
"""
BMI-Rechner
Berechnet den Body-Mass-Index
"""

print("=" * 40)
print("       BMI-Rechner")
print("=" * 40)
print()

# Eingaben
name = input("Ihr Name: ")
groesse_cm = float(input("Körpergrösse (cm): "))
gewicht_kg = float(input("Gewicht (kg): "))

# Verarbeitung
groesse_m = groesse_cm / 100
bmi = gewicht_kg / (groesse_m ** 2)

# Bewertung (vereinfacht)
if bmi < 18.5:
    bewertung = "Untergewicht"
elif bmi < 25:
    bewertung = "Normalgewicht"
elif bmi < 30:
    bewertung = "Übergewicht"
else:
    bewertung = "Starkes Übergewicht"

# Ausgabe
print()
print("=" * 40)
print(f"Ergebnis für {name}:")
print(f"BMI: {bmi:.1f}")
print(f"Bewertung: {bewertung}")
print("=" * 40)
```

### Beispiel 2: Passwort-Validator (10 Min)

```python
"""Passwort-Validator mit mehreren Kriterien"""

print("=== PASSWORT-VALIDATOR ===\n")

passwort = input("Passwort: ")
fehler = []

# Mindestlänge
if len(passwort) < 8:
    fehler.append("Mindestens 8 Zeichen")

# Grossbuchstabe
hat_gross = False
for zeichen in passwort:
    if zeichen.isupper():
        hat_gross = True
        break
if not hat_gross:
    fehler.append("Mindestens 1 Grossbuchstabe")

# Zahl
hat_zahl = False
for zeichen in passwort:
    if zeichen.isdigit():
        hat_zahl = True
        break
if not hat_zahl:
    fehler.append("Mindestens 1 Zahl")

# Ergebnis
if len(fehler) == 0:
    print("✓ Passwort ist gültig!")
else:
    print("\n✗ Passwort ungültig:")
    for fehler_text in fehler:
        print(f"  - {fehler_text}")
```

### Beispiel 3: Text-Statistik (5 Min)

```python
"""Erweiterte Textanalyse"""

text = input("Text eingeben:\n")

# Statistiken
anzahl_zeichen = len(text)
anzahl_woerter = len(text.split())
anzahl_buchstaben = 0
anzahl_zahlen = 0

for zeichen in text:
    if zeichen.isalpha():
        anzahl_buchstaben += 1
    elif zeichen.isdigit():
        anzahl_zahlen += 1

# Ausgabe
print("\n" + "=" * 40)
print("TEXTANALYSE")
print("=" * 40)
print(f"Zeichen gesamt:        {anzahl_zeichen:6d}")
print(f"Buchstaben:            {anzahl_buchstaben:6d}")
print(f"Zahlen:                {anzahl_zahlen:6d}")
print(f"Wörter:                {anzahl_woerter:6d}")
print("=" * 40)
```

---

## ✏️ Teil 3: Übung (15 Min)

### Übung 4-8

Wählen Sie eine der Übungen aus [02-uebungen](../02-uebungen/):

- **Übung 4:** Interaktiver Rechner
- **Übung 5:** String-Methoden
- **Übung 6:** Formatierung
- **Übung 7:** Input-Validierung
- **Übung 8:** Textanalyse

---

## 📝 Zusammenfassung

- **Kombination** aller Konzepte
- **Benutzerfreundlichkeit** ist wichtig
- **Struktur:** Titel → Eingabe → Verarbeitung → Ausgabe
- **Formatierung** mit F-Strings
- **Validierung** mit String-Methoden und try-except
- **Visuelle Elemente** (Linien, Leerzeilen)

## 🎯 Lernzielkontrolle

- ✅ Alle Konzepte kombinieren?
- ✅ Benutzerfreundliche Programme?
- ✅ Eingaben verarbeiten und validieren?
- ✅ Formatierte Ausgaben?
- ✅ Fehlerbehandlung verstehen?

## 🎓 Abschluss Modul 2

Herzlichen Glückwunsch! Sie haben Modul 2 abgeschlossen.

**Nächste Schritte:**

- Hausaufgaben in [03-nachbearbeitung](../03-nachbearbeitung/)
- Beispielcode in [05-beispiele](../05-beispiele/)
- Materialien in [04-materialien](../04-materialien/)
