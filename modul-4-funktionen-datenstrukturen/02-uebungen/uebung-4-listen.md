# Übung 4: Funktionen & Listen

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐⭐⭐ Fortgeschritten

## 🎯 Lernziele

- Funktionen mit Listen erstellen
- Listen-Operationen anwenden
- List Comprehensions nutzen

## 📝 Aufgaben

Schreiben Sie folgende Funktionen, die mit Listen arbeiten:

### Aufgabe 1: Summe berechnen

```python
def summe(zahlen):
    """Gibt die Summe aller Zahlen in der Liste zurück."""
    # Ihr Code hier
```

### Aufgabe 2: Maximum finden

```python
def finde_maximum(zahlen):
    """Gibt die grösste Zahl in der Liste zurück."""
    # Ihr Code hier
```

### Aufgabe 3: Nur positive Zahlen

```python
def nur_positive(zahlen):
    """Gibt eine neue Liste mit nur den positiven Zahlen zurück."""
    # Ihr Code hier
```

## ✅ Erfolgskriterien

- [ ] Alle Funktionen haben Docstrings
- [ ] Funktionen geben korrekte Ergebnisse zurück
- [ ] Funktionen wurden mit verschiedenen Listen getestet

## 💡 Lösung

<details>
<summary>Klicken für Lösung</summary>

```python
def summe(zahlen):
    """Gibt die Summe aller Zahlen in der Liste zurück."""
    return sum(zahlen)

def finde_maximum(zahlen):
    """Gibt die grösste Zahl in der Liste zurück."""
    return max(zahlen)

def nur_positive(zahlen):
    """Gibt eine neue Liste mit nur den positiven Zahlen zurück."""
    return [x for x in zahlen if x > 0]

# Tests
test_liste = [5, -3, 10, -1, 8, 0]
print(summe(test_liste))  # 19
print(finde_maximum(test_liste))  # 10
print(nur_positive(test_liste))  # [5, 10, 8]
```

</details>

