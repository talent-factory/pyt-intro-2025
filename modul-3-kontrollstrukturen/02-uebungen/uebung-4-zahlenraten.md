# Übung 4: Zahlenraten

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel  
**Lektion:** 2 (While-Schleifen)

## 📝 Aufgabe

Erstellen Sie ein einfaches Zahlenrate-Spiel `zahlenraten_einfach.py`:

- Computer "denkt" sich Zahl zwischen 1-20
- Benutzer hat 5 Versuche
- Nach jedem Versuch: "Zu hoch" oder "Zu niedrig"
- Bei Erfolg: Glückwunsch + Anzahl Versuche

## 💡 Beispiel

```
Ich habe mir eine Zahl zwischen 1 und 20 ausgedacht.

Versuch 1/5: 10
Zu niedrig!

Versuch 2/5: 15
Zu hoch!

Versuch 3/5: 13
Richtig! Sie haben gewonnen nach 3 Versuchen!
```

## ✅ Checkliste

- [ ] Zufallszahl generiert (import random)
- [ ] While-Schleife für Versuche
- [ ] Hinweise korrekt
- [ ] Gewinn/Verlust-Meldung

## 💻 Tipp

```python
import random
geheimzahl = random.randint(1, 20)
```
