# Übung 7: Erste Tests schreiben

**Dauer:** 15 Minuten | **Schwierigkeit:** ⭐⭐ Mittel

## Aufgabe

Schreiben Sie Ihre ersten eigenen Tests mit pytest!

1. Erstellen Sie eine neue Datei `test_meine_tests.py`
2. Importieren Sie die Funktionen aus `testen_beispiel.py`
3. Schreiben Sie **3 Tests** für `ist_gerade()`:
   - Test mit einer geraden Zahl (z.B. 4)
   - Test mit einer ungeraden Zahl (z.B. 7)
   - Test mit Null (0)
4. Schreiben Sie **2 Tests** für `berechne_durchschnitt()`:
   - Test mit einer normalen Liste (z.B. Schulnoten `[5.5, 4.0, 6.0, 5.0]`)
   - Test mit einer leeren Liste
5. Führen Sie die Tests aus:
   ```bash
   uv run pytest test_meine_tests.py -v
   ```

## Hinweise

- Jede Testfunktion beginnt mit `test_`
- Verwenden Sie `assert ergebnis == erwartet`
- Import: `from testen_beispiel import ist_gerade, berechne_durchschnitt`

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
from testen_beispiel import ist_gerade, berechne_durchschnitt


def test_ist_gerade_mit_gerader_zahl():
    """Testet ob 4 als gerade erkannt wird."""
    assert ist_gerade(4) == True


def test_ist_gerade_mit_ungerader_zahl():
    """Testet ob 7 als ungerade erkannt wird."""
    assert ist_gerade(7) == False


def test_ist_gerade_mit_null():
    """Testet ob 0 als gerade erkannt wird."""
    assert ist_gerade(0) == True


def test_durchschnitt_mit_noten():
    """Testet den Durchschnitt von Schulnoten."""
    noten = [5.5, 4.0, 6.0, 5.0]
    assert berechne_durchschnitt(noten) == 5.125


def test_durchschnitt_leere_liste():
    """Testet den Durchschnitt einer leeren Liste."""
    assert berechne_durchschnitt([]) == 0.0
```

</details>
