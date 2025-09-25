# Hauptbestandteile von Computernetzwerken


## Netzarten
- **PAN** (z. B. Bluetooth), **LAN** (Gebäude/Standort), **MAN/WAN** (stadt-/länderweit), **Internet** (weltweit), **Intranet** (intern), **Extranet** (Partnerzugang).


## LAN‑Bausteine
- **Switch** (Layer 2, MAC‑Lernen, SAT), **Router** (Layer 3, Routingtabelle), **AP** (Funkzelle), **NAS/SAN** (Datei vs. Block‑Storage), **Serverrollen** (AD, DNS, DHCP, Files, Print, Update, App).
- **VLAN** (logische Netze auf gemeinsamem Medium, Tagging 802.1Q), **Trunk** (mehrere VLANs über einen Link), **Port‑Typen** (Access/Trunk/Hybrid).


## VPN & NAT
- **VPN:** Site‑to‑Site (Standorte koppeln), Remote‑Access (Einzelgeräte), End‑to‑Site (Client→Zentrale). Tunnel/Authentifizierung/Schutz.
- **NAT/PAT:** Übersetzung privater in öffentliche Adressen; Port‑Übersetzung bei vielen Clients.


## IP/Ports (Kurz)
- **IPv4:** 32‑Bit, dotted decimal; **Spezial:** 127.0.0.1 Loopback, 169.254.0.0/16 APIPA. **IPv6:** 128‑Bit, Hex, ::1 Loopback.
- **Ports:** Well‑Known 0–1023 (HTTP 80/443, DNS 53, DHCP 67/68), Registered 1024–49151.


**Prüfungstipp:** VLAN ≠ VPN, NAS ≠ SAN; Router ≠ Switch; private Adressen werden im Internet nicht geroutet (NAT nötig).
```md
# Hauptbestandteile von Computernetzwerken


## Netzarten & Bereiche
- **Internet** (weltweit), **Intranet** (unternehmensweit), **LAN** (lokal). Telefonnetz: leitungsvermittelt; Datenwelt: paketvermittelt. **Carrier-/Providernetze** verbinden. fileciteturn7file1
- **Privat vs. öffentlich:** Private IP‑Bereiche intern; öffentlich geroutete Netze bei Providern/Carriern. **LAN/WLAN/VLAN/VPN/SAN/PAN** sauber unterscheiden. VLAN‑Tagging via **802.1Q** (12‑Bit‑VLAN‑ID); **Trunk** trägt mehrere VLANs. fileciteturn7file1


## VPN‑Modi
- **End‑to‑End**, **Site‑to‑Site**, **End‑to‑Site** – tunnelt/ver‑schlüsselt Verkehr über unsichere Netze. fileciteturn7file1


## Server & Clients
- Servertypen: File, Print, Mail, DNS, Web/Shop, Update, App, **NAS**, Terminal‑Server. **Fat‑ vs. Thin‑Clients**, BYOD, Embedded, CPS. fileciteturn7file1


**Merken (IHK):** VLAN ≠ VPN; SAN ≠ NAS; P2P vs. Client‑Server; private IPs werden im Internet **nicht** geroutet.
