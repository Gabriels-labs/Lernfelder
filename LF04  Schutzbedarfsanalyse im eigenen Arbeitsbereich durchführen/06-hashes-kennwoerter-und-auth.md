# Hashes, Kennwörter & Authentifizierung (MFA)

## Hashing (Integrität)
- **Hash** = Einwegfunktion (feste Länge, kollisionsarm); kleine Änderung → völlig anderer Hash; Einsatz u. a. für Integritätsprüfung & Erkennung von Manipulationen.
## Kennwortsicherheit & Richtlinien
- Länge/Komplexität + **Salting/Stretching** (Server-Speicherung), Rotationsregeln sinnvoll.  
- Beispiel-Rechnung (Brute Force): Erhöhung der Suchmenge/Länge steigert Aufwand nichtlinear.

## Authentifizierung (MFA)
- **AAA/„Triple-A“**: Authentication, Authorization, Accounting.  
- **MFA** kombiniert **Wissen** (Passwort) + **Besitz** (Token/App) + **Inhärenz** (Biometrie); 2FA-Beispiel: Passwort + Einmal-Code.

### IHK-Kernanforderungen
- Hash-Eigenschaften & Nutzen erklären; solide Passwortrichtlinie/MFA begründen.
