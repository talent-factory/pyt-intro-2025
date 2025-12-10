# Übung: Funktionen & Listen

**Dauer:** 15 Minuten

Schreiben Sie:

1. `summe(zahlen)` - Gibt Summe aller Zahlen zurück
2. `finde_maximum(zahlen)` - Gibt grösste Zahl zurück
3. `nur_positive(zahlen)` - Gibt Liste nur mit positiven Zahlen zurück

**Lösung:**
```python
def summe(zahlen):
    return sum(zahlen)

def finde_maximum(zahlen):
    return max(zahlen)

def nur_positive(zahlen):
    return [x for x in zahlen if x > 0]
```

