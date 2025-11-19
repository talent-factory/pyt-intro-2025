"""Formatierte Produktliste mit Berechnungen"""

# Produktdaten
produkte = [
    {"name": "Apfel", "menge": 10, "preis": 2.50},
    {"name": "Banane", "menge": 5, "preis": 3.20},
    {"name": "Orange", "menge": 15, "preis": 1.80},
    {"name": "Kiwi", "menge": 8, "preis": 4.50},
    {"name": "Mango", "menge": 3, "preis": 5.90},
]

# Kopfzeile
print("\n" + "=" * 60)
print("                    PRODUKTLISTE")
print("=" * 60)
print(f"{'Nr':>3} {'Produkt':<20} {'Menge':>8} {'Preis CHF':>12} {'Total CHF':>12}")
print("-" * 60)

# Produkte ausgeben
gesamt_menge = 0
gesamt_preis = 0.0

for i, produkt in enumerate(produkte, start=1):
    name = produkt["name"]
    menge = produkt["menge"]
    preis = produkt["preis"]
    total = menge * preis
    
    print(f"{i:3d} {name:<20} {menge:8d} {preis:12.2f} {total:12.2f}")
    
    gesamt_menge += menge
    gesamt_preis += total

# Summenzeile
print("=" * 60)
print(f"{'GESAMT:':<24} {gesamt_menge:8d} {gesamt_preis:24.2f}")
print("=" * 60)

# Statistiken
durchschnitt_preis = gesamt_preis / gesamt_menge
print(f"\nDurchschnittspreis pro Stück: CHF {durchschnitt_preis:.2f}")
print(f"Anzahl Produkte: {len(produkte)}")
