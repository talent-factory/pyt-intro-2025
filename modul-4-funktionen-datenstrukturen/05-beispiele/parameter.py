"""
Beispiel: Funktionen mit Parametern

Zeigt:
- Parameter übergeben
- Return-Werte
- Default-Parameter
"""

def gruesse(name: str) -> None:
    """Begrüsst eine Person."""
    print(f"Hallo {name}!")

def addiere(a: int | float, b: int | float) -> int | float:
    """Addiert zwei Zahlen."""
    return a + b

def formatiere_preis(betrag: float, waehrung: str = "CHF") -> str:
    """Formatiert einen Preis."""
    return f"{betrag:.2f} {waehrung}"

def berechne_rechteck(laenge: int | float, breite: int | float) -> tuple[int | float, int | float]:
    """Berechnet Fläche eines Rechtecks."""
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    return flaeche, umfang

if __name__ == "__main__":
    print("=" * 50)
    print("PARAMETER DEMO")
    print("=" * 50)
    
    # Einfache Parameter
    gruesse("Anna")
    gruesse("Max")
    
    # Return-Werte
    summe = addiere(5, 3)
    print(f"\n5 + 3 = {summe}")
    
    # Default-Parameter
    print(f"\nPreis: {formatiere_preis(19.99)}")
    print(f"Preis: {formatiere_preis(29.50, 'EUR')}")
    
    # Mehrere Rückgabewerte
    f, u = berechne_rechteck(5, 3)
    print(f"\nRechteck 5×3:")
    print(f"  Fläche: {f} m²")
    print(f"  Umfang: {u} m")
