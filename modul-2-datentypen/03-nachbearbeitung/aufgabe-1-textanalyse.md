# Aufgabe 1: Textanalyse-Tool

**Dauer:** 2 Stunden
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

String-Methoden und Berechnungen kombinieren

> **Hinweis:** Sie brauchen für diese Aufgabe weder `if` noch Schleifen – diese folgen
> in Modul 3. Neu ist nur `max()`/`min()` mit `key=len` (Schritt 3), das im Tipp unten erklärt wird.

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

```text
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
- Zeichen (ohne Leerzeichen): 59
- Wörter: 10
- Sätze: 2

Wort-Analyse:
- Längstes Wort: Programmiersprache (18 Zeichen)
- Kürzestes Wort: zu (2 Zeichen)
- Durchschnittliche Wortlänge: 5.7 Zeichen

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
anzahl_saetze = text.count(".")
```

### Schritt 3: Wort-Analyse

```python
# Satzzeichen entfernen, damit sie nicht zur Wortlänge zählen
text_sauber = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
woerter = text_sauber.split()
anzahl_woerter = len(woerter)

# Längstes und kürzestes Wort: key=len vergleicht die Wörter nach ihrer Länge
laengstes = max(woerter, key=len)
kuerzestes = min(woerter, key=len)

# Durchschnittliche Länge: alle Wörter aneinanderhängen und die Zeichen zählen
gesamt_laenge = len("".join(woerter))
durchschnitt = gesamt_laenge / anzahl_woerter

print(f"Längstes Wort: {laengstes} ({len(laengstes)} Zeichen)")
```

> 💡 `max(woerter, key=len)` liefert das Wort mit der grössten Länge,
> `min(...)` das mit der kleinsten. `"".join(woerter)` hängt alle Wörter
> ohne Leerzeichen aneinander.

## ✅ Checkliste

- [ ] Text-Eingabe funktioniert
- [ ] Alle Statistiken berechnet
- [ ] Wort-Analyse implementiert
- [ ] Formatierungen ausgegeben
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm getestet

## 🚀 Bonus-Aufgaben

**Schon jetzt lösbar:**

1. **Vokal-Analyse:**
   - Zählen Sie Vokale (a, e, i, o, u) mit `.count()`

2. **Erweiterte Satz-Erkennung:**
   - Berücksichtigen Sie auch `!` und `?`

**Nach Modul 3 bzw. Modul 5** (benötigen Schleifen bzw. Dateien):

3. **Häufigste Wörter:**
   - Zählen Sie, welche Wörter am häufigsten vorkommen

4. **Datei-Eingabe:**
   - Lesen Sie den Text aus einer Datei

## 💡 Tipps

- Testen Sie mit verschiedenen Texten
- Entfernen Sie Satzzeichen vor der Wort-Analyse (siehe Schritt 3)
- Nutzen Sie F-Strings für die Ausgabe
- Strukturieren Sie den Code übersichtlich

## 🆘 Häufige Probleme

**Problem:** Satzzeichen werden als Teil des Wortes gezählt

**Lösung:**

```python
# Satzzeichen vor dem Aufteilen entfernen
text_sauber = text.replace(".", "").replace(",", "")
woerter = text_sauber.split()
```

**Problem:** Das Programm bricht bei leerer Eingabe ab (`ValueError` bzw. `ZeroDivisionError`)

**Lösung:** Testen Sie mit einem Text, der mindestens ein Wort enthält. Wie Sie
leere Eingaben mit `if` abfangen, lernen Sie in Modul 3.

## 📚 Nützliche String-Methoden

- `.split()` - Text in Wörter aufteilen
- `.count()` - Zeichen/Wörter zählen
- `.replace()` - Zeichen ersetzen
- `.strip()` - Leerzeichen am Rand entfernen
- `.upper()`, `.lower()`, `.title()` - Formatierung

Viel Erfolg! 🚀
