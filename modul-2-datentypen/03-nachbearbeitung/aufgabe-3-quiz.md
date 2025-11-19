# Aufgabe 3: Interaktives Quiz

**Dauer:** 2 Stunden  
**Schwierigkeit:** ⭐⭐⭐ Schwer

## 🎯 Lernziel

Alle Konzepte kombinieren und ein vollständiges Programm erstellen

## 📝 Aufgabenstellung

Erstellen Sie ein interaktives Quiz-Programm `quiz.py` mit:

1. **Mindestens 5 Fragen** zu einem Thema Ihrer Wahl
2. **Verschiedene Fragetypen:**
   - Multiple Choice
   - Ja/Nein-Fragen
   - Zahlen-Fragen
3. **Punktezählung** und Auswertung
4. **Benutzerfreundliche Ausgabe**

## 💡 Beispiel-Ausgabe

```
========================================
         Python-Quiz
========================================

Willkommen zum Python-Quiz!
Beantworten Sie 5 Fragen und testen Sie Ihr Wissen.

========================================

Frage 1 von 5:
Was ist 5 + 3?
Ihre Antwort: 8
✓ Richtig! (+1 Punkt)

----------------------------------------

Frage 2 von 5:
Ist Python eine Programmiersprache? (ja/nein)
Ihre Antwort: ja
✓ Richtig! (+1 Punkt)

----------------------------------------

Frage 3 von 5:
Welcher Datentyp ist "Hallo"?
a) int
b) float
c) str
d) bool
Ihre Antwort: c
✓ Richtig! (+1 Punkt)

----------------------------------------

Frage 4 von 5:
Wie viele Buchstaben hat "Python"?
Ihre Antwort: 5
✗ Falsch! Richtig wäre: 6

----------------------------------------

Frage 5 von 5:
Was gibt 10 / 2 zurück?
Ihre Antwort: 5
✓ Richtig! (+1 Punkt)

========================================
         Quiz beendet!
========================================

Ergebnis: 4 von 5 Punkten (80%)

Bewertung: Sehr gut! 👍

Danke fürs Mitspielen!
========================================
```

## 🔧 Hilfestellung

### Grundstruktur

```python
print("=" * 40)
print("         Python-Quiz")
print("=" * 40)

punkte = 0
gesamt_fragen = 5

# Frage 1
print("\nFrage 1 von 5:")
print("Was ist 5 + 3?")
antwort = input("Ihre Antwort: ")

if antwort == "8":
    print("✓ Richtig! (+1 Punkt)")
    punkte += 1
else:
    print("✗ Falsch! Richtig wäre: 8")

# ... weitere Fragen

# Auswertung
prozent = (punkte / gesamt_fragen) * 100
print(f"\nErgebnis: {punkte} von {gesamt_fragen} Punkten ({prozent:.0f}%)")

if prozent >= 80:
    print("Bewertung: Sehr gut! 👍")
elif prozent >= 60:
    print("Bewertung: Gut! ✓")
else:
    print("Bewertung: Weiter üben! 📚")
```

### Multiple Choice

```python
print("Welcher Datentyp ist 'Hallo'?")
print("a) int")
print("b) float")
print("c) str")
print("d) bool")
antwort = input("Ihre Antwort: ").lower()

if antwort == "c" or antwort == "str":
    print("✓ Richtig!")
    punkte += 1
else:
    print("✗ Falsch! Richtig wäre: c (str)")
```

### Ja/Nein-Frage

```python
print("Ist Python eine Programmiersprache? (ja/nein)")
antwort = input("Ihre Antwort: ").lower()

if antwort == "ja" or antwort == "j" or antwort == "yes":
    print("✓ Richtig!")
    punkte += 1
else:
    print("✗ Falsch!")
```

## ✅ Checkliste

- [ ] Mindestens 5 Fragen erstellt
- [ ] Verschiedene Fragetypen verwendet
- [ ] Punktezählung implementiert
- [ ] Auswertung am Ende
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm ausführlich getestet

## 🚀 Bonus-Aufgaben

1. **Zufällige Reihenfolge:**
   - Fragen in zufälliger Reihenfolge stellen

2. **Highscore:**
   - Besten Score speichern

3. **Kategorien:**
   - Verschiedene Quiz-Kategorien

4. **Zeitlimit:**
   - Zeit pro Frage messen

5. **Schwierigkeitsgrade:**
   - Einfach, Mittel, Schwer

## 💡 Tipps

- Wählen Sie ein Thema, das Sie interessiert
- Machen Sie die Fragen nicht zu schwer
- Geben Sie hilfreiche Rückmeldungen
- Testen Sie mit verschiedenen Antworten
- Achten Sie auf Gross-/Kleinschreibung (`.lower()`)

## 🎨 Themen-Ideen

- Python-Grundlagen
- Mathematik
- Geografie
- Geschichte
- Sport
- Filme/Serien
- Allgemeinwissen

## 🆘 Häufige Probleme

**Problem:** Antwort wird nicht erkannt (Gross-/Kleinschreibung)

**Lösung:**
```python
antwort = input("Ihre Antwort: ").lower()
```

**Problem:** Mehrere richtige Antworten möglich

**Lösung:**
```python
if antwort in ["ja", "j", "yes", "y"]:
    print("✓ Richtig!")
```

Viel Erfolg und viel Spass beim Erstellen Ihres Quiz! 🚀

