# Übung 3: Fakultät

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel  
**Lektion:** 2 (While-Schleifen)

## 📝 Aufgabe

Erstellen Sie ein Programm `fakultaet.py`, das die Fakultät einer Zahl berechnet.

**Fakultät:** n! = 1 × 2 × 3 × ... × n

Beispiele:
- 5! = 1 × 2 × 3 × 4 × 5 = 120
- 3! = 1 × 2 × 3 = 6
- 0! = 1 (per Definition)

## 💡 Beispiele

### Beispiel 1
```
Zahl: 5

5! = 1 x 2 x 3 x 4 x 5 = 120
```

### Beispiel 2
```
Zahl: 7

7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040
```

### Beispiel 3
```
Zahl: 0

0! = 1
```

## ✅ Checkliste

- [ ] While-Schleife verwendet
- [ ] Fakultät korrekt berechnet
- [ ] Sonderfall 0! behandelt
- [ ] Berechnung angezeigt

## 🎯 Lernziele

- While-Schleifen für Berechnungen
- Multiplikation in Schleife
- Sonderfälle behandeln

## 💻 Musterlösung

<details>
<summary>Klicken zum Anzeigen</summary>

```python
"""
Fakultät berechnen
Berechnet n! = 1 x 2 x 3 x ... x n
"""

# Eingabe
n = int(input("Zahl: "))

# Sonderfall 0!
if n == 0:
    print("\n0! = 1")
else:
    # Fakultät berechnen
    fakultaet = 1
    zaehler = 1
    berechnung = ""
    
    while zaehler <= n:
        fakultaet *= zaehler
        
        # Berechnung als String aufbauen
        if zaehler == 1:
            berechnung = "1"
        else:
            berechnung += f" x {zaehler}"
        
        zaehler += 1
    
    # Ausgabe
    print(f"\n{n}! = {berechnung} = {fakultaet}")
```

**Alternative (kompakter):**

```python
n = int(input("Zahl: "))

fakultaet = 1
zaehler = 1

while zaehler <= n:
    fakultaet *= zaehler
    zaehler += 1

print(f"\n{n}! = {fakultaet}")
```

</details>

## 🔗 Weiter

[Übung 4: Zahlenraten](./uebung-4-zahlenraten.md)

