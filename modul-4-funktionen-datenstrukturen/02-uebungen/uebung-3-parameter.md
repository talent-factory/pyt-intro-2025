# Übung: Parameter-Varianten

**Dauer:** 15 Minuten

Schreiben Sie eine Funktion `formatiere_name(vorname, nachname, titel="")`:

- Gibt formatierten Namen zurück
- Titel ist optional
- Beispiele:
  - `formatiere_name("Anna", "Muster")` → "Anna Muster"
  - `formatiere_name("Max", "Meier", "Dr.")` → "Dr. Max Meier"

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
def formatiere_name(vorname, nachname, titel=""):
    if titel:
        return f"{titel} {vorname} {nachname}"
    return f"{vorname} {nachname}"
```

</details>

