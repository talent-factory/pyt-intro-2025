# Übung: Verschachtelte Daten

**Dauer:** 15 Minuten

Erstellen Sie eine Datenstruktur für 3 Studenten mit Namen, Alter und Noten.

Berechnen Sie dann für jeden den Notendurchschnitt.

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
studenten = [
    {"name": "Anna", "alter": 20, "noten": [5.5, 6.0, 5.0]},
    {"name": "Max", "alter": 22, "noten": [4.5, 5.0, 5.5]},
    {"name": "Lisa", "alter": 21, "noten": [6.0, 5.5, 6.0]}
]

for student in studenten:
    durchschnitt = sum(student["noten"]) / len(student["noten"])
    print(f"{student['name']}: {durchschnitt:.2f}")
```

</details>

