# Übung: Einfache Funktionen

**Dauer:** 15 Minuten

Schreiben Sie folgende Funktionen:

1. `zeige_willkommen()` - Gibt "Willkommen!" aus
2. `zeige_linie()` - Gibt eine Linie aus 50 Zeichen "-" aus
3. `zeige_box(text)` - Gibt Text in einer Box aus

**Beispiel:**
```python
zeige_box("Hallo")
```

**Ausgabe:**
```
**********
* Hallo  *
**********
```

**Lösung:**
```python
def zeige_willkommen():
    print("Willkommen!")

def zeige_linie():
    print("-" * 50)

def zeige_box(text):
    breite = len(text) + 4
    print("*" * breite)
    print(f"* {text} *")
    print("*" * breite)
```

