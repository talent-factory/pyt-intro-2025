# Lektion 4: Interaktive Programme erstellen

**Dauer:** 50 Minuten  
**Format:** 10 Min Theorie + 20 Min Live-Coding + 20 Min Übung

## 🎯 Lernziele

- Alle Konzepte kombinieren
- Benutzerfreundliche Programme erstellen
- Eingaben validieren
- Best Practices anwenden

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

**4. Eingabe-Validierung:**
```python
alter_str = input("Alter: ")
if alter_str.isdigit():
    alter = int(alter_str)
else:
    print("Ungültige Eingabe!")
```

### 1.2 Programm-Struktur

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

## 💻 Teil 2: Live-Coding (20 Min)

### Beispiel 1: BMI-Rechner

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

### Beispiel 2: Währungsrechner

```python
"""
Währungsrechner
Rechnet CHF in EUR um
"""

print("=" * 40)
print("    Währungsrechner CHF → EUR")
print("=" * 40)
print()

# Wechselkurs (Beispiel)
KURS_EUR = 0.95

# Eingabe
betrag_chf = float(input("Betrag in CHF: "))

# Berechnung
betrag_eur = betrag_chf * KURS_EUR

# Ausgabe
print()
print(f"{betrag_chf:.2f} CHF = {betrag_eur:.2f} EUR")
print(f"(Kurs: 1 CHF = {KURS_EUR} EUR)")
```

### Beispiel 3: Quiz-Programm

```python
"""
Einfaches Quiz
Stellt Fragen und zählt Punkte
"""

print("=" * 40)
print("         Python Quiz")
print("=" * 40)
print()

punkte = 0

# Frage 1
print("Frage 1: Was ist 5 + 3?")
antwort1 = input("Ihre Antwort: ")
if antwort1 == "8":
    print("✓ Richtig!")
    punkte += 1
else:
    print("✗ Falsch! Richtig wäre: 8")
print()

# Frage 2
print("Frage 2: Wie viele Buchstaben hat 'Python'?")
antwort2 = input("Ihre Antwort: ")
if antwort2 == "6":
    print("✓ Richtig!")
    punkte += 1
else:
    print("✗ Falsch! Richtig wäre: 6")
print()

# Frage 3
print("Frage 3: Ist Python eine Programmiersprache? (ja/nein)")
antwort3 = input("Ihre Antwort: ").lower()
if antwort3 == "ja":
    print("✓ Richtig!")
    punkte += 1
else:
    print("✗ Falsch! Richtig wäre: ja")
print()

# Ergebnis
print("=" * 40)
print(f"Ergebnis: {punkte} von 3 Punkten")
if punkte == 3:
    print("Perfekt! 🌟")
elif punkte >= 2:
    print("Gut gemacht! 👍")
else:
    print("Weiter üben! 📚")
print("=" * 40)
```

---

## ✏️ Teil 3: Übung (20 Min)

### Übung 4: Interaktiver Rechner

Siehe [02-uebungen/uebung-4-rechner.md](../02-uebungen/uebung-4-rechner.md)

**Aufgabe:**

Erstellen Sie einen interaktiven Rechner, der:

1. Nach zwei Zahlen fragt
2. Alle Grundrechenarten durchführt
3. Die Ergebnisse formatiert ausgibt
4. Benutzerfreundlich gestaltet ist

**Anforderungen:**

- Titel mit Linien
- Klare Eingabeaufforderungen
- Formatierte Ausgabe (2 Dezimalstellen)
- Visuelle Trennung

**Beispiel-Ausgabe:**

```
========================================
        Interaktiver Rechner
========================================

Erste Zahl: 10
Zweite Zahl: 3

========================================
Ergebnisse:
----------------------------------------
10.00 + 3.00 = 13.00
10.00 - 3.00 = 7.00
10.00 * 3.00 = 30.00
10.00 / 3.00 = 3.33
========================================
```

---

## 📝 Zusammenfassung

- **Kombination** aller Konzepte
- **Benutzerfreundlichkeit** ist wichtig
- **Struktur:** Titel → Eingabe → Verarbeitung → Ausgabe
- **Formatierung** mit F-Strings
- **Visuelle Elemente** (Linien, Leerzeilen)

## 🎯 Lernzielkontrolle

- ✅ Alle Konzepte kombinieren?
- ✅ Benutzerfreundliche Programme?
- ✅ Eingaben verarbeiten?
- ✅ Formatierte Ausgaben?

## 📚 Nächste Schritte

- Hausaufgaben in [03-nachbearbeitung](../03-nachbearbeitung/)
- Beispielcode in [05-beispiele](../05-beispiele/)
- Materialien in [04-materialien](../04-materialien/)

