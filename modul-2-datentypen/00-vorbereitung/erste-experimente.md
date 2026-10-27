# Erste Experimente mit Strings und Datentypen

**Zeitaufwand:** 45-60 Minuten

## 🎯 Ziel

Experimentieren Sie mit Strings, Booleans und Typkonvertierung in der Python Shell, um ein Gefühl für diese Datentypen zu bekommen.

## 🚀 Vorbereitung

1. Öffnen Sie VS Code oder GitHub Codespaces
2. Öffnen Sie ein Terminal
3. Starten Sie die Python Shell mit `python` oder `python3`
4. Sie sollten den Prompt `>>>` sehen

## 📝 Experiment 1: String-Grundlagen (10 Min)

Probieren Sie folgende Befehle aus und beobachten Sie die Ausgabe:

```python
# Strings erstellen
name = "Anna"
stadt = 'Zürich'
print(name)
print(stadt)

# Strings verketten
volltext = name + " wohnt in " + stadt
print(volltext)

# String-Multiplikation
linie = "=" * 30
print(linie)

# String-Länge
print(len(name))
print(len(volltext))
```

**Aufgaben:**

1. Erstellen Sie einen String mit Ihrem Namen
2. Erstellen Sie einen String mit Ihrer Stadt
3. Verketten Sie beide zu einem Satz
4. Erstellen Sie eine Linie aus 50 Sternen (`*`)

## 📝 Experiment 2: String-Indexierung (10 Min)

```python
wort = "Python"

# Einzelne Zeichen
print(wort[0])   # Erstes Zeichen
print(wort[1])   # Zweites Zeichen
print(wort[-1])  # Letztes Zeichen
print(wort[-2])  # Vorletztes Zeichen

# Slicing
print(wort[0:3])   # Erste 3 Zeichen
print(wort[2:])    # Ab 3. Zeichen
print(wort[:4])    # Erste 4 Zeichen
print(wort[::2])   # Jedes 2. Zeichen
```

**Aufgaben:**

1. Extrahieren Sie die ersten 3 Buchstaben Ihres Namens
2. Extrahieren Sie die letzten 2 Buchstaben
3. Extrahieren Sie jedes zweite Zeichen

## 📝 Experiment 3: String-Methoden (15 Min)

```python
text = "  Hallo Welt  "

# Gross-/Kleinschreibung
print(text.upper())
print(text.lower())
print(text.title())  # Jedes Wort gross

# Leerzeichen entfernen
print(text.strip())   # Beide Seiten
print(text.lstrip())  # Links
print(text.rstrip())  # Rechts

# Ersetzen
print(text.replace("Hallo", "Hi"))
print(text.replace(" ", "_"))

# Prüfen
print(text.startswith("  Hallo"))
print(text.endswith("Welt  "))
print("Welt" in text)  # Enthält?

# Aufteilen
woerter = text.split()
print(woerter)
```

**Aufgaben:**

1. Erstellen Sie einen String mit Leerzeichen am Anfang und Ende
2. Entfernen Sie die Leerzeichen
3. Wandeln Sie den Text in Grossbuchstaben um
4. Ersetzen Sie ein Wort durch ein anderes

## 📝 Experiment 4: F-Strings (10 Min)

```python
name = "Max"
alter = 25
groesse = 1.75

# Einfache F-Strings
print(f"Ich heisse {name}")
print(f"Ich bin {alter} Jahre alt")
print(f"Ich bin {groesse} Meter gross")

# Mit Berechnungen
print(f"Nächstes Jahr bin ich {alter + 1}")
print(f"In 10 Jahren bin ich {alter + 10}")

# Formatierung
preis = 19.99
print(f"Preis: {preis:.2f} CHF")  # 2 Dezimalstellen
print(f"Preis: {preis:>10.2f} CHF")  # Rechtsbündig, 10 Zeichen

# Mehrere Variablen
print(f"{name} ist {alter} Jahre alt und {groesse}m gross")
```

**Aufgaben:**

1. Erstellen Sie Variablen für Name, Alter und Wohnort
2. Geben Sie einen Satz mit allen drei Variablen aus
3. Berechnen Sie Ihr Alter in 5 Jahren und geben Sie es aus

## 📝 Experiment 5: Boolesche Werte (10 Min)

```python
# Vergleiche
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(3 < 5)    # True
print(5 >= 5)   # True
print(3 <= 5)   # True

# Mit Variablen
alter = 18
print(alter >= 18)  # Volljährig?

temperatur = 25
print(temperatur > 30)  # Heiss?

# Logische Operatoren
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Kombiniert
alter = 25
hat_fuehrerschein = True
print(alter >= 18 and hat_fuehrerschein)
```

**Aufgaben:**

1. Prüfen Sie, ob 10 grösser als 5 ist
2. Prüfen Sie, ob 10 gleich 10 ist
3. Kombinieren Sie zwei Bedingungen mit `and`
4. Negieren Sie eine Bedingung mit `not`

## 📝 Experiment 6: Typkonvertierung (10 Min)

```python
# Typ ermitteln
print(type(42))
print(type(3.14))
print(type("Hallo"))
print(type(True))

# String zu Zahl
alter_str = "25"
alter_int = int(alter_str)
print(alter_int + 5)  # 30

preis_str = "19.99"
preis_float = float(preis_str)
print(preis_float * 2)  # 39.98

# Zahl zu String
zahl = 42
text = str(zahl)
print("Die Antwort ist " + text)

# Zu Boolean
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Hi"))   # True
```

**Aufgaben:**

1. Konvertieren Sie den String `"100"` zu einer Zahl
2. Addieren Sie 50 dazu
3. Konvertieren Sie das Ergebnis zurück zu einem String
4. Geben Sie einen Satz mit dem Ergebnis aus

## 📝 Experiment 7: Input/Output (10 Min)

**Wichtig:** Für `input()` müssen Sie ein Python-Skript erstellen, nicht die Shell verwenden!

Erstellen Sie eine Datei `test_input.py`:

```python
# Einfache Eingabe
name = input("Wie heissen Sie? ")
print(f"Hallo {name}!")

# Zahl eingeben
alter_str = input("Wie alt sind Sie? ")
alter = int(alter_str)
print(f"Nächstes Jahr sind Sie {alter + 1}")

# Mehrere Eingaben
vorname = input("Vorname: ")
nachname = input("Nachname: ")
print(f"Ihr vollständiger Name ist {vorname} {nachname}")

# Mit Berechnung
zahl1 = int(input("Erste Zahl: "))
zahl2 = int(input("Zweite Zahl: "))
summe = zahl1 + zahl2
print(f"Die Summe ist {summe}")
```

Führen Sie das Skript aus:

```bash
python test_input.py
```

**Aufgaben:**

1. Erstellen Sie ein Programm, das nach Name und Alter fragt
2. Berechnen Sie das Geburtsjahr (2025 - Alter)
3. Geben Sie einen Satz mit allen Informationen aus

## ✅ Checkliste

Nach den Experimenten sollten Sie:

- [ ] Strings erstellen und verketten können
- [ ] String-Indexierung und Slicing verstehen
- [ ] String-Methoden anwenden können
- [ ] F-Strings für Formatierung nutzen
- [ ] Vergleichsoperatoren verwenden
- [ ] Logische Operatoren verstehen
- [ ] Typkonvertierung durchführen
- [ ] `input()` für Benutzereingaben nutzen

## 💡 Tipps

- **Experimentieren Sie frei:** Probieren Sie Variationen aus
- **Machen Sie Fehler:** Fehler sind Lernchancen
- **Notieren Sie Fragen:** Schreiben Sie auf, was unklar ist
- **Wiederholen Sie:** Üben Sie die Beispiele mehrmals

## 🆘 Häufige Fehler

1. **Anführungszeichen vergessen:**
   ```python
   name = Anna  # Fehler!
   name = "Anna"  # Korrekt
   ```

2. **Typ-Fehler bei input():**
   ```python
   alter = input("Alter: ")
   print(alter + 5)  # Fehler! (String + Zahl)
   
   alter = int(input("Alter: "))
   print(alter + 5)  # Korrekt
   ```

3. **Index out of range:**
   ```python
   wort = "Hi"
   print(wort[5])  # Fehler! (nur 2 Zeichen)
   ```

Viel Erfolg beim Experimentieren! 🚀

