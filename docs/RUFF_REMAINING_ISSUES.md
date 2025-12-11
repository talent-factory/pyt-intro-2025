# Verbleibende Ruff-Probleme nach Auto-Fix

Nach dem Ausführen von `./format_code.sh` bleiben **51 Fehler** übrig, die manuell behoben werden müssen.

## Kategorien der verbleibenden Fehler

### 1. UP031: Use format specifiers instead of percent format (2 Fehler)

**Betroffen:**
- `modul-2-datentypen/05-beispiele/formatierung.py:97`
- `tests/modul-2/test_formatierung.py:126`

**Problem:** Veraltete %-Formatierung wird verwendet

**Beispiel:**
```python
# ❌ Alt (%-Formatierung)
text = "Ich heisse %s und bin %d Jahre alt" % (name, alter)

# ✅ Modern (f-string)
text = f"Ich heisse {name} und bin {alter} Jahre alt"
```

**Warum nicht automatisch behoben?**
Diese Dateien demonstrieren bewusst verschiedene Formatierungs-Methoden für Lernzwecke.

**Empfehlung:** Behalten Sie diese für didaktische Zwecke, fügen Sie aber einen Kommentar hinzu:
```python
# %-Formatierung (veraltet, nur zu Demonstrationszwecken)  # noqa: UP031
text = "Ich heisse %s und bin %d Jahre alt" % (name, alter)
```

---

### 2. F401: Module imported but unused (23 Fehler)

**Betroffen:** Alle Test-Dateien mit Import-Tests

**Problem:** Module werden importiert, aber nicht verwendet

**Beispiel:**
```python
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import hello_world  # F401: imported but unused
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")
```

**Warum nicht automatisch behoben?**
Der Import ist der eigentliche Test - wir wollen nur prüfen, ob das Modul importierbar ist.

**Lösung 1: noqa-Kommentar** (empfohlen für Tests)
```python
import hello_world  # noqa: F401
```

**Lösung 2: importlib verwenden** (wie Ruff vorschlägt)
```python
import importlib.util
spec = importlib.util.find_spec("hello_world")
assert spec is not None
```

**Empfehlung:** Verwenden Sie `# noqa: F401` in Test-Dateien.

---

### 3. E721: Use `is` and `is not` for type comparisons (14 Fehler)

**Betroffen:** Test-Dateien in Modul 2

**Problem:** `type(x) == int` statt `isinstance(x, int)`

**Beispiel:**
```python
# ❌ Nicht empfohlen
assert type(result) == int

# ✅ Besser
assert isinstance(result, int)
```

**Warum nicht automatisch behoben?**
Dies könnte die Semantik ändern (z.B. bei Subklassen).

**Empfehlung:** Manuell zu `isinstance()` ändern.

---

### 4. N806: Variable should be lowercase (1 Fehler)

**Betroffen:** `tests/modul-1/test_taschenrechner.py:74`

**Problem:** Variable `PI` sollte kleingeschrieben sein

**Beispiel:**
```python
# ❌ Nicht PEP 8 konform
PI = 3.14159

# ✅ PEP 8 konform
pi = 3.14159
```

**Empfehlung:** Zu `pi` ändern oder als Konstante markieren (wenn es eine Modul-Konstante ist).

---

### 5. E712: Avoid equality comparisons to `True` (1 Fehler)

**Betroffen:** `tests/modul-2/test_vergleiche.py:111`

**Problem:** Vergleich mit `True` ist redundant

**Beispiel:**
```python
# ❌ Redundant
assert zugang == True

# ✅ Pythonic
assert zugang
```

**Empfehlung:** Manuell ändern.

---

## Schnelle Fixes

### Option 1: Unsafe Fixes anwenden (automatisch)

```bash
./format_code_unsafe.sh
```

Dies behebt automatisch die "unsafe" Fixes (z.B. UP031, UP032).

### Option 2: Manuelle Fixes mit noqa-Kommentaren

Für Test-Dateien können Sie `# noqa: F401` Kommentare hinzufügen:

```bash
# Beispiel für eine Test-Datei
sed -i '' 's/import hello_world$/import hello_world  # noqa: F401/' tests/modul-1/test_hello_world.py
```

### Option 3: Ruff-Konfiguration anpassen

Fügen Sie in `pyproject.toml` hinzu:

```toml
[tool.ruff.lint.per-file-ignores]
# In Test-Dateien: Erlaube ungenutzte Imports
"tests/**/*.py" = ["F401"]
```

---

## Zusammenfassung

| Fehlertyp | Anzahl | Automatisch behebbar? | Empfehlung |
|-----------|--------|----------------------|------------|
| UP031 (%-Format) | 2 | Ja (unsafe) | `# noqa: UP031` für Demos |
| F401 (unused import) | 23 | Nein | `# noqa: F401` in Tests |
| E721 (type comparison) | 14 | Nein | Zu `isinstance()` ändern |
| N806 (variable naming) | 1 | Nein | Zu lowercase ändern |
| E712 (== True) | 1 | Nein | Zu `assert var` ändern |
| **Gesamt** | **51** | **2** | - |

---

## Empfohlene Vorgehensweise

1. **Für didaktische Dateien** (formatierung.py):
   ```python
   # noqa: UP031
   ```

2. **Für Test-Dateien** (alle test_*.py):
   Fügen Sie in `pyproject.toml` hinzu:
   ```toml
   [tool.ruff.lint.per-file-ignores]
   "tests/**/*.py" = ["F401", "E721"]
   ```

3. **Für echte Code-Probleme**:
   - E721 → `isinstance()` verwenden
   - N806 → Variable umbenennen
   - E712 → Direkten Boolean-Check verwenden

Nach diesen Änderungen sollten alle Ruff-Checks erfolgreich durchlaufen! ✅

