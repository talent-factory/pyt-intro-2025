# Design: Projekt-Reorganisation

**Datum:** 2026-02-28
**Status:** Genehmigt

## Ziel

Top-Level-Struktur bereinigen: Einmal-Scripts und veraltete Dokumentation entfernen,
Shell-Scripts durch ein Makefile ersetzen.

## Zu loeschende Dateien

| Datei | Grund |
|-------|-------|
| `apply_type_hints.py` | Einmal-Migrationsskript, abgeschlossen |
| `fix_test_type_hints.py` | Einmal-Migrationsskript, abgeschlossen |
| `DOKUMENTATION_ZUSAMMENFASSUNG.md` | Protokoll abgeschlossener Migration |
| `TEST_SUMMARY.md` | Veraltet (Zahlen stimmen nicht mehr) |
| `docs/RUFF_REMAINING_ISSUES.md` | Protokoll abgeschlossener Bereinigung |
| `docs/RUFF_USAGE.md` | Wird durch Makefile-Targets ersetzt |
| `check_code.sh` | Wird durch `make lint` ersetzt |
| `format_code.sh` | Wird durch `make format` ersetzt |
| `format_code_unsafe.sh` | Wird durch `make format-unsafe` ersetzt |
| `run_tests.sh` | Wird durch `make test` ersetzt |

Alle Dateien bleiben in der Git-History erhalten.

## Neue Struktur (Top-Level)

```
pyt-intro-2025/
├── Makefile
├── modul-1-einstieg/
├── modul-2-datentypen/
├── modul-3-kontrollstrukturen/
├── modul-4-funktionen-datenstrukturen/
├── modul-5-dateien-module/
├── tests/
├── docs/
├── .devcontainer/
├── .vscode/
├── README.md
├── CLAUDE.md
├── pyproject.toml
├── uv.lock
├── pytest.ini
├── pyrightconfig.json
├── .gitignore
└── .python-version
```

## Makefile

Targets:

- `make help` -- Uebersicht aller Targets
- `make test` -- Alle Tests ausfuehren
- `make test-modul1` ... `test-modul5` -- Tests pro Modul
- `make test-coverage` -- Tests mit Coverage-Report
- `make test-quick` -- Nur Import-Tests
- `make lint` -- Code pruefen ohne Aenderungen
- `make format` -- Code formatieren + Linting-Fixes
- `make format-unsafe` -- Inklusive unsafe Fixes
- `make clean` -- Temporaere Dateien loeschen

Vereinfachungen gegenueber den alten Scripts:

- `uv run` statt `.venv/bin/` -- funktioniert ohne aktiviertes venv
- Keine farbigen Echo-Ausgaben -- `pytest` und `ruff` haben eigene Farben
- Pattern-Rule `test-modul%` deckt alle Module mit einer Regel ab

## .gitignore

`.DS_Store` wird ergaenzt (fehlt aktuell).
