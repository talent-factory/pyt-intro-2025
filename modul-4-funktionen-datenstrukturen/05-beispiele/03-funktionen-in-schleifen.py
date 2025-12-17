"""
Beispiel: Funktionen in Schleifen aufrufen

Dieses Beispiel zeigt, wie man eine Funktion wiederholt in einer
Schleife aufrufen kann, um repetitive Aufgaben zu erledigen.
"""


def zeige_stern() -> None:
    """Zeigt einen Stern."""
    print("⭐", end=" ")


# 10 Sterne ausgeben
for i in range(10):
    zeige_stern()
print()  # Neue Zeile
