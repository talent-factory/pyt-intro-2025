# Übung: Textstatistik

**Dauer:** 15 Minuten

Schreiben Sie eine Funktion `analysiere_datei(dateiname)` die ausgibt:
- Anzahl Zeilen
- Anzahl Wörter
- Anzahl Zeichen

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
def analysiere_datei(dateiname):
    with open(dateiname, "r") as f:
        zeilen = f.readlines()

    anzahl_zeilen = len(zeilen)
    anzahl_woerter = sum(len(z.split()) for z in zeilen)
    anzahl_zeichen = sum(len(z) for z in zeilen)

    print(f"Zeilen: {anzahl_zeilen}")
    print(f"Wörter: {anzahl_woerter}")
    print(f"Zeichen: {anzahl_zeichen}")
```

</details>

