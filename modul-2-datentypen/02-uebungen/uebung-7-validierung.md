# Übung 7: Input-Validierung

**Dauer:** 15 Minuten  
**Schwierigkeit:** ⭐⭐⭐ Schwer  
**Lektion:** 5 (Vertiefung)


*Lektion:** 5 (Vertiefung)
 Schwer  
ebung-7-validierung.md << 'EOF'
dresse
- Prüfe: @ vorhanden, . nach @, nicht leer

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

- [ ] @ vorhanden
- [ ] . nach @ vorhanden
- [ ] Nicht leer
- [ ] Fehlerme ldungen klar
