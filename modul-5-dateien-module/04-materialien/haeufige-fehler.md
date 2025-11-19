# Häufige Fehler

## 1. Datei nicht geschlossen

❌ Falsch:
```python
f = open("datei.txt", "r")
inhalt = f.read()
# Vergessen: f.close()
```

✅ Richtig:
```python
with open("datei.txt", "r") as f:
    inhalt = f.read()
```

## 2. Falscher Modus

❌ Falsch:
```python
with open("datei.txt", "r") as f:with open("datei.txt", "r") as f:with open("datei.txt", "r") as f:with datei.txt", "w") as f:
    f.write("Text")
```
