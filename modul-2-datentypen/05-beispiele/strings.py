"""
String-Operationen
Demonstriert grundlegende String-Operationen in Python.

Konzepte:
- String-Erstellung
- Konkatenation
- Multiplikation
- Indexierung
- Slicing
- String-Methoden
"""

# String-Erstellung
print("=== String-Erstellung ===\n")

name = "Anna"
stadt = 'Zürich'
text = """Dies ist ein
mehrzeiliger
Text"""

print(f"Name: {name}")
print(f"Stadt: {stadt}")
print(f"Text:\n{text}\n")

# Konkatenation (Verkettung)
print("=== Konkatenation ===\n")

vorname = "Max"
nachname = "Muster"
vollname = vorname + " " + nachname

print(f"Vorname: {vorname}")
print(f"Nachname: {nachname}")
print(f"Vollname: {vollname}\n")

# Multiplikation
print("=== Multiplikation ===\n")

linie = "=" * 40
stern_linie = "*" * 20

print(linie)
print("Titel")
print(linie)
print(stern_linie)
print()

# Länge
print("=== Länge ===\n")

wort = "Python"
laenge = len(wort)

print(f"Wort: {wort}")
print(f"Länge: {laenge} Zeichen\n")

# Indexierung
print("=== Indexierung ===\n")

text = "Python"
print(f"Text: {text}")
print(f"Erstes Zeichen (Index 0): {text[0]}")
print(f"Zweites Zeichen (Index 1): {text[1]}")
print(f"Letztes Zeichen (Index -1): {text[-1]}")
print(f"Vorletztes Zeichen (Index -2): {text[-2]}\n")

# Slicing
print("=== Slicing ===\n")

text = "Python Programmierung"
print(f"Text: {text}")
print(f"Erste 6 Zeichen [0:6]: {text[0:6]}")
print(f"Ab Zeichen 7 [7:]: {text[7:]}")
print(f"Bis Zeichen 6 [:6]: {text[:6]}")
print(f"Jedes 2. Zeichen [::2]: {text[::2]}")
print(f"Rückwärts [::-1]: {text[::-1]}\n")

# String-Methoden
print("=== String-Methoden ===\n")

text = "  Hallo Welt  "
print(f"Original: '{text}'")
print(f"Grossbuchstaben: '{text.upper()}'")
print(f"Kleinbuchstaben: '{text.lower()}'")
print(f"Titel-Format: '{text.title()}'")
print(f"Ohne Leerzeichen: '{text.strip()}'")
print(f"Ersetzen: '{text.replace('Hallo', 'Hi')}'")
print(f"Aufteilen: {text.split()}\n")

# Weitere Methoden
print("=== Weitere Methoden ===\n")

text = "Python"
print(f"Text: {text}")
print(f"Beginnt mit 'Py': {text.startswith('Py')}")
print(f"Endet mit 'on': {text.endswith('on')}")
print(f"Enthält 'th': {'th' in text}")
print(f"Ist Grossbuchstaben: {text.isupper()}")
print(f"Ist Kleinbuchstaben: {text.islower()}")
print(f"Ist Alphanumerisch: {text.isalnum()}\n")

# String-Verkettung mit join()
print("=== Join-Methode ===\n")

woerter = ["Python", "ist", "toll"]
satz = " ".join(woerter)

print(f"Wörter: {woerter}")
print(f"Satz: {satz}")
print(f"Mit Bindestrichen: {'-'.join(woerter)}\n")

# Wichtig: Strings sind unveränderlich!
print("=== Unveränderlichkeit ===\n")

name = "anna"
print(f"Original: {name}")

name.upper()  # Ändert NICHT den Original-String!
print(f"Nach .upper() (ohne Zuweisung): {name}")

name = name.upper()  # Korrekt: Neuen Wert zuweisen
print(f"Nach .upper() (mit Zuweisung): {name}")

