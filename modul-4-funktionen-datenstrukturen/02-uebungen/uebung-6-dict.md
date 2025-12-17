# Übung: Dictionary-Operationen

**Dauer:** 15 Minuten

Erstellen Sie ein Dictionary `buch` mit:
- titel: "Python Basics"
- autor: "Max Muster"
- jahr: 2025
- seiten: 300

Dann:
1. Fügen Sie "preis": 29.90 hinzu
2. Ändern Sie das Jahr auf 2024
3. Geben Sie alle Keys aus
4. Geben Sie alle Values aus

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
buch = {
    "titel": "Python Basics",
    "autor": "Max Muster",
    "jahr": 2025,
    "seiten": 300
}

buch["preis"] = 29.90
buch["jahr"] = 2024

print("Keys:", buch.keys())
print("Values:", buch.values())
```

</details>

