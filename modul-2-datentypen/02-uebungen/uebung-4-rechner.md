# Übung 4: Interaktiver Rechner

**Dauer:** 20 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

Alle Konzepte kombinieren und benutzerfreundliches Programm erstellen

## 📝 Aufgabe

Erstellen Sie einen interaktiven Rechner `rechner.py`, der:

1. Nach zwei Zahlen fragt
2. Alle Grundrechenarten durchführt (+ - * /)
3. Die Ergebnisse formatiert ausgibt
4. Benutzerfreundlich gestaltet ist

## 💡 Beispiel-Ausgabe

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

## 🔧 Hilfestellung

```python
print("=" * 40)
print("        Interaktiver Rechner")
print("=" * 40)

zahl1 = float(input("\nErste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

summe = zahl1 + zahl2
# ... weitere Berechnungen

print(f"\n{zahl1:.2f} + {zahl2:.2f} = {summe:.2f}")
```

## ✅ Checkliste

- [ ] Titel mit Linien
- [ ] Zwei Zahlen eingeben
- [ ] Alle 4 Rechenarten
- [ ] Formatierte Ausgabe (2 Dezimalstellen)
- [ ] Visuelle Trennung

## 🚀 Bonus

- Modulo-Operation (%) hinzufügen
- Potenz (**) berechnen
- Prüfen ob Division durch 0

