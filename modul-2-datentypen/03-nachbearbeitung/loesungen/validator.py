"""
Musterlösung zu Aufgabe 2: Eingabe-Validator

Validiert drei verschiedene Benutzereingaben hintereinander:
- E-Mail-Adresse
- Passwort (mit Stärke-Bewertung)
- Telefonnummer (Schweizer Format)

Enthält zusätzlich folgende Bonus-Aufgaben:
- Erweiterte E-Mail-Validierung (kein `@` am Anfang oder Ende,
  Punkt nach dem `@`)
- Passwort-Stärke (Schwach / Mittel / Stark)
- Schweizer Telefonnummer (beginnt mit `0`, genau 10 Ziffern)
"""

# Titel
print("=" * 40)
print("        Eingabe-Validator")
print("=" * 40)


# ============================================================
# E-Mail-Validierung
# ============================================================
print("\n=== E-Mail-Validierung ===")
email = input("E-Mail-Adresse: ")

print(f"\nE-Mail-Adresse: {email}\n")
print("Prüfungen:")

# Prüfung 1: Genau ein @
hat_at = email.count("@") == 1
if hat_at:
    print("✓ Enthält genau ein @")
else:
    print("✗ Enthält genau ein @")

# Prüfung 2: @ nicht am Anfang oder Ende
at_richtig_platziert = False
if hat_at:
    position_at = email.index("@")
    if position_at > 0 and position_at < len(email) - 1:
        at_richtig_platziert = True

if at_richtig_platziert:
    print("✓ @ nicht am Anfang oder Ende")
else:
    print("✗ @ nicht am Anfang oder Ende")

# Prüfung 3: Punkt nach dem @
punkt_nach_at = False
if hat_at:
    position_at = email.index("@")
    if "." in email[position_at:]:
        punkt_nach_at = True

if punkt_nach_at:
    print("✓ Punkt nach dem @")
else:
    print("✗ Punkt nach dem @")

# Prüfung 4: Mindestlänge
lang_genug = len(email) >= 5
if lang_genug:
    print("✓ Mindestens 5 Zeichen")
else:
    print("✗ Mindestens 5 Zeichen")

# Gesamtergebnis
if hat_at and at_richtig_platziert and punkt_nach_at and lang_genug:
    print("→ E-Mail ist gültig!")
else:
    print("→ E-Mail ist ungültig!")


# ============================================================
# Passwort-Validierung
# ============================================================
print("\n=== Passwort-Validierung ===")
passwort = input("Passwort: ")

# Passwort nicht im Klartext anzeigen
print(f"\nPasswort: {'*' * len(passwort)} ({len(passwort)} Zeichen)\n")
print("Prüfungen:")

# Kriterien prüfen
lang_genug = len(passwort) >= 8

hat_gross = False
hat_klein = False
hat_zahl = False
hat_sonderzeichen = False
sonderzeichen = "!?@#$%&*+-_.,;:"

for zeichen in passwort:
    if zeichen.isupper():
        hat_gross = True
    elif zeichen.islower():
        hat_klein = True
    elif zeichen.isdigit():
        hat_zahl = True
    elif zeichen in sonderzeichen:
        hat_sonderzeichen = True

# Ausgabe der Prüfungen
if lang_genug:
    print("✓ Mindestens 8 Zeichen")
else:
    print("✗ Mindestens 8 Zeichen")

if hat_gross:
    print("✓ Enthält Grossbuchstaben")
else:
    print("✗ Enthält Grossbuchstaben")

if hat_klein:
    print("✓ Enthält Kleinbuchstaben")
else:
    print("✗ Enthält Kleinbuchstaben")

if hat_zahl:
    print("✓ Enthält Zahlen")
else:
    print("✗ Enthält Zahlen")

if hat_sonderzeichen:
    print("✓ Enthält Sonderzeichen (Bonus)")
else:
    print("✗ Enthält Sonderzeichen (Bonus)")

# Passwort-Stärke berechnen (Bonus)
erfuellte_kriterien = 0
if hat_gross:
    erfuellte_kriterien += 1
if hat_klein:
    erfuellte_kriterien += 1
if hat_zahl:
    erfuellte_kriterien += 1
if hat_sonderzeichen:
    erfuellte_kriterien += 1

if not lang_genug:
    staerke = "Schwach"
elif len(passwort) > 12 and erfuellte_kriterien == 4:
    staerke = "Stark"
elif erfuellte_kriterien >= 2:
    staerke = "Mittel"
else:
    staerke = "Schwach"

print(f"→ Passwort-Stärke: {staerke}!")


# ============================================================
# Telefonnummer-Validierung (Schweizer Format)
# ============================================================
print("\n=== Telefonnummer-Validierung ===")
telefon = input("Telefonnummer: ")

print(f"\nTelefonnummer: {telefon}\n")
print("Prüfungen:")

# Prüfung 1: Nur Ziffern, Leerzeichen oder Bindestriche
erlaubte_zeichen = True
for zeichen in telefon:
    if not zeichen.isdigit() and zeichen != " " and zeichen != "-":
        erlaubte_zeichen = False

if erlaubte_zeichen:
    print("✓ Nur Zahlen, Leerzeichen oder Bindestriche")
else:
    print("✗ Nur Zahlen, Leerzeichen oder Bindestriche")

# Nur die Ziffern aus der Telefonnummer extrahieren
nur_zahlen = ""
for zeichen in telefon:
    if zeichen.isdigit():
        nur_zahlen = nur_zahlen + zeichen

# Prüfung 2: Beginnt mit 0 (Schweizer Format)
beginnt_mit_null = nur_zahlen.startswith("0")
if beginnt_mit_null:
    print("✓ Beginnt mit 0 (Schweizer Format)")
else:
    print("✗ Beginnt mit 0 (Schweizer Format)")

# Prüfung 3: Genau 10 Ziffern
zehn_ziffern = len(nur_zahlen) == 10
if zehn_ziffern:
    print("✓ Genau 10 Ziffern")
else:
    print("✗ Genau 10 Ziffern")

# Gesamtergebnis und formatierte Ausgabe
if erlaubte_zeichen and beginnt_mit_null and zehn_ziffern:
    # Schöne Formatierung: 079 123 45 67
    formatiert = (
        nur_zahlen[0:3] + " "
        + nur_zahlen[3:6] + " "
        + nur_zahlen[6:8] + " "
        + nur_zahlen[8:10]
    )
    print(f"→ Telefonnummer ist gültig: {formatiert}")
else:
    print("→ Telefonnummer ist ungültig!")

print("=" * 40)
