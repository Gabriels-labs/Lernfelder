# OPC UA – Industriestandard für M2M

## Worum geht’s?
**OPC UA (Open Platform Communications – Unified Architecture)** ist **platt­form- und herstellerunabhängig**.  
Es bringt **Informationsmodelle**, **Dienste** (Read/Write, Events, Subscriptions), **Discovery** und **Security** (Auth, Signatur, Verschlüsselung).

## Kommunikationsmodelle & Transports
- **Client/Server**: gezielte Abfragen/Schreiben  
- **Pub/Sub**: Verteilung an viele Empfänger (z. B. über UDP, AMQP, MQTT)  
- **Transporte**: TCP, HTTPS, UDP, AMQP, MQTT – OPC UA bleibt dabei das **Daten-/Dienst-Gerüst**.

## Server & Clients
- **Server**: vom Gerätehersteller eingebettet oder als Gateway/Software.  
- **Clients**: SCADA/HMI, Analytik, eigene Apps/Services.

## OPC UA vs. MQTT – sauber getrennt denken
- **MQTT** = schlanker **Transport** mit Pub/Sub (Telemetrie), **ohne** eigenes Informationsmodell.  
- **OPC UA** = **Standardisierte M2M-Schicht** mit Modell, Diensten und integrierter **Sicherheit**.

> **Kurzdefinition**  
> **OPC UA:** **Hersteller- und plattformunabhängiger Industriestandard** für **Maschine-zu-Maschine**-Kommunikation mit **Informationsmodell**, Diensten (Read/Write/Events/Subscriptions) und eingebauter **Sicherheit**.

---

## IHK-Kernanforderungen
- OPC UA Zweck/Eigenschaften nennen (Informationsmodell, Dienste, Security, Discovery).
- Kommunikationsmodelle unterscheiden: **Client/Server** vs. **Pub/Sub**; mögliche **Transporte** aufzählen.
- Abgrenzung zu MQTT: **OPC UA = Standardisierte M2M-Schicht**, **MQTT = schlanker Transport (Pub/Sub)**.
