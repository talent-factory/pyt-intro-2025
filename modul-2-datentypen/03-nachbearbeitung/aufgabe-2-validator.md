# Aufgabe 2: Eingabe-Validator

**Dauer:** 1.5 Stunden  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziel

Boolesche Werte und String-Methoden für Validierung nutzen

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
   - Mindestens 10 Zeichen

## 💡 Beispiel-Ausgabe

```
========================================
        Eingabe-Validator
========================================

=== E-Mail-Validierung ===
E-Mail-Adresse: max@example.com

Prüfungen:
✓ Enthält @
✓ Enthält .
✓ Mindestens 5 Zeichen
→ E-Mail ist gültig!

=== Passwort-Validierung ===
Passwort: Test1234

Prüfungen:
✓ Mindestens 8 Zeichen
✓ Enthält Grossbuchstaben
✓ Enthält Kleinbuchstaben
✓ Enthält Zahlen
→ Passwort ist stark!

=== Telefonnummer-Validierung ===
Telefonnummer: 079 123 45 67

Prüfungen:
✓ Nur Zahlen und Leerzeichen
✓ Mindestens 10 Zeichen
→ Telefonnummer ist gültig!
========================================
```

## 🔧 Hilfestellung

### E-Mail-Validierung

```python
email = input("E-Mail-Adresse: ")

hat_at = "@" in email
hat_punkt = "." in email
lang_genug = len(email) >= 5

if hat_at and hat_punkt and lang_genug:
    print("→ E-Mail ist gültig!")
else:
    print("→ E-Mail ist ungültig!")
```

### Passwort-Validierung

```python
passwort = input("Passwort: ")

lang_genug = len(passwort) >= 8
hat_gross = any(c.isupper() for c in passwort)
hat_klein = any(c.islower() for c in passwort)
hat_zahl = any(c.isdigit() for c in passwort)

# Vereinfachte Version ohne any():
hat_gross = False
for zeichen in passwort:
    if zeichen.isupper():
        hat_gross = True
        break
```

### Telefonnummer-Validierung

```python
telefon = input("Telefonnummer: ")

# Leerzeichen und Bindestriche entfernen
nur_zahlen = telefon.replace(" ", "").replace("-", "")

ist_numerisch = nur_zahlen.isdigit()
lang_genug = len(nur_zahlen) >= 10
```

## ✅ Checkliste

- [ ] E-Mail-Validierung implementiert
- [ ] Passwort-Validierung implementiert
- [ ] Telefonnummer-Validierung implementiert
- [ ] Alle Prüfungen ausgegeben
- [ ] Benutzerfreundliche Ausgabe
- [ ] Programm getestet

## 🚀 Bonus-Aufgaben

1. **Erweiterte E-Mail-Validierung:**
   - Kein `@` am Anfang oder Ende
   - Punkt nach dem `@`

2. **Passwort-Stärke:**
   - Schwach (< 8 Zeichen)
   - Mittel (8-12 Zeichen, 2 Kriterien)
   - Stark (> 12 Zeichen, alle Kriterien)

3. **Schweizer Telefonnummer:**
   - Beginnt mit 0
   - Genau 10 Ziffern

4. **Wiederholung:**
   - Lassen Sie den Benutzer wiederholen bei ungültiger Eingabe

## 💡 Tipps

- Nutzen Sie String-Methoden: `.isupper()`, `.islower()`, `.isdigit()`
- Verwenden Sie `in` für Teilstring-Prüfung
- Kombinieren Sie Bedingungen mit `and`, `or`
- Geben Sie hilfreiche Fehlermeldungen aus

## 🆘 Häufige Probleme

**Problem:** `any()` ist unbekannt

**Lösung:** Verwenden Sie eine Schleife:
```python
hat_gross = False
for zeichen in passwort:
    if zeichen.isupper():
        hat_gross = True
```

**Problem:** Telefonnummer mit Sonderzeichen

**Lösung:** Entfernen Sie alle Nicht-Zahlen:
```python
nur_zahlen = ""
for zeichen in telefon:
    if zeichen.isdigit():
        nur_zahlen += zeichen
```

Viel Erfolg! 🚀

