# Lektion 4: Verschachtelte Strukturen

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- If in If verstehen
- Schleife in Schleife nutzen
- If in Schleife anwenden
- Komplexe Muster erstellen

## 📖 Theorie (15 Min)

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
    else:
        print(f"{zahl} ist ungerade")
```

### Schleife in If

```python
ist_wochenende = True

if ist_wochenende:
    aktivitaeten = ["Ausschlafen", "Sport", "Freunde"]
    for aktivitaet in aktivitaeten:
        print(f"- {aktivitaet}")
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Muster zeichnen

```python
"""Verschiedene Muster mit verschachtelten Schleifen"""

# Rechteck
print("=== Rechteck ===")
for i in range(5):
    for j in range(8):
        print("*", end="")
    print()

print()

# Dreieck
print("=== Dreieck ===")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print()

# Umgekehrtes Dreieck
print("=== Umgekehrtes Dreieck ===")
for i in range(5, 0, -1):
    for j in range(i):
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

### Beispiel 2: Primzahlen finden

```python
"""Primzahlen bis N finden"""
n = int(input("Primzahlen bis: "))

print(f"\nPrimzahlen bis {n}:")

for zahl in range(2, n + 1):
    ist_primzahl = True
    
    # Prüfen ob Teiler existiert
    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            ist_primzahl = False
            break
    
    if ist_primzahl:
        print(zahl, end=" ")

print()
```

**Erklärung:**
- Äussere Schleife: Alle Zahlen von 2 bis n
- Innere Schleife: Prüft Teiler von 2 bis √zahl
- Break: Stoppt bei erstem Teiler
- Nur Primzahlen werden ausgegeben

### Beispiel 3: Schachbrett

```python
"""Schachbrett-Muster"""
groesse = 8

print("=== Schachbrett ===\n")

for zeile in range(groesse):
    for spalte in range(groesse):
        # Wechselndes Muster
        if (zeile + spalte) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()
```

**Ausgabe:**
```
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
...
```

## ✏️ Übungen (15 Min)

### Übung 7: Multiplikationstabelle
Siehe [Übung 7: Multiplikationstabelle](../02-uebungen/uebung-7-multiplikationstabelle.md)

### Übung 8: Zahlen-Pyramide
Siehe [Übung 8: Zahlen-Pyramide](../02-uebungen/uebung-8-zahlen-pyramide.md)

## 📝 Zusammenfassung

### Verschachtelungsarten

| Typ | Beispiel | Verwendung |
|-----|----------|------------|
| If in If | `if x: if y:` | Mehrere Bedingungen |
| Loop in Loop | `for i: for j:` | Muster, Matrizen |
| If in Loop | `for x: if x:` | Filtern |
| Loop in If | `if x: for y:` | Bedingte Iteration |

### Wichtige Punkte

✅ **DO:**
- Einrückung beachten (4 Leerzeichen pro Ebene)
- Aussagekräftige Variablennamen (i, j, k für Schleifen OK)
- Kommentare bei komplexer Logik

❌ **DON'T:**
- Zu viele Verschachtelungsebenen (max 3-4)
- Unklare Variablennamen
- Fehlende Kommentare

### Performance-Tipp

Bei verschachtelten Schleifen:
- n Iterationen in äusserer Schleife
- m Iterationen in innerer Schleife
- **Gesamt: n × m Iterationen**

Beispiel: 100 × 100 = 10'000 Iterationen!

## 🎓 Abschluss Modul 3

Herzlichen Glückwunsch! Sie haben alle 4 Lektionen abgeschlossen.

**Nächste Schritte:**
1. [Nachbearbeitung](../03-nachbearbeitung/) - Hausaufgaben
2. [Beispiele](../05-beispiele/) - Zum Nachschlagen
3. Modul 4 vorbereiten

