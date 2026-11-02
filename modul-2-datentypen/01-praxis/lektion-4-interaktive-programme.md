# Lektion 4: Interaktive Programme & Vertiefung

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 25 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Alle Konzepte aus Modul 2 kombinieren
- Benutzerfreundliche Programme erstellen
- Eingaben mit String-Methoden und Vergleichen **prüfen** (Ergebnis: `True`/`False`)
- Erweiterte String-Methoden anwenden
- Verstehen, warum ungültige Eingaben zu Fehlern führen

> **Hinweis:** In dieser Lektion *prüfen* wir Eingaben nur und zeigen das Ergebnis
> als Boolescher Wert an. Wie ein Programm auf das Ergebnis *reagiert*
> (`if`/`else`, Wiederholung bei falscher Eingabe, `try`/`except`), lernen Sie
> in **Modul 3**.

---

## 📖 Teil 1: Theorie (10 Min)

### 1.1 Best Practices für interaktive Programme

**1. Klare Anweisungen:**

```python
# Schlecht:
name = input()

# Gut:
name = input("Bitte geben Sie Ihren Namen ein: ")
```

**2. Formatierte Ausgaben:**

```python
# Schlecht:
print(name, alter, stadt)

# Gut:
print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")
```

**3. Visuelle Trennung:**

```python
print("=" * 40)
print("Titel")
print("=" * 40)
```

### 1.2 Eingaben prüfen (Validierung)

`input()` liefert immer einen String. Bevor wir ihn umwandeln, können wir
**prüfen**, ob die Umwandlung gelingen würde. Das Ergebnis ist ein Boolescher Wert:

```python
alter_str = input("Alter: ")

ist_zahl = alter_str.isdigit()        # True bei "25", False bei "abc"
nicht_leer = len(alter_str) > 0       # True, sobald etwas eingegeben wurde

print(f"Eingabe ist eine ganze Zahl: {ist_zahl}")
print(f"Eingabe ist nicht leer:      {nicht_leer}")
```

Warum ist das wichtig? Ohne Prüfung bricht das Programm bei ungültigen
Eingaben ab:

```python
alter = int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
```

> 💡 **Ausblick Modul 3:** Dort lernen Sie, mit `if` auf `False` zu reagieren,
> die Eingabe zu wiederholen und Fehler mit `try`/`except` abzufangen.

Nützliche Prüfungen mit String-Methoden:

| Prüfung | Bedeutung | Beispiel |
|---------|-----------|----------|
| `s.isdigit()` | nur Ziffern | `"123".isdigit()` → `True` |
| `s.isalpha()` | nur Buchstaben | `"Anna".isalpha()` → `True` |
| `s.isupper()` / `s.islower()` | nur Gross-/Kleinbuchstaben | `"ABC".isupper()` → `True` |
| `"@" in s` | Zeichen enthalten | `"a@b.ch"` → `True` |
| `len(s) >= 8` | Mindestlänge | `len("geheim")` → 6 → `False` |

### 1.3 Programm-Struktur

```python
# 1. Titel/Begrüssung
print("=== Programm-Titel ===\n")

# 2. Eingaben sammeln
name = input("Name: ")
alter = int(input("Alter: "))

# 3. Verarbeitung
ergebnis = alter + 1

# 4. Ausgabe
print(f"\nErgebnis: {ergebnis}")
```

---

## 💻 Teil 2: Live-Coding (25 Min)

### Beispiel 1: BMI-Rechner (10 Min)

```python
"""
BMI-Rechner
Berechnet den Body-Mass-Index und zeigt die Einordnung als Wahrheitswerte
"""

print("=" * 40)
print("       BMI-Rechner")
print("=" * 40)
print()

# Eingaben
name = input("Ihr Name: ")
groesse_cm = float(input("Körpergrösse (cm): "))
gewicht_kg = float(input("Gewicht (kg): "))

# Verarbeitung
groesse_m = groesse_cm / 100
bmi = gewicht_kg / (groesse_m ** 2)

# Einordnung (Vergleiche liefern True/False)
untergewicht = bmi < 18.5
normalgewicht = bmi >= 18.5 and bmi < 25
uebergewicht = bmi >= 25

# Ausgabe
print()
print("=" * 40)
print(f"Ergebnis für {name}:")
print(f"BMI: {bmi:.1f}")
print(f"Untergewicht:  {untergewicht}")
print(f"Normalgewicht: {normalgewicht}")
print(f"Übergewicht:   {uebergewicht}")
print("=" * 40)
```

> 💡 In Modul 3 ersetzen Sie die drei True/False-Zeilen durch eine
> `if`/`elif`/`else`-Kette, die direkt den passenden Text ausgibt.

### Beispiel 2: Passwort-Check (10 Min)

```python
"""Passwort-Check mit mehreren Kriterien (Ausgabe als Checkliste)"""

print("=== PASSWORT-CHECK ===\n")

passwort = input("Passwort: ")

# Jedes Kriterium ist ein Boolescher Wert
lang_genug = len(passwort) >= 8
hat_gross = passwort != passwort.lower()   # unterscheidet sich von der Kleinschreibung
hat_klein = passwort != passwort.upper()   # unterscheidet sich von der Grossschreibung
nicht_nur_buchstaben = not passwort.isalpha()   # enthält Zahl oder Sonderzeichen

alles_erfuellt = lang_genug and hat_gross and hat_klein and nicht_nur_buchstaben

print("\nPrüfungen:")
print(f"  Mindestens 8 Zeichen:      {lang_genug}")
print(f"  Enthält Grossbuchstaben:   {hat_gross}")
print(f"  Enthält Kleinbuchstaben:   {hat_klein}")
print(f"  Zahl oder Sonderzeichen:   {nicht_nur_buchstaben}")
print(f"\nPasswort gültig: {alles_erfuellt}")
```

**Trick erklärt:** `"Hallo" != "hallo"` ist `True` – also muss mindestens ein
Grossbuchstabe enthalten sein. Bei `"hallo"` ist `"hallo" != "hallo"` `False`.

### Beispiel 3: Text-Statistik (5 Min)

```python
"""Erweiterte Textanalyse mit String-Methoden"""

text = input("Text eingeben:\n")

# Statistiken
anzahl_zeichen = len(text)
anzahl_woerter = len(text.split())
anzahl_saetze = text.count(".")
text_klein = text.lower()
anzahl_vokale = (
    text_klein.count("a")
    + text_klein.count("e")
    + text_klein.count("i")
    + text_klein.count("o")
    + text_klein.count("u")
)

# Ausgabe
print("\n" + "=" * 40)
print("TEXTANALYSE")
print("=" * 40)
print(f"Zeichen gesamt:        {anzahl_zeichen:6d}")
print(f"Wörter:                {anzahl_woerter:6d}")
print(f"Sätze (Punkte):        {anzahl_saetze:6d}")
print(f"Vokale (a,e,i,o,u):    {anzahl_vokale:6d}")
print("=" * 40)
```

---

## ✏️ Teil 3: Übung (15 Min)

### Übung 4: Interaktiver Rechner

Bearbeiten Sie [Übung 4: Interaktiver Rechner](../02-uebungen/uebung-4-rechner.md).

**Schon fertig?** Die Vertiefungsübungen 5–8 sind für zu Hause gedacht, Sie dürfen
aber gerne schon starten:
[String-Methoden](../02-uebungen/uebung-5-string-methoden.md),
[Formatierung](../02-uebungen/uebung-6-formatierung.md),
[Input-Validierung](../02-uebungen/uebung-7-validierung.md),
[Textanalyse](../02-uebungen/uebung-8-textanalyse.md)

---

## 📝 Zusammenfassung

- **Kombination** aller Konzepte
- **Benutzerfreundlichkeit** ist wichtig
- **Struktur:** Titel → Eingabe → Verarbeitung → Ausgabe
- **Formatierung** mit F-Strings
- **Prüfen** von Eingaben mit String-Methoden und Vergleichen (`True`/`False`)
- **Visuelle Elemente** (Linien, Leerzeilen)
- **Ausblick:** Reagieren auf Prüfergebnisse (`if`, Wiederholung, `try`/`except`) in Modul 3

## 🎯 Lernzielkontrolle

- ✅ Alle Konzepte kombinieren?
- ✅ Benutzerfreundliche Programme?
- ✅ Eingaben mit String-Methoden prüfen?
- ✅ Formatierte Ausgaben?
- ✅ Verstehen, warum `int("abc")` einen `ValueError` auslöst?

## 🎓 Abschluss Modul 2

Herzlichen Glückwunsch! Sie haben Modul 2 abgeschlossen.

**Nächste Schritte:**

- Hausaufgaben in [03-nachbearbeitung](../03-nachbearbeitung/)
- Beispielcode in [05-beispiele](../05-beispiele/)
- Materialien in [04-materialien](../04-materialien/)
