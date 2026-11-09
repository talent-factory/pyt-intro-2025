# Aufgabe 2: Eingabe-Validator

**Dauer:** 1.5 Stunden
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

Boolesche Werte und String-Methoden für Validierung nutzen

> **Hinweis:** Jede Prüfung ergibt einen Booleschen Wert (`True`/`False`), den Sie
> mit einem F-String ausgeben. Wie Ihr Programm mit `if` darauf reagiert, lernen
> Sie in Modul 3 – hier brauchen Sie weder `if` noch Schleifen.

## 📝 Aufgabenstellung

Erstellen Sie ein Programm `validator.py`, das verschiedene Benutzereingaben validiert:

1. **E-Mail-Adresse:**
   - Enthält `@`
   - Enthält `.`
   - Mindestens 5 Zeichen lang

2. **Passwort:**
   - Mindestens 8 Zeichen
   - Enthält Grossbuchstaben
   - Enthält Kleinbuchstaben
   - Enthält Zahlen

3. **Telefonnummer:**
   - Nur Zahlen und Leerzeichen/Bindestriche
   - Mindestens 10 Ziffern

## 💡 Beispiel-Ausgabe

```text
========================================
        Eingabe-Validator
========================================

=== E-Mail-Validierung ===
E-Mail-Adresse: max@example.com

Prüfungen:
  Enthält @:               True
  Enthält .:               True
  Mindestens 5 Zeichen:    True
→ E-Mail gültig: True

=== Passwort-Validierung ===
Passwort: Test1234

Prüfungen:
  Mindestens 8 Zeichen:    True
  Enthält Grossbuchstaben: True
  Enthält Kleinbuchstaben: True
  Enthält Zahlen:          True
→ Passwort gültig: True

=== Telefonnummer-Validierung ===
Telefonnummer: 079 123 45 67

Prüfungen:
  Nur Zahlen/Leerzeichen/Bindestriche:  True
  Mindestens 10 Ziffern:   True
→ Telefonnummer gültig: True
========================================
```

## 🔧 Hilfestellung

### E-Mail-Validierung

```python
email = input("E-Mail-Adresse: ")

hat_at = "@" in email
hat_punkt = "." in email
lang_genug = len(email) >= 5

email_gueltig = hat_at and hat_punkt and lang_genug

print("\nPrüfungen:")
print(f"  Enthält @:               {hat_at}")
print(f"  Enthält .:               {hat_punkt}")
print(f"  Mindestens 5 Zeichen:    {lang_genug}")
print(f"→ E-Mail gültig: {email_gueltig}")
```

### Passwort-Validierung

```python
passwort = input("Passwort: ")

lang_genug = len(passwort) >= 8

# Grossbuchstabe enthalten? Dann unterscheidet sich das Passwort von seiner Kleinschreibung
hat_gross = passwort != passwort.lower()
# Kleinbuchstabe enthalten? Dann unterscheidet es sich von seiner Grossschreibung
hat_klein = passwort != passwort.upper()

# Zahl enthalten? Jede Ziffer einzeln mit "in" und "or" prüfen
hat_zahl = (
    "0" in passwort or "1" in passwort or "2" in passwort or "3" in passwort
    or "4" in passwort or "5" in passwort or "6" in passwort or "7" in passwort
    or "8" in passwort or "9" in passwort
)

passwort_gueltig = lang_genug and hat_gross and hat_klein and hat_zahl
```

> 💡 Das ist mit `or` etwas lang. Mit einer Schleife (Modul 3) geht es
> deutlich kürzer – ein guter Grund, sich auf Modul 3 zu freuen.

### Telefonnummer-Validierung

```python
telefon = input("Telefonnummer: ")

# Leerzeichen und Bindestriche entfernen
nur_ziffern = telefon.replace(" ", "").replace("-", "")

ist_numerisch = nur_ziffern.isdigit()
lang_genug = len(nur_ziffern) >= 10

telefon_gueltig = ist_numerisch and lang_genug
```

## ✅ Checkliste

- [ ] E-Mail-Validierung implementiert
- [ ] Passwort-Validierung implementiert
- [ ] Telefonnummer-Validierung implementiert
- [ ] Alle Prüfungen ausgegeben
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm getestet

## 🚀 Bonus-Aufgaben

**Schon jetzt lösbar:**

1. **Erweiterte E-Mail-Validierung:**
   - Kein `@` am Anfang oder Ende (`.startswith()`, `.endswith()`)
   - Genau ein `@` (`.count("@") == 1`)

2. **Schweizer Telefonnummer:**
   - Beginnt mit 0
   - Genau 10 Ziffern

**Nach Modul 3** (benötigen `if` bzw. Schleifen):

3. **Passwort-Stärke:**
   - Schwach (< 8 Zeichen)
   - Mittel (8-12 Zeichen, 2 Kriterien)
   - Stark (> 12 Zeichen, alle Kriterien)

4. **Rückmeldung mit `if`/`else`:**
   - Statt `True`/`False` Meldungen wie «E-Mail ist gültig!» ausgeben

5. **Wiederholung:**
   - Lassen Sie den Benutzer wiederholen bei ungültiger Eingabe

## 💡 Tipps

- Nutzen Sie String-Methoden: `.isdigit()`, `.lower()`, `.upper()`, `.replace()`
- Verwenden Sie `in` für Teilstring-Prüfung
- Kombinieren Sie Bedingungen mit `and`, `or`, `not`
- Geben Sie die Ergebnisse jeder Prüfung einzeln aus

## 🆘 Häufige Probleme

**Problem:** Telefonnummer mit Sonderzeichen

**Lösung:** Entfernen Sie die erlaubten Trennzeichen mit `.replace()` und prüfen Sie den Rest mit `.isdigit()` (siehe oben).

**Problem:** `hat_gross` ist `True`, obwohl nur Kleinbuchstaben eingegeben wurden

**Lösung:** Prüfen Sie den Vergleich: Er muss `passwort != passwort.lower()` lauten
(nicht `==`).

Viel Erfolg! 🚀
