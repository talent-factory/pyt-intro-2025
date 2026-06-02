# Design: Streamlit-Notizen-App

**Datum:** 2026-06-02
**Autor:** Daniel Senften (mit KI-Assistenz)
**Modul:** modul-5-dateien-module / 05-beispiele

## Ziel

Eine neue Notizen-App auf Basis von Streamlit, die auf der bestehenden
Konsolen-App `notizen_app.py` aufbaut und deren Kern-Logik wiederverwendet.
Der Benutzer wählt die zu lesenden/schreibenden Notizen-Dateien über einen
Datei-Dialog (Finder/Explorer) aus – nicht durch Eintippen eines Pfades.

## Entscheidungen (aus dem Brainstorming)

1. **Datei-Auswahl:** Streamlit-native Widgets statt nativem `tkinter`-Dialog.
   Grund: portabel (läuft auch in GitHub Codespaces), keine
   Server-/Client-Einschränkung von `tkinter.filedialog`.
2. **Datei-Modell:** Upload + Download.
   - `st.file_uploader` → Button „Browse files" öffnet den **Finder/Explorer**
     zum Auswählen einer `.txt`-Datei (= der gewünschte Öffnen-Dialog).
   - `st.download_button` → Browser öffnet den **„Speichern unter"-Dialog**
     (Finder/Explorer), wo Name und Ort gewählt werden.
3. **Architektur:** Kern-Logik teilen (Ansatz A). Reine, I/O-freie Funktionen
   werden aus `notizen_app.py` extrahiert; beide Apps nutzen dieselbe Funktion.
4. **Tests:** Ein Mini-Test für die extrahierte Kern-Funktion wird mitgeliefert
   (passend zum Projektziel „Tests erweitern"; Modul 5 hat bereits Tests).

## Dateien & Änderungen

| Datei | Änderung |
|-------|----------|
| `modul-5-dateien-module/05-beispiele/notizen_app.py` | **Refactor:** Kern-Funktion `formatiere_notiz()` extrahieren; `neue_notiz()` nutzt sie. Konsolen-App bleibt voll funktionsfähig. |
| `modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py` | **Neu:** Streamlit-App, importiert `formatiere_notiz` aus `notizen_app`. |
| `tests/modul-5/test_notizen_app.py` | **Neu:** Mini-Test für `formatiere_notiz()`. |
| `modul-5-dateien-module/05-beispiele/README.md` | Neue App + Startbefehl dokumentieren. |

`pyproject.toml` bleibt unverändert – `streamlit>=1.58.0` ist bereits als
Abhängigkeit vorhanden.

## Geteilte Kern-Logik (`notizen_app.py`)

```python
def formatiere_notiz(notiz: str, zeitpunkt: datetime | None = None) -> str:
    """
    Erzeugt eine Notiz-Zeile mit Zeitstempel.

    Args:
        notiz: Der Notiztext.
        zeitpunkt: Zeitstempel; Standard ist die aktuelle Zeit.

    Returns:
        Formatierte Zeile, z. B. '[2026-06-02 14:30] Einkaufen gehen'.
    """
    if zeitpunkt is None:
        zeitpunkt = datetime.now()
    zeit = zeitpunkt.strftime("%Y-%m-%d %H:%M")
    return f"[{zeit}] {notiz}"
```

`neue_notiz()` ersetzt seine Inline-Formatierung durch
`datei.write(formatiere_notiz(notiz) + "\n")`. Verhalten unverändert.

## Streamlit-Komponenten & Datenfluss

- **Zustand:** `st.session_state["notizen_inhalt"]` – ein String im selben
  Format wie `notizen.txt` (aktuell geladene und neu erfasste Notizen).
  `st.session_state["geladene_datei_id"]` merkt sich die zuletzt geladene
  Datei, damit der Upload nur einmal verarbeitet wird (Streamlit führt das
  Skript bei jeder Interaktion erneut aus).

- **📂 Notizen-Datei öffnen:** `st.file_uploader(type=["txt"])`. Beim Auswählen
  einer Datei wird ihr Inhalt UTF-8-dekodiert und in `notizen_inhalt` geladen
  (ersetzt den aktuellen Stand). Hinweis-Meldung nach erfolgreichem Laden.

- **✏️ Neue Notiz:** `st.text_area` + `st.button("Notiz hinzufügen")`. Beim
  Klick wird der Text via `formatiere_notiz()` formatiert und an
  `notizen_inhalt` angehängt.

- **📋 Meine Notizen:** Anzeige des aktuellen `notizen_inhalt`. Ist nichts
  vorhanden → `st.info("Keine Notizen vorhanden.")`.

- **💾 Speichern:** `st.download_button(data=notizen_inhalt,
  file_name="notizen.txt", mime="text/plain")` → Browser-Speichern-Dialog.

## Fehlerbehandlung

- **Leere Notiz:** `notiz.strip() == ""` → `st.warning`, nicht hinzufügen
  (spiegelt den `strip()`-Check der Konsolen-App).
- **Upload-/Dekodier-Fehler:** `try/except` um `decode("utf-8")` → `st.error`
  mit verständlicher Meldung.
- **Keine Notizen:** freundlicher `st.info`-Hinweis statt Fehler
  (spiegelt das `FileNotFoundError`-Verhalten von `zeige_notizen()`).

## Tests

`tests/modul-5/test_notizen_app.py` mit `@pytest.mark.modul5`:

- Import von `notizen_app` funktioniert.
- `formatiere_notiz("Text", datetime(2026, 6, 2, 14, 30))` liefert exakt
  `"[2026-06-02 14:30] Text"`.
- `formatiere_notiz` ohne Zeitstempel liefert eine Zeile, die mit `"["`
  beginnt und den Text enthält.

## Ausführen

```bash
streamlit run modul-5-dateien-module/05-beispiele/notizen_app_streamlit.py
```

Konsolen-App weiterhin:

```bash
python modul-5-dateien-module/05-beispiele/notizen_app.py
```

## Didaktischer Wert

Zeigt Anfängern die **Trennung von Logik und Oberfläche**: dieselbe reine
Funktion `formatiere_notiz()` versorgt sowohl eine Konsolen- als auch eine
Web-Oberfläche. Deutsche Namen, Docstrings und ausführliche Kommentare gemäss
Projekt-Richtlinien.
