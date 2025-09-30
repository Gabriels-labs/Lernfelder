# Elementare Gefährdungen & Risikobegriff

## Gefährdungen (Beispiele)
- Mensch (Fehler/Missbrauch), Technik (Ausfall/Schwachstelle), Umfeld (Brand/Wasser), Organisation (fehlende Richtlinien). BSI listet **elementare Gefährdungen** systematisch.

## Risiko & Schaden
- **Risiko** aus Eintrittswahrscheinlichkeit × Schadensausmaß (qualitativ). **Schadenskategorien**: finanziell, rechtlich, reputativ, betrieblich (Ausfall).

## Top-Gefährdungen ↔ typische Schutzmaßnahmen

| Gefährdung | Wirkung | Typische Schutzmaßnahmen |
|---|---|---|
| **Phishing / Social Engineering** | Kontoübernahme, Datendiebstahl | Awareness-Trainings, Phishing-Simulation, MFA, Mail-Filter, Prozess „Rückruf/4-Augen“ bei Zahlungen |
| **Malware / Ransomware** | Verschlüsselung/Stillstand | EDR/AV, Applocker/Allow-List, Patch-Mgmt, Netzwerksegmentierung, Offline-Backups + Restore-Tests |
| **Fehlkonfiguration** | Lücken/Datenschutzverstöße | Secure-Baseline, IaC/Vorlagen, 4-Augen-Prinzip, regelmäßige Konfig-Reviews/Audits |
| **Schwachstellen (ungepatcht)** | Ausnutzung/Einbruch | Patch-/Vuln-Mgmt (SLA), Test-Fenster, Wartungsfenster, Asset-Inventar, Priorisierung nach CVSS/Exposure |
| **Verlust/Diebstahl mobiler Geräte** | Datenabfluss | FDE (BitLocker/FileVault), MDM, Remote-Wipe, starke Sperre/MFA, minimale lokale Datenhaltung |
| **Unsichere Passwörter** | Account-Missbrauch | Passwort-Policy, Passwortmanager, MFA, Hashing mit Salt/Stretching, Bruteforce-Schutz/Lockout |
| **Ausfall IT-Systeme/Hardware** | Betriebsunterbrechung | Redundanz (RAID, Ersatzteile), Monitoring/Proaktiver Tausch, Wartungsverträge, Kapazitätsplanung |
| **Strom/Störung Gebäude** | Datenverlust/Ausfall | USV/NEA, Überspannungsschutz, geordnete Abschaltung, Test der Notstrom-Prozesse |
| **Brand/Wasser/Umwelt** | Totalausfall | Brandabschnitte, Detektion/Löschung, Sensorik (Leckage), Lagerung außerhalb, Notfallarbeitsplätze |
| **Datenabfluss durch Dritte (Cloud/AV)** | Compliance-Verstoß | AV-Verträge, TOM-Nachweise, Verschlüsselung/KMS, Logging/Geofencing, Exit-/Lösch-Prozesse |
| **Rechtsverstöße (Urheber/Lizenzen)** | Bußen/Abmahnungen | Lizenzinventar, Freigabeprozess für Software/Assets, Schulung, klare Nutzungsrichtlinien |
| **DoS/Netzangriffe** | Nichtverfügbarkeit | Rate-Limits/WAF, DDoS-Schutz, Segmentierung, Notfall-Runbooks, Kontaktwege Provider/BSI |

> **Risikoabschätzung (qualitativ):** *Eintrittswahrscheinlichkeit × Schadensausmaß* → priorisierte Maßnahmen, Definition von **RPO/RTO** und Verantwortlichkeiten.


### IHK-Kernanforderungen
- Typische Gefährdungen benennen und Risiko qualitativ bewerten; Schutzmaßnahmen ableiten.
