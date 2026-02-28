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
