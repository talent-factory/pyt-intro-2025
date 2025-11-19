# Übung 2: Rabatt-Rechner

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐ Einfach  
**Lektion:** 1 (Bedingte Anweisungen)

## 📝 Aufgabe

Erstellen Sie ein Programm `rabatt.py`, das Rabatte berechnet:

**Rabatt-Regeln:**
- Mitglieder: 10% Rabatt
- Bestellwert ≥ 100 CHF: zusätzlich 5% Rabatt
- Bestellwert ≥ 200 CHF: zusätzlich 10% Rabatt (statt 5%)

## 💡 Beispiele

### Beispiel 1: Mitglied, 150 CHF
```
Preis: 150
Mitglied (j/n): j

Originalpreis: 150.00 CHF
Rabatt: 15% (Mitglied + Bestellwert)
Endpreis: 127.50 CHF
```

### Beispiel 2: Kein Mitglied, 80 CHF
```
Preis: 80
Mitglied (j/n): n

Originalpreis: 80.00 CHF
Rabatt: 0%
Endpreis: 80.00 CHF
```

### Beispiel 3: Mitglied, 250 CHF
```
Preis: 250
Mitglied (j/n): j

Originalpreis: 250.00 CHF
Rabatt: 20% (Mitglied + Bestellwert)
Endpreis: 200.00 CHF
```

## ✅ Checkliste

- [ ] Eingabe: Preis und Mitgliedschaft
- [ ] Rabatt korrekt berechnet
- [ ] Alle Fälle getestet
- [ ] Ausgabe formatiert (2 Dezimalstellen)

## 🎯 Lernziele

- If-Anweisungen kombinieren
- Berechnungen mit Rabatten
- Formatierte Ausgabe

## 💻 Musterlösung

<details>
<summary>Klicken zum Anzeigen</summary>

```python
"""
Rabatt-Rechner
Berechnet Rabatte basierend auf Mitgliedschaft und Bestellwert.
"""

# Eingabe
preis = float(input("Preis: "))
ist_mitglied = input("Mitglied (j/n): ").lower() == "j"

# Rabatt berechnen
rabatt = 0

if ist_mitglied:
    rabatt = 10

if preis >= 200:
    rabatt += 10
elif preis >= 100:
    rabatt += 5

# Endpreis berechnen
endpreis = preis * (1 - rabatt / 100)

# Ausgabe
print()
print(f"Originalpreis: {preis:.2f} CHF")
print(f"Rabatt: {rabatt}%", end="")

if ist_mitglied and preis >= 100:
    print(" (Mitglied + Bestellwert)")
elif ist_mitglied:
    print(" (Mitglied)")
elif preis >= 100:
    print(" (Bestellwert)")
else:
    print()

print(f"Endpreis: {endpreis:.2f} CHF")
```

</details>

## 🔗 Weiter

[Übung 3: Fakultät](./uebung-3-fakultaet.md)

