# Übung 4: KI-gestützt programmieren

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐⭐ Mittel

## 📝 Aufgabe

Entwickeln Sie mit Hilfe von Claude Code einen **Passwort-Generator**. Dokumentieren Sie dabei jeden Schritt des Prozesses.

### Anforderungen an den Passwort-Generator

- Länge des Passworts wählbar (Benutzereingabe)
- Grossbuchstaben und Kleinbuchstaben enthalten
- Ziffern enthalten
- Optional: Sonderzeichen (!, @, #, $, %, etc.)
- Mindestens ein Zeichen jeder gewählten Kategorie

### Schritt 1: Ersten Prompt formulieren

Formulieren Sie einen klaren Prompt für Claude Code. Beschreiben Sie alle Anforderungen.

### Schritt 2: Code generieren lassen

Lassen Sie Claude Code den Code generieren und prüfen Sie das Ergebnis.

### Schritt 3: Iterativ verbessern

Falls der Code nicht perfekt ist, stellen Sie Nachfragen:

```
Kannst du eine Funktion hinzufügen, die die Passwortstärke bewertet?
Füge bitte Fehlerbehandlung für ungültige Eingaben hinzu.
```

### Schritt 4: Prozess dokumentieren

Füllen Sie für jeden Schritt diese Vorlage aus:

| Schritt | Prompt | Antwort (Zusammenfassung) | Bewertung |
|---------|--------|--------------------------|-----------|
| 1 | "Erstelle einen Passwort-Generator..." | Code mit Grundfunktion | Gut / Anpassung nötig |
| 2 | "Füge Sonderzeichen hinzu..." | Erweiterte Version | ... |
| 3 | ... | ... | ... |

## 💡 Beispiel-Ausgabe

```
Passwort-Generator
==================
Gewünschte Länge: 12
Sonderzeichen einschliessen? (ja/nein): ja

Generiertes Passwort: Kx7#mP2$nQ9w
Passwortstärke: Stark
```

## ✅ Checkliste

- [ ] Prompt formuliert und an Claude Code gegeben
- [ ] Generierten Code getestet
- [ ] Mindestens eine Verbesserungsrunde durchgeführt
- [ ] Jeden Schritt dokumentiert (Prompt → Antwort → Bewertung)
- [ ] Fertiges Programm funktioniert
