"""
Beispiel: Notizen-App mit Streamlit-Oberfläche

Eine Web-Version der Notizen-App. Sie nutzt dieselbe Kern-Funktion
'formatiere_notiz()' wie die Konsolen-App 'notizen_app.py' und zeigt damit,
wie sich Logik und Oberfläche trennen lassen.

Bedienung:
- Notizen-Datei öffnen: über den Datei-Dialog (Finder/Explorer) eine
  .txt-Datei auswählen.
- Neue Notiz: Text eingeben und hinzufügen (mit Zeitstempel).
- Speichern: Notizen als Datei herunterladen (Speichern-Dialog).

Start:
    streamlit run modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py
"""

import streamlit as st
from notizen_app import formatiere_notiz

# Name, der beim Herunterladen vorgeschlagen wird
STANDARD_DATEINAME = "notizen.txt"


def lade_hochgeladene_datei() -> None:
    """
    Zeigt den Datei-Auswahl-Dialog und lädt die gewählte Datei.

    Streamlit führt das Skript bei jeder Interaktion neu aus. Damit eine
    hochgeladene Datei nur einmal verarbeitet wird, merken wir uns ihre ID
    im Session-State.
    """
    datei = st.file_uploader(
        "Notizen-Datei öffnen (Finder/Explorer)",
        type=["txt"],
        help="Klicke auf 'Browse files', um eine .txt-Datei auszuwählen.",
    )

    if datei is None:
        return

    # Datei nur einmal laden (nicht bei jedem erneuten Skript-Durchlauf)
    if st.session_state.get("geladene_datei_id") == datei.file_id:
        return

    try:
        inhalt = datei.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Die Datei konnte nicht gelesen werden (keine UTF-8-Textdatei).")
        return

    st.session_state["notizen_inhalt"] = inhalt
    st.session_state["geladene_datei_id"] = datei.file_id
    st.success(f"✓ Datei '{datei.name}' geladen.")


def neue_notiz_erfassen() -> None:
    """Zeigt das Eingabefeld und hängt eine neue Notiz an den Arbeitsstand an."""
    notiz = st.text_area("Neue Notiz", placeholder="Was möchtest du festhalten?")

    if st.button("Notiz hinzufügen"):
        if notiz.strip() == "":
            st.warning("✗ Leere Notiz wurde nicht gespeichert.")
        else:
            zeile = formatiere_notiz(notiz.strip())
            st.session_state["notizen_inhalt"] += zeile + "\n"
            st.success("✓ Notiz hinzugefügt")


def notizen_anzeigen() -> None:
    """Zeigt die aktuell erfassten Notizen an."""
    inhalt = st.session_state["notizen_inhalt"]

    if inhalt.strip() == "":
        st.info("Keine Notizen vorhanden.")
    else:
        st.text(inhalt)


def main() -> None:
    """Baut die Streamlit-Oberfläche auf."""
    st.title("📝 Notizen-App")
    st.write("Eine Web-Version der Notizen-App aus Modul 5.")

    # Arbeitsstand im Session-State initialisieren
    if "notizen_inhalt" not in st.session_state:
        st.session_state["notizen_inhalt"] = ""

    st.header("📂 Notizen-Datei öffnen")
    lade_hochgeladene_datei()

    st.header("✏️ Neue Notiz")
    neue_notiz_erfassen()

    st.header("📋 Meine Notizen")
    notizen_anzeigen()

    st.header("💾 Speichern")
    st.download_button(
        "Notizen herunterladen (Speichern unter …)",
        data=st.session_state["notizen_inhalt"],
        file_name=STANDARD_DATEINAME,
        mime="text/plain",
    )


if __name__ == "__main__":
    main()
