# Übung 2: Funktionen mit Return

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Lernziele

- Funktionen mit Rückgabewerten erstellen
- `return`-Statement verwenden
- Funktionen testen

## 📝 Aufgaben

Schreiben Sie folgende Funktionen mit Rückgabewerten:

### Aufgabe 1: Quadrat-Funktion

```python
def quadrat(x):
    """Gibt x² zurück."""
    # Ihr Code hier
```

### Aufgabe 2: Volljährigkeits-Prüfung

```python
def ist_volljaehrig(alter):
    """Gibt True zurück, wenn alter >= 18, sonst False."""
    # Ihr Code hier
```

### Aufgabe 3: Maximum von drei Zahlen

```python
def max_von_drei(a, b, c):
    """Gibt die grösste der drei Zahlen zurück."""
    # Ihr Code hier
```

## ✅ Erfolgskriterien

- [ ] Alle Funktionen haben Docstrings
- [ ] Alle Funktionen verwenden `return`
- [ ] Funktionen wurden getestet

## 💡 Lösung

<details>
<summary>Klicken für Lösung</summary>

```python
def quadrat(x):
    """Gibt x² zurück."""
    return x * x

def ist_volljaehrig(alter):
    """Gibt True zurück, wenn alter >= 18, sonst False."""
    return alter >= 18

def max_von_drei(a, b, c):
    """Gibt die grösste der drei Zahlen zurück."""
    return max(a, b, c)

# Tests
print(quadrat(5))  # 25
print(ist_volljaehrig(20))  # True
print(ist_volljaehrig(16))  # False
print(max_von_drei(5, 10, 3))  # 10
```

</details>
