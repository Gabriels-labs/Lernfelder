# Protokolle: HTTP vs. MQTT – wann was?

## HTTP (Client/Server)
Zustandsloses Request/Response-Protokoll (Ports 80/443). Gut für **APIs, Web, Konfiguration**.  
Mit **HTTPS** transportverschlüsselt.  
**Stärken:** verbreitet, Tools reichlich, Firewalls kennen es.  
**Grenze:** Polling/Overhead bei Telemetrie, keine eingebaute Pub/Sub-Logik.

## MQTT (Publish/Subscribe)
**Broker** vermittelt zwischen **Publisher** und **Subscriber** über **Topics**.  
**Asynchron, leichtgewichtig**, effizient auf wackeligen Netzen.

### Topics & Wildcards
- Hierarchisch, z. B. `werk/linie/geraet/temperatur`  
- **`+`** = genau eine Ebene, **`#`** = alle Folgeebenen

### Quality of Service (QoS)
- **0** „at most once“ – schnell, keine Garantie  
- **1** „at least once“ – zustellgarantiert, Duplikate möglich  
- **2** „exactly once“ – genau einmal, teuer (Handshake)

### Zustandsfeatures
- **Retained** (letzte Nachricht „geparkt“),  
- **Persistent Session** (Sitzung beim Broker),  
- **Keep-Alive**, **LWT** (Last-Will-Testament bei Client-Absturz)

### Sicherheit – unbedingt ergänzen
- **TLS** erzwingen (auch über WebSockets),  
- **AuthN/AuthZ** mit **ACL** (wer darf welches Topic),  
- **Netzsegmentierung** und Rate-Limits gegen Missbrauch.

**Daumenregel:** **HTTP** für Konfiguration/Abfragen, **MQTT** für **Telemetrie/Events** (viele kleine Nachrichten, viele Teilnehmer).


> **Kurzdefinitionen**  
> **HTTP:** Zustandsloses **Anfrage-Antwort-Protokoll** (Client/Server) – ideal für Web-APIs, Konfiguration und Abrufe.  
> **MQTT:** **Leichtgewichtiges Nachrichtenprotokoll** mit **Vermittler (Broker)** – Geräte **veröffentlichen** Nachrichten auf **Topics**, andere **abonnieren** sie (Pub/Sub) – ideal für Telemetrie/Events.

---

## IHK-Kernanforderungen
- HTTP vs. MQTT am **Use-Case** entscheiden (API/Abfrage vs. Telemetrie/Events, Netzqualität, Overhead).
- MQTT-Begriffe sicher erklären: **Broker, Topic, Wildcard (+/#), QoS 0/1/2, Retained, Persistent Session, LWT**.
- Grundschutz für MQTT nennen: **TLS**, **AuthN/AuthZ**, **ACL pro Topic**, **Segmentierung**, **Rate-Limits**.
