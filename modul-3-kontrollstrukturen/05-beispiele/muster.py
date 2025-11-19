"""
Muster zeichnen
Demonstriert verschachtelte Schleifen für visuelle Muster.

Konzepte:
- Verschachtelte for-Schleifen
- Print mit end=""
- Mathematische Muster
- Bedingte Ausgabe
"""


def rechteck(breite: int, hoehe: int) -> None:
    """Zeichnet ein Rechteck."""
    print(f"\n=== Rechteck {breite}x{hoehe} ===\n")
    
    for i in range(hoehe):
        for j in range(breite):
            print("*", end="")
        print()


def dreieck(hoehe: int) -> None:
    """Zeichnet ein Dreieck."""
    print(f"\n=== Dreieck (Höhe {hoehe}) ===\n")
    
    for i in range(1, hoehe + 1):
        for j in range(i):
            print("*", end="")
        print()


def umgekehrtes_dreieck(hoehe: int) -> None:
    """Zeichnet ein umgekehrtes Dreieck."""
    print(f"\n=== Umgekehrtes Dreieck (Höhe {hoehe}) ===\n")
    
    for i in range(hoehe, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


def pyramide(hoehe: int) -> None:
    """Zeichnet eine Pyramide."""
    print(f"\n=== Pyramide (Höhe {hoehe}) ===\n")
    
    for i in range(1, hoehe + 1):
        # Leerzeichen
        for j in range(hoehe - i):
            print(" ", end="")
        
        # Sterne
        for k in range(2 * i - 1):
            print("*", end="")
        
        print()


def raute(groesse: int) -> None:
    """Zeichnet eine Raute."""
    print(f"\n=== Raute (Grösse {groesse}) ===\n")
    
    # Obere Hälfte (inkl. Mitte)
    for i in range(1, groesse + 1):
        # Leerzeichen
        for j in range(groesse - i):
            print(" ", end="")
        
        # Sterne
        for k in range(2 * i - 1):
            print("*", end="")
        
        print()
    
    # Untere Hälfte
    for i in range(groesse - 1, 0, -1):
        # Leerzeichen
        for j in range(groesse - i):
            print(" ", end="")
        
        # Sterne
        for k in range(2 * i - 1):
            print("*", end="")
        
        print()


def schachbrett(groesse: int) -> None:
    """Zeichnet ein Schachbrett-Muster."""
    print(f"\n=== Schachbrett {groesse}x{groesse} ===\n")
    
    for zeile in range(groesse):
        for spalte in range(groesse):
            if (zeile + spalte) % 2 == 0:
                print("□", end=" ")
            else:
                print("■", end=" ")
        print()


def zahlen_pyramide(hoehe: int) -> None:
    """Zeichnet eine Pyramide mit Zahlen."""
    print(f"\n=== Zahlen-Pyramide (Höhe {hoehe}) ===\n")
    
    for i in range(1, hoehe + 1):
        # Leerzeichen
        for j in range(hoehe - i):
            print(" ", end="")
        
        # Aufsteigende Zahlen
        for k in range(1, i + 1):
            print(k, end="")
        
        # Absteigende Zahlen
        for k in range(i - 1, 0, -1):
            print(k, end="")
        
        print()


def multiplikationstabelle(groesse: int) -> None:
    """Zeichnet eine Multiplikationstabelle."""
    print(f"\n=== Multiplikationstabelle {groesse}x{groesse} ===\n")
    
    # Kopfzeile
    print("   ", end="")
    for i in range(1, groesse + 1):
        print(f"{i:3}", end=" ")
    print()
    print("   " + "-" * (groesse * 4))
    
    # Tabelle
    for i in range(1, groesse + 1):
        print(f"{i:2} |", end="")
        for j in range(1, groesse + 1):
            print(f"{i*j:3}", end=" ")
        print()


def main() -> None:
    """Hauptprogramm - zeigt alle Muster."""
    print("=" * 50)
    print("           MUSTER-GENERATOR")
    print("=" * 50)
    
    rechteck(8, 5)
    dreieck(5)
    umgekehrtes_dreieck(5)
    pyramide(5)
    raute(5)
    schachbrett(8)
    zahlen_pyramide(5)
    multiplikationstabelle(10)
    
    print("\n" + "=" * 50)
    print("Alle Muster angezeigt!")
    print("=" * 50)


if __name__ == "__main__":
    main()

