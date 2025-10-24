# Integration & Sicherheit: Zonen, Broker/Server, Betrieb

## Netz & Zonen
- **OT** (Produktion) strikt von **IT** (Office) trennen – VLAN/VRF/Firewall.  
- **Broker/OPC-UA-Server** in eigener, gehärteter Zone (DMZ-ähnlich) platzieren.  
- Nur **notwendige Ports/Flows** erlauben; Protokolle & Pfade dokumentieren.

## Broker/Server-Härtung (Kurzcheck)
- **TLS** Pflicht, Zertifikate/Keys im Griff (Rotation/Storage).  
- **ACL** je Topic/Namensraum; Geräte bekommen **minimal nötige Rechte**.  
- **QoS** passend wählen (Telemetrie vs. Kommandos).  
- **Retained** sparsam, **LWT** nutzen (Offline-Erkennung).  
- **Logging/Monitoring** (Rate-Limits, Anomalien), **Backup**/Recovery testen.

## Sensorik in der Fläche
- Werte **validieren** (Plausibilität), **Ausreißer** behandeln, **Zeitstempel** konsistent.  
- Datenflüsse **entkoppeln** (Buffer/Queue), um Backpressure zu vermeiden.

> Governance-Tipp: Ein **kurzer Standard** für Topic-Namen, Rechte und Schlüsselpflege verhindert 80 % der Reibung.

---

## IHK-Kernanforderungen
- OT/IT-Trennung und **sichere Zonen** für Broker/OPC-UA-Server begründen (nur nötige Ports/Flows).
- Mindestschutz beschreiben: **TLS**, **Zertifikate/Key-Rotation**, **ACL/Least-Privilege**, **Logging/Monitoring**, **Backup/Recovery-Test**.
- Betriebskonzept skizzieren: Topic-Konvention, Rechteverwaltung, Offline-Erkennung (LWT/Heartbeat).
