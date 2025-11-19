# Übung: Listen-Methoden

**Dauer:** 15 Minuten

Gegeben: `zahlen = [3, 1, 4, 1, 5, 9, 2, 6]`

Schreiben Sie Code für:

1. Sortiere die Liste
2. Entferne alle 1en
3. Füge 7 und 8 hinzu
4. Gib die Länge aus

**Lösung:**
```python
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]

zahlen.sort()
while 1 in zahlen:
    zahlen.remove(1)
zahlen.extend([7, 8])
print(f"Länge: {len(zahlen)}")
```

