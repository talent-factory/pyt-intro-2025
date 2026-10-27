# Lektion 4: Verschachtelte Strukturen & Mini-Projekt

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 20 Min Live-Coding + 20 Min Mini-Projekt

## 🎯 Lernziele

- Verschachtelte Strukturen verstehen (If in If, Schleife in Schleife)
- Komplexe Muster erstellen
- Alle Konzepte in einem Projekt kombinieren

## 📖 Theorie (10 Min)

### If in If (Verschachtelte Bedingungen)

```python
alter = 20
hat_fuehrerschein = True

if alter >= 18:
    if hat_fuehrerschein:
        print("Darf Auto fahren")
    else:
        print("Braucht Führerschein")
else:
    print("Zu jung")
```

### Schleife in Schleife

```python
# Multiplikationstabelle
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

### If in Schleife

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for zahl in zahlen:
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade")
```

### Verschachtelungsarten

| Typ | Beispiel | Verwendung |
|-----|----------|------------|
| If in If | `if x: if y:` | Mehrere Bedingungen |
| Loop in Loop | `for i: for j:` | Muster, Matrizen |
| If in Loop | `for x: if x:` | Filtern |

## 💻 Live-Coding (20 Min)

### Beispiel 1: Muster zeichnen (10 Min)

```python
"""Verschiedene Muster mit verschachtelten Schleifen"""

# Dreieck
print("=== Dreieck ===")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print()

# Pyramide
print("=== Pyramide ===")
hoehe = 5
for i in range(1, hoehe + 1):
    # Leerzeichen
    for j in range(hoehe - i):
        print(" ", end="")
    # Sterne
    for k in range(2 * i - 1):
        print("*", end="")
    print()
```

### Beispiel 2: Schachbrett (5 Min)

```python
"""Schachbrett-Muster"""
groesse = 8

print("=== Schachbrett ===\n")

for zeile in range(groesse):
    for spalte in range(groesse):
        if (zeile + spalte) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()
```

### Beispiel 3: Primzahlen (5 Min)

```python
"""Primzahlen bis N finden"""
n = 30

print(f"Primzahlen bis {n}:")

for zahl in range(2, n + 1):
    ist_primzahl = True

    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            ist_primzahl = False
            break

    if ist_primzahl:
        print(zahl, end=" ")
print()
```

---

## ✏️ Mini-Projekt (20 Min)

Wählen Sie **eines** der folgenden Projekte:

### Option 1: Kontakt-Manager (einfach)

> **Vorgriff:** Dieses Konzept (Dictionaries) wird in Modul 4 behandelt.

```python
kontakte = []

while True:
    print("\n=== KONTAKT-MANAGER ===")
    print("1. Kontakt hinzufügen")
    print("2. Alle Kontakte anzeigen")
    print("3. Beenden")

    wahl = input("Wahl: ")

    if wahl == "1":
        name = input("Name: ")
        telefon = input("Telefon: ")
        kontakte.append({"name": name, "telefon": telefon})
        print("✓ Gespeichert!")
    elif wahl == "2":
        for k in kontakte:
            print(f"- {k['name']}: {k['telefon']}")
    elif wahl == "3":
        break
```

### Option 2: Zahlenraten (einfach)

> **Vorgriff:** Dieses Konzept (z. B. Module importieren) wird in Modul 5 behandelt.

```python
import random

zahl = random.randint(1, 100)
versuche = 0

print("=== ZAHLENRATEN ===")
print("Ich denke an eine Zahl zwischen 1 und 100.")

while True:
    tipp = int(input("Dein Tipp: "))
    versuche += 1

    if tipp < zahl:
        print("Höher!")
    elif tipp > zahl:
        print("Niedriger!")
    else:
        print(f"✓ Richtig! In {versuche} Versuchen!")
        break
```

### Option 3: Hangman (mittel)

> **Vorgriff:** Dieses Konzept (z. B. Module importieren) wird in Modul 5 behandelt.

```python
import random

woerter = ["PYTHON", "PROGRAMMIEREN", "COMPUTER"]
wort = random.choice(woerter)
geraten = []
versuche = 6

print("=== HANGMAN ===")

while versuche > 0:
    # Wort anzeigen
    anzeige = ""
    for b in wort:
        if b in geraten:
            anzeige += b + " "
        else:
            anzeige += "_ "
    print(f"\nWort: {anzeige}")
    print(f"Versuche: {versuche}")

    # Gewonnen?
    if "_" not in anzeige:
        print("🎉 Gewonnen!")
        break

    buchstabe = input("Buchstabe: ").upper()
    geraten.append(buchstabe)

    if buchstabe in wort:
        print("✓ Richtig!")
    else:
        print("✗ Falsch!")
        versuche -= 1

if versuche == 0:
    print(f"Verloren! Das Wort war: {wort}")
```

---

## 📝 Zusammenfassung

### Wichtige Punkte

✅ **DO:**

- Einrückung beachten (4 Leerzeichen pro Ebene)
- Aussagekräftige Variablennamen
- Kommentare bei komplexer Logik

❌ **DON'T:**

- Zu viele Verschachtelungsebenen (max 3-4)
- Unklare Variablennamen

## 🎓 Abschluss Modul 3

Herzlichen Glückwunsch! Sie haben Modul 3 abgeschlossen.

**Nächste Schritte:**

1. [Nachbearbeitung](../03-nachbearbeitung/) - Hausaufgaben
2. [Beispiele](../05-beispiele/) - Zum Nachschlagen
3. Modul 4 vorbereiten
