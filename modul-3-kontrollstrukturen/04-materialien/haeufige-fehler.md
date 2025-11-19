# Häufige Fehler bei Kontrollstrukturen

## 1. Endlosschleifen

### ❌ FALSCH
```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    # Fehler: zaehler wird nie erhöht!
```

### ✅ RICHTIG
```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1  # Wichtig!
```

## 2. Falsche Einrückung

### ❌ FALSCH
```python
if alter >= 18:
print("Volljährig")  # Fehler: Keine Einrückung
```

### ✅ RICHTIG
```python
if alter >= 18:
    print("Volljährig")  # 4 Leerzeichen
```

## 3. Vergleich vs. Zuweisung

### ❌ FALSCH
```python
if x = 5:  # Fehler: = ist Zuweisung
    print("x ist 5")
```

### ✅ RICHTIG
```python
if x == 5:  # == ist Vergleich
    print("x ist 5")
```

## 4. Range-Grenzen

### ❌ FALSCH
```python
for i in range(1, 5):
    print(i)  # Gibt 1,2,3,4 (nicht 5!)
```

### ✅ RICHTIG
```python
for i in range(1, 6):  # Bis 6 (exklusiv)
    print(i)  # Gibt 1,2,3,4,5
```

## 5. Liste während Iteration ändern

### ❌ FALSCH
```python
for element in liste:
    liste.remove(element)  # Fehler!
```

### ✅ RICHTIG
```python
liste_kopie = liste.copy()
for element in liste_kopie:
    liste.remove(element)
```

## 6. Index out of Range

### ❌ FALSCH
```python
liste = [1, 2, 3]
print(liste[3])  # Fehler: Index 3 existiert nicht
```

### ✅ RICHTIG
```python
liste = [1, 2, 3]
print(liste[2])  # Index 0,1,2
```

## 7. Leere Liste prüfen

### ❌ FALSCH
```python
if liste == []:  # Funktioniert, aber unschön
    print("Leer")
```

### ✅ RICHTIG
```python
if not liste:  # Pythonic!
    print("Leer")
```

## 8. Break in falscher Schleife

### ❌ FALSCH
```python
for i in range(10):
    for j in range(10):
        if i == 5:
            break  # Bricht nur innere Schleife ab
```

### ✅ RICHTIG
```python
gefunden = False
for i in range(10):
    for j in range(10):
        if i == 5:
            gefunden = True
            break
    if gefunden:
        break
```

## Debugging-Tipps

1. **Print-Statements:**
   ```python
   print(f"zaehler = {zaehler}")
   ```

2. **Bedingungen prüfen:**
   ```python
   print(f"Bedingung: {zaehler <= 5}")
   ```

3. **Schleifendurchläufe zählen:**
   ```python
   durchlauf = 0
   while bedingung:
       durchlauf += 1
       print(f"Durchlauf {durchlauf}")
   ```
