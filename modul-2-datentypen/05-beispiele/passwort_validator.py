"""Passwort-Validator mit mehreren Kriterien"""

def validiere_passwort(passwort: str) -> tuple[bool, list[str]]:
    """
    Validiert ein Passwort nach mehreren Kriterien.
    
    Args:
        passwort: Das zu validierende Passwort
        
    Returns:
        (ist_gueltig, fehler_liste)
    """
    fehler = []
    
    # Mindestlänge
    if len(passwort) < 8:
        fehler.append("❌ Mindestens 8 Zeichen erforderlich")
    
    # Grossbuchstabe
    if not any(c.isupper() for c in passwort):
        fehler.append("❌ Mindestens 1 Grossbuchstabe erforderlich")
    
    # Kleinbuchstabe
    if not any(c.islower() for c in passwort):
        fehler.append("❌ Mindestens 1 Kleinbuchstabe erforderlich")
    
    # Zahl
    if not any(c.isdigit() for c in passwort):
        fehler.append("❌ Mindestens 1 Zahl erforderlich")
    
    # Sonderzeichen
    sonderzeichen = "!@#$%^&*"
    if not any(c in sonderzeichen for c in passwort):
        fehler.append(f"❌ Mindestens 1 Sonderzeichen ({sonderzeichen}) erforderlich")
    
    return len(fehler) == 0, fehler


# Hauptprogramm
print("=" * 50)
print("      PASSWORT-VALIDATOR")
print("=" * 50)
print("\nKriterien:")
print("- Mindestens 8 Zeichen")
print("- Mindestens 1 Grossbuchstabe")
print("- Mindestens 1 Kleinbuchstabe")
print("- Mindestens 1 Zahl")
print("- Mindestens 1 Sonderzeichen (!@#$%^&*)")
print("=" * 50)

while True:
    passwort = input("\nPasswort eingeben (oder 'q' zum Beenden): ")
    
    if passwort.lower() == 'q':
        print("\nAuf Wiedersehen!")
        break
    
    ist_gueltig, fehler = validiere_passwort(passwort)
    
    if ist_gueltig:
        print("\n✓ Passwort ist gültig! 🎉")
        break
    else:
        print("\n✗ Passwort ungültig:")
        for fehler_text in fehler:
            print(f"  {fehler_text}")
