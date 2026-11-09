# Aufgabe 3: Primzahlen-Finder

**Zeitaufwand:** 2 Stunden  
**Schwierigkeit:** ⭐⭐⭐ Schwer

## 🎯 Ziel

Erstellen Sie ein Programm, das Primzahlen findet und analysiert.

## 📝 Anforderungen

### Basis-Features (Pflicht)

1. **Primzahl-Test:**
   - Eingabe: Eine Zahl
   - Ausgabe: Ist Primzahl? Ja/Nein

2. **Primzahlen bis N:**
   - Eingabe: Obergrenze N
   - Ausgabe: Alle Primzahlen bis N

3. **Statistik:**
   - Anzahl gefundener Primzahlen
   - Grösste Primzahl
   - Kleinste Primzahl

### Erweiterte Features (Optional)

4. **Primfaktorzerlegung:**
   - Zerlege Zahl in Primfaktoren
   - Beispiel: 60 = 2 × 2 × 3 × 5

5. **Primzahl-Zwillinge:**
   - Finde Paare (p, p+2) die beide prim sind
   - Beispiel: (3,5), (5,7), (11,13)

6. **Performance:**
   - Zeitmessung
   - Optimierter Algorithmus

## 💡 Beispiel-Ablauf

```
=== PRIMZAHLEN-FINDER ===

1. Primzahl-Test
2. Primzahlen bis N
3. Primfaktorzerlegung
4. Primzahl-Zwillinge
5. Beenden

Wahl: 1
Zahl: 17
✓ 17 ist eine Primzahl

Wahl: 2
Bis zu welcher Zahl? 30

Primzahlen bis 30:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Statistik:
- Anzahl: 10
- Kleinste: 2
- Grösste: 29

Wahl: 3
Zahl: 60

Primfaktorzerlegung von 60:
60 = 2 × 2 × 3 × 5

Wahl: 4
Bis zu welcher Zahl? 20

Primzahl-Zwillinge bis 20:
(3, 5)
(5, 7)
(11, 13)
(17, 19)

Wahl: 5
Auf Wiedersehen! 👋
```

## ✅ Checkliste

### Basis
- [ ] Primzahl-Test funktioniert
- [ ] Alle Primzahlen bis N
- [ ] Statistik korrekt
- [ ] Menü-System

### Erweitert
- [ ] Primfaktorzerlegung
- [ ] Primzahl-Zwillinge
- [ ] Zeitmessung
- [ ] Optimierter Algorithmus

## 🎯 Lernziele

- Verschachtelte Schleifen
- Break für Optimierung
- Listen für Ergebnisse
- Mathematische Algorithmen
- Performance-Überlegungen

## 💻 Hilfe

> **Hinweis:** Funktionen (`def`) lernen Sie erst in Modul 4 kennen. Lösen Sie
> die Aufgabe deshalb mit Schleifen und Bedingungen direkt im Hauptprogramm.

### Primzahl-Test (Basis)

```python
zahl = int(input("Zahl: "))

ist_primzahl = zahl >= 2          # Zahlen kleiner als 2 sind keine Primzahlen

for teiler in range(2, zahl):
    if zahl % teiler == 0:
        ist_primzahl = False
        break                     # Ein Teiler genügt, die Schleife kann enden

if ist_primzahl:
    print(f"✓ {zahl} ist eine Primzahl")
else:
    print(f"✗ {zahl} ist keine Primzahl")
```

### Primzahl-Test (Optimiert)

```python
zahl = int(input("Zahl: "))

ist_primzahl = zahl >= 2
if zahl > 2 and zahl % 2 == 0:
    ist_primzahl = False

# Nur ungerade Teiler bis zur Wurzel prüfen
teiler = 3
while ist_primzahl and teiler * teiler <= zahl:
    if zahl % teiler == 0:
        ist_primzahl = False
    teiler += 2

print(f"{zahl} ist eine Primzahl: {ist_primzahl}")
```

**Warum nur bis √n?**
- Wenn n = a × b, dann ist a ≤ √n oder b ≤ √n
- Beispiel: 36 = 6 × 6, √36 = 6

### Primzahlen sammeln

Der Primzahl-Test steckt hier in einer äusseren Schleife über alle Zahlen:

```python
grenze = int(input("Bis zu welcher Zahl? "))
primzahlen = []

for zahl in range(2, grenze + 1):
    ist_primzahl = True
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            ist_primzahl = False
            break
    if ist_primzahl:
        primzahlen.append(zahl)

print(primzahlen)
```

### Primfaktorzerlegung

```python
n = int(input("Zahl: "))
faktoren = []
teiler = 2

while n > 1:
    while n % teiler == 0:
        faktoren.append(teiler)
        n //= teiler
    teiler += 1

print(faktoren)
```

### Zeitmessung

> **Vorgriff:** Dieses Konzept (z. B. Module importieren) wird in Modul 5 behandelt.

```python
import time

start = time.time()
# ... Code ...
ende = time.time()

dauer = ende - start
print(f"Dauer: {dauer:.3f} Sekunden")
```

## 📦 Abgabe

**Datei:** `primzahlen.py`

**Testen Sie:**
- Kleine Zahlen (< 100)
- Grosse Zahlen (> 1000)
- Sonderfälle (0, 1, 2)
- Performance

## 🌟 Bonus-Ideen

- Sieb des Eratosthenes (sehr schnell!)
- Primzahl-Dichte visualisieren
- N-te Primzahl finden
- Mersenne-Primzahlen (2^p - 1)

## 🔗 Weiter

[Reflexion](./reflexion.md)

