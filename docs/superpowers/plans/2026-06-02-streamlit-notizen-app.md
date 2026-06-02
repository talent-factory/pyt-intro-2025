# Streamlit-Notizen-App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eine Streamlit-Web-App für Notizen, die die Kern-Logik der bestehenden Konsolen-App `notizen_app.py` wiederverwendet und Notizen-Dateien über den Browser-Datei-Dialog (Finder/Explorer) öffnet und speichert.

**Architecture:** Die reine Formatierungs-Logik wird als I/O-freie Funktion `formatiere_notiz()` aus `notizen_app.py` extrahiert. Die Konsolen-App nutzt sie weiter; die neue Streamlit-App importiert dieselbe Funktion. Datei-Öffnen via `st.file_uploader`, Speichern via `st.download_button`; der Arbeitsstand liegt in `st.session_state`.

**Tech Stack:** Python 3.11+, Streamlit (>=1.58.0, bereits in pyproject.toml), pytest (Modul-5-Tests mit Marker `@pytest.mark.modul5`).

---

## File Structure

- `modul-5-dateien-module/05-beispiele/notizen_app.py` — **Modify.** Neue reine Funktion `formatiere_notiz()`; `neue_notiz()` ruft sie auf. Konsolen-App unverändert nutzbar.
- `modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py` — **Create.** Streamlit-Oberfläche, importiert `formatiere_notiz`.
- `tests/modul-5/test_notizen_app.py` — **Create.** Tests für `formatiere_notiz()`.
- `modul-5-dateien-module/05-beispiele/README.md` — **Modify.** Eintrag + Startbefehl für die Streamlit-App.

---

## Task 1: Kern-Funktion `formatiere_notiz()` extrahieren (TDD)

**Files:**
- Test: `tests/modul-5/test_notizen_app.py`
- Modify: `modul-5-dateien-module/05-beispiele/notizen_app.py`

- [ ] **Step 1: Schreibe die fehlschlagenden Tests**

Erstelle `tests/modul-5/test_notizen_app.py`:

```python
"""
Tests für notizen_app.py
Testet die reine Formatierungs-Logik der Notizen-App.
"""

import sys
from datetime import datetime
from pathlib import Path

import pytest

# Modul importieren
modul_pfad = (
    Path(__file__).parent.parent.parent / "modul-5-dateien-module" / "05-beispiele"
)
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul5
def test_modul_kann_importiert_werden() -> None:
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import notizen_app

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul5
def test_formatiere_notiz_mit_zeitpunkt() -> None:
    """Test: formatiere_notiz() erzeugt korrekte Zeile mit gegebenem Zeitpunkt."""
    import notizen_app

    zeitpunkt = datetime(2026, 6, 2, 14, 30)
    ergebnis = notizen_app.formatiere_notiz("Einkaufen gehen", zeitpunkt)

    assert ergebnis == "[2026-06-02 14:30] Einkaufen gehen"


@pytest.mark.modul5
def test_formatiere_notiz_ohne_zeitpunkt() -> None:
    """Test: formatiere_notiz() ohne Zeitpunkt nutzt aktuelle Zeit und enthält Text."""
    import notizen_app

    ergebnis = notizen_app.formatiere_notiz("Test")

    assert ergebnis.startswith("[")
    assert ergebnis.endswith("Test")
    assert "] " in ergebnis
```

- [ ] **Step 2: Tests ausführen und Fehlschlag prüfen**

Run: `uv run pytest tests/modul-5/test_notizen_app.py -v`
Expected: `test_formatiere_notiz_*` FAIL mit `AttributeError: module 'notizen_app' has no attribute 'formatiere_notiz'`

- [ ] **Step 3: Funktion `formatiere_notiz()` in `notizen_app.py` ergänzen**

In `modul-5-dateien-module/05-beispiele/notizen_app.py` direkt **nach** der Zeile `NOTIZEN_DATEI = "notizen.txt"` (Zeile 19) und der folgenden Leerzeile diese Funktion einfügen:

```python
def formatiere_notiz(notiz: str, zeitpunkt: datetime | None = None) -> str:
    """
    Erzeugt eine Notiz-Zeile mit Zeitstempel.

    Diese reine Funktion enthält keine Ein-/Ausgabe und kann darum sowohl
    von der Konsolen-App als auch von der Streamlit-App genutzt werden.

    Args:
        notiz: Der Notiztext.
        zeitpunkt: Zeitstempel der Notiz. Standard ist die aktuelle Zeit.

    Returns:
        Formatierte Zeile, z. B. '[2026-06-02 14:30] Einkaufen gehen'.
    """
    if zeitpunkt is None:
        zeitpunkt = datetime.now()
    zeit = zeitpunkt.strftime("%Y-%m-%d %H:%M")
    return f"[{zeit}] {notiz}"
```

- [ ] **Step 4: `neue_notiz()` auf die neue Funktion umstellen**

In `modul-5-dateien-module/05-beispiele/notizen_app.py` den `with`-Block in `neue_notiz()` (aktuell Zeilen 38-40) ersetzen.

Vorher:

```python
    # Datei im Anhänge-Modus 'a' öffnen
    with open(NOTIZEN_DATEI, "a", encoding="utf-8") as datei:
        zeit = datetime.now().strftime("%Y-%m-%d %H:%M")
        datei.write(f"[{zeit}] {notiz}\n")
```

Nachher:

```python
    # Datei im Anhänge-Modus 'a' öffnen
    with open(NOTIZEN_DATEI, "a", encoding="utf-8") as datei:
        datei.write(formatiere_notiz(notiz) + "\n")
```

- [ ] **Step 5: Tests ausführen und Erfolg prüfen**

Run: `uv run pytest tests/modul-5/test_notizen_app.py -v`
Expected: 3 Tests PASS

- [ ] **Step 6: Konsolen-App-Verhalten sicherstellen (ruff)**

Run: `uv run ruff check modul-5-dateien-module/05-beispiele/notizen_app.py`
Expected: keine Fehler (All checks passed)

- [ ] **Step 7: Commit**

```bash
git add tests/modul-5/test_notizen_app.py modul-5-dateien-module/05-beispiele/notizen_app.py
git commit -m "$(cat <<'EOF'
♻️ refactor: Extrahiere formatiere_notiz() aus notizen_app

- Reine, I/O-freie Funktion für Wiederverwendung
- neue_notiz() nutzt jetzt formatiere_notiz()
- Tests für formatiere_notiz() ergänzt

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Streamlit-App `notizen_app_streamlit.py` erstellen

**Files:**
- Create: `modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py`

- [ ] **Step 1: Streamlit-App schreiben**

Erstelle `modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py` mit exakt diesem Inhalt:

```python
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
```

- [ ] **Step 2: Import-Smoke-Test (ohne Streamlit-Server)**

Run: `uv run python -c "import sys; sys.path.insert(0, 'modul-5-dateien-module/05-beispiele'); import notizen_app_streamlit; print('OK', notizen_app_streamlit.STANDARD_DATEINAME)"`
Expected: Ausgabe `OK notizen.txt` ohne Traceback (prüft, dass Importe und `formatiere_notiz`-Import auflösen).

- [ ] **Step 3: ruff-Prüfung**

Run: `uv run ruff check modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py`
Expected: All checks passed

- [ ] **Step 4: Streamlit-App manuell starten und prüfen**

Run: `uv run streamlit run modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py`
Expected: Server startet, Browser öffnet die App. Manuell prüfen:
1. „Browse files" öffnet den Finder/Explorer.
2. Eine Notiz hinzufügen → erscheint unter „Meine Notizen" mit Zeitstempel.
3. „Notizen herunterladen" bietet `notizen.txt` zum Speichern an.
Danach Server mit `Ctrl+C` beenden.

- [ ] **Step 5: Commit**

```bash
git add modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py
git commit -m "$(cat <<'EOF'
🎉 feat: Füge Streamlit-Notizen-App hinzu

- Datei öffnen via file_uploader (Finder/Explorer)
- Speichern via download_button
- Nutzt geteilte Funktion formatiere_notiz() aus notizen_app

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: README dokumentieren

**Files:**
- Modify: `modul-5-dateien-module/05-beispiele/README.md`

- [ ] **Step 1: Eintrag für die neue App ergänzen**

In `modul-5-dateien-module/05-beispiele/README.md` nach der Zeile für `notizen_app.py` (aktuell Punkt 11, Zeile 33) diese Zeile einfügen:

```markdown
12. **[notizen_app_streamlit.py](./notizen_app_streamlit.py)** - Notizen-App mit Streamlit-Oberfläche (öffnen/speichern via Finder/Explorer)
```

- [ ] **Step 2: Startbefehl im Abschnitt „🚀 Verwendung" ergänzen**

Im Abschnitt „🚀 Verwendung" nach dem bestehenden Code-Block diese Zeilen anfügen:

```markdown

Die Streamlit-App wird so gestartet:

```bash
streamlit run notizen_app_streamlit.py
```
```

- [ ] **Step 3: Commit**

```bash
git add modul-5-dateien-module/05-beispiele/README.md
git commit -m "$(cat <<'EOF'
📚 docs: Dokumentiere Streamlit-Notizen-App in Modul-5-README

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Self-Review-Ergebnis

- **Spec-Abdeckung:** Datei-Auswahl (Task 2, file_uploader), Speichern (Task 2, download_button), geteilte Kern-Logik (Task 1, formatiere_notiz), Tests (Task 1), README (Task 3) — alle Spec-Punkte abgedeckt.
- **Platzhalter:** keine.
- **Typ-/Namens-Konsistenz:** `formatiere_notiz` und `notizen_inhalt` durchgängig gleich benannt; `file_id`/`getvalue()` sind Streamlit-`UploadedFile`-API.
- **Hinweis:** `README.md` ist bereits als geändert markiert (`M`) und `notizen.txt`/`notizen_app.py` sind noch untracked — bei den Commits in Task 1/3 nur die genannten Pfade stagen (kein `git add -A`).
```
