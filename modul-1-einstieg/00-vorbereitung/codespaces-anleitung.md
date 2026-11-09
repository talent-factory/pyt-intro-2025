# GitHub Codespaces Anleitung

**Zeitaufwand:** 10-15 Minuten  
**Schwierigkeit:** Einfach  
**Empfohlen für:** Anfänger, bei Installationsproblemen

## 🎯 Was ist GitHub Codespaces?

GitHub Codespaces ist eine **Cloud-basierte Entwicklungsumgebung**, die direkt in Ihrem Browser läuft.

**Vorteile:**

- ✅ Keine Installation notwendig
- ✅ Funktioniert auf jedem Computer mit Browser
- ✅ Alles ist bereits vorkonfiguriert
- ✅ Sofort einsatzbereit
- ✅ Kostenlos für Studenten (60 Stunden/Monat)

**Nachteile:**

- ❌ Benötigt Internetverbindung
- ❌ Monatliches Limit (aber ausreichend für den Kurs)

---

## 📋 Voraussetzungen

- GitHub-Account (kostenlos)
- Moderner Browser (Chrome, Firefox, Safari, Edge)
- Stabile Internetverbindung

---

## 1️⃣ GitHub-Account erstellen

Falls Sie noch keinen haben:

1. Besuchen Sie [github.com](https://github.com)
2. Klicken Sie auf "Sign up"
3. Folgen Sie den Anweisungen
4. Verifizieren Sie Ihre E-Mail-Adresse

---

## 2️⃣ Codespace erstellen

### Schritt 1: Repository öffnen

1. Gehen Sie zu: `https://github.com/talent-factory/pyt-intro-2025`
2. Klicken Sie auf den grünen **"Code"** Button
3. Wählen Sie den Tab **"Codespaces"**

### Schritt 2: Codespace starten

1. Klicken Sie auf **"Create codespace on main"**
2. Warten Sie 1-2 Minuten (beim ersten Mal etwas länger)
3. VS Code öffnet sich im Browser!

### Schritt 3: Umgebung ist bereit

Sie sehen jetzt:

- VS Code im Browser
- Alle Kursmaterialien im Explorer (links)
- Ein Terminal unten
- Python ist bereits installiert!

---

## 3️⃣ Codespace nutzen

### Python testen

1. Öffnen Sie das Terminal (unten)
2. Tippen Sie:

```bash
python --version
```

Sie sollten sehen: `Python 3.12.x`

### Python Shell starten

Im Terminal:

```bash
python
```

Testen Sie:

```python
>>> print("Hello from Codespaces!")
Hello from Codespaces!
>>> 2 + 2
4
>>> exit()
```

### Erste Python-Datei erstellen

1. Klicken Sie auf "New File" im Explorer
2. Nennen Sie sie `test.py`
3. Schreiben Sie:

   ```python
   print("Mein erstes Python-Programm!")
   ```

4. Speichern Sie mit `Ctrl+S` (Windows/Linux) oder `Cmd+S` (macOS)
5. Führen Sie aus:

   ```bash
   python test.py
   ```

---

## 4️⃣ Wichtige Funktionen

### Dateien bearbeiten

- **Explorer:** Linke Seitenleiste zeigt alle Dateien
- **Editor:** Mittlerer Bereich zum Schreiben
- **Terminal:** Unten für Befehle

### Speichern

- **Auto-Save:** Ist bereits aktiviert
- **Manuell:** `Ctrl+S` / `Cmd+S`

### Terminal

- **Neues Terminal:** `Terminal` → `New Terminal`
- **Mehrere Terminals:** Möglich!

### Extensions

Bereits installiert:

- Python
- Pylance
- Jupyter

---

## 5️⃣ Codespace verwalten

### Codespace stoppen

**Wichtig:** Codespaces verbrauchen Stunden, auch wenn Sie nichts tun!

**Stoppen:**

1. Klicken Sie auf Ihren Namen (unten links)
2. Wählen Sie "Stop Current Codespace"

**Oder:** Schliessen Sie einfach den Browser-Tab. Der Codespace stoppt nach 30 Min. Inaktivität automatisch.

### Codespace wieder starten

1. Gehen Sie zu [github.com/codespaces](https://github.com/codespaces)
2. Klicken Sie auf Ihren Codespace
3. Er startet in wenigen Sekunden

### Codespace löschen

Wenn Sie ihn nicht mehr brauchen:

1. Gehen Sie zu [github.com/codespaces](https://github.com/codespaces)
2. Klicken Sie auf "..." neben dem Codespace
3. Wählen Sie "Delete"

---

## 6️⃣ Tipps & Tricks

### Kostenlose Stunden

- **Kostenlos:** 60 Stunden/Monat für alle
- **Studenten:** 90 Stunden/Monat mit [GitHub Student Pack](https://education.github.com/pack)

### Stunden sparen

- ✅ Stoppen Sie den Codespace, wenn Sie fertig sind
- ✅ Löschen Sie alte Codespaces
- ✅ Nutzen Sie Auto-Stop (Standard: 30 Min.)

### Shortcuts

- `Ctrl+Shift+P` / `Cmd+Shift+P`: Command Palette
- `Ctrl+` ` / `Cmd+` `: Terminal öffnen/schliessen
- `Ctrl+B` / `Cmd+B`: Explorer ein/ausblenden

### Dateien hochladen

Drag & Drop funktioniert! Ziehen Sie Dateien in den Explorer.

---

## 🐛 Problemlösung

### Codespace startet nicht

**Lösung:**

1. Warten Sie 2-3 Minuten
2. Aktualisieren Sie die Seite
3. Versuchen Sie einen anderen Browser

### Python nicht gefunden

**Lösung:**

```bash
# Im Terminal
which python
python --version
```

Falls nicht gefunden, warten Sie noch etwas. Die Umgebung wird noch eingerichtet.

### Änderungen gehen verloren

**Lösung:**

- Codespaces speichern automatisch
- Aber: Löschen Sie den Codespace nicht, bevor Sie Ihre Arbeit gesichert haben!
- Nutzen Sie Git für wichtige Änderungen

---

## ✅ Checkliste

Nach dieser Anleitung sollten Sie:

- [ ] Einen GitHub-Account haben
- [ ] Einen Codespace erstellt haben
- [ ] Python im Terminal getestet haben
- [ ] Eine erste Python-Datei erstellt haben
- [ ] Wissen, wie man den Codespace stoppt

---

## 📚 Nächste Schritte

1. ✅ Lesen Sie den [Leseauftrag](./leseauftrag.md)
2. ✅ Arbeiten Sie [Erste Schritte](./erste-experimente.md) durch
3. ✅ Bereiten Sie sich auf den Präsenztag vor

---

## 💡 Warum Codespaces?

> "Ich hatte Probleme mit der Installation auf meinem alten Laptop. Mit Codespaces konnte ich sofort loslegen!" - Student, Kurs 2024

Codespaces ist perfekt für:

- Anfänger ohne Installationserfahrung
- Ältere Computer
- Verschiedene Geräte (Laptop, Tablet)
- Schnellen Einstieg

---

**Viel Erfolg mit Codespaces!**
Bei Fragen: Notieren Sie sie für den Präsenztag.
