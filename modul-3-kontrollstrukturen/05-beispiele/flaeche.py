def berechne_rechteck(laenge, breite):
    """
    Berechnet Fläche und Umfang eines Rechtecks.

    Args:
        laenge (float): Länge des Rechtecks in Metern.
        breite (float): Breite des Rechtecks in Metern.
    """

    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)

    return flaeche, umfang


def get_float_input(prompt):
    """
    Fragt so lange nach einer Zahl, bis die Eingabe gültig ist.

    Akzeptiert Dezimalpunkt und Dezimalkomma (3.5 oder 3,5).
    Nur positive Zahlen sind erlaubt, da Längen nicht negativ sein können.

    Args:
        prompt (str): Text, der vor der Eingabe angezeigt wird.

    Returns:
        float: Die eingegebene positive Zahl.
    """
    while True:
        eingabe = input(prompt).strip().replace(",", ".")
        # Höchstens ein Dezimalpunkt, sonst nur Ziffern
        if not eingabe.replace(".", "", 1).isdecimal():
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            continue

        zahl = float(eingabe)
        if zahl > 0:
            return zahl
        print("Der Wert muss grösser als 0 sein.")


laenge = get_float_input("Geben Sie die Länge des Rechtecks in Metern ein : ")
breite = get_float_input("Geben Sie die Breite des Rechtecks in Metern ein: ")

flaeche, umfang = berechne_rechteck(laenge, breite)

print(f"Rechteck {laenge} × {breite}:")
print(f"  Fläche: {flaeche:6.2f} m²")
print(f"  Umfang: {umfang:6.2f} m")
