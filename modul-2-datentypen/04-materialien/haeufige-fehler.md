# Häufige Fehler bei Datentypen

## 1. Typfehler bei Verkettung

### ❌ FALSCH
```python
alter = 25
print("Ich bin " + alter + " Jahre alt")
# TypeError: can only concatenate str (not "int") to str
```

### ✅ RICHTIG
```python
alter = 25
print("Ich bin " + str(alter) + " Jahre alt")
# Oder besser:
print(f"Ich bin {alter} Jahre alt")
```

## 2. Input ist immer String

### ❌ FALSCH
```python
alter = input("Alter: ")
if alter >= 18:  # TypeError!
    print("Volljährig")
```

### ✅ RICHTIG
```python
alter = int(input("Alter: "))
if alter >= 18:
    print("Volljährig")
```

## 3. Division gibt immer Float

### ❌ FALSCH (Annahme)
```python
ergebnis = 10 / 2  # ergebnis ist 5.0, nicht 5!
```

### ✅ RICHTIG
```python
# Ganzzahl-Division
ergebnis = 10 // 2  # 5 (Integer)

# Oder explizit konvertieren
ergebnis = int(10 / 2)  # 5
```

## 4. Strings sind unveränderlich

### ❌ FALSCH
```python
text = "Hallo"
text[0] = "h"  # TypeError: 'str' object does not support item assignment
```

### ✅ RICHTIG
```python
text = "Hallo"
text = "h" + text[1:]  # "hallo"
# Oder:
text = text.replace("H", "h")
```

## 5. Vergleich vs. Zuweisung

### ❌ FALSCH
```python
if x = 5:  # SyntaxError!
    print("x ist 5")
```

### ✅ RICHTIG
```python
if x == 5:  # == ist Vergleich
    print("x ist 5")
```

## 6. Float-Präzision

### ❌ FALSCH (Annahme)
```python
print(0.1 + 0.2)  # 0.30000000000000004 (nicht 0.3!)
```

### ✅ RICHTIG
```python
# Für Vergleiche
import math
if math.isclose(0.1 + 0.2, 0.3):
    print("Gleich")

# Für Ausgabe
print(f"{0.1 + 0.2:.1f}")  # 0.3
```

## 7. Typkonvertierung ohne Fehlerbehandlung

### ❌ FALSCH
```python
alter = int(input("Alter: "))  # ValueError bei "abc"!
```

### ✅ RICHTIG
```python
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Bitte eine Zahl eingeben!")
    alter = 0
```

## 8. Leerer String ist False

### ❌ FALSCH (Annahme)
```python
name = ""
if name == False:  # False! (name ist "", nicht False)
    print("Leer")
```

### ✅ RICHTIG
```python
name = ""
if not name:  # True (leerer String ist "falsy")
    print("Leer")
# Oder explizit:
if name == "":
    print("Leer")
```

## 9. String-Verkettung in Schleifen

### ❌ FALSCH (ineffizient)
```python
text = ""
for i in range(1000):
    text += str(i)  # Sehr langsam!
```

### ✅ RICHTIG
```python
teile = []
for i in range(1000):
    teile.append(str(i))
text = "".join(teile)  # Viel schneller!
```

## 10. Escape-Sequenzen in Pfaden

### ❌ FALSCH
```python
pfad = "C:\Users\Name"  # \U und \N sind Escape-Sequenzen!
```

### ✅ RICHTIG
```python
# Raw String
pfad = r"C:\Users\Name"
# Oder doppelte Backslashes
pfad = "C:\\Users\\Name"
# Oder Forward Slashes (funktioniert auch auf Windows)
pfad = "C:/Users/Name"
```

## 11. Boolean-Vergleiche

### ❌ FALSCH (umständlich)
```python
if ist_aktiv == True:
    print("Aktiv")
```

### ✅ RICHTIG
```python
if ist_aktiv:  # Direkt prüfen
    print("Aktiv")
```

## 12. None-Vergleich

### ❌ FALSCH
```python
if wert == None:  # Funktioniert, aber nicht pythonic
    print("Leer")
```

### ✅ RICHTIG
```python
if wert is None:  # 'is' für None-Vergleich
    print("Leer")
```

## 13. Formatierung mit +

### ❌ FALSCH (umständlich)
```python
name = "Anna"
alter = 25
print("Ich bin " + name + ", " + str(alter) + " Jahre alt")
```

### ✅ RICHTIG
```python
print(f"Ich bin {name}, {alter} Jahre alt")
```

## 14. Integer-Overflow

### ❌ FALSCH (in anderen Sprachen)
```python
# In Python gibt es keinen Integer-Overflow!
zahl = 10 ** 100  # Funktioniert problemlos
```

### ✅ RICHTIG
```python
# Python kann beliebig grosse Zahlen
zahl = 10 ** 1000  # Kein Problem!
```

## Debugging-Tipps

### 1. Typ prüfen
```python
print(type(variable))
```

### 2. Wert und Typ ausgeben
```python
print(f"{variable=}, {type(variable)=}")
```

### 3. Repr verwenden
```python
print(repr(text))  # Zeigt Escape-Sequenzen
```

### 4. Interaktiv testen
```python
# In Python-Shell
>>> type(5)
<class 'int'>
>>> type(5.0)
<class 'float'>
>>> type("5")
<class 'str'>
```

## Checkliste

✅ **Vor dem Ausführen:**
- [ ] Input konvertiert?
- [ ] Typfehler möglich?
- [ ] Fehlerbehandlung vorhanden?
- [ ] Float-Vergleiche korrekt?
- [ ] Escape-Sequenzen beachtet?

