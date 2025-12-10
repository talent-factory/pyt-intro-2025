# Aufgabe 2: BMI-Rechner

**Zeitaufwand:** 60-90 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziele

- Formeln anwenden
- Mit Dezimalzahlen rechnen
- Ausgabe gestalten

## 📝 Aufgabenstellung

Erstellen Sie `bmi_rechner.py`, der den Body-Mass-Index berechnet.

### Formel

```
BMI = Gewicht (kg) / (Grösse (m))²
```

### Anforderungen

1. Berechnen Sie BMI für verschiedene Personen
2. Geben Sie BMI mit 1 Dezimalstelle aus
3. Zeigen Sie Interpretation (siehe unten)

### BMI-Kategorien

- Untergewicht: BMI < 18.5
- Normalgewicht: 18.5 ≤ BMI < 25
- Übergewicht: 25 ≤ BMI < 30
- Adipositas: BMI ≥ 30

## 💻 Beispiel-Ausgabe

```
=== BMI-Rechner ===

Person 1:
Grösse: 1.75 m
Gewicht: 70 kg
BMI: 22.9
Kategorie: Normalgewicht

Person 2:
Grösse: 1.80 m
Gewicht: 90 kg
BMI: 27.8
Kategorie: Übergewicht
```

## ✅ Bewertungskriterien

- [ ] BMI wird korrekt berechnet
- [ ] Ausgabe ist formatiert
- [ ] Mindestens 3 Personen berechnet
- [ ] Code ist kommentiert

## 🚀 Erweiterungen (optional)

1. **Idealgewicht:** Berechnen Sie Idealgewicht für BMI 22
2. **Differenz:** Zeigen Sie Differenz zum Idealgewicht
3. **Verschiedene Einheiten:** cm und kg als Eingabe

## 💡 Tipps

- Potenz: `groesse ** 2`
- Formatierung: `f"{bmi:.1f}"`
- Kommentare für Formeln

