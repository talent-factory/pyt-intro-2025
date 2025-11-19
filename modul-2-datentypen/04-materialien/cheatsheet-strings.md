# Cheatsheet: Strings

## Erstellen

```python
# Einfache Anführungszeichen
text1 = 'Hallo'

# Doppelte Anführungszeichen
text2 = "Welt"

# Mehrzeilig
text3 = """Zeile 1
Zeile 2
Zeile 3"""

# Raw String (keine Escape-Sequenzen)
pfad = r"C:\Users\Name"
```

## Operationen

```python
# Verketten
"Hallo" + " " + "Welt"  # Hallo Welt

# Wiederholen
"=" * 20  # ====================

# Länge
len("Hallo")  # 5

# Zugriff
text = "Python"
text[0]    # 'P'
text[-1]   # 'n'
text[1:4]  # 'yth'
```

## Wichtige Methoden

### Gross-/Kleinschreibung
```python
text = "Hallo Welt"
text.upper()       # HALLO WELT
text.lower()       # hallo welt
text.capitalize()  # Hallo welt
text.title()       # Hallo Welt
text.swapcase()    # hALLO wELT
```

### Suchen & Prüfen
```python
text = "Hallo Welt"
text.find("Welt")      # 6 (Index)
text.count("l")        # 3
text.startswith("H")   # True
text.endswith("t")     # True
"Welt" in text         # True
```

### Ändern
```python
text = "Hallo Welt"
text.replace("Welt", "Python")  # Hallo Python
text.strip()           # Leerzeichen entfernen
text.lstrip()          # Links entfernen
text.rstrip()          # Rechts entfernen
```

### Teilen & Verbinden
```python
# Teilen
text = "Apfel,Banane,Orange"
liste = text.split(",")  # ['Apfel', 'Banane', 'Orange']

# Verbinden
liste = ["Apfel", "Banane", "Orange"]
text = ", ".join(liste)  # Apfel, Banane, Orange
```

### Prüfungen
```python
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
"Hallo".islower()    # False
"HALLO".isupper()    # True
```

## Formatierung

### f-Strings (Python 3.6+)
```python
name = "Anna"
alter = 25
print(f"Ich bin {name}, {alter} Jahre alt")

# Mit Formatierung
zahl = 3.14159
print(f"{zahl:.2f}")      # 3.14
print(f"{zahl:10.2f}")    # '      3.14'
print(f"{42:05d}")        # 00042
```

### format()
```python
"Ich bin {}, {} Jahre alt".format("Anna", 25)
"Ich bin {name}, {alter} Jahre alt".format(name="Anna", alter=25)
```

### %-Formatierung (alt)
```python
"Ich bin %s, %d Jahre alt" % ("Anna", 25)
```

## Escape-Sequenzen

```python
\n   # Neue Zeile
\t   # Tabulator
\\   # Backslash
\'   # Einfaches Anführungszeichen
\"   # Doppeltes Anführungszeichen
\r   # Carriage Return
```

## Slicing

```python
text = "Python"

text[0]      # 'P' (erstes Zeichen)
text[-1]     # 'n' (letztes Zeichen)
text[0:3]    # 'Pyt' (Index 0-2)
text[:3]     # 'Pyt' (von Anfang)
text[3:]     # 'hon' (bis Ende)
text[::2]    # 'Pto' (jedes 2.)
text[::-1]   # 'nohtyP' (rückwärts)
```

## Häufige Muster

```python
# String umkehren
text[::-1]

# Ersten Buchstaben gross
text[0].upper() + text[1:]

# Leerzeichen entfernen
text.strip()

# Mehrere Leerzeichen → eins
" ".join(text.split())

# Zählen von Zeichen
text.count("a")

# Ersetzen (alle)
text.replace("alt", "neu")

# Prüfen ob leer
if not text.strip():
    print("Leer")
```

## Tipps

✅ **Strings sind unveränderlich (immutable)**
```python
text = "Hallo"
text[0] = "h"  # ❌ Fehler!
text = "h" + text[1:]  # ✅ Neu erstellen
```

✅ **Verwende f-Strings für Formatierung**
```python
# ❌ Umständlich
print("Hallo " + name + ", du bist " + str(alter))

# ✅ Elegant
print(f"Hallo {name}, du bist {alter}")
```

