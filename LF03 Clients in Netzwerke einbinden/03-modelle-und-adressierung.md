# Modelle & Adressierung (OSI & TCP/IP)

## 1) Modelle im Überblick (DE/EN)
| Ebene |    OSI (DE)   |  OSI (EN)   |   TCP/IP (DE)  |    TCP/IP (EN)   | Typische PDU |
|-------|---------------|-------------|----------------|------------------|--------------|
|   7   |   Anwendung   | Application |    Anwendung   |    Application   |     Daten    |
|   6   |  Darstellung  | Presentation|                |                  |     Daten    |
|   5   |    Sitzung    |   Session   |                |                  |     Daten    |
|   4   |   Transport   |  Transport  |    Transport   |     Transport    | **Segment/Datagramm** (TCP/UDP + **Ports**) |
|   3   |  Vermittlung  |   Network   |    Internet    | Internet/Network | **Paket** (IP) |
|   2   |   Sicherung   |  Data Link  | Netzwerkzugang |       Link       | **Frame** (MAC) |
|   1   | Bitübertragung|   Physical  | Netzwerkzugang |       Link       | **Bits** |

**Geräte (DE/EN) je Ebene:**  
Hub/Repeater (L1), Bridge/Switch (L2), Router (L3), Firewall (L3–L7 je nach Typ), Load Balancer (L4–L7), Access Point (L2, Funk↔Ethernet).

## 2) Basisprotokolle (DE/EN)
- **ARP** (Address Resolution Protocol) – IP↔MAC im LAN (oft „Layer 2,5“).  
- **DHCP** (Dynamic Host Configuration Protocol) – Adressvergabe; **DORA**: Discover → Offer → Request → Ack.  
- **DNS** (Domain Name System) – Namensauflösung; Records **A/AAAA**, **CNAME**, **MX**.  
- **ICMP** (Internet Control Message Protocol) – Meldungen/Fehler (ping, traceroute).  
- **TCP/UDP** – Transport; **Ports** (z. B. 80/443 HTTP(S), 53 DNS, 445 SMB).

## 3) VLAN & Inter-VLAN-Routing (802.1Q)
- **Access-Port**: untagged, genau **ein** VLAN.  
- **Trunk-Port**: mehrere VLANs **getaggt** (802.1Q-Tag mit **12-Bit VLAN-ID**).  
- **Native VLAN** bewusst wählen/härten.  
- **Inter-VLAN-Routing** über L3-Switch/Firewall (Policies).

## 4) IPv4/IPv6 & Subnetting (Kurzleitfaden)
**Private IPv4-Bereiche:** 10.0.0.0/8 · 172.16.0.0/12 · 192.168.0.0/16.  
**Loopback:** 127.0.0.1 / **::1**.  
**IPv6:** Link-Local **fe80::/64**, **ULA** fc00::/7, **Global Unicast** 2000::/3. (Adressierung via **SLAAC** oder **DHCPv6**.)

**Algorithmus (IPv4):**
1. **Hosts** = 2^(32 − Präfix) − 2  
2. **Sprungweite** (bei /24-Netzen): 256 − Maskenwert im letzten Oktett  
3. **Netz/Broadcast** bestimmen → **erste/letzte Hostadresse**

**Beispiel /26:** 192.168.10.0/26 (Maske 255.255.255.192)  
Netze: 0–63, 64–127, 128–191, 192–255  
Netz 1: **192.168.10.0** | Hosts **.1–.62** | Broadcast **.63**  
Netz 2: **192.168.10.64** | Hosts **.65–.126** | Broadcast **.127**  
usw.

## 5) IHK-Kernanforderungen
- **Schichten mappen** (OSI↔TCP/IP) und **Protokolle/Geräte** korrekt zuordnen (DE/EN-Begriffe).  
- **ARP/DHCP/DNS** im Modell verorten (DORA, Record-Typen).  
- **802.1Q** (Access/Trunk/Native VLAN) erklären und Einsatz begründen.  
- **Subnetting** für /24, /25, /26 durchführen (Netz/Broadcast/erste/letzte Hostadresse).
