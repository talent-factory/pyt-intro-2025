"""
Pascal'sches Dreieck

Jede Zahl ist die Summe der beiden Zahlen direkt darüber.
Hier berechnen wir sie ohne Listen: Der Wert in einer Zeile entsteht
aus dem vorherigen Wert derselben Zeile (Binomialkoeffizient).
"""

groesse = int(input("Geben Sie die Grösse des Dreiecks ein: "))

for zeile in range(groesse):
    # Jede Zeile beginnt mit 1
    wert = 1

    # Einrückung, damit das Dreieck symmetrisch aussieht
    print(" " * (groesse - zeile - 1), end="")

    for spalte in range(zeile + 1):
        print(wert, end=" ")
        # Nächsten Wert der Zeile berechnen
        wert = wert * (zeile - spalte) // (spalte + 1)

    print()
