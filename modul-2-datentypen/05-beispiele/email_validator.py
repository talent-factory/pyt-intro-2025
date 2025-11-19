"""E-Mail-Validator mit detaillierter Prüfung"""

def validiere_email(email: str) -> tuple[bool, str]:
    """
    Validiert eine E-Mail-Adresse.
    
    Args:
        email: Die zu validierende E-Mail
        
    Returns:
        (ist_gueltig, fehlermeldung)
    """
    # Leer?
    if not email or email.strip() == "":
        return False, "E-Mail darf nicht leer sein"
    
    email = email.strip()
    
    # @ vorhanden?
    if "@" not in email:
        return False, "@ fehlt"
    
    # Nur ein @?
    if email.count("@") > 1:
        return False, "Nur ein @ erlaubt"
    
    # Teile aufsplitten
    teile = email.split("@")
    local = teile[0]
    domain = teile[1]
    
    # Local-Part prüfen
    if not local:
        return False, "Benutzername fehlt"
    
    # Domain prüfen
    if not domain:
        return False, "Domain fehlt"
    
    # . in Domain?
    if "." not in domain:
        return False, ". in Domain fehlt"
    
    # Domain-Teile
    domain_teile = domain.split(".")
    
    # Letzter Teil (TLD) mindestens 2 Zeichen?
    if len(domain_teile[-1]) < 2:
        return False, "Top-Level-Domain zu kurz"
    
    # Alles OK
    return True, "Gültige E-Mail"


# Hauptprogramm
print("=" * 50)
print("         E-MAIL-VALIDATOR")
print("=" * 50)

while True:
    email = input("\nE-Mail (oder 'q' zum Beenden): ")
    
    if email.lower() == 'q':
        print("\nAuf Wiedersehen!")
        break
    
    ist_gueltig, meldung = validiere_email(email)
    
    if ist_gueltig:
        print(f"✓ {meldung}")
    else:
        print(f"✗ {meldung}")
