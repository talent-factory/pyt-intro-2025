# Lektion 2: Parameter & Rückgabewerte

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

Nach dieser Lektion können Sie:
- Funktionen mit Parametern definieren
- Rückgabewerte mit `return` verwenden
- Default-Werte für Parameter setzen
- Funktionsergebnisse in Variablen speichern

## 📖 Theorie (15 Min)

### Parameter

Parameter ermöglichen es, **Werte an Funktionen zu übergeben**:

```python
def gruesse(name):
    """Begrüsst eine Person."""
    print(f"Hallo {name}!")

gruesse("Anna")  # Hallo Anna!
gruesse("Max")   # Hallo Max!
```

### Mehrere Parameter

```python
def addiere(a, b):
    """Addiert zwei Zahlen."""
    summe = a + b
    print(f"{a} + {b} = {summe}")

addiere(5, 3)  # 5 + 3 = 8
```

### Rückgabewerte mit `return`

```python
def addiere(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

ergebnis = addiere(5, 3)
print(ergebnis)  # 8
```

**Wichtig:** `return` beendet die Funktion und gibt einen Wert zurück!

### Default-Werte

```python
def gruesse(name="Gast"):
    """Begrüsst eine Person (Standard: Gast)."""
    print(f"Hallo {name}!")

gruesse()         # Hallo Gast!
gruesse("Anna")   # Hallo Anna!
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Berechnung mit Return

```python
def berechne_quadrat(zahl):
    """Berechnet das Quadrat einer Zahl."""
    return zahl * zahl

# Verwendung
x = 5
quadrat = berechne_quadrat(x)
print(f"Das Quadrat von {x} ist {quadrat}")

# Direkt in Berechnung
flaeche = berechne_quadrat(10)
print(f"Fläche: {flaeche} m²")
```

### Beispiel 2: Mehrere Parameter

```python
def berechne_rechteck(laenge, breite):
    """Berechnet Fläche und Umfang eines Rechtecks."""
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    
    print(f"Rechteck {laenge} × {breite}:")
    print(f"  Fläche: {flaeche} m²")
    print(f"  Umfang: {umfang} m")
    
    return flaeche

# Verwendung
f = berechne_rechteck(5, 3)
print(f"Gespeicherte Fläche: {f}")
```

### Beispiel 3: Default-Parameter

```python
def formatiere_preis(betrag, waehrung="CHF"):
    """Formatiert einen Preis mit Währung."""
    return f"{betrag:.2f} {waehrung}"

# Verschiedene Aufrufe
print(formatiere_preis(19.99))           # 19.99 CHF
print(formatiere_preis(29.50, "EUR"))    # 29.50 EUR
print(formatiere_preis(15))              # 15.00 CHF
```

### Beispiel 4: Funktionen kombinieren

```python
def ist_gerade(zahl):
    """Prüft ob eine Zahl gerade ist."""
    return zahl % 2 == 0

def zaehle_gerade(zahlen):
    """Zählt gerade Zahlen in einer Liste."""
    anzahl = 0
    for zahl in zahlen:
        if ist_gerade(zahl):
            anzahl += 1
    return anzahl

# Verwendung
meine_zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = zaehle_gerade(meine_zahlen)
print(f"Anzahl gerader Zahlen: {gerade}")
```

## ✏️ Übungen (15 Min)

### Übung 3: Parameter-Varianten (10 Min)

Siehe [Übung 3](../02-uebungen/uebung-3-parameter.md)

### Übung 4: Funktionen & Listen (5 Min)

Siehe [Übung 4](../02-uebungen/uebung-4-listen.md)

## 📚 Zusammenfassung

- Parameter: `def funktion(parameter):`
- Return: `return wert`
- Default-Werte: `def funktion(param="default"):`
- Rückgabewerte in Variablen speichern

## 🔗 Weiter

- [Lektion 3: Listen vertiefen](./lektion-3-listen.md)
- [Beispiele](../05-beispiele/parameter.py)

