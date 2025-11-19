"""
Beispiel: Währungsrechner
Musterlösung für Aufgabe 1
"""

# Wechselkurse (Stand: 2025)
EUR_ZU_CHF = 0.95
EUR_ZU_USD = 1.10
EUR_ZU_GBP = 0.85

print("=== Währungsrechner ===\n")

# EUR zu anderen Währungen
betrag_eur = 100.00

print("EUR zu anderen Währungen:")
print(f"{betrag_eur:.2f} EUR = {betrag_eur * EUR_ZU_CHF:.2f} CHF")
print(f"{betrag_eur:.2f} EUR = {betrag_eur * EUR_ZU_USD:.2f} USD")
print(f"{betrag_eur:.2f} EUR = {betrag_eur * EUR_ZU_GBP:.2f} GBP\n")

# Rückrechnung: CHF zu EUR
betrag_chf = 100.00
betrag_eur = betrag_chf / EUR_ZU_CHF
print("CHF zu EUR:")
print(f"{betrag_chf:.2f} CHF = {betrag_eur:.2f} EUR\n")

# USD zu EUR
betrag_usd = 100.00
betrag_eur = betrag_usd / EUR_ZU_USD
print("USD zu EUR:")
print(f"{betrag_usd:.2f} USD = {betrag_eur:.2f} EUR\n")

# GBP zu EUR
betrag_gbp = 100.00
betrag_eur = betrag_gbp / EUR_ZU_GBP
print("GBP zu EUR:")
print(f"{betrag_gbp:.2f} GBP = {betrag_eur:.2f} EUR\n")

# Umrechnungstabelle
print("=== Umrechnungstabelle ===")
print("EUR    | CHF    | USD    | GBP")
print("-------|--------|--------|-------")

betraege = [10, 50, 100, 500, 1000]
for eur in betraege:
    chf = eur * EUR_ZU_CHF
    usd = eur * EUR_ZU_USD
    gbp = eur * EUR_ZU_GBP
    print(f"{eur:6.2f} | {chf:6.2f} | {usd:6.2f} | {gbp:6.2f}")

# Mit Wechselgebühren (2%)
print("\n=== Mit Wechselgebühren (2%) ===")
betrag_eur = 100.00
gebuehr = 0.02  # 2%

chf_ohne_gebuehr = betrag_eur * EUR_ZU_CHF
chf_mit_gebuehr = chf_ohne_gebuehr * (1 - gebuehr)

print(f"Betrag: {betrag_eur:.2f} EUR")
print(f"Ohne Gebühr: {chf_ohne_gebuehr:.2f} CHF")
print(f"Mit Gebühr: {chf_mit_gebuehr:.2f} CHF")
print(f"Gebühr: {chf_ohne_gebuehr - chf_mit_gebuehr:.2f} CHF")
