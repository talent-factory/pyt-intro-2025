#!/bin/bash

# ============================================
# Ruff Code-Prüfung (ohne Änderungen)
# ============================================
# Dieses Skript prüft alle Python-Dateien, ändert aber nichts

set -e  # Bei Fehler abbrechen

# Farben für Output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Ruff Code-Prüfung (Dry Run)${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Prüfen, ob ruff installiert ist
if [ ! -f ".venv/bin/ruff" ]; then
    echo -e "${RED}❌ Ruff nicht gefunden!${NC}"
    echo "Bitte führen Sie 'uv sync' aus."
    exit 1
fi

# 1. LINTING: Fehler finden (ohne zu beheben)
echo -e "${BLUE}📋 Linting-Prüfung${NC}"
echo "Prüfe auf Linting-Fehler..."
echo ""

if .venv/bin/ruff check . --output-format=grouped; then
    echo ""
    echo -e "${GREEN}✅ Keine Linting-Fehler gefunden!${NC}"
    LINT_OK=true
else
    echo ""
    echo -e "${YELLOW}⚠️  Linting-Fehler gefunden (siehe oben)${NC}"
    LINT_OK=false
fi

echo ""
echo -e "${BLUE}----------------------------------------${NC}"
echo ""

# 2. FORMATIERUNG: Prüfen (ohne zu formatieren)
echo -e "${BLUE}🎨 Formatierungs-Prüfung${NC}"
echo "Prüfe Code-Formatierung..."
echo ""

if .venv/bin/ruff format . --check; then
    echo ""
    echo -e "${GREEN}✅ Code ist korrekt formatiert!${NC}"
    FORMAT_OK=true
else
    echo ""
    echo -e "${YELLOW}⚠️  Code muss formatiert werden (siehe oben)${NC}"
    FORMAT_OK=false
fi

echo ""
echo -e "${BLUE}========================================${NC}"

# Zusammenfassung
if [ "$LINT_OK" = true ] && [ "$FORMAT_OK" = true ]; then
    echo -e "${GREEN}✅ Alle Prüfungen bestanden!${NC}"
    echo -e "${BLUE}========================================${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Es gibt Probleme, die behoben werden müssen:${NC}"
    if [ "$LINT_OK" = false ]; then
        echo -e "   - Linting-Fehler: Führen Sie './format_code.sh' aus"
    fi
    if [ "$FORMAT_OK" = false ]; then
        echo -e "   - Formatierungs-Probleme: Führen Sie './format_code.sh' aus"
    fi
    echo -e "${BLUE}========================================${NC}"
    exit 1
fi

