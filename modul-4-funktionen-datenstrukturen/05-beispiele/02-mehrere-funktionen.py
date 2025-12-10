# Beispiel 2: Mehrere Funktionen kombinieren
# Dieses Beispiel zeigt, wie man mehrere Funktionen definiert und
# diese nacheinander aufruft, um ein strukturiertes Programm zu erstellen.

def zeige_header():
    """Zeigt einen Header."""
    print("=" * 40)
    print("MEIN PROGRAMM")
    print("=" * 40)

def zeige_menu():
    """Zeigt ein Menü."""
    print("1. Option A")
    print("2. Option B")
    print("3. Beenden")

def zeige_footer():
    """Zeigt einen Footer."""
    print("-" * 40)
    print("© 2025 Mein Programm")

# Programm
zeige_header()
zeige_menu()
zeige_footer()