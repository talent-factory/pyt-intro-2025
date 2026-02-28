# Projekt-Reorganisation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Top-Level-Struktur bereinigen, veraltete Dateien entfernen, Makefile als zentralen Einstiegspunkt einführen.

**Architecture:** 10 obsolete Dateien löschen (Einmal-Scripts, veraltete Docs, Shell-Wrapper), ein Makefile mit allen Build/Test/Lint-Targets erstellen, .gitignore ergänzen.

**Tech Stack:** GNU Make, uv, ruff, pytest

---

### Task 1: Veraltete Dokumentation löschen

**Files:**
- Delete: `DOKUMENTATION_ZUSAMMENFASSUNG.md`
- Delete: `TEST_SUMMARY.md`
- Delete: `docs/RUFF_REMAINING_ISSUES.md`
- Delete: `docs/RUFF_USAGE.md`

**Step 1: Dateien löschen**

```bash
git rm DOKUMENTATION_ZUSAMMENFASSUNG.md TEST_SUMMARY.md docs/RUFF_REMAINING_ISSUES.md docs/RUFF_USAGE.md
```

**Step 2: Verifizieren, dass keine Referenzen übrig sind**

```bash
grep -r "DOKUMENTATION_ZUSAMMENFASSUNG\|TEST_SUMMARY\|RUFF_REMAINING\|RUFF_USAGE" --include="*.md" .
```

Expected: Keine Treffer (bereits verifiziert, dass CLAUDE.md und README.md keine Referenzen enthalten).

**Step 3: Commit**

```bash
git commit -m "🗑️ chore: Entferne veraltete Dokumentation

- DOKUMENTATION_ZUSAMMENFASSUNG.md (abgeschlossene Type-Hints-Migration)
- TEST_SUMMARY.md (veraltete Testzahlen)
- docs/RUFF_REMAINING_ISSUES.md (abgeschlossene Bereinigung)
- docs/RUFF_USAGE.md (wird durch Makefile ersetzt)"
```

---

### Task 2: Einmal-Migrations-Scripts löschen

**Files:**
- Delete: `apply_type_hints.py`
- Delete: `fix_test_type_hints.py`

**Step 1: Dateien löschen**

```bash
git rm apply_type_hints.py fix_test_type_hints.py
```

**Step 2: __pycache__ aufräumen (falls vorhanden)**

```bash
rm -rf __pycache__
```

**Step 3: Commit**

```bash
git commit -m "🗑️ chore: Entferne Einmal-Migrations-Scripts

- apply_type_hints.py (Type-Hints aus Feature-Branch, abgeschlossen)
- fix_test_type_hints.py (Test-Type-Hints-Korrektur, abgeschlossen)"
```

---

### Task 3: Shell-Scripts löschen

**Files:**
- Delete: `check_code.sh`
- Delete: `format_code.sh`
- Delete: `format_code_unsafe.sh`
- Delete: `run_tests.sh`

**Step 1: Dateien löschen**

```bash
git rm check_code.sh format_code.sh format_code_unsafe.sh run_tests.sh
```

**Step 2: Commit**

```bash
git commit -m "🗑️ chore: Entferne Shell-Scripts (werden durch Makefile ersetzt)

- check_code.sh -> make lint
- format_code.sh -> make format
- format_code_unsafe.sh -> make format-unsafe
- run_tests.sh -> make test"
```

---

### Task 4: Makefile erstellen

**Files:**
- Create: `Makefile`

**Step 1: Makefile schreiben**

```makefile
.PHONY: help test test-coverage test-quick lint format format-unsafe clean

help: ## Zeigt diese Hilfe an
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# --- Tests ---

test: ## Alle Tests ausfuehren
	uv run pytest -v --tb=short

test-modul%: ## Tests fuer ein Modul (z.B. make test-modul1)
	uv run pytest -m modul$* -v

test-coverage: ## Tests mit Coverage-Report
	uv run pytest --cov --cov-report=html --cov-report=term
	@echo "HTML-Report: htmlcov/index.html"

test-quick: ## Nur Import-Tests (schnell)
	uv run pytest -k "import" -v

# --- Code-Qualitaet ---

lint: ## Code pruefen (ohne Aenderungen)
	uv run ruff check . --output-format=grouped
	uv run ruff format . --check

format: ## Code formatieren und Linting-Fehler beheben
	uv run ruff check . --fix --show-fixes
	uv run ruff format .

format-unsafe: ## Code formatieren inkl. unsafe Fixes
	@echo "WARNUNG: Wendet auch unsafe Fixes an!"
	@read -p "Fortfahren? (j/n) " ans && [ "$$ans" = "j" ] || exit 1
	uv run ruff check . --fix --unsafe-fixes --show-fixes
	uv run ruff format .

# --- Aufraeumen ---

clean: ## Temporaere Dateien loeschen
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov .coverage
```

WICHTIG: Alle eingerückten Zeilen im Makefile MÜSSEN Tabs sein, keine Spaces.

**Step 2: Testen, dass `make help` funktioniert**

```bash
make help
```

Expected: Tabelle mit allen Targets und Beschreibungen.

**Step 3: Testen, dass `make test` funktioniert**

```bash
make test
```

Expected: pytest läuft durch, alle Tests bestehen.

**Step 4: Testen, dass `make lint` funktioniert**

```bash
make lint
```

Expected: ruff prüft Code ohne Fehler.

**Step 5: Commit**

```bash
git add Makefile
git commit -m "✨ feat: Fuege Makefile als zentralen Einstiegspunkt hinzu

Targets: test, test-modul[1-5], test-coverage, test-quick,
lint, format, format-unsafe, clean, help"
```

---

### Task 5: .gitignore ergänzen

**Files:**
- Modify: `.gitignore`

**Step 1: .DS_Store zu .gitignore hinzufügen**

Füge am Anfang der Datei hinzu:

```
# macOS
.DS_Store
```

**Step 2: .DS_Store aus Tracking entfernen (falls getrackt)**

```bash
git rm --cached .DS_Store 2>/dev/null || true
```

**Step 3: Commit**

```bash
git add .gitignore
git commit -m "🔧 chore: Ergaenze .gitignore um .DS_Store"
```

---

### Task 6: Verifikation

**Step 1: Top-Level-Struktur prüfen**

```bash
ls -la | grep -v '^\.' | grep -v '^total'
```

Expected: Nur noch `Makefile`, `README.md`, `CLAUDE.md`, `pyproject.toml`, `uv.lock`,
`pytest.ini`, `pyrightconfig.json`, und die Modul-/Test-/Docs-Ordner.

**Step 2: Alle Make-Targets durchlaufen lassen**

```bash
make test && make lint
```

Expected: Alles grün.

**Step 3: Kein Commit nötig** -- reine Verifikation.
