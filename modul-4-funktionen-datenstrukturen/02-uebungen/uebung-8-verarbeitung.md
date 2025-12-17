# Übung: Datenverarbeitung

**Dauer:** 15 Minuten

Schreiben Sie eine Funktion `analysiere_text(text)` die ein Dictionary zurückgibt mit:
- anzahl_woerter
- anzahl_zeichen
- laengstes_wort

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
def analysiere_text(text):
    woerter = text.split()
    return {
        "anzahl_woerter": len(woerter),
        "anzahl_zeichen": len(text),
        "laengstes_wort": max(woerter, key=len) if woerter else ""
    }

# Test
text = "Python ist eine tolle Programmiersprache"
ergebnis = analysiere_text(text)
print(ergebnis)
```

</details>

