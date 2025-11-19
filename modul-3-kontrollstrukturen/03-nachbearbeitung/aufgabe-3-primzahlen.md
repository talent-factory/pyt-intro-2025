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

### Primzahl-Test (Basis)

```python
def ist_primzahl(n):
    """Prüft ob n eine Primzahl ist"""
    if n < 2:
        return False
    
    for teiler in range(2, n):
        if n % teiler == 0:
            return False
    
    return True
```

### Primzahl-Test (Optimiert)

```python
def ist_primzahl(n):
    """Optimierter Primzahl-Test"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Nur bis Wurzel prüfen
    for teiler in range(3, int(n ** 0.5) + 1, 2):
        if n % teiler == 0:
            return False
    
    return True
```

**Warum nur bis √n?**
- Wenn n = a × b, dann ist a ≤ √n oder b ≤ √n
- Beispiel: 36 = 6 × 6, √36 = 6

### Primzahlen sammeln

```python
def finde_primzahlen(n):
    """Findet alle Primzahlen bis n"""
    primzahlen = []
    
    for zahl in range(2, n + 1):
        if ist_primzahl(zahl):
            primzahlen.append(zahl)
    
    return primzahlen
```

### Primfaktorzerlegung

```python
def primfaktoren(n):
    """Zerlegt n in Primfaktoren"""
    faktoren = []
    teiler = 2
    
    while n > 1:
        while n % teiler == 0:
            faktoren.append(teiler)
            n //= teiler
        teiler += 1
    
    return faktoren
```

### Zeitmessung

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

