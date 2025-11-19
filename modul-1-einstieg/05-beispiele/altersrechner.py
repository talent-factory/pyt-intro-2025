"""
Beispiel: Altersrechner
Musterlösung für Übung 3
"""

# Altersrechner
# Berechnet das Alter basierend auf Geburtsjahr

geburtsjahr = 2000
aktuelles_jahr = 2025

alter = aktuelles_jahr - geburtsjahr

print("=== Altersrechner ===\n")
print(f"Geburtsjahr: {geburtsjahr}")
print(f"Aktuelles Jahr: {aktuelles_jahr}")
print(f"Alter: {alter} Jahre\n")

# Erweiterungen

# Alter in Monaten
alter_monate = alter * 12
print(f"Das sind {alter_monate} Monate")

# Alter in Tagen (ungefähr)
alter_tage = alter * 365
print(f"Das sind ungefähr {alter_tage} Tage\n")

# Bis zum nächsten runden Geburtstag
naechster_runder = ((alter // 10) + 1) * 10
jahre_bis_rund = naechster_runder - alter
print(f"Bis zum {naechster_runder}. Geburtstag: {jahre_bis_rund} Jahre\n")

# Verschiedene Personen
print("=== Verschiedene Personen ===\n")

personen = [
    ("Anna", 2000),
    ("Max", 1995),
    ("Lisa", 2005),
]

for name, geburtsjahr in personen:
    alter = aktuelles_jahr - geburtsjahr
    print(f"{name} (geboren {geburtsjahr}): {alter} Jahre alt")
