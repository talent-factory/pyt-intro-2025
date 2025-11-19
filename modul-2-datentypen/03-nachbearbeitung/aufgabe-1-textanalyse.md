# Aufgabe 1: Textanalyse-Tool

**Dauer:** 2 Stunden  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

String-Methoden und Berechnungen kombinieren

## 📝 Aufgabenstellung

Erstellen Sie ein Programm `textanalyse.py`, das einen Text analysiert und folgende Informationen ausgibt:

1. **Grundlegende Statistiken:**
   - Anzahl Zeichen (mit und ohne Leerzeichen)
   - Anzahl Wörter
   - Anzahl Sätze (vereinfacht: Anzahl Punkte)

2. **Wort-Analyse:**
   - Längstes Wort
   - Kürzestes Wort
   - Durchschnittliche Wortlänge

3. **Formatierung:**
   - Text in Grossbuchstaben
   - Text in Kleinbuchstaben
   - Jedes Wort gross (Title Case)

## 💡 Beispiel-Ausgabe

```
========================================
        Textanalyse-Tool
========================================

Bitte geben Sie einen Text ein:
> Python ist eine tolle Programmiersprache. Sie ist einfach zu lernen.

========================================
Analyse-Ergebnisse:
========================================

Grundlegende Statistiken:
- Zeichen (mit Leerzeichen): 68
- Zeichen (ohne Leerzeichen): 56
- Wörter: 10
- Sätze: 2

Wort-Analyse:
- Längstes Wort: Programmiersprache (18 Zeichen)
- Kürzestes Wort: zu (2 Zeichen)
- Durchschnittliche Wortlänge: 5.6 Zeichen

Formatierungen:
- Grossbuchstaben: PYTHON IST EINE TOLLE...
- Kleinbuchstaben: python ist eine tolle...
- Titel-Format: Python Ist Eine Tolle...
========================================
```

## 🔧 Hilfestellung

### Schritt 1: Text einlesen

```python
text = input("Bitte geben Sie einen Text ein:\n> ")
```

### Schritt 2: Grundlegende Statistiken

```python
anzahl_zeichen_mit = len(text)
anzahl_zeichen_ohne = len(text.replace(" ", ""))
woerter = text.split()
anzahl_woerter = len(woerter)
anzahl_saetze = text.count(".")
```

### Schritt 3: Wort-Analyse

```python
# Längstes Wort finden
laengstes = ""
for wort in woerter:
    if len(wort) > len(laengstes):
        laengstes = wort

# Durchschnittliche Länge
gesamt_laenge = sum(len(wort) for wort in woerter)
durchschnitt = gesamt_laenge / anzahl_woerter
```

## ✅ Checkliste

- [ ] Text-Eingabe funktioniert
- [ ] Alle Statistiken berechnet
- [ ] Wort-Analyse implementiert
- [ ] Formatierungen ausgegeben
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm getestet

## 🚀 Bonus-Aufgaben

1. **Häufigste Wörter:**
   - Zählen Sie, welche Wörter am häufigsten vorkommen

2. **Vokal-Analyse:**
   - Zählen Sie Vokale (a, e, i, o, u)

3. **Datei-Eingabe:**
   - Lesen Sie den Text aus einer Datei

4. **Erweiterte Satz-Erkennung:**
   - Berücksichtigen Sie auch `!` und `?`

## 💡 Tipps

- Testen Sie mit verschiedenen Texten
- Achten Sie auf Satzzeichen bei der Wort-Analyse
- Nutzen Sie F-Strings für die Ausgabe
- Strukturieren Sie den Code übersichtlich

## 🆘 Häufige Probleme

**Problem:** Satzzeichen werden als Teil des Wortes gezählt

**Lösung:**
```python
# Satzzeichen entfernen
wort_sauber = wort.strip(".,!?")
```

**Problem:** Division durch Null bei leerem Text

**Lösung:**
```python
if anzahl_woerter > 0:
    durchschnitt = gesamt_laenge / anzahl_woerter
else:
    durchschnitt = 0
```

## 📚 Nützliche String-Methoden

- `.split()` - Text in Wörter aufteilen
- `.count()` - Zeichen/Wörter zählen
- `.replace()` - Zeichen ersetzen
- `.strip()` - Leerzeichen entfernen
- `.upper()`, `.lower()`, `.title()` - Formatierung

Viel Erfolg! 🚀

