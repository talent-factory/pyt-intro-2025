# Übung: Funktionen mit Return

**Dauer:** 15 Minuten

Schreiben Sie Funktionen mit Rückgabewerten:

1. `quadrat(x)` - Gibt x² zurück
2. `ist_volljährig(alter)` - Gibt True/False zurück
3. `max_von_drei(a, b, c)` - Gibt größte Zahl zurück

**Lösung:**
```python
def quadrat(x):
    return x * x

def ist_volljaehrig(alter):
    return alter >= 18

def max_von_drei(a, b, c):
    return max(a, b, c)
```

