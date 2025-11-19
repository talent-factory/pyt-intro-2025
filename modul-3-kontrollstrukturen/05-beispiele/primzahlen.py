"""
Primzahlen-Finder
Demonstriert verschachtelte Schleifen und mathematische Algorithmen.

Konzepte:
- Verschachtelte for-Schleifen
- Break für Optimierung
- Funktionen
- Listen
- Mathematik
"""

import time


def ist_primzahl(n: int) -> bool:
    """
    Prüft ob n eine Primzahl ist.
    
    Optimiert: Prüft nur bis √n und nur ungerade Zahlen.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Nur bis Wurzel prüfen, nur ungerade Teiler
    for teiler in range(3, int(n ** 0.5) + 1, 2):
        if n % teiler == 0:
            return False
    
    return True


def finde_primzahlen(bis: int) -> list[int]:
    """Findet alle Primzahlen bis zur angegebenen Zahl."""
    primzahlen = []
    
    for zahl in range(2, bis + 1):
        if ist_primzahl(zahl):
            primzahlen.append(zahl)
    
    return primzahlen


def primfaktoren(n: int) -> list[int]:
    """Zerlegt n in Primfaktoren."""
    faktoren = []
    teiler = 2
    
    while n > 1:
        while n % teiler == 0:
            faktoren.append(teiler)
            n //= teiler
        teiler += 1
        
        # Optimierung: Wenn teiler > √n, dann ist n prim
        if teiler * teiler > n and n > 1:
            faktoren.append(n)
            break
    
    return faktoren


def finde_primzahl_zwillinge(bis: int) -> list[tuple[int, int]]:
    """Findet Primzahl-Zwillinge (p, p+2) bis zur angegebenen Zahl."""
    zwillinge = []
    primzahlen = finde_primzahlen(bis)
    
    for i in range(len(primzahlen) - 1):
        if primzahlen[i + 1] - primzahlen[i] == 2:
            zwillinge.append((primzahlen[i], primzahlen[i + 1]))
    
    return zwillinge


def main() -> None:
    """Hauptprogramm."""
    print("=" * 50)
    print("           PRIMZAHLEN-FINDER")
    print("=" * 50)
    
    while True:
        print("\n1. Primzahl-Test")
        print("2. Primzahlen bis N")
        print("3. Primfaktorzerlegung")
        print("4. Primzahl-Zwillinge")
        print("5. Beenden")
        
        wahl = input("\nWahl: ").strip()
        
        if wahl == "1":
            # Primzahl-Test
            try:
                n = int(input("\nZahl: "))
                if ist_primzahl(n):
                    print(f"✓ {n} ist eine Primzahl")
                else:
                    print(f"✗ {n} ist keine Primzahl")
            except ValueError:
                print("❌ Bitte eine Zahl eingeben!")
        
        elif wahl == "2":
            # Primzahlen bis N
            try:
                n = int(input("\nBis zu welcher Zahl? "))
                
                start = time.time()
                primzahlen = finde_primzahlen(n)
                dauer = time.time() - start
                
                print(f"\nPrimzahlen bis {n}:")
                
                # Ausgabe in Zeilen zu je 10 Zahlen
                for i in range(0, len(primzahlen), 10):
                    zeile = primzahlen[i:i+10]
                    print(", ".join(map(str, zeile)))
                
                print(f"\nStatistik:")
                print(f"- Anzahl: {len(primzahlen)}")
                if primzahlen:
                    print(f"- Kleinste: {primzahlen[0]}")
                    print(f"- Grösste: {primzahlen[-1]}")
                print(f"- Dauer: {dauer:.3f} Sekunden")
            
            except ValueError:
                print("❌ Bitte eine Zahl eingeben!")
        
        elif wahl == "3":
            # Primfaktorzerlegung
            try:
                n = int(input("\nZahl: "))
                
                if n < 2:
                    print("❌ Zahl muss mindestens 2 sein!")
                    continue
                
                faktoren = primfaktoren(n)
                
                print(f"\nPrimfaktorzerlegung von {n}:")
                print(f"{n} = {' × '.join(map(str, faktoren))}")
            
            except ValueError:
                print("❌ Bitte eine Zahl eingeben!")
        
        elif wahl == "4":
            # Primzahl-Zwillinge
            try:
                n = int(input("\nBis zu welcher Zahl? "))
                
                zwillinge = finde_primzahl_zwillinge(n)
                
                print(f"\nPrimzahl-Zwillinge bis {n}:")
                for p1, p2 in zwillinge:
                    print(f"({p1}, {p2})")
                
                print(f"\nGesamt: {len(zwillinge)} Paare")
            
            except ValueError:
                print("❌ Bitte eine Zahl eingeben!")
        
        elif wahl == "5":
            print("\n👋 Auf Wiedersehen!")
            break
        
        else:
            print("\n❌ Ungültige Wahl! Bitte 1-5 wählen.")


if __name__ == "__main__":
    main()

