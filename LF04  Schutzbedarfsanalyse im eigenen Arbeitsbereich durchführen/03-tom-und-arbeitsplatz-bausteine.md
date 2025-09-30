# TOM & Arbeitsplatz-Bausteine (BSI/IT-GSK)

## TOM nach § 64 BDSG (Beispiele)
- Zugangskontrolle, Datenträger-/Speicher-/Benutzer-/Zugriffskontrolle, Übertragungs-/Eingabe-/Transportkontrolle, Wiederherstellbarkeit, Zuverlässigkeit, Datenintegrität, Verfügbarkeitskontrolle, Trennbarkeit. 

## Bausteine (Auszug) für Arbeitsplätze
- **INF** (Gebäude, Büro, mobil, Home), **OPS** (Telearbeit, Cloud-Nutzung), **SYS** (Client, Smartphone/Tablet, Drucker, Wechseldatenträger), **APP** (Office), **CON** (Standardsoftware).

## TOM ↔ Beispielmaßnahmen (Praxis, Arbeitsplatz)

| TOM (DE/EN) | Ziel | Beispielmaßnahmen (kurz & konkret) |
|---|---|---|
| **Zugangskontrolle / Physical Access Control** | Unbefugte physische Nutzung verhindern | Zutrittszonen (Serverraum), Schließsystem/Badge, Besucherbuch, Begleitpflicht, abschließbare Racks |
| **Zutritts-/Benutzerkontrolle / User Account Control** | Nur berechtigte Personen erhalten Accounts | Joiner/Mover/Leaver-Prozess, Vier-Augen-Freigabe, AD-Gruppenrollen, periodische Rezertifizierung |
| **Zugriffskontrolle / Logical Access Control** | Nur befugter Zugriff auf Daten/Funktionen | Rollen/Rechte (RBAC), Least Privilege, MFA, Session-Timeout, Bildschirmsperre, starke Passwortrichtlinie |
| **Speicherkontrolle / Storage Control** | Schutz gespeicherter Daten | Vollverschlüsselung (FDE) auf Notebooks, Server-/NAS-Verschlüsselung, Rechte auf Freigaben, DLP-Regeln |
| **Übertragungskontrolle / Transmission Control** | Schutz bei Transport/Netz | TLS (HTTPS, SMTPS), VPN für Remote, Signierung von Updates, HSTS, sichere Protokolle (SFTP/SMB3) |
| **Eingabekontrolle / Input Control** | Nachvollziehbarkeit der Dateneingabe | Protokollierung relevanter Eingaben/Änderungen, Änderungsjournal in Fachanwendungen |
| **Auftragskontrolle / Processor Control** | DSGVO-konforme Auslagerung | AV-Vertrag (Art. 28), TOM-Nachweise des Auftragsverarbeiters, Exit-/Löschkonzept, Sub-Prozessor-Liste |
| **Trennbarkeit / Data Separation** | Daten verschiedener Zwecke/Kunden trennen | Getrennte Mandanten/VLAN/Netzsegmente, getrennte Freigaben/Buckets, eigene Schlüssel je Mandant |
| **Pseudonymisierung & Verschlüsselung / Pseudonymisation & Encryption** | Vertraulichkeit/Datenschutz | Pseudonyme IDs statt Klardaten, Datenbank-/Feld-Verschlüsselung, Schlüsselmanagement (HSM/KMS) |
| **Integrität / Integrity** | Unverfälschtheit | Signaturen/Checksummen, Code-Signierung, Write-Once-Medien für Logs, 4-Augen-Prinzip bei Änderungen |
| **Verfügbarkeit / Availability** | Betriebsfähigkeit sichern | Redundanz (RAID, USV, Cluster), Monitoring/Alerting, Kapazitätsplanung, Härtung gegen DoS |
| **Wiederherstellbarkeit / Recoverability** | Wiederanlauf nach Störung | Backup 3-2-1, RPO/RTO, regelmäßige Restore-Tests, Notfallhandbuch/Übungen |
| **Regelmäßige Bewertung / Evaluation** | Wirksamkeit nachweisen | Interne Audits, Pen-Tests/Basis-Checks, Patch-/Vuln-Management, KPI/Reporting an Management |


### IHK-Kernanforderungen
- TOM-Kategorien aufzählen und sinnvollen Maßnahmenbezug herstellen; passende Bausteine für Arbeitsplatzszenarien nennen. 
