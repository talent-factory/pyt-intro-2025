# Lektion 5: Mini-Projekt

**Dauer:** 50 Minuten  
**Format:** 5 Min Einführung + 40 Min Projekt + 5 Min Präsentation

## 🎯 Lernziele

- Alle Konzepte kombinieren
- Eigenständiges Projekt entwickeln
- Code strukturieren
- Testen und debuggen

## 📖 Einführung (5 Min)

In dieser Lektion entwickeln Sie ein kleines Projekt, das alle gelernten Konzepte kombiniert:

- If-Anweisungen
- While-Schleifen
- For-Schleifen
- Listen
- Verschachtelte Strukturen

### Projekt-Optionen

Wählen Sie **eines** der folgenden Projekte:

1. **Kontakt-Manager** (einfach)
2. **Tic-Tac-Toe** (mittel)
3. **Hangman** (mittel-schwer)

## 💻 Projekt-Arbeit (40 Min)

### Option 1: Kontakt-Manager

**Anforderungen:**
- Kontakte hinzufügen (Name, Telefon, E-Mail)
- Kontakte anzeigen
- Kontakte suchen
- Kontakte löschen
- Menü-System

**Beispiel:**
```
=== KONTAKT-MANAGER ===
1. Kontakt hinzufügen
2. Alle Kontakte
3. Kontakt suchen
4. Kontakt löschen
5. Beenden

Wahl: 1
Name: Max Muster
Telefon: 079 123 45 67
E-Mail: max@example.com
✓ Kontakt hinzugefügt
```

**Hilfe:**
```python
kontakte = []

# Kontakt als Dictionary
kontakt = {
    "name": "Max Muster",
    "telefon": "079 123 45 67",
    "email": "max@example.com"
}
kontakte.append(kontakt)
```

### Option 2: Tic-Tac-Toe

**Anforderungen:**
- 3x3 Spielfeld
- Zwei Spieler (X und O)
- Gewinn-Prüfung
- Unentschieden-Erkennung
- Eingabe-Validierung

**Beispiel:**
```
  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9

Spieler X, Feld (1-9): 5

  1 | 2 | 3
 -----------
  4 | X | 6
 -----------
  7 | 8 | 9
```

**Hilfe:**
```python
# Spielfeld als Liste
feld = [" "] * 9

# Gewinn-Kombinationen
gewinn = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Zeilen
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Spalten
    [0, 4, 8], [2, 4, 6]              # Diagonalen
]
```

### Option 3: Hangman (Wortrate-Spiel)

**Anforderungen:**
- Wort aus Liste wählen
- Buchstaben raten
- Versuche zählen (max. 6)
- Wort anzeigen mit _ für unbekannte Buchstaben
- Gewinn/Verlust-Erkennung

**Beispiel:**
```
=== HANGMAN ===

Wort: _ _ _ _ _ _
Versuche: 6

Buchstabe: e
✓ Richtig!

Wort: _ _ _ _ e _
Versuche: 6

Buchstabe: a
✗ Falsch!

Wort: _ _ _ _ e _
Versuche: 5
```

**Hilfe:**
```python
import random

woerter = ["PYTHON", "PROGRAMMIEREN", "COMPUTER"]
wort = random.choice(woerter)
geraten = []

# Wort anzeigen
anzeige = ""
for buchstabe in wort:
    if buchstabe in geraten:
        anzeige += buchstabe + " "
    else:
        anzeige += "_ "
```

## 🎯 Anforderungen (alle Projekte)

### Pflicht
- [ ] Menü-System (while-Schleife)
- [ ] Mindestens 3 Funktionen
- [ ] Input-Validierung
- [ ] Fehlerbehandlung (try-except)
- [ ] Kommentare im Code

### Optional
- [ ] Schöne Formatierung
- [ ] Statistiken
- [ ] Speichern/Laden
- [ ] Erweiterte Features

## 📋 Vorgehen

1. **Planen** (5 Min)
   - Welche Funktionen brauche ich?
   - Welche Datenstrukturen?
   - Wie ist der Ablauf?

2. **Grundgerüst** (10 Min)
   - Menü-System
   - Basis-Funktionen

3. **Implementieren** (20 Min)
   - Funktionen ausarbeiten
   - Testen

4. **Verfeinern** (5 Min)
   - Fehlerbehandlung
   - Formatierung

## 🎤 Präsentation (5 Min)

Zeigen Sie Ihr Projekt:
- Was haben Sie gebaut?
- Welche Herausforderungen gab es?
- Was würden Sie verbessern?

## 📝 Zusammenfassung

Sie haben gelernt:
- Komplexe Programme zu strukturieren
- Alle Konzepte zu kombinieren
- Eigenständig zu entwickeln
- Code zu testen

## 🎓 Abschluss Modul 3

Herzlichen Glückwunsch! Sie haben Modul 3 abgeschlossen.

**Nächste Schritte:**
1. [Nachbearbeitung](../03-nachbearbeitung/)
2. Modul 4 vorbereiten

## 💡 Tipps

- Beginnen Sie einfach
- Testen Sie oft
- Nutzen Sie print() zum Debuggen
- Fragen Sie bei Problemen
- Haben Sie Spass! 🎉

