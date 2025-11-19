# Häufige Fehler

Typische Anfängerfehler und wie man sie behebt.

## 🐛 Syntaxfehler

### 1. Fehlende Klammer

**Fehler:**
```python
print("Hallo"
```

**Fehlermeldung:**
```
SyntaxError: '(' was never closed
```

**Lösung:**
```python
print("Hallo")
```

### 2. Fehlende Anführungszeichen

**Fehler:**
```python
name = "Anna
```

**Fehlermeldung:**
```
SyntaxError: unterminated string literal
```

**Lösung:**
```python
name = "Anna"
```

### 3. Falsche Anführungszeichen

**Fehler:**
```python
print('Hallo")  # Gemischt!
```

**Lösung:**
```python
print("Hallo")  # Beide gleich
# oder
print('Hallo')  # Beide gleich
```

## 🔤 NameError

### Variable nicht definiert

**Fehler:**
```python
print(xyz)
```

**Fehlermeldung:**
```
NameError: name 'xyz' is not defined
```

**Lösung:**
```python
xyz = 10
print(xyz)
```

### Tippfehler

**Fehler:**
```python
name = "Anna"
print(nane)  # Tippfehler!
```

**Lösung:**
```python
name = "Anna"
print(name)  # Richtig geschrieben
```

## 🔢 TypeError

### Typ-Mismatch

**Fehler:**
```python
"5" + 5
```

**Fehlermeldung:**
```
TypeError: can only concatenate str (not "int") to str
```

**Lösung:**
```python
int("5") + 5  # 10
# oder
"5" + str(5)  # "55"
```

### Falsche Operation

**Fehler:**
```python
"Hallo" - "H"
```

**Fehlermeldung:**
```
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

**Lösung:**
```python
# Strings können nicht subtrahiert werden
# Verwenden Sie .replace() oder Slicing
text = "Hallo"
text.replace("H", "")  # "allo"
```

## ➗ ZeroDivisionError

**Fehler:**
```python
10 / 0
```

**Fehlermeldung:**
```
ZeroDivisionError: division by zero
```

**Lösung:**
```python
# Prüfen vor Division
if b != 0:
    ergebnis = a / b
else:
    print("Division durch 0 nicht möglich!")
```

## 🔢 ValueError

### Ungültige Konvertierung

**Fehler:**
```python
int("Hallo")
```

**Fehlermeldung:**
```
ValueError: invalid literal for int() with base 10: 'Hallo'
```

**Lösung:**
```python
# Nur Zahlen konvertieren
int("42")  # OK
int("3.14")  # Fehler! Verwenden Sie float()
float("3.14")  # OK
```

## 💡 Tipps zur Fehlerbehebung

### 1. Fehlermeldung lesen

```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    print(xyz)
NameError: name 'xyz' is not defined
```

**Wichtig:**
- **Zeile:** `line 3` - Fehler in Zeile 3
- **Fehlertyp:** `NameError`
- **Beschreibung:** `name 'xyz' is not defined`

### 2. Häufige Ursachen

- **Tippfehler:** Variablennamen falsch geschrieben
- **Vergessene Zeichen:** Klammern, Anführungszeichen
- **Falsche Typen:** String + int
- **Nicht definiert:** Variable vor Verwendung definieren

### 3. Debugging-Strategie

1. **Fehlermeldung lesen** - Was sagt Python?
2. **Zeile finden** - Wo ist der Fehler?
3. **Code prüfen** - Syntax korrekt?
4. **Typen prüfen** - Passen die Datentypen?
5. **Testen** - Schritt für Schritt testen

### 4. Hilfreiche Befehle

```python
# Typ prüfen
type(variable)

# Wert prüfen
print(variable)

# Alle Variablen anzeigen (in Shell)
dir()
```

## 🔍 Checkliste bei Fehlern

- [ ] Alle Klammern geschlossen?
- [ ] Alle Anführungszeichen geschlossen?
- [ ] Variable definiert?
- [ ] Variablenname richtig geschrieben?
- [ ] Richtige Datentypen?
- [ ] Einrückung korrekt? (wichtig ab Modul 3)

## 📚 Weitere Ressourcen

- Python-Dokumentation: [docs.python.org](https://docs.python.org)
- Stack Overflow: [stackoverflow.com](https://stackoverflow.com)
- Dozenten fragen!

