# Übung 3: Altersrechner

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐ Mittel  
**Lektion:** 3 - VS Code

## 🎯 Lernziele

- Python-Datei in VS Code erstellen
- Code schreiben und ausführen
- Variablen sinnvoll benennen

## 📝 Aufgaben

### Teil 1: Datei erstellen (3 Min.)

1. Öffnen Sie VS Code
2. Erstellen Sie neue Datei: `altersrechner.py`
3. Speichern Sie im Ordner `python-kurs`

### Teil 2: Einfacher Altersrechner (7 Min.)

Schreiben Sie:

```python
# Altersrechner
# Berechnet das Alter basierend auf Geburtsjahr

geburtsjahr = 2000
aktuelles_jahr = 2025

alter = aktuelles_jahr - geburtsjahr

print(f"Geburtsjahr: {geburtsjahr}")
print(f"Aktuelles Jahr: {aktuelles_jahr}")
print(f"Alter: {alter} Jahre")
```

4. Speichern Sie (`Ctrl+S` / `Cmd+S`)
5. Führen Sie aus (▶️ Button oder Terminal)

### Teil 3: Erweitern (5 Min.)

Fügen Sie hinzu:

```python
# Alter in Monaten
alter_monate = alter * 12
print(f"Das sind {alter_monate} Monate")

# Alter in Tagen (ungefähr)
alter_tage = alter * 365
print(f"Das sind ungefähr {alter_tage} Tage")

# Bis zum nächsten runden Geburtstag
naechster_runder = ((alter // 10) + 1) * 10
jahre_bis_rund = naechster_runder - alter
print(f"Bis zum {naechster_runder}. Geburtstag: {jahre_bis_rund} Jahre")
```

## ✅ Erfolgskriterien

- [ ] Datei `altersrechner.py` erstellt
- [ ] Code geschrieben
- [ ] Programm ausgeführt
- [ ] Erweiterungen hinzugefügt
- [ ] Verschiedene Geburtsjahre getestet

## 🚀 Erweiterungen

- Berechnen Sie Alter in Stunden
- Berechnen Sie Alter in Sekunden
- Fügen Sie mehr Kommentare hinzu
- Testen Sie mit verschiedenen Jahren

## 💡 Tipps

- `//` für Ganzzahldivision
- Kommentare mit `#` beginnen
- Aussagekräftige Variablennamen verwenden
- Code formatieren für bessere Lesbarkeit

## 🐛 Häufige Fehler

**Fehler:** Datei nicht gefunden  
**Lösung:** Prüfen Sie den Speicherort

**Fehler:** Syntax Error  
**Lösung:** Klammern und Anführungszeichen prüfen

