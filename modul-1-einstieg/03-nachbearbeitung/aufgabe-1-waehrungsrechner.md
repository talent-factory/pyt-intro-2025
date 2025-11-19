# Aufgabe 1: Währungsrechner

**Zeitaufwand:** 60-90 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziele

- Mit float-Zahlen arbeiten
- Formeln implementieren
- Ausgabe formatieren
- Code dokumentieren

## 📝 Aufgabenstellung

Erstellen Sie ein Programm `waehrungsrechner.py`, das Beträge zwischen verschiedenen Währungen umrechnet.

### Anforderungen

1. **EUR zu CHF** (Schweizer Franken)
2. **EUR zu USD** (US-Dollar)
3. **EUR zu GBP** (Britisches Pfund)
4. **Rückrechnung** (z.B. CHF zu EUR)

### Wechselkurse (Stand: 2025)

```python
EUR_ZU_CHF = 0.95
EUR_ZU_USD = 1.10
EUR_ZU_GBP = 0.85
```

## 💻 Beispiel-Ausgabe

```
=== Währungsrechner ===

EUR zu anderen Währungen:
100.00 EUR = 95.00 CHF
100.00 EUR = 110.00 USD
100.00 EUR = 85.00 GBP

CHF zu EUR:
100.00 CHF = 105.26 EUR

USD zu EUR:
100.00 USD = 90.91 EUR

GBP zu EUR:
100.00 GBP = 117.65 EUR
```

## ✅ Bewertungskriterien

- [ ] Alle Umrechnungen funktionieren
- [ ] Ausgabe ist formatiert (2 Dezimalstellen)
- [ ] Code ist kommentiert
- [ ] Variablennamen sind aussagekräftig
- [ ] Verschiedene Beträge getestet

## 🚀 Erweiterungen (optional)

1. **Mehr Währungen:** JPY, CNY, AUD
2. **Tabelle:** Umrechnungstabelle für verschiedene Beträge
3. **Gebühren:** Berücksichtigen Sie Wechselgebühren (z.B. 2%)

## 💡 Tipps

- Rückrechnung: `eur = chf / EUR_ZU_CHF`
- Formatierung: `f"{betrag:.2f}"`
- Konstanten in GROSSBUCHSTABEN

