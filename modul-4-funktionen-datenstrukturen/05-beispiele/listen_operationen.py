"""
Beispiel: Listen-Operationen

Zeigt:
- List Comprehensions
- Listen-Methoden
- Listen als Parameter
"""

def zeige_liste(liste, titel="Liste"):
    """Zeigt eine Liste formatiert an."""
    print(f"\n{titel}:")
    print(f"  {liste}")
    print(f"  Länge: {len(liste)}")

def nur_gerade(zahlen):
    """Filtert gerade Zahlen."""
    return [x for x in zahlen if x % 2 == 0]

def verdopple(zahlen):
    """Verdoppelt alle Werte."""
    return [x * 2 for x in zahlen]

def statistik(zahlen):
    """Berechnet Statistiken."""
    return {
        "min": min(zahlen),
        "max": max(zahlen),
        "summe": sum(zahlen),
        "durchschnitt": sum(zahlen) / len(zahlen)
    }

if __name__ == "__main__":
    print("=" * 50)
    print("LISTEN-OPERATIONEN")
    print("=" * 50)
    
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    zeige_liste(zahlen, "Original")
    
    gerade = nur_gerade(zahlen)
    zeige_liste(gerade, "Nur gerade")
    
    verdoppelt = verdopple(zahlen)
    zeige_liste(verdoppelt, "Verdoppelt")
    
    stats = statistik(zahlen)
    print(f"\nStatistik:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
