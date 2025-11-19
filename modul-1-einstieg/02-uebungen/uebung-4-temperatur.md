# Übung 4: Temperaturumrechner

**Dauer:** 20 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel  
**Lektion:** 4 - Variablen und Zahlen

## 🎯 Lernziele

- Mit Formeln arbeiten
- float-Zahlen nutzen
- Ausgabe formatieren
- Best Practices anwenden

## 📝 Aufgaben

### Teil 1: Celsius zu Fahrenheit (7 Min.)

Erstellen Sie `temperatur.py`:

```python
# Temperaturumrechner
# Celsius zu Fahrenheit: F = (C * 9/5) + 32

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print("=== Celsius zu Fahrenheit ===")
print(f"{celsius}°C = {fahrenheit}°F")
```

Testen Sie mit verschiedenen Werten:
- 0°C (Gefrierpunkt)
- 100°C (Siedepunkt)
- 37°C (Körpertemperatur)

### Teil 2: Fahrenheit zu Celsius (7 Min.)

Fügen Sie hinzu:

```python
# Fahrenheit zu Celsius: C = (F - 32) * 5/9

print("\n=== Fahrenheit zu Celsius ===")
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

Testen Sie:
- 32°F (Gefrierpunkt)
- 212°F (Siedepunkt)
- 98.6°F (Körpertemperatur)

### Teil 3: Kelvin-Umrechnung (6 Min.)

Erweitern Sie:

```python
# Celsius zu Kelvin: K = C + 273.15
# Kelvin zu Celsius: C = K - 273.15

print("\n=== Celsius zu Kelvin ===")
celsius = 25
kelvin = celsius + 273.15
print(f"{celsius}°C = {kelvin}K")

print("\n=== Kelvin zu Celsius ===")
kelvin = 300
celsius = kelvin - 273.15
print(f"{kelvin}K = {celsius}°C")
```

## ✅ Erfolgskriterien

- [ ] Celsius ↔ Fahrenheit funktioniert
- [ ] Kelvin-Umrechnung implementiert
- [ ] Ausgabe schön formatiert
- [ ] Verschiedene Werte getestet
- [ ] Kommentare hinzugefügt

## 🚀 Erweiterungen

### Erweiterung 1: Tabelle

Erstellen Sie eine Umrechnungstabelle:

```python
print("\n=== Umrechnungstabelle ===")
print("Celsius | Fahrenheit | Kelvin")
print("--------|------------|-------")

for c in [0, 10, 20, 30, 40]:
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f"{c:7}°C | {f:10.1f}°F | {k:6.2f}K")
```

### Erweiterung 2: Konstanten

Nutzen Sie Konstanten:

```python
# Konstanten
GEFRIERPUNKT_C = 0
SIEDEPUNKT_C = 100
ABSOLUTER_NULLPUNKT_C = -273.15
```

## 💡 Tipps

- `.1f` = 1 Dezimalstelle
- `.2f` = 2 Dezimalstellen
- `\n` = Neue Zeile
- Formeln in Kommentaren dokumentieren

## 📐 Formeln

**Celsius ↔ Fahrenheit:**
- F = (C × 9/5) + 32
- C = (F - 32) × 5/9

**Celsius ↔ Kelvin:**
- K = C + 273.15
- C = K - 273.15

**Fahrenheit ↔ Kelvin:**
- K = (F - 32) × 5/9 + 273.15
- F = (K - 273.15) × 9/5 + 32

## 🐛 Häufige Fehler

**Fehler:** Falsche Reihenfolge in Formel  
**Lösung:** Klammern verwenden: `(celsius * 9/5) + 32`

**Fehler:** Integer statt Float  
**Lösung:** `9/5` statt `9//5` verwenden

