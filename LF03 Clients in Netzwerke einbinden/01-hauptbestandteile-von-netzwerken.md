# Hauptbestandteile von Netzwerken


## Netzarten
- **PAN** (z. B. Bluetooth), **LAN** (Gebäude/Standort), **MAN/WAN** (stadt-/länderweit), **Internet** (weltweit), **Intranet** (intern), **Extranet** (Partnerzugang).

## Netzbereiche & Rollen
- **Private Netze vs. öffentliche Netze**: Firmen-LAN/WLAN intern; Übergang ins Internet am Perimeter. Private IPv4-Adressen werden im Internet nicht geroutet (NAT am Rand). :contentReference[oaicite:0]{index=0}
- **Zonen**: Benutzer-LAN, Server-LAN/DMZ, Management; Gast-WLAN nach Bedarf. Trennung auf L3 (Router/Firewall) mit klaren Policies. :contentReference[oaicite:1]{index=1}
- **Dienste**: **DNS/DHCP**, Verzeichnis/Anmeldung (AD/LDAP), Datei/Druck, Mail/Web, Zeit (NTP) – Grundlage für Integration/Policies. :contentReference[oaicite:2]{index=2}

## LAN/WLAN/VLAN/VPN (Überblick)
- **LAN/WLAN**: Zugang lokal per Ethernet/Wi-Fi. **VLAN**: logische Segmentierung auf gemeinsamer Verkabelung, getaggte Uplinks (**Trunks**), untagged **Access-Ports** zu Endgeräten. :contentReference[oaicite:3]{index=3}
- **VPN**: Tunnel zwischen Standorten (Site-to-Site) oder für Remote-User (End-to-Site); Transport über das Internet, innen bleibt die interne IP-Kommunikation erhalten. :contentReference[oaicite:4]{index=4}
- **NAT/PAT:** Übersetzung privater in öffentliche Adressen; Port‑Übersetzung bei vielen Clients.

## LAN‑Bausteine
- **Switch** (Layer 2, MAC‑Lernen, SAT), **Router** (Layer 3, Routingtabelle), **AP** (Funkzelle), **NAS/SAN** (Datei vs. Block‑Storage), **Serverrollen** (AD, DNS, DHCP, Files, Print, Update, App).
- **VLAN** (logische Netze auf gemeinsamem Medium, Tagging 802.1Q), **Trunk** (mehrere VLANs über einen Link), **Port‑Typen** (Access/Trunk/Hybrid).

## NAS vs. SAN
- **NAS** = Dateifreigaben (SMB/NFS); **SAN** = Blockzugriff für Server. Zweck und Protokolle unterscheiden. :contentReference[oaicite:5]{index=5}

## IP/Ports (Kurz)
- **IPv4:** 32‑Bit, dotted decimal; **Spezial:** 127.0.0.1 Loopback, 169.254.0.0/16 APIPA. **IPv6:** 128‑Bit, Hex, ::1 Loopback.
- **Ports:** Well‑Known 0–1023 (HTTP 80/443, DNS 53, DHCP 67/68), Registered 1024–49151.


### IHK-Kernanforderungen
- Netzbereiche und Zonen begründen; NAT am Perimeter einordnen. :contentReference[oaicite:6]{index=6}  
- VLAN/Trunk/Access korrekt zuordnen und dokumentieren. :contentReference[oaicite:7]{index=7}  
- VPN-Einsatzszenarien unterscheiden (Site-to-Site vs. Remote). :contentReference[oaicite:8]{index=8}

