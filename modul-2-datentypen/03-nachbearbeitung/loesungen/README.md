# Musterlösungen – Nachbearbeitung Modul 2

Dieser Ordner enthält die offiziellen Musterlösungen zu den drei
Nachbearbeitungs-Aufgaben aus Modul 2 (Datentypen).

> **Hinweis für Studierende:** Versuchen Sie die Aufgaben zuerst selbst zu
> lösen! Die Musterlösungen sind als Vergleich und zum Nachschlagen gedacht,
> nicht zum Abschreiben.

## 📋 Übersicht

| Datei | Aufgabe | Schwerpunkt |
|-------|---------|-------------|
| [`textanalyse.py`](./textanalyse.py) | [Aufgabe 1](../aufgabe-1-textanalyse.md) | String-Methoden, Berechnungen, for-Schleifen |
| [`validator.py`](./validator.py) | [Aufgabe 2](../aufgabe-2-validator.md) | Boolean-Logik, String-Prüfungen, `if/elif/else` |
| [`quiz.py`](./quiz.py) | [Aufgabe 3](../aufgabe-3-quiz.md) | Alle Konzepte aus Modul 2 kombinieren |

## ▶️ Ausführen

```bash
cd modul-2-datentypen/03-nachbearbeitung/loesungen

python textanalyse.py
python validator.py
python quiz.py
```

## 📚 Verwendete Konzepte (Ausbildungsstand Modul 2)

Die Lösungen verwenden **nur** Konzepte, die nach Modul 2 bekannt sind:

- Variablen und Datentypen (`int`, `float`, `str`, `bool`)
- String-Methoden (`.upper()`, `.lower()`, `.title()`, `.strip()`,
  `.replace()`, `.split()`, `.startswith()`, `.count()`,
  `.isdigit()`, `.isupper()`, `.islower()`, `.index()`)
- F-Strings für die Ausgabe
- Boolesche Werte und logische Operatoren (`and`, `or`, `not`)
- Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- `if/elif/else`-Verzweigungen
- `for`-Schleifen mit Listen
- Listen mit `.append()` und Indexierung
- `len()`, `int()`, `str()`, `float()`
- `input()` und `print()`

**Bewusst nicht verwendet** (kommt erst später):

- Eigene Funktionen (`def`) → Modul 4
- Dictionaries → Modul 4
- `while`-Schleifen → Modul 3
- Module wie `random` → Modul 5

## 🎁 Enthaltene Bonus-Aufgaben

### `textanalyse.py`

- Vokal-Analyse (Bonus)
- Erweiterte Satz-Erkennung mit `!` und `?` (Bonus)
- Bereinigung von Satzzeichen am Wortrand

### `validator.py`

- Erweiterte E-Mail-Validierung (Bonus): genau ein `@`, Position
  des `@`, Punkt nach dem `@`
- Passwort-Stärke-Bewertung (Bonus): Schwach / Mittel / Stark
- Schweizer Telefonnummer (Bonus): beginnt mit `0`, genau 10 Ziffern
- Formatierte Ausgabe der Telefonnummer

### `quiz.py`

- 5 Fragen mit vier verschiedenen Antworttypen
- Mehrere zulässige Schreibweisen pro Antwort (`ja` / `j` / `yes`)
- Differenzierte Bewertung (Perfekt / Sehr gut / Gut / Geht so /
  Weiter üben)

## 📐 Code-Stil

Die Musterlösungen folgen den Konventionen aus
[`CLAUDE.md`](../../../CLAUDE.md):

- Deutsche Variablennamen in `snake_case`
- Kommentare auf Deutsch
- Trennlinien mit `"=" * 40` für eine übersichtliche Ausgabe
- Strukturierte Abschnitte mit Kommentar-Blöcken
- Bewusst didaktisch geschrieben – Klarheit vor Kompaktheit

## 💡 Eigene Lösung vergleichen

Beim Vergleichen Ihrer eigenen Lösung mit der Musterlösung lohnen sich
diese Fragen:

1. **Funktioniert mein Programm bei allen Eingaben?** (auch bei leeren
   Texten, ungültigen Eingaben, Sonderzeichen?)
2. **Sind meine Variablennamen aussagekräftig?**
3. **Ist meine Ausgabe übersichtlich und benutzerfreundlich?**
4. **Habe ich Randfälle bedacht?** (Division durch Null, leere Strings)
5. **Verstehe ich, was jede Zeile meines Codes tut?**

Es gibt nicht *die eine* richtige Lösung – wichtig ist, dass Ihr Programm
korrekt funktioniert und für Sie selbst lesbar bleibt.

## 🔭 Ausblick

Sie werden sehen: Manche Stellen wiederholen sich (z.B. bei den
Validator-Prüfungen oder den Quiz-Fragen). Im **Modul 4** lernen Sie
**Funktionen** kennen – damit lassen sich solche Wiederholungen elegant
vermeiden. Sie können die Musterlösungen später gerne mit Funktionen
umschreiben, um den Unterschied zu erleben!
