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
ist_volljaehrig = alter >= 18  # TypeError!
```

### ✅ RICHTIG
```python
alter = int(input("Alter: "))
ist_volljaehrig = alter >= 18
print(f"Volljährig: {ist_volljaehrig}")
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
ist_fuenf = (x = 5)  # SyntaxError! = ist keine Vergleichsoperation
```

### ✅ RICHTIG
```python
x = 5                # = weist einen Wert zu
ist_fuenf = x == 5   # == vergleicht und liefert True oder False
print(ist_fuenf)
```

## 6. Float-Präzision

### ❌ FALSCH (Annahme)
```python
print(0.1 + 0.2)  # 0.30000000000000004 (nicht 0.3!)
```

### ✅ RICHTIG

> **Vorgriff:** Dieses Konzept (z. B. Module importieren) wird in Modul 5 behandelt.

```python
# Für Vergleiche
import math
sind_gleich = math.isclose(0.1 + 0.2, 0.3)  # True
print(sind_gleich)

# Für Ausgabe
print(f"{0.1 + 0.2:.1f}")  # 0.3
```

## 7. Typkonvertierung ohne Prüfung

### ❌ FALSCH
```python
alter = int(input("Alter: "))  # ValueError bei "abc"!
```

### ✅ RICHTIG (Modul 2): Eingabe vorher prüfen
```python
alter_str = input("Alter: ")
ist_zahl = alter_str.isdigit()   # True, wenn nur Ziffern: "25" → True, "abc" → False
print(f"Gültige Zahl: {ist_zahl}")
```

> ⚠️ `isdigit()` erkennt nur Ziffern. Negative Zahlen (`"-5"`) und Dezimalzahlen
> (`"2.5"`) liefern `False`, obwohl `int("-5")` bzw. `float("2.5")` funktionieren.

> 💡 Wie Ihr Programm auf `False` reagiert (`if`) oder Fehler mit
> `try`/`except` abfängt, lernen Sie in Modul 3.

## 8. Leerer String ist False

### ❌ FALSCH (Annahme)
```python
name = ""
ist_leer = name == False  # False! (name ist "", nicht False)
```

### ✅ RICHTIG
```python
name = ""
ist_leer = not name  # True (leerer String ist "falsy")
# Oder explizit:
ist_leer = name == ""  # True
```

## 9. Viele Strings verketten

### ❌ FALSCH (umständlich)
```python
text = "a" + "b" + "c" + "d" + "e"
```

### ✅ RICHTIG
```python
teile = ["a", "b", "c", "d", "e"]
text = "".join(teile)  # "abcde"
```

> **Vorgriff:** Listen lernen Sie in Modul 4 kennen. Bei sehr vielen Teilen
> (z. B. in einer Schleife, Modul 3) ist `join()` die empfohlene und meist effizientere Variante.

## 10. Escape-Sequenzen in Pfaden

### ❌ FALSCH
```python
pfad = "C:\Users\Name"  # SyntaxError: \U beginnt eine Unicode-Escape-Sequenz
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
ist_aktiv = True
ergebnis = ist_aktiv == True
```

### ✅ RICHTIG
```python
ist_aktiv = True
ergebnis = ist_aktiv  # Der Wert ist bereits True oder False
```

## 12. None-Vergleich

### ❌ FALSCH
```python
wert = None
ist_leer = wert == None  # Funktioniert, aber nicht pythonic
```

### ✅ RICHTIG
```python
wert = None
ist_leer = wert is None  # 'is' für None-Vergleich
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
- [ ] Eingabe vor der Konvertierung geprüft (z.B. `.isdigit()`)?
- [ ] Float-Vergleiche korrekt?
- [ ] Escape-Sequenzen beachtet?

