# Lektion 4: Funktionen testen mit pytest

**Dauer:** 50 Minuten
**Format:** 5 Min Motivation + 10 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

Nach dieser Lektion können Sie:
- Verstehen, warum Testing wichtig ist
- Testbare Funktionen erkennen (return statt print)
- Einfache Tests mit pytest schreiben
- Tests ausführen und Ergebnisse interpretieren

## 💡 Motivation (5 Min)

Stellen Sie sich vor: Sie schreiben eine Funktion `berechne_durchschnitt()`. Sie testen sie einmal von Hand — sieht gut aus. Zwei Wochen später ändern Sie etwas am Code. Funktioniert die Funktion noch? Sie müssten alles nochmal von Hand prüfen...

**Automatische Tests lösen dieses Problem:** Sie schreiben die Prüfung einmal und können sie danach in Sekunden immer wieder ausführen. Jede Änderung wird sofort geprüft.

## 📖 Theorie (10 Min)

### 1. Warum testen? (3 Min)

**Analogie:** Stellen Sie sich einen Taschenrechner vor. Sie geben eine Rechnung ein und prüfen, ob das Ergebnis stimmt. Genau das machen automatische Tests — nur viel schneller.

**Manuelles Testen:**
- Programm starten, Werte eingeben, Ausgabe prüfen
- Langsam, fehleranfällig, langweilig
- Wird oft vergessen oder übersprungen

**Automatisches Testen:**
- Tests laufen in Sekunden — immer wieder
- Prüfen zuverlässig, ob alles noch funktioniert
- Finden Fehler sofort nach einer Änderung

### 2. Testbare Funktionen (3 Min)

Nicht jede Funktion lässt sich einfach testen:

```python
# ❌ Schwer testbar — gibt nur etwas aus
def begruessung():
    print("Hallo Welt!")

# ✅ Gut testbar — gibt einen Wert zurück
def ist_gerade(zahl):
    return zahl % 2 == 0
```

**Die Regel:** Funktionen mit `return` sind testbar — Eingabe rein, Ergebnis raus.

**Deshalb haben wir in Lektion 1-2 immer `return` genutzt!**

### 3. pytest Basics (4 Min)

**Drei einfache Regeln:**

1. **Testdatei:** Dateiname beginnt mit `test_` (z.B. `test_rechner.py`)
2. **Testfunktion:** Funktionsname beginnt mit `test_` (z.B. `def test_addition():`)
3. **assert:** Behaupte, dass etwas wahr ist

```python
# test_beispiel.py

def test_ist_gerade():
    assert ist_gerade(4) == True
    assert ist_gerade(3) == False
```

**Tests ausführen:**

```bash
uv run pytest -v
```

Die Ausgabe zeigt grüne **PASSED** oder rote **FAILED** Ergebnisse.

## 💻 Live-Coding (20 Min)

> Die folgenden Funktionen stammen aus der Datei
> [`testen_beispiel.py`](../05-beispiele/testen_beispiel.py).

### Beispiel 1: `ist_gerade()` testen (5 Min)

**Die Funktion:**

```python
def ist_gerade(zahl):
    """Prüft, ob eine Zahl gerade ist."""
    return zahl % 2 == 0
```

**Die Tests:**

```python
# test_testen_beispiel.py
from testen_beispiel import ist_gerade

def test_gerade_zahl():
    assert ist_gerade(4) == True

def test_ungerade_zahl():
    assert ist_gerade(3) == False

def test_null_ist_gerade():
    assert ist_gerade(0) == True
```

**pytest ausführen:**

```bash
uv run pytest -v
```

```
test_testen_beispiel.py::test_gerade_zahl     PASSED
test_testen_beispiel.py::test_ungerade_zahl   PASSED
test_testen_beispiel.py::test_null_ist_gerade PASSED
```

Alles grün — die Funktion funktioniert korrekt!

### Beispiel 2: `berechne_durchschnitt()` testen (8 Min)

**Die Funktion:**

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe / len(zahlen)
```

**Die Tests:**

```python
from testen_beispiel import berechne_durchschnitt

def test_normale_liste():
    assert berechne_durchschnitt([1, 2, 3]) == 2.0

def test_ein_element():
    assert berechne_durchschnitt([5]) == 5.0

def test_gleiche_werte():
    assert berechne_durchschnitt([3, 3, 3]) == 3.0

def test_leere_liste():
    assert berechne_durchschnitt([]) == 0
```

**pytest ausführen — Überraschung!**

```
test_testen_beispiel.py::test_normale_liste   PASSED
test_testen_beispiel.py::test_ein_element     PASSED
test_testen_beispiel.py::test_gleiche_werte   PASSED
test_testen_beispiel.py::test_leere_liste     FAILED
    ZeroDivisionError: division by zero
```

**Der Test hat einen Bug gefunden!** Bei einer leeren Liste teilen wir durch Null.

**Der Fix — Guard Clause:**

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
    if not zahlen:
        return 0
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe / len(zahlen)
```

Nochmal `uv run pytest -v` — jetzt alles grün!

**Aha-Moment:** Der automatische Test hat einen Fehler gefunden, den wir beim manuellen Testen wahrscheinlich übersehen hätten.

### Beispiel 3: `erstelle_kontakt()` testen (7 Min)

**Die Funktion:**

```python
def erstelle_kontakt(name, email, telefon=""):
    """Erstellt ein Kontakt-Dictionary."""
    return {
        "name": name,
        "email": email,
        "telefon": telefon
    }
```

**Die Tests:**

```python
from testen_beispiel import erstelle_kontakt

def test_kontakt_vollstaendig():
    kontakt = erstelle_kontakt("Anna", "anna@mail.ch", "079 123 45 67")
    assert kontakt["name"] == "Anna"
    assert kontakt["email"] == "anna@mail.ch"
    assert kontakt["telefon"] == "079 123 45 67"

def test_kontakt_ohne_telefon():
    kontakt = erstelle_kontakt("Max", "max@mail.ch")
    assert kontakt["name"] == "Max"
    assert kontakt["telefon"] == ""

def test_kontakt_ist_dictionary():
    kontakt = erstelle_kontakt("Lisa", "lisa@mail.ch")
    assert type(kontakt) == dict
    assert len(kontakt) == 3
```

**Wichtig:** Wir prüfen hier verschiedene Aspekte:
- Sind die Werte korrekt?
- Funktioniert der Standardwert?
- Hat das Dictionary die richtige Struktur?

## ✏️ Übungen (15 Min)

### Übung 7: Testing geführt (10 Min)

Siehe [Übung 7: Testing geführt](../02-uebungen/uebung-7-testing.md)

### Übung 8: Testing selbständig (5 Min)

Siehe [Übung 8: Testing selbständig](../02-uebungen/uebung-8-testing.md)

## 📚 Zusammenfassung

- **Testbare Funktionen** geben Werte mit `return` zurück
- **pytest:** `test_`-Prefix für Dateien und Funktionen, `assert` für Prüfungen
- **Ausführen:** `uv run pytest -v`
- **Gute Tests** prüfen Normalfall UND Grenzfälle
- **Tests finden Fehler** BEVOR Nutzer sie finden

## 🎉 Modul abgeschlossen!

Sie haben gelernt:

- ✅ Funktionen definieren
- ✅ Parameter und Return
- ✅ Listen, Dictionaries & Co.
- ✅ Funktionen testen mit pytest
- ✅ Code modular strukturieren

**Weiter:** [Hausaufgaben](../03-nachbearbeitung/)
