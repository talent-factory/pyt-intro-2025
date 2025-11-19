# Handout: Datentypen

**Modul 2 | Python Einführung**

## Grundlegende Datentypen

### Integer (Ganzzahlen)
```python
alter = 25
temperatur = -5
```

### Float (Fliesskommazahlen)
```python
preis = 19.99
pi = 3.14159
```

### String (Zeichenketten)
```python
name = "Anna"
text = 'Hallo Welt'
mehrzeilig = """Zeile 1
Zeile 2"""
```

### Boolean (Wahrheitswerte)
```python
ist_aktiv = True
ist_fertig = False
```

## String-Operationen

### Verketten
```python
vorname = "Max"
nachname = "Muster"
vollname = vorname + " " + nachname
```

### Wiederholen
```python
linie = "-" * 20  # --------------------
```

### Zugriff
```python
text = "Python"
text[0]    # 'P' (erstes Zeichen)
text[-1]   # 'n' (letztes Zeichen)
text[0:3]  # 'Pyt' (Slicing)
```

### Methoden
```python
text = "Hallo Welt"
text.upper()        # HALLO WELT
text.lower()        # hallo welt
text.strip()        # Leerzeichen entfernen
text.replace("a", "o")  # Hollo Welt
text.split()        # ['Hallo', 'Welt']
len(text)           # 10
```

## String-Formatierung

### f-Strings (empfohlen)
```python
name = "Anna"
alter = 25
print(f"Ich bin {name}, {alter} Jahre alt")
```

### format()
```python
print("Ich bin {}, {} Jahre alt".format(name, alter))
```

### Formatierungs-Optionen
```python
zahl = 3.14159
print(f"{zahl:.2f}")     # 3.14 (2 Dezimalstellen)
print(f"{zahl:10.2f}")   # '      3.14' (10 Zeichen breit)
print(f"{42:05d}")       # 00042 (5 Stellen, mit Nullen)
```

## Typkonvertierung

```python
# String → Integer
alter = int("25")

# String → Float
preis = float("19.99")

# Integer → String
text = str(42)

# Zu Boolean
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("text") # True
```

## Input/Output

### Eingabe
```python
name = input("Ihr Name: ")
alter = int(input("Ihr Alter: "))
```

### Ausgabe
```python
print("Hallo")
print("Hallo", "Welt")  # Hallo Welt
print("Hallo", end="")  # Kein Zeilenumbruch
```

## Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `==` | Gleich | `5 == 5` → True |
| `!=` | Ungleich | `5 != 3` → True |
| `<` | Kleiner | `3 < 5` → True |
| `>` | Grösser | `5 > 3` → True |
| `<=` | Kleiner/Gleich | `5 <= 5` → True |
| `>=` | Grösser/Gleich | `5 >= 3` → True |

## Logische Operatoren

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `and` | Und | `True and False` → False |
| `or` | Oder | `True or False` → True |
| `not` | Nicht | `not True` → False |

## Escape-Sequenzen

```python
print("Zeile 1\nZeile 2")  # Zeilenumbruch
print("Tab\tTab")          # Tabulator
print("Er sagte \"Hallo\"") # Anführungszeichen
print("C:\\Users\\Name")   # Backslash
```

## Tipps

✅ **DO:**
- f-Strings für Formatierung nutzen
- Aussagekräftige Variablennamen
- Input validieren (try-except)

❌ **DON'T:**
- Strings mit + in Schleifen verketten (langsam)
- Typkonvertierung ohne Fehlerbehandlung
- Magische Zahlen ohne Erklärung

