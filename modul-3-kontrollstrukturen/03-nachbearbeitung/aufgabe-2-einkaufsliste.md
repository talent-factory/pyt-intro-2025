# Aufgabe 2: Einkaufsliste

**Zeitaufwand:** 1.5 Stunden  
**Schwierigkeit:** ⭐⭐ Mittel

## 🎯 Ziel

Erstellen Sie einen Einkaufslisten-Manager mit Menü-System.

## 📝 Anforderungen

### Basis-Features (Pflicht)

1. **Menü anzeigen:**
   ```
   === EINKAUFSLISTE ===
   1. Artikel hinzufügen
   2. Liste anzeigen
   3. Artikel löschen
   4. Liste leeren
   5. Beenden
   ```

2. **Artikel hinzufügen**
   - Eingabe: Artikelname
   - Zur Liste hinzufügen

3. **Liste anzeigen**
   - Nummeriert ausgeben
   - Anzahl Artikel zeigen

4. **Artikel löschen**
   - Nach Nummer
   - Fehlerbehandlung

5. **Liste leeren**
   - Sicherheitsabfrage

### Erweiterte Features (Optional)

6. **Mengen:**
   - "2x Milch"
   - "500g Mehl"

7. **Kategorien:**
   - Lebensmittel
   - Haushalt
   - Sonstiges

8. **Speichern/Laden:**
   - In Datei speichern
   - Beim Start laden

## 💡 Beispiel-Ablauf

```
=== EINKAUFSLISTE ===

1. Artikel hinzufügen
2. Liste anzeigen
3. Artikel löschen
4. Liste leeren
5. Beenden

Wahl: 1
Artikel: Milch
✓ Milch hinzugefügt

Wahl: 1
Artikel: Brot
✓ Brot hinzugefügt

Wahl: 2

=== IHRE EINKAUFSLISTE ===
1. Milch
2. Brot
Gesamt: 2 Artikel

Wahl: 3
Welchen Artikel löschen? (Nummer): 1
✓ Milch gelöscht

Wahl: 2

=== IHRE EINKAUFSLISTE ===
1. Brot
Gesamt: 1 Artikel

Wahl: 5
Auf Wiedersehen! 👋
```

## ✅ Checkliste

### Basis
- [ ] Menü-System funktioniert
- [ ] Artikel hinzufügen
- [ ] Liste anzeigen
- [ ] Artikel löschen
- [ ] Liste leeren
- [ ] Beenden

### Erweitert
- [ ] Mengen unterstützt
- [ ] Kategorien
- [ ] Speichern/Laden
- [ ] Fehlerbehandlung
- [ ] Schöne Formatierung

## 🎯 Lernziele

- While-Schleife für Menü
- If-elif-else für Auswahl
- Listen manipulieren (append, remove, clear)
- For-Schleife für Ausgabe
- Input-Validierung

## 💻 Hilfe

### Menü-Schleife

```python
einkaufsliste = []

while True:
    print("\n=== EINKAUFSLISTE ===")
    print("1. Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Artikel löschen")
    print("4. Liste leeren")
    print("5. Beenden")
    
    wahl = input("\nWahl: ")
    
    if wahl == "1":
        # Hinzufügen
        pass
    elif wahl == "2":
        # Anzeigen
        pass
    # ...
    elif wahl == "5":
        break
```

### Liste anzeigen

```python
if len(einkaufsliste) == 0:
    print("Liste ist leer")
else:
    print("\n=== IHRE EINKAUFSLISTE ===")
    for i, artikel in enumerate(einkaufsliste, start=1):
        print(f"{i}. {artikel}")
    print(f"Gesamt: {len(einkaufsliste)} Artikel")
```

### Artikel löschen

```python
try:
    nummer = int(input("Nummer: "))
    if 1 <= nummer <= len(einkaufsliste):
        artikel = einkaufsliste.pop(nummer - 1)
        print(f"✓ {artikel} gelöscht")
    else:
        print("Ungültige Nummer!")
except ValueError:
    print("Bitte eine Zahl eingeben!")
```

## 📦 Abgabe

**Datei:** `einkaufsliste.py`

**Testen Sie:**
- Alle Menüpunkte
- Leere Liste
- Ungültige Eingaben
- Löschen von Artikeln

## 🌟 Bonus-Ideen

- Artikel als erledigt markieren (✓)
- Sortieren (alphabetisch)
- Suchen
- Export als Text-Datei

## 🔗 Weiter

[Aufgabe 3: Primzahlen-Finder](./aufgabe-3-primzahlen.md)

