# Übung 8: Tests für Kontakte

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐⭐ Schwer

## Aufgabe

Schreiben Sie Tests für die Funktion `erstelle_kontakt()` aus `testen_beispiel.py`.

Überlegen Sie selbst: Was sollte man testen?

Hier einige Denkanstösse:

- Hat das Ergebnis die richtigen Schlüssel (`name`, `email`, `telefon`)?
- Stimmen die Werte im Dictionary?
- Was passiert bei einem leeren Namen?

Erstellen Sie eine Datei `test_kontakte.py` und führen Sie die Tests aus:

```bash
uv run pytest test_kontakte.py -v
```

## Hinweise

- Import: `from testen_beispiel import erstelle_kontakt`
- Ein Dictionary können Sie mit `==` vergleichen
- Einzelne Schlüssel prüfen Sie mit `ergebnis["name"] == "Anna"`

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
from testen_beispiel import erstelle_kontakt


def test_kontakt_hat_richtige_schluessel():
    """Testet ob der Kontakt alle erwarteten Schluessel hat."""
    kontakt = erstelle_kontakt("Anna", "anna@example.com", "079 123 45 67")
    assert "name" in kontakt
    assert "email" in kontakt
    assert "telefon" in kontakt


def test_kontakt_hat_richtige_werte():
    """Testet ob die Werte korrekt gespeichert werden."""
    kontakt = erstelle_kontakt("Anna", "anna@example.com", "079 123 45 67")
    assert kontakt["name"] == "Anna"
    assert kontakt["email"] == "anna@example.com"
    assert kontakt["telefon"] == "079 123 45 67"


def test_kontakt_komplett():
    """Testet das gesamte Dictionary auf einmal."""
    erwartet = {
        "name": "Max",
        "email": "max@example.com",
        "telefon": "079 987 65 43"
    }
    ergebnis = erstelle_kontakt("Max", "max@example.com", "079 987 65 43")
    assert ergebnis == erwartet


def test_kontakt_leerer_name():
    """Testet was bei einem leeren Namen passiert."""
    kontakt = erstelle_kontakt("", "test@example.com", "079 000 00 00")
    assert kontakt["name"] == ""
```

</details>
