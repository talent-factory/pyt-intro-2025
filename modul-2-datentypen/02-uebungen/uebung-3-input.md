# Übung 3: Benutzereingaben verarbeiten

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

`input()` nutzen und Typkonvertierung anwenden

## 📝 Aufgabe

Erstellen Sie ein Programm `benutzereingaben.py`, das:

1. Nach Name, Alter und Lieblingsfarbe fragt
2. Das Geburtsjahr berechnet (aktuelles Jahr minus Alter)
3. Alle Informationen formatiert ausgibt
4. Das Alter im nächsten Jahr berechnet

## 💡 Beispiel-Ausgabe

```
=== Persönliche Daten ===

Wie heissen Sie? Max Muster
Wie alt sind Sie? 25
Lieblingsfarbe? Blau

========================================
Name: Max Muster
Alter: 25 Jahre
Geburtsjahr: ca. 2001
Lieblingsfarbe: Blau

Nächstes Jahr sind Sie 26 Jahre alt!
========================================
```

## 🔧 Hilfestellung

```python
# Eingabe
name = input("Wie heissen Sie? ")
alter = int(input("Wie alt sind Sie? "))

# Berechnung
aktuelles_jahr = 2026  # Aktuelles Jahr von Hand eintragen
geburtsjahr = aktuelles_jahr - alter

# Ausgabe
print(f"Name: {name}")
```

## ✅ Checkliste

- [ ] Alle Eingaben gesammelt
- [ ] Alter konvertiert
- [ ] Geburtsjahr berechnet
- [ ] Formatierte Ausgabe

