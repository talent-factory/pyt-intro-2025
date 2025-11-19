# Lektion 3: For-Schleifen & Listen

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- For-Schleifen mit range() nutzen
- Über Listen iterieren
- Listen erstellen und manipulieren
- Enumerate verstehen

## 📖 Theorie (15 Min)

### For-Schleife mit range()

```python
# 0 bis 4
for i in range(5):
    print(i)

# 1 bis 5
for i in range(1, 6):
    print(i)

# Schrittweite 2
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Listen

```python
# Liste erstellen
fruechte = ["Apfel", "Banane", "Orange"]

# Zugriff
print(fruechte[0])  # Apfel
print(fruechte[-1])  # Orange (letztes Element)

# Hinzufügen
fruechte.append("Kiwi")

# Entfernen
fruechte.remove("Banane")

# Länge
print(len(fruechte))
```

### Über Listen iterieren

```python
fruechte = ["Apfel", "Banane", "Orange"]

# Direkt über Elemente
for frucht in fruechte:
    print(frucht)

# Mit Index
for i in range(len(fruechte)):
    print(f"{i}: {fruechte[i]}")

# Mit enumerate (elegant!)
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Multiplikationstabelle

```python
"""Multiplikationstabelle für eine Zahl"""
zahl = int(input("Zahl: "))

print(f"\nMultiplikationstabelle für {zahl}:")
print("-" * 20)

for i in range(1, 11):
    ergebnis = zahl * i
    print(f"{zahl} x {i:2} = {ergebnis:3}")
```

**Ausgabe für zahl=7:**
```
Multiplikationstabelle für 7:
--------------------
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
...
```

### Beispiel 2: Einkaufsliste

```python
"""Einfache Einkaufsliste"""
einkaufsliste = []

print("Einkaufsliste (leer = fertig)")

while True:
    artikel = input("Artikel: ")
    
    if artikel == "":
        break
    
    einkaufsliste.append(artikel)

print("\n=== Ihre Einkaufsliste ===")
for i, artikel in enumerate(einkaufsliste, start=1):
    print(f"{i}. {artikel}")

print(f"\nGesamt: {len(einkaufsliste)} Artikel")
```

**Interaktion:**
```
Artikel: Milch
Artikel: Brot
Artikel: Eier
Artikel: 

=== Ihre Einkaufsliste ===
1. Milch
2. Brot
3. Eier

Gesamt: 3 Artikel
```

### Beispiel 3: Statistik berechnen

```python
"""Statistik für Zahlenliste"""
zahlen = [23, 45, 12, 67, 34, 89, 15, 56]

# Summe
summe = 0
for zahl in zahlen:
    summe += zahl

# Durchschnitt
durchschnitt = summe / len(zahlen)

# Maximum
maximum = zahlen[0]
for zahl in zahlen:
    if zahl > maximum:
        maximum = zahl

# Minimum
minimum = zahlen[0]
for zahl in zahlen:
    if zahl < minimum:
        minimum = zahl

# Ausgabe
print(f"Zahlen: {zahlen}")
print(f"Anzahl: {len(zahlen)}")
print(f"Summe: {summe}")
print(f"Durchschnitt: {durchschnitt:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
```

## ✏️ Übungen (15 Min)

### Übung 5: Gerade Zahlen filtern
Siehe [Übung 5: Gerade Zahlen](../02-uebungen/uebung-5-gerade-zahlen.md)

### Übung 6: Notenliste
Siehe [Übung 6: Notenliste](../02-uebungen/uebung-6-notenliste.md)

## 📝 Zusammenfassung

### For-Schleifen

| Syntax | Verwendung |
|--------|------------|
| `for i in range(n)` | 0 bis n-1 |
| `for i in range(a, b)` | a bis b-1 |
| `for i in range(a, b, s)` | a bis b-1, Schritt s |
| `for x in liste` | Über Liste iterieren |

### Listen-Methoden

| Methode | Beschreibung |
|---------|--------------|
| `append(x)` | Element hinzufügen |
| `remove(x)` | Element entfernen |
| `pop()` | Letztes Element entfernen |
| `len(liste)` | Länge |
| `sort()` | Sortieren |

## 🔗 Weiter

[Lektion 4: Verschachtelte Strukturen](./lektion-4-verschachtelt.md)

