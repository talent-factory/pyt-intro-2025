"""
Listen
Demonstriert Listen-Operationen in Python.

Konzepte:
- Listen erstellen
- Auf Elemente zugreifen
- Listen ändern
- Listen-Methoden
- Listen durchlaufen
"""

# Listen erstellen
print("=== Listen erstellen ===\n")

zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Max", "Lisa"]
gemischt = [1, "Hallo", 3.14, True]
leer = []

print(f"Zahlen: {zahlen}")
print(f"Namen: {namen}")
print(f"Gemischt: {gemischt}")
print(f"Leer: {leer}\n")

# Auf Elemente zugreifen
print("=== Auf Elemente zugreifen ===\n")

fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]

print(f"Liste: {fruechte}")
print(f"Erstes Element [0]: {fruechte[0]}")
print(f"Zweites Element [1]: {fruechte[1]}")
print(f"Letztes Element [-1]: {fruechte[-1]}")
print(f"Vorletztes Element [-2]: {fruechte[-2]}\n")

# Slicing
print("=== Slicing ===\n")

zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Liste: {zahlen}")
print(f"Erste 3 [0:3]: {zahlen[0:3]}")
print(f"Ab Index 5 [5:]: {zahlen[5:]}")
print(f"Bis Index 5 [:5]: {zahlen[:5]}")
print(f"Jedes 2. Element [::2]: {zahlen[::2]}")
print(f"Rückwärts [::-1]: {zahlen[::-1]}\n")

# Elemente hinzufügen
print("=== Elemente hinzufügen ===\n")

fruechte = ["Apfel", "Banane"]
print(f"Start: {fruechte}")

fruechte.append("Orange")
print(f"Nach append: {fruechte}")

fruechte.insert(1, "Kiwi")
print(f"Nach insert(1): {fruechte}\n")

# Elemente entfernen
print("=== Elemente entfernen ===\n")

fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]
print(f"Start: {fruechte}")

fruechte.remove("Banane")
print(f"Nach remove: {fruechte}")

letztes = fruechte.pop()
print(f"Pop gibt zurück: {letztes}")
print(f"Nach pop: {fruechte}\n")

# Listen-Methoden
print("=== Listen-Methoden ===\n")

zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {zahlen}")

zahlen.sort()
print(f"Sortiert: {zahlen}")

zahlen.reverse()
print(f"Umgekehrt: {zahlen}")

anzahl = zahlen.count(1)
print(f"Anzahl 1: {anzahl}")

index = zahlen.index(5)
print(f"Index von 5: {index}\n")

# Länge
print("=== Länge ===\n")

fruechte = ["Apfel", "Banane", "Orange"]
print(f"Liste: {fruechte}")
print(f"Länge: {len(fruechte)}\n")

# Listen kombinieren
print("=== Listen kombinieren ===\n")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

kombiniert = liste1 + liste2
print(f"Liste 1: {liste1}")
print(f"Liste 2: {liste2}")
print(f"Kombiniert: {kombiniert}\n")

# Listen vervielfachen
print("=== Listen vervielfachen ===\n")

liste = [1, 2, 3]
verdoppelt = liste * 2

print(f"Original: {liste}")
print(f"Verdoppelt: {verdoppelt}\n")

# In Liste prüfen
print("=== In Liste prüfen ===\n")

fruechte = ["Apfel", "Banane", "Orange"]

print(f"Liste: {fruechte}")
print(f"'Apfel' in Liste: {'Apfel' in fruechte}")
print(f"'Kiwi' in Liste: {'Kiwi' in fruechte}\n")

# Liste durchlaufen
print("=== Liste durchlaufen ===\n")

namen = ["Anna", "Max", "Lisa"]

for name in namen:
    print(f"Hallo {name}!")

print()

# Mit Index
print("=== Mit Index durchlaufen ===\n")

for i in range(len(namen)):
    print(f"{i + 1}. {namen[i]}")

print()

# Liste kopieren
print("=== Liste kopieren ===\n")

original = [1, 2, 3]
kopie = original.copy()  # Oder: kopie = original[:]

kopie.append(4)

print(f"Original: {original}")
print(f"Kopie: {kopie}\n")

# Liste leeren
print("=== Liste leeren ===\n")

liste = [1, 2, 3, 4, 5]
print(f"Vor clear: {liste}")

liste.clear()
print(f"Nach clear: {liste}")
