# Aufgabe 3: Quiz-Auswertung mit Booleschen Werten

**Dauer:** 2 Stunden
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

Alle Konzepte aus Modul 2 kombinieren: `input()`, Typkonvertierung, Vergleiche,
Boolesche Werte und F-Strings

> **Hinweis:** Das Quiz arbeitet in Modul 2 **ohne `if`**. Jede Antwort wird mit
> einem Vergleich geprüft und ergibt `True` oder `False`. Weil `True` wie `1` und
> `False` wie `0` zählt, können Sie die Punkte einfach addieren. Die Version mit
> Rückmeldungen (`if`/`else`) bauen Sie nach Modul 3 als Bonus.

## 📝 Aufgabenstellung

Erstellen Sie ein Quiz-Programm `quiz.py` mit:

1. **Mindestens 5 Fragen** zu einem Thema Ihrer Wahl
2. **Verschiedene Fragetypen:**
   - Multiple Choice
   - Ja/Nein-Fragen
   - Zahlen-Fragen
3. **Punktezählung** durch Addition der Vergleichsergebnisse
4. **Auswertung** am Ende (Punkte und Prozent)
5. **Benutzerfreundliche Ausgabe**

## 💡 Beispiel-Ausgabe

```text
========================================
         Python-Quiz
========================================

Willkommen zum Python-Quiz!
Beantworten Sie 5 Fragen und testen Sie Ihr Wissen.

----------------------------------------
Frage 1 von 5: Was ist 5 + 3?
Ihre Antwort: 8

Frage 2 von 5: Ist Python eine Programmiersprache? (ja/nein)
Ihre Antwort: ja

Frage 3 von 5: Welcher Datentyp ist "Hallo"?
a) int
b) float
c) str
d) bool
Ihre Antwort: c

Frage 4 von 5: Wie viele Buchstaben hat "Python"?
Ihre Antwort: 5

Frage 5 von 5: Was gibt 10 / 2 zurück?
Ihre Antwort: 5.0

========================================
         Auswertung
========================================
Frage 1 richtig: True
Frage 2 richtig: True
Frage 3 richtig: True
Frage 4 richtig: False
Frage 5 richtig: True

Ergebnis: 4 von 5 Punkten (80%)
Danke fürs Mitspielen!
========================================
```

## 🔧 Hilfestellung

### Grundstruktur

Stellen Sie zuerst alle Fragen und speichern Sie die Antworten. Prüfen Sie erst
danach alles gemeinsam:

```python
print("=" * 40)
print("         Python-Quiz")
print("=" * 40)
gesamt_fragen = 5

# Fragen stellen
antwort_1 = input("Frage 1 von 5: Was ist 5 + 3?\nIhre Antwort: ")
antwort_2 = input("Frage 2 von 5: Ist Python eine Programmiersprache? (ja/nein)\nIhre Antwort: ")
# ... weitere Fragen

# Antworten prüfen: Jeder Vergleich ergibt True oder False
richtig_1 = int(antwort_1) == 8
richtig_2 = antwort_2.lower() == "ja"
# ... weitere Prüfungen

# Punkte: True zählt als 1, False als 0
punkte = richtig_1 + richtig_2   # + weitere Fragen
prozent = punkte / gesamt_fragen * 100

print(f"Frage 1 richtig: {richtig_1}")
print(f"Frage 2 richtig: {richtig_2}")
print(f"\nErgebnis: {punkte} von {gesamt_fragen} Punkten ({prozent:.0f}%)")
```

### Multiple Choice

```python
antwort_3 = input("Welcher Datentyp ist 'Hallo'? (a: int, b: float, c: str, d: bool)\nIhre Antwort: ")

# .lower() und .strip(): Gross-/Kleinschreibung und Leerzeichen ignorieren
richtig_3 = antwort_3.lower().strip() == "c" or antwort_3.lower().strip() == "str"
```

### Ja/Nein-Frage

```python
antwort_2 = input("Ist Python eine Programmiersprache? (ja/nein)\nIhre Antwort: ")

richtig_2 = antwort_2.lower() == "ja" or antwort_2.lower() == "j"
```

### Zahlen-Frage

```python
antwort_5 = input("Was gibt 10 / 2 zurück?\nIhre Antwort: ")

# Mit float() sind "5" und "5.0" beide richtig
richtig_5 = float(antwort_5) == 5.0
```

> ⚠️ Gibt jemand bei einer Zahlen-Frage Text ein, bricht das Programm mit einem
> `ValueError` ab. Das ist in Modul 2 in Ordnung – das Abfangen lernen Sie in Modul 3.

## ✅ Checkliste

- [ ] Mindestens 5 Fragen erstellt
- [ ] Verschiedene Fragetypen verwendet
- [ ] Punktezählung durch Addition der `True`/`False`-Werte
- [ ] Auswertung am Ende (Punkte und Prozent)
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm ausführlich getestet

## 🚀 Bonus-Aufgaben

**Schon jetzt lösbar:**

1. **Richtige Lösungen anzeigen:**
   - Geben Sie in der Auswertung zu jeder Frage die richtige Antwort aus

2. **Mehr Fragen und mehrere Themen:**
   - Mindestens 8 Fragen, aufgeteilt in zwei Themenblöcke mit eigener Zwischenpunktzahl

**Nach Modul 3** (benötigen `if` bzw. Schleifen):

3. **Sofortige Rückmeldung:**
   - Nach jeder Frage «✓ Richtig!» oder «✗ Falsch!» mit `if`/`else`

4. **Bewertungstext:**
   - Je nach Prozent «Sehr gut», «Gut» oder «Weiter üben» (`if`/`elif`/`else`)

5. **Zufällige Reihenfolge, Highscore, Kategorien, Zeitlimit, Schwierigkeitsgrade**

## 💡 Tipps

- Wählen Sie ein Thema, das Sie interessiert
- Machen Sie die Fragen nicht zu schwer
- Testen Sie mit richtigen *und* falschen Antworten
- Achten Sie auf Gross-/Kleinschreibung (`.lower()`) und Leerzeichen (`.strip()`)
- Nummerieren Sie Ihre Variablen (`antwort_1`, `richtig_1`, ...) – das hält den Code übersichtlich

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

**Problem:** `punkte` zeigt `True` statt einer Zahl

**Lösung:** Addieren Sie mindestens zwei Werte (`True + True` ergibt `2`) oder
wandeln Sie mit `int()` um: `int(richtig_1)`.

**Problem:** Mehrere richtige Antworten möglich

**Lösung:** Verbinden Sie die Vergleiche mit `or`:

```python
richtig = antwort == "ja" or antwort == "j" or antwort == "yes"
```

Viel Erfolg und viel Spass beim Erstellen Ihres Quiz! 🚀
