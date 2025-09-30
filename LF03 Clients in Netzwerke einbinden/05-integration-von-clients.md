# Integration von Clients

## Was vorbereitet sein muss
- Korrektes Patchen (Dose→Patchfeld→Switch), passendes VLAN, freie Ports; WLAN-Abdeckung/SSID bekannt.
- Adressierung: DHCP-Scope oder statisch (IP/Maske/Gateway/DNS), Zeit via NTP; DNS/Zonen sauber.
- Identität/Policies: Domänenbeitritt (Zeit/DNS!), Laufwerke/Drucker/Updates, Gruppenzugehörigkeit.
- **Dokumentation**: Hostname↔Port↔IP/MAC, Standort/Benutzer.

## Typische Stolpersteine
- Falscher Port/VLAN, doppelte IP, falscher DNS/Gateway, Zeitabweichung (Domänenbeitritt scheitert), fehlende Rechte.

### IHK-Kernanforderungen
- Voraussetzungen/Parameter (IP/Maske/GW/DNS/NTP) benennen.
- Fehlbild „kein DNS“ vs. „kein Routing“ begründet unterscheiden.
