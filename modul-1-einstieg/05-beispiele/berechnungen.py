"""
Beispiel: Einfache Berechnungen
Musterlösung für Aufgabe 3
"""

print("=== Berechnungen ===\n")

# 1. Zinsrechner
print("1. Zinsrechner:")
startkapital = 1000.00
zinssatz = 0.03  # 3%
jahre = 5
endkapital = startkapital * ((1 + zinssatz) ** jahre)
gewinn = endkapital - startkapital

print(f"Startkapital: {startkapital:.2f} EUR")
print(f"Zinssatz: {zinssatz * 100:.1f}%")
print(f"Jahre: {jahre}")
print(f"Endkapital: {endkapital:.2f} EUR")
print(f"Gewinn: {gewinn:.2f} EUR\n")

# 2. Benzinverbrauch
print("2. Benzinverbrauch:")
strecke = 350  # km
verbrauch_pro_100km = 6.5  # Liter
preis_pro_liter = 1.80  # EUR

benoetigte_liter = strecke * verbrauch_pro_100km / 100
kosten = benoetigte_liter * preis_pro_liter

print(f"Strecke: {strecke} km")
print(f"Verbrauch: {verbrauch_pro_100km} L/100km")
print(f"Preis: {preis_pro_liter} EUR/L")
print(f"Benötigte Liter: {benoetigte_liter:.2f} L")
print(f"Kosten: {kosten:.2f} EUR\n")

# 3. Pizzarechner
print("3. Pizzarechner:")
anzahl_pizzen = 3
preis_pro_pizza = 12.00
anzahl_personen = 4

gesamtpreis = anzahl_pizzen * preis_pro_pizza
preis_pro_person = gesamtpreis / anzahl_personen

print(f"{anzahl_pizzen} Pizzen à {preis_pro_pizza:.2f} EUR")
print(f"{anzahl_personen} Personen")
print(f"Preis pro Person: {preis_pro_person:.2f} EUR\n")

# 4. Zeitumrechnung
print("4. Zeitumrechnung:")
gesamt_sekunden = 7325

stunden = gesamt_sekunden // 3600
rest_sekunden = gesamt_sekunden % 3600
minuten = rest_sekunden // 60
sekunden = rest_sekunden % 60

print(
    f"{gesamt_sekunden} Sekunden = {stunden} Stunden, "
    f"{minuten} Minuten, {sekunden} Sekunden\n"
)

# Weitere Beispiele
print("=== Weitere Berechnungen ===\n")

# Trinkgeld
print("5. Trinkgeld:")
rechnung = 45.50
trinkgeld_prozent = 0.10  # 10%
trinkgeld = rechnung * trinkgeld_prozent
gesamt = rechnung + trinkgeld

print(f"Rechnung: {rechnung:.2f} EUR")
print(f"Trinkgeld ({trinkgeld_prozent * 100:.0f}%): {trinkgeld:.2f} EUR")
print(f"Gesamt: {gesamt:.2f} EUR\n")

# Rabatt
print("6. Rabatt:")
originalpreis = 100.00
rabatt_prozent = 0.20  # 20%
rabatt = originalpreis * rabatt_prozent
endpreis = originalpreis - rabatt

print(f"Originalpreis: {originalpreis:.2f} EUR")
print(f"Rabatt ({rabatt_prozent * 100:.0f}%): {rabatt:.2f} EUR")
print(f"Endpreis: {endpreis:.2f} EUR\n")

# Mehrwertsteuer
print("7. Mehrwertsteuer:")
netto = 100.00
mwst_satz = 0.19  # 19%
mwst = netto * mwst_satz
brutto = netto + mwst

print(f"Netto: {netto:.2f} EUR")
print(f"MwSt ({mwst_satz * 100:.0f}%): {mwst:.2f} EUR")
print(f"Brutto: {brutto:.2f} EUR")
