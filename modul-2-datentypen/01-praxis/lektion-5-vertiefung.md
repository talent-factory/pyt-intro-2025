# Lektion 5: Vertiefung & Praxis

**Dauer:** 50 Minuten  
**Format:** 10 Min Theorie + 25 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- String-Methoden vertiefen
- Komplexe Formatierung
- Input-Validierung
- Fehlerbehandlung

## 📖 Theorie (10 Min)

### Erweiterte String-Methoden

```python
text = "  Hallo Welt  "

# Whitespace
text.strip()      # "Hallo Welt"
text.lstrip()     # "Hallo Welt  "
text.rstrip()     # "  Hallo Welt"

# Suchen
text.find("Welt")     # 8 (Index)
text.index("Welt")    # 8 (wirft Error wenn nicht gefunden)
text.count("l")       # 3

# Prüfen
text.startswith("H")  # False (wegen Leerzeichen)
text.strip().startswith("H")  # True
text.endswith("t")    # False (wegen Leerzeichen)
```

### Fehlerbehandlung

```python
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Ungültige Eingabe!")
    alter = 0
```

## 💻 Live-Coding (25 Min)

### Beispiel 1: Passwort-Validator

```python
"""Passwort-Validator mit mehreren Kriterien"""

def validiere_passwort(passwort: str) -> tuple[bool, list[str]]:
    """
    Validiert ein Passwort.
    
    Returns:
        (ist_gueltig, fehler_liste)
    """
    fehler = []
    
    # Mindestlänge
    if len(passwort) < 8:
        fehler.append("Mindestens 8 Zeichen")
    
    # Grossbuchstabe
    if not any(c.isupper() for c in passwort):
        fehler.append("Mindestens 1 Grossbuchstabe")
    
    # Kleinbuchstabe
    if not any(c.islower() for c in passwort):
        fehler.append("Mindestens 1 Kleinbuchstabe")
    
    # Zahl
    if not any(c.isdigit() for c in passwort):
        fehler.append("Mindestens 1 Zahl")
    
    # Sonderzeichen
    sonderzeichen = "!@#$%^&*"
    if not any(c in sonderzeichen for c in passwort):
        fehler.append("Mindestens 1 Sonderzeichen (!@#$%^&*)")
    
    return len(fehler) == 0, fehler


# Hauptprogramm
print("=== PASSWORT-VALIDATOR ===\n")

while True:
    passwort = input("Passwort: ")
    
    ist_gueltig, fehler = validiere_passwort(passwort)
    
    if ist_gueltig:
        print("✓ Passwort ist gültig!")
        break
    else:
        print("\n✗ Passwort ungültig:")
        for fehler_text in fehler:
            print(f"  - {fehler_text}")
        print()
```

### Beispiel 2: Formatierte Tabelle

```python
"""Produktliste mit formatierter Ausgabe"""

produkte = [
    {"name": "Apfel", "menge": 10, "preis": 2.50},
    {"name": "Banane", "menge": 5, "preis": 3.20},
    {"name": "Orange", "menge": 15, "preis": 1.80},
    {"name": "Kiwi", "menge": 8, "preis": 4.50},
]

print("PRODUKTLISTE")
print("=" * 50)
print(f"{'Nr':>3} {'Produkt':<20} {'Menge':>6} {'Preis CHF':>10}")
print("-" * 50)

gesamt_menge = 0
gesamt_preis = 0.0

for i, produkt in enumerate(produkte, start=1):
    name = produkt["name"]
    menge = produkt["menge"]
    preis = produkt["preis"]
    
    print(f"{i:3d} {name:<20} {menge:6d} {preis:10.2f}")
    
    gesamt_menge += menge
    gesamt_preis += preis * menge

print("=" * 50)
print(f"{'Gesamt:':<24} {gesamt_menge:6d} {gesamt_preis:10.2f}")
```

### Beispiel 3: Text-Statistik

```python
"""Erweiterte Textanalyse"""

text = input("Text eingeben:\n")

# Statistiken
anzahl_zeichen = len(text)
anzahl_zeichen_ohne_leer = len(text.replace(" ", ""))
anzahl_woerter = len(text.split())
anzahl_saetze = text.count(".") + text.count("!") + text.count("?")

# Zeichen zählen
anzahl_buchstaben = sum(c.isalpha() for c in text)
anzahl_zahlen = sum(c.isdigit() for c in text)
anzahl_leerzeichen = text.count(" ")

# Ausgabe
print("\n" + "=" * 40)
print("TEXTANALYSE")
print("=" * 40)
print(f"Zeichen gesamt:        {anzahl_zeichen:6d}")
print(f"Zeichen ohne Leer:     {anzahl_zeichen_ohne_leer:6d}")
print(f"Buchstaben:            {anzahl_buchstaben:6d}")
print(f"Zahlen:                {anzahl_zahlen:6d}")
print(f"Leerzeichen:           {anzahl_leerzeichen:6d}")
print(f"Wörter:                {anzahl_woerter:6d}")
print(f"Sätze:                 {anzahl_saetze:6d}")

if anzahl_saetze > 0:
    durchschnitt = anzahl_woerter / anzahl_saetze
    print(f"Wörter/Satz:           {durchschnitt:6.1f}")

print("=" * 40)
```

## ✏️ Übungen (15 Min)

### Übung 5-8
Siehe [Übungen 5-8](../02-uebungen/)

## 📝 Zusammenfassung

- String-Methoden für Validierung
- Try-except für Fehlerbehandlung
- Formatierung für Tabellen
- Komplexe Textanalyse

## 🎓 Abschluss Modul 2

Herzlichen Glückwunsch! Sie haben Modul 2 abgeschlossen.

**Nächste Schritte:**
1. [Nachbearbeitung](../03-nachbearbeitung/)
2. Modul 3 vorbereiten

