"""
Beispiel: Tupel und Sets

Zeigt:
- Tupel für feste Daten
- Sets für eindeutige Elemente
- Mengenoperationen
"""

def berechne_distanz(punkt1, punkt2):
    """Berechnet Distanz zwischen zwei Punkten."""
    x1, y1 = punkt1
    x2, y2 = punkt2
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

def eindeutige_woerter(text):
    """Findet eindeutige Wörter."""
    return set(text.lower().split())

def gemeinsame_elemente(set1, set2):
    """Findet gemeinsame Elemente."""
    return set1 & set2

if __name__ == "__main__":
    print("=" * 50)
    print("TUPEL & SETS")
    print("=" * 50)
    
    # Tupel für Koordinaten
    p1 = (0, 0)
    p2 = (3, 4)
    distanz = berechne_distanz(p1, p2)
    print(f"\nDistanz von {p1} zu {p2}: {distanz}")
    
    # Sets für eindeutige Wörter
    text = "Python ist toll Python macht Spass"
    woerter = eindeutige_woerter(text)
    print(f"\nEindeutige Wörter: {woerter}")
    
    # Mengenoperationen
    kurs_a = {"Anna", "Max", "Lisa"}
    kurs_b = {"Lisa", "Tom", "Sara"}
    
    print(f"\nKurs A: {kurs_a}")
    print(f"Kurs B: {kurs_b}")
    print(f"Beide Kurse: {kurs_a | kurs_b}")
    print(f"In beiden: {kurs_a & kurs_b}")
    print(f"Nur A: {kurs_a - kurs_b}")
