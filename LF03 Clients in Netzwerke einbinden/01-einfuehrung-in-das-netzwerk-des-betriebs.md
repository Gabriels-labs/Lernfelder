# Einführung in das Netzwerk des Betriebs


## Überblick (betriebliche Sicht)
- **Dienste:** Datei-/Druckdienste, Authentifizierung (AD/LDAP), E-Mail, DNS/DHCP, TK/VoIP, DMS, Zeit/NTP, Softwareverteilung.
- **Infrastruktur:** Verteilerräume (SV/GV/EV), strukturierte Verkabelung, Switch-Stacks, Router/Firewall, WLAN (APs/Controller), Internet-Uplink.
- **Netzsegmente:** LAN, WLAN (Mitarbeiter/Gast), Servernetz/DMZ, ggf. Produktionsnetz (OT), Management-Netz.


## Namens- & Adresskonzept (Kurz)
- **IPv4:** private Netze (10/8, 172.16/12, 192.168/16), Subnetting per CIDR (z. B. /24). **IPv6:** global/ULA, Autokonfiguration.
- **DNS-Namensraum:** klare, sprechende Hostnamen (z. B. `pc-fibu-23`), getrennte Zonen intern/extern.
- **VLAN-Design:** Access‑Ports (Endgeräte) vs. Trunks (Uplinks), Tagging (802.1Q); Dokumentation der VLAN‑IDs.


## Dokumentation (Minimum)
- **Netzplan** (Topologie, IP‑Bereiche, VLANs), **Patch-/Portpläne**, **Adressliste** (Client ↔ Port ↔ IP), **WLAN‑Plan** (AP‑Positionen/Kanäle), **Betriebsdoku** (Passwörter im Tresor, Notfallnummern).


**Prüfungstipp:** Begriffe sauber trennen (LAN/WLAN/Router/Switch), Segmentierung erklären, warum DNS/DHCP grundlegend sind.
```md
# Einführung in das Netzwerk des Betriebs


- Betriebsweite IT-Dienste (z. B. Zutritt, Zeiterfassung, DMS, TK) hängen am LAN/WLAN; zentrale Server/Services im Serverraum oder extern im RZ/Cloud. Übergang ins Internet über Router. fileciteturn7file0
- Endgeräte erhalten **IP-Adressen**; Zugriff über **LAN** (verkabelt) oder **WLAN** (drahtlos). Stockwerks‑Switches leiten Daten zielgerichtet weiter; IP‑Telefone & TK‑Anlage hängen im selben Netz. fileciteturn7file0


**Merken (IHK):** Grundbegriffe sauber zuordnen (LAN/WLAN/Server/Router), Rolle der zentralen Dienste kurz beschreiben.
