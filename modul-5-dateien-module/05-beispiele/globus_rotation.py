"""
Rotierende Weltkugel mit gefüllten Kontinenten und Gradnetz.

Benötigt: numpy, matplotlib, cartopy (nur beim allerersten Start, für die
Landmasse)

Ablauf:
1. Beim ersten Start wird aus den Natural-Earth-Küstendaten eine Landmaske
   berechnet und lokal als .npy-Datei gespeichert.
2. Jeder weitere Start lädt diese Datei direkt, ohne cartopy und ohne
   Netzzugriff.
3. Pro Bild wird jeder Pixel der Kugel zurück auf die ursprüngliche Position
   gerechnet. Liegt dieser Punkt auf Land, wird er grün gefärbt.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.path import Path as Polygonpfad

# ---------- Einstellungen ----------
# Rotationsachse (beliebiger Vektor, wird normiert)
ACHSE = np.array([0.3, 0.5, 1.0])
# Anzahl Bilder einer vollen Umdrehung
ANZAHL_BILDER = 240
# Verzögerung zwischen zwei Bildern in Millisekunden
INTERVALL_MS = 40
# Auflösung der Kugel (Pixel pro Seite)
PIXEL = 400
# Auflösung der Landmaske in Grad
GRADSCHRITT = 0.5
# True: Animation als GIF speichern statt anzeigen
SPEICHERN = False
DATEINAME = "globus.gif"

# Ordner des Skripts, in dem die Landmaske zwischengespeichert wird
CACHE_DATEI = Path(__file__).resolve().parent / f"landmaske_{GRADSCHRITT}.npy"

OZEAN_FARBE = np.array([0.80, 0.92, 0.99])
LAND_FARBE = np.array([0.74, 0.87, 0.58])
GITTER_FARBE = "#4a7fc1"


def geo_zu_xyz(breite_grad, laenge_grad):
    """
    Wandelt geografische Koordinaten in Punkte auf der Einheitskugel um.

    Args:
        breite_grad: Breitengrade (Array), -90 bis +90
        laenge_grad: Längengrade (Array), -180 bis +180 bzw. 0 bis 360

    Returns:
        numpy.ndarray: Array der Form (N, 3) mit den Spalten x, y, z
    """
    breite = np.radians(breite_grad)
    laenge = np.radians(laenge_grad)
    return np.column_stack(
        [
            np.cos(breite) * np.cos(laenge),
            np.cos(breite) * np.sin(laenge),
            np.sin(breite),
        ]
    )


def rotationsmatrix(achse, winkel):
    """
    Berechnet die Rotationsmatrix um eine beliebige Achse (Rodrigues-Formel).

    Args:
        achse: Rotationsachse als Vektor mit drei Komponenten
        winkel: Drehwinkel im Bogenmass

    Returns:
        numpy.ndarray: Rotationsmatrix der Form (3, 3)
    """
    k = achse / np.linalg.norm(achse)
    kreuz = np.array(
        [
            [0.0, -k[2], k[1]],
            [k[2], 0.0, -k[0]],
            [-k[1], k[0], 0.0],
        ]
    )
    return np.eye(3) + np.sin(winkel) * kreuz + (1 - np.cos(winkel)) * (kreuz @ kreuz)


def maskengroesse():
    """
    Bestimmt die Grösse der Landmaske anhand des Gradschritts.

    Returns:
        tuple: (Anzahl Zeilen, Anzahl Spalten)
    """
    zeilen = int(round(180 / GRADSCHRITT))
    spalten = int(round(360 / GRADSCHRITT))
    return zeilen, spalten


def landmaske_berechnen():
    """
    Berechnet die Landmaske aus den Natural-Earth-Daten.

    Das dauert einige Sekunden und benötigt cartopy sowie beim ersten Mal
    einen Netzzugriff.

    Returns:
        numpy.ndarray: Wahrheitswerte der Form (Zeilen, Spalten),
        True = Land, False = Meer
    """
    import cartopy.io.shapereader as shpreader

    zeilen, spalten = maskengroesse()
    pfad = shpreader.natural_earth(resolution="50m", category="physical", name="land")

    # Mittelpunkte aller Gitterzellen
    laengen = -180 + GRADSCHRITT / 2 + GRADSCHRITT * np.arange(spalten)
    breiten = -90 + GRADSCHRITT / 2 + GRADSCHRITT * np.arange(zeilen)
    laengen_gitter, breiten_gitter = np.meshgrid(laengen, breiten)
    punkte = np.column_stack([laengen_gitter.ravel(), breiten_gitter.ravel()])

    maske = np.zeros(len(punkte), dtype=bool)
    for geometrie in shpreader.Reader(pfad).geometries():
        # Eine Geometrie ist entweder ein Polygon oder ein MultiPolygon
        for teil in getattr(geometrie, "geoms", [geometrie]):
            polygon = Polygonpfad(np.asarray(teil.exterior.coords))
            maske |= polygon.contains_points(punkte)
    return maske.reshape(zeilen, spalten)


def landmaske():
    """
    Liefert die Landmaske als Gitter: True = Land, False = Meer.

    Liegt die Maske schon lokal vor, wird sie geladen. Sonst wird sie einmal
    berechnet und gespeichert. Schlägt die Berechnung fehl, wird eine Maske
    ohne Land zurückgegeben, damit die Wasserkugel trotzdem erscheint.

    Returns:
        numpy.ndarray: Wahrheitswerte der Form (Zeilen, Spalten)
    """
    if CACHE_DATEI.exists():
        return np.load(CACHE_DATEI)

    try:
        maske = landmaske_berechnen()
    except Exception as fehler:  # z. B. cartopy fehlt oder kein Netzzugriff
        print(
            f"Landmasse nicht verfügbar ({fehler}).\n",
            "Es wird nur die Wasserkugel gezeichnet.\n",
            "Im terminal 'uv add cartopy' ausführen",
        )
        return np.zeros(maskengroesse(), dtype=bool)

    np.save(CACHE_DATEI, maske)
    print(f"Landmaske gespeichert unter {CACHE_DATEI.name}")
    return maske


def gradnetz():
    """
    Erzeugt die Längen- und Breitenkreise des Gradnetzes.

    Returns:
        list: Liste von Linien, jede Linie ist ein Array der Form (N, 3)
    """
    linien = []
    breiten = np.linspace(-90, 90, 181)
    laengen = np.linspace(0, 360, 361)

    for laenge in range(0, 360, 30):  # Meridiane (Längenkreise)
        linien.append(geo_zu_xyz(breiten, np.full_like(breiten, laenge)))
    for breite in range(-60, 61, 30):  # Breitenkreise
        linien.append(geo_zu_xyz(np.full_like(laengen, breite), laengen))
    return linien


def kugelbild(rotation, maske):
    """
    Berechnet für jeden Pixel die Farbe der gedrehten Kugel.

    Rückrechnung: Pixel -> Punkt auf der Kugel -> ursprüngliche Position
    -> Land oder Meer?

    Args:
        rotation: Rotationsmatrix der Form (3, 3)
        maske: Landmaske (True = Land, False = Meer)

    Returns:
        numpy.ndarray: RGBA-Bild der Form (PIXEL, PIXEL, 4)
    """
    achse = np.linspace(-1, 1, PIXEL)
    y, z = np.meshgrid(achse, achse[::-1])  # oben = +z
    abstand_quadrat = y**2 + z**2
    innen = abstand_quadrat <= 1
    # Tiefe (sichtbar, wenn > 0)
    x = np.sqrt(np.clip(1 - abstand_quadrat, 0, None))

    gedreht = np.stack([x, y, z], axis=-1)
    urspruenglich = gedreht @ rotation  # Umkehrung der Drehung

    breite = np.degrees(np.arcsin(np.clip(urspruenglich[..., 2], -1, 1)))
    laenge = np.degrees(np.arctan2(urspruenglich[..., 1], urspruenglich[..., 0]))
    zeile = np.clip(((breite + 90) / GRADSCHRITT).astype(int), 0, maske.shape[0] - 1)
    spalte = np.clip(((laenge + 180) / GRADSCHRITT).astype(int), 0, maske.shape[1] - 1)

    ist_land = maske[zeile, spalte]
    farbe = np.where(ist_land[..., None], LAND_FARBE, OZEAN_FARBE)
    # Einfache Schattierung zum Rand hin
    farbe = farbe * (0.75 + 0.25 * x[..., None])

    # Ausserhalb der Kugel transparent
    alpha = innen[..., None].astype(float)
    return np.concatenate([farbe, alpha], axis=-1)


def erzeuge_animation(maske):
    """
    Baut die Grafik auf und erstellt die Animation.

    Args:
        maske: Landmaske (True = Land, False = Meer)

    Returns:
        FuncAnimation: Animation (muss vom Aufrufer behalten werden,
        sonst wird sie von Python vorzeitig gelöscht)
    """
    gitter = gradnetz()

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor("white")
    ax.set_aspect("equal")
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.axis("off")

    bild = ax.imshow(
        kugelbild(np.eye(3), maske),
        extent=(-1, 1, -1, 1),
        origin="upper",
        interpolation="bilinear",
        zorder=1,
    )

    linien = []
    for punkte in gitter:
        (linie,) = ax.plot([], [], color=GITTER_FARBE, lw=0.8, zorder=2)
        linien.append((punkte, linie))

    # Kugelrand
    ax.add_patch(
        Circle((0, 0), 1, facecolor="none", edgecolor=GITTER_FARBE, lw=2, zorder=3)
    )

    def aktualisiere(bildnummer):
        """Zeichnet das Bild mit der angegebenen Nummer neu."""
        winkel = 2 * np.pi * bildnummer / ANZAHL_BILDER
        rotation = rotationsmatrix(ACHSE, winkel)

        bild.set_data(kugelbild(rotation, maske))

        for punkte, linie in linien:
            gedreht = punkte @ rotation.T
            sichtbar = gedreht[:, 0] > 0  # nur die Vorderseite zeichnen
            y = np.where(sichtbar, gedreht[:, 1], np.nan)
            z = np.where(sichtbar, gedreht[:, 2], np.nan)
            linie.set_data(y, z)

        return [bild] + [linie for _, linie in linien]

    return FuncAnimation(
        fig,
        aktualisiere,
        frames=ANZAHL_BILDER,
        interval=INTERVALL_MS,
        blit=True,
    )


def main():
    """Lädt die Landmaske und zeigt die Animation an bzw. speichert sie."""
    print("=" * 40)
    print("Rotierende Weltkugel")
    print("=" * 40)

    maske = landmaske()
    animation = erzeuge_animation(maske)

    if SPEICHERN:
        animation.save(DATEINAME, writer="pillow", fps=1000 // INTERVALL_MS)
        print(f"Gespeichert als {DATEINAME}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
