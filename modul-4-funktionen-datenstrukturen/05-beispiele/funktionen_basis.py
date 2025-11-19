"""
Beispiel: Grundlegende Funktionen

Zeigt:
- Funktionen definieren
- Funktionen aufrufen
- Docstrings
"""

def zeige_header():
    """Zeigt einen Header."""
    print("=" * 50)
    print("FUNKTIONEN DEMO")
    print("=" * 50)

def zeige_menu():
    """Zeigt ein Menü."""
    print("\n1. Begrüssung")
    print("2. Rechner")
    print("3. Beenden")

def begruessung():
    """Gibt eine Begrüssung aus."""
    print("\nWillkommen zum Python-Kurs!")
    print("Schön, dass Sie da sind!")

def zeige_footer():
    """Zeigt einen Footer."""
    print("\n" + "-" * 50)
    print("© 2025 Python Kurs")
    print("-" * 50)

if __name__ == "__main__":
    zeige_header()
    zeige_menu()
    begruessung()
    zeige_footer()
