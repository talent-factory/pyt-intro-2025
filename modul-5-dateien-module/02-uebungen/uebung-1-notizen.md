# Übung: Notizen-App

**Dauer:** 15 Minuten

Erstellen Sie eine einfache Notizen-App:

1. Funktion `neue_notiz()` - Fragt nach Text und speichert in `notizen.txt`
2. Funktion `zeige_notizen()` - Zeigt alle Notizen

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
def neue_notiz():
    notiz = input("Notiz: ")
    with open("notizen.txt", "a") as f:
        from datetime import datetime
        zeit = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{zeit}] {notiz}\n")
    print("✓ Gespeichert")

def zeige_notizen():
    try:
        with open("notizen.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Keine Notizen vorhanden")
```

</details>

