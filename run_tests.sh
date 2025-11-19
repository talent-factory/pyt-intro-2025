#!/bin/bash
# Test-Suite Ausführungs-Skript für Python-Intro-2025

echo "================================================"
echo "   Python-Intro-2025 Test-Suite"
echo "================================================"
echo ""

# Farben für Output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Prüfe ob pytest installiert ist
if ! command -v pytest &> /dev/null
then
    echo "❌ pytest ist nicht installiert!"
    echo "Installiere mit: pip install pytest pytest-cov"
    exit 1
fi

echo -e "${GREEN}✓ pytest gefunden${NC}"
echo ""

# Zeige Test-Statistik
echo "📊 Test-Statistik:"
echo "----------------------------------------"
pytest --collect-only -q | tail -1
echo ""

# Standardmäßig alle Tests ausführen
if [ $# -eq 0 ]; then
    echo "🚀 Führe alle Tests aus..."
    echo ""
    pytest -v --tb=short
else
    # Argument übergeben
    case "$1" in
        "modul1"|"m1")
            echo "🚀 Führe Modul 1 Tests aus..."
            pytest -m modul1 -v
            ;;
        "modul2"|"m2")
            echo "🚀 Führe Modul 2 Tests aus..."
            pytest -m modul2 -v
            ;;
        "modul3"|"m3")
            echo "🚀 Führe Modul 3 Tests aus..."
            pytest -m modul3 -v
            ;;
        "coverage"|"cov")
            echo "🚀 Führe Tests mit Coverage aus..."
            pytest --cov=modul-1-einstieg --cov=modul-2-datentypen --cov=modul-3-kontrollstrukturen --cov-report=html --cov-report=term
            echo ""
            echo -e "${YELLOW}💡 HTML Coverage-Report: htmlcov/index.html${NC}"
            ;;
        "quick"|"q")
            echo "🚀 Führe Quick-Tests aus (nur Import-Tests)..."
            pytest -k "import" -v
            ;;
        "help"|"-h"|"--help")
            echo "Verwendung: ./run_tests.sh [OPTION]"
            echo ""
            echo "Optionen:"
            echo "  (keine)        Alle Tests ausführen"
            echo "  modul1, m1     Nur Modul 1 Tests"
            echo "  modul2, m2     Nur Modul 2 Tests"
            echo "  modul3, m3     Nur Modul 3 Tests"
            echo "  coverage, cov  Tests mit Coverage-Report"
            echo "  quick, q       Nur Import-Tests (schnell)"
            echo "  help, -h       Diese Hilfe anzeigen"
            echo ""
            echo "Beispiele:"
            echo "  ./run_tests.sh"
            echo "  ./run_tests.sh modul1"
            echo "  ./run_tests.sh coverage"
            ;;
        *)
            echo "❌ Unbekannte Option: $1"
            echo "Nutze './run_tests.sh help' für Hilfe"
            exit 1
            ;;
    esac
fi

echo ""
echo "================================================"
echo "   Tests abgeschlossen"
echo "================================================"
