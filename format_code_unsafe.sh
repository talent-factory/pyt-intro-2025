#!/bin/bash

# ============================================
# Ruff Code-Formatierung mit UNSAFE Fixes
# ============================================
# Dieses Skript wendet auch "unsafe" Fixes an

set -e  # Bei Fehler abbrechen

# Farben für Output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Ruff mit UNSAFE Fixes${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo -e "${YELLOW}⚠️  WARNUNG: Dieses Skript wendet auch 'unsafe' Fixes an!${NC}"
echo -e "${YELLOW}   Diese können in seltenen Fällen die Code-Semantik ändern.${NC}"
echo ""
read -p "Möchten Sie fortfahren? (j/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Jj]$ ]]; then
    echo -e "${RED}Abgebrochen.${NC}"
    exit 1
fi

echo ""

# Prüfen, ob ruff installiert ist
if [ ! -f ".venv/bin/ruff" ]; then
    echo -e "${YELLOW}⚠️  Ruff nicht gefunden. Installiere Dependencies...${NC}"
    uv sync
    echo ""
fi

# 1. LINTING: Fehler finden und automatisch beheben (inkl. unsafe)
echo -e "${BLUE}📋 Schritt 1: Linting mit UNSAFE Fixes${NC}"
echo "Führe Ruff Linting mit Auto-Fix (inkl. unsafe) aus..."
.venv/bin/ruff check . --fix --unsafe-fixes --show-fixes

echo ""
echo -e "${GREEN}✅ Linting abgeschlossen${NC}"
echo ""

# 2. FORMATIERUNG: Code formatieren
echo -e "${BLUE}🎨 Schritt 2: Code-Formatierung${NC}"
echo "Formatiere alle Python-Dateien..."
.venv/bin/ruff format .

echo ""
echo -e "${GREEN}✅ Formatierung abgeschlossen${NC}"
echo ""

# 3. FINALE PRÜFUNG: Zeige verbleibende Probleme
echo -e "${BLUE}🔍 Schritt 3: Finale Prüfung${NC}"
echo "Prüfe auf verbleibende Probleme..."
if .venv/bin/ruff check . --output-format=concise; then
    echo ""
    echo -e "${GREEN}✅ Keine Probleme gefunden!${NC}"
else
    echo ""
    echo -e "${YELLOW}⚠️  Es gibt noch einige Warnungen (siehe oben)${NC}"
    echo -e "${YELLOW}   Diese müssen manuell behoben werden.${NC}"
fi

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ Fertig!${NC}"
echo -e "${BLUE}========================================${NC}"

