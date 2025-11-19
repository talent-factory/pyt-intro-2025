# Installationsanleitung: Lokale Entwicklungsumgebung

**Zeitaufwand:** 30-60 Minuten  
**Schwierigkeit:** Mittel

> **💡 Tipp:** Wenn Sie unsicher sind oder Probleme haben, nutzen Sie stattdessen [GitHub Codespaces](./codespaces-anleitung.md). Das ist einfacher und funktioniert im Browser.

## 🎯 Was werden wir installieren?

1. **Python** - Die Programmiersprache
2. **VS Code** - Der Code-Editor
3. **Git** - Versionskontrolle
4. **uv** - Package Manager (optional)

## 📋 Voraussetzungen

- Windows 10/11, macOS 10.15+ oder Linux
- Mindestens 4 GB RAM (8 GB empfohlen)
- 2 GB freier Festplattenspeicher
- Administratorrechte auf Ihrem Computer

---

## 1️⃣ Python installieren

### Windows

1. Besuchen Sie [python.org/downloads](https://www.python.org/downloads/)
2. Laden Sie **Python 3.12** oder höher herunter
3. **Wichtig:** Aktivieren Sie "Add Python to PATH" beim Installieren!
4. Klicken Sie auf "Install Now"

**Überprüfung:**

```bash
python --version
```

Sollte ausgeben: `Python 3.12.x` oder höher

### macOS

**Option A: Mit Homebrew (empfohlen)**

```bash
# Homebrew installieren (falls noch nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python installieren
brew install python@3.12
```

**Option B: Von python.org**

1. Besuchen Sie [python.org/downloads](https://www.python.org/downloads/)
2. Laden Sie den macOS Installer herunter
3. Führen Sie den Installer aus

**Überprüfung:**

```bash
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.12 python3-pip python3-venv
```

**Überprüfung:**

```bash
python3 --version
```

---

## 2️⃣ VS Code installieren

### Alle Betriebssysteme

1. Besuchen Sie [code.visualstudio.com](https://code.visualstudio.com/)
2. Laden Sie die Version für Ihr Betriebssystem herunter
3. Installieren Sie VS Code

### Wichtige Extensions installieren

Nach der Installation von VS Code:

1. Öffnen Sie VS Code
2. Klicken Sie auf das Extensions-Symbol (linke Seitenleiste)
3. Installieren Sie folgende Extensions:
   - **Python** (von Microsoft)
   - **Pylance** (von Microsoft)
   - **Jupyter** (von Microsoft)

**Oder per Kommandozeile:**

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
```

---

## 3️⃣ Git installieren

### Windows

1. Besuchen Sie [git-scm.com](https://git-scm.com/)
2. Laden Sie Git für Windows herunter
3. Installieren Sie mit Standardeinstellungen

### macOS

```bash
# Mit Homebrew
brew install git

# Oder: Xcode Command Line Tools
xcode-select --install
```

### Linux

```bash
sudo apt install git
```

**Überprüfung:**

```bash
git --version
```

**Git konfigurieren:**

```bash
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
```

---

## 4️⃣ uv installieren (optional)

**uv** ist ein moderner Python Package Manager.

### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Überprüfung:**

```bash
uv --version
```

---

## ✅ Alles testen

### 1. Python testen

Öffnen Sie ein Terminal/Kommandozeile:

```bash
python --version  # Windows
python3 --version # macOS/Linux
```

### 2. Python Shell starten

```bash
python  # Windows
python3 # macOS/Linux
```

Sie sollten den Python-Prompt sehen:

```python
>>>
```

Testen Sie:

```python
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 2
4
>>> exit()
```

### 3. VS Code testen

1. Öffnen Sie VS Code
2. Erstellen Sie eine neue Datei: `test.py`
3. Schreiben Sie:

```python
print("VS Code funktioniert!")
```

4. Speichern Sie die Datei
5. Klicken Sie auf den "Run"-Button (▶️) oben rechts

---

## 🐛 Problemlösung

### Python nicht im PATH (Windows)

**Symptom:** `python` Befehl nicht gefunden

**Lösung:**

1. Python erneut installieren
2. "Add Python to PATH" aktivieren
3. Oder manuell zum PATH hinzufügen

### VS Code findet Python nicht

**Lösung:**

1. Öffnen Sie VS Code
2. Drücken Sie `Ctrl+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (macOS)
3. Tippen Sie "Python: Select Interpreter"
4. Wählen Sie Ihre Python-Installation

### Permission Denied (macOS/Linux)

**Lösung:**

```bash
sudo chown -R $(whoami) /usr/local/bin
```

---

## 📚 Nächste Schritte

Nach erfolgreicher Installation:

1. ✅ Lesen Sie den [Leseauftrag](./leseauftrag.md)
2. ✅ Arbeiten Sie [Erste Schritte](./erste-schritte.md) durch
3. ✅ Bereiten Sie sich auf den Präsenztag vor

---

## 💡 Alternative: GitHub Codespaces

Wenn die Installation Probleme macht:

👉 **[Nutzen Sie GitHub Codespaces](./codespaces-anleitung.md)**

- Keine Installation nötig
- Funktioniert im Browser
- Sofort einsatzbereit

---

**Bei Problemen:** Notieren Sie Ihre Fragen für den Präsenztag!

