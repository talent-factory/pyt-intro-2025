# Aufgabe 3: Einfache Berechnungen

**Zeitaufwand:** 60-90 Minuten  
**Schwierigkeit:** ⭐⭐⭐ Fortgeschritten

## 🎯 Lernziele

- Verschiedene Berechnungen durchführen
- Code strukturieren
- Best Practices anwenden

## 📝 Aufgabenstellung

Erstellen Sie `berechnungen.py` mit folgenden Berechnungen:

### 1. Zinsrechner

Berechnen Sie Zinsen für ein Sparkonto:

```
Endkapital = Startkapital * (1 + Zinssatz)^Jahre
```

**Beispiel:**
- Startkapital: 1000 EUR
- Zinssatz: 3% (0.03)
- Jahre: 5
- Endkapital: ?

### 2. Benzinverbrauch

Berechnen Sie Kosten für eine Fahrt:

```
Verbrauch (Liter) = Strecke (km) * Verbrauch pro 100km / 100
Kosten = Verbrauch * Preis pro Liter
```

**Beispiel:**
- Strecke: 350 km
- Verbrauch: 6.5 L/100km
- Preis: 1.80 EUR/L
- Kosten: ?

### 3. Pizzarechner

Berechnen Sie Preis pro Person:

```
Preis pro Person = (Anzahl Pizzen * Preis pro Pizza) / Anzahl Personen
```

**Beispiel:**
- 3 Pizzen à 12 EUR
- 4 Personen
- Preis pro Person: ?

### 4. Zeitumrechnung

Rechnen Sie Sekunden in Stunden, Minuten, Sekunden um:

```
Stunden = Sekunden // 3600
Minuten = (Sekunden % 3600) // 60
Sekunden = Sekunden % 60
```

**Beispiel:**
- 7325 Sekunden = ? Stunden, ? Minuten, ? Sekunden

## 💻 Beispiel-Ausgabe

```
=== Berechnungen ===

1. Zinsrechner:
Startkapital: 1000.00 EUR
Zinssatz: 3.0%
Jahre: 5
Endkapital: 1159.27 EUR
Gewinn: 159.27 EUR

2. Benzinverbrauch:
Strecke: 350 km
Verbrauch: 6.5 L/100km
Preis: 1.80 EUR/L
Benötigte Liter: 22.75 L
Kosten: 40.95 EUR

3. Pizzarechner:
3 Pizzen à 12.00 EUR
4 Personen
Preis pro Person: 9.00 EUR

4. Zeitumrechnung:
7325 Sekunden = 2 Stunden, 2 Minuten, 5 Sekunden
```

## ✅ Bewertungskriterien

- [ ] Alle 4 Berechnungen funktionieren
- [ ] Ausgabe ist schön formatiert
- [ ] Code ist gut strukturiert
- [ ] Kommentare erklären Formeln
- [ ] Variablennamen sind aussagekräftig

## 🚀 Erweiterungen (optional)

1. **Mehr Berechnungen:** Trinkgeld, Rabatt, Mehrwertsteuer
2. **Funktionen:** Jede Berechnung als Funktion (Vorgriff auf Modul 4)
3. **Fehlerbehandlung:** Prüfen Sie auf Division durch 0

## 💡 Tipps

- `//` für Ganzzahldivision
- `%` für Rest (Modulo)
- `**` für Potenz
- Konstanten in GROSSBUCHSTABEN

