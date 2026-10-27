# Aufgabe 1: Zahlenspiel

**Zeitaufwand:** 2 Stunden  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Ziel

Erstellen Sie ein interaktives Zahlenrate-Spiel mit erweiterten Features.

## 📝 Anforderungen

### Basis-Features (Pflicht)

1. **Zufallszahl generieren** (1-100)
2. **Benutzer raten lassen**
3. **Hinweise geben:**
   - "Zu hoch!"
   - "Zu niedrig!"
   - "Ganz nah dran!" (±5)
4. **Versuche zählen** (max. 10)
5. **Gewinn/Verlust-Meldung**

### Erweiterte Features (Optional)

6. **Schwierigkeitsgrade:**
   - Einfach: 1-50, 10 Versuche
   - Mittel: 1-100, 7 Versuche
   - Schwer: 1-200, 5 Versuche

7. **Statistik:**
   - Beste Leistung (wenigste Versuche)
   - Anzahl Spiele
   - Gewinn-Quote

8. **Nochmal spielen?**

## 💡 Beispiel-Ablauf

```
=== ZAHLENRATE-SPIEL ===

Schwierigkeit (1=Einfach, 2=Mittel, 3=Schwer): 2

Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.
Sie haben 7 Versuche.

Versuch 1/7: 50
Zu niedrig!

Versuch 2/7: 75
Zu hoch!

Versuch 3/7: 63
Zu niedrig, aber ganz nah dran! 🔥

Versuch 4/7: 67
Richtig! 🎉

Sie haben gewonnen nach 4 Versuchen!
Bewertung: Sehr gut! 👍

Nochmal spielen? (j/n): n

=== STATISTIK ===
Spiele: 1
Gewonnen: 1
Quote: 100%
Beste Leistung: 4 Versuche

Danke fürs Spielen! 👋
```

## ✅ Checkliste

### Basis
- [ ] Zufallszahl generiert
- [ ] While-Schleife für Versuche
- [ ] Hinweise korrekt
- [ ] Versuche gezählt
- [ ] Gewinn/Verlust erkannt

### Erweitert
- [ ] Schwierigkeitsgrade
- [ ] Statistik
- [ ] Nochmal spielen
- [ ] Schöne Formatierung
- [ ] Fehlerbehandlung (ungültige Eingaben)

## 🎯 Lernziele

- While-Schleifen mit Bedingungen
- If-elif-else Strukturen
- Input-Validierung
- Variablen für Statistik
- Break für Spielende

## 💻 Hilfe

### Zufallszahl

> **Vorgriff:** Dieses Konzept (z. B. Module importieren) wird in Modul 5 behandelt.

```python
import random
zahl = random.randint(1, 100)
```

### Eingabe validieren

```python
while True:
    try:
        eingabe = int(input("Zahl: "))
        if 1 <= eingabe <= 100:
            break
        print("Zahl muss zwischen 1 und 100 liegen!")
    except ValueError:
        print("Bitte eine Zahl eingeben!")
```

### Differenz berechnen

```python
differenz = abs(geraten - geheimzahl)
if differenz <= 5:
    print("Ganz nah dran! 🔥")
```

## 📦 Abgabe

**Datei:** `zahlenspiel.py`

**Testen Sie:**
- Verschiedene Schwierigkeitsgrade
- Gewinn und Verlust
- Ungültige Eingaben
- Mehrere Spiele hintereinander

## 🌟 Bonus-Ideen

- Highscore-Liste (Top 5)
- Zeitlimit pro Versuch
- Zwei-Spieler-Modus
- Sound-Effekte (mit `winsound` oder `playsound`)

## 🔗 Weiter

[Aufgabe 2: Einkaufsliste](./aufgabe-2-einkaufsliste.md)

