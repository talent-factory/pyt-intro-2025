# Übung 7: Input-Validierung

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐⭐ Schwer  
**Status:** Vertiefung (zu Hause)

## 📝 Aufgabe

Schreiben Sie ein Programm `email_pruefung.py`, das eine E-Mail-Adresse einliest und prüft, ob sie plausibel ist.

- Die Eingabe darf nicht leer sein
- Die Adresse muss genau ein `@` enthalten
- Nach dem `@` muss ein `.` vorkommen
- Die Adresse darf keine Leerzeichen enthalten
- Gibt die Prüfung einen Fehler, nennen Sie den Grund

## 💡 Beispiel

```
E-Mail: test@example.com
✓ Gültige E-Mail

E-Mail: test.example.com
✗ Fehlt @

E-Mail: test@
✗ Fehlt Domain
```

## ✅ Checkliste

- [ ] Leere Eingabe wird abgefangen
- [ ] Genau ein `@` wird geprüft
- [ ] Ein `.` nach dem `@` wird geprüft
- [ ] Leerzeichen werden erkannt
- [ ] Fehlermeldungen sind klar formuliert
