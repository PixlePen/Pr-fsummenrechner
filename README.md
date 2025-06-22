# Pr-fsummenrechner
Ein Prüfsummenrechner aufbauend auf mein Passwortmanager-Projekt

# Datei Prüfsummen Rechner (Python / Tkinter)

Ein intuitiver und effizienter Prüfsummenrechner mit grafischer Benutzeroberfläche, entwickelt in Python. Dieses Tool dient der **Überprüfung der Integrität von Dateien** und ist ein unverzichtbares Hilfsmittel in der IT, um sicherzustellen, dass heruntergeladene oder übertragene Daten unverändert und unbeschädigt sind. Es demonstriert die Fähigkeit zur Entwicklung nützlicher Anwendungen, die direkt zur Datensicherheit beitragen.

## Motivation

In der digitalen Welt, in der Dateien ständig transferiert, kopiert oder gespeichert werden, ist die Gewährleistung ihrer Unversehrtheit von größter Bedeutung. Unbemerkte Änderungen oder Beschädigungen können zu Fehlfunktionen von Software, Datenkorruption oder sogar Sicherheitslücken führen. Mein Ziel war es, ein **benutzerfreundliches Desktop-Tool** zu schaffen, das eine schnelle und zuverlässige Integritätsprüfung ermöglicht und dabei folgende Aspekte berücksichtigt:

* **Sicherstellung der Datenintegrität:** Bestätigung der Unverfälschtheit von Dateien.
* **Benutzerfreundlichkeit:** Intuitive Bedienung durch eine grafische Oberfläche.
* **Algorithmus-Flexibilität:** Unterstützung gängiger Hashing-Algorithmen.
* **Ressourceneffizienz:** Verarbeitung auch sehr großer Dateien ohne hohe Speicherauslastung.

## Funktionen

* **Dateiauswahl:** Einfache Auswahl von Dateien über einen Standard-Dateidialog.
* **Algorithmus-Auswahl:** Unterstützung der Hashing-Algorithmen **SHA256** und **MD5**.
* **Prüfsummenberechnung:** Schnelle und präzise Berechnung der Prüfsumme der ausgewählten Datei.
* **Ergebnisanzeige:** Das berechnete Hash-Ergebnis wird übersichtlich dargestellt und kann einfach kopiert werden.
* **Dateigrößenanzeige:** Zeigt die Größe der ausgewählten Datei an.
* **Fehlerbehandlung:** Robuste Behandlung von Dateizugriffsfehlern oder ungültigen Eingaben.
* **Effiziente Dateiverarbeitung:** Nutzt Chunk-Verarbeitung (64KB Blöcke), um auch sehr große Dateien (Gigabyte-Bereich) speichereffizient zu verarbeiten.

## Sicherheitsaspekte und Algorithmen

Die Integrität von Daten ist ein fundamentales Schutzziel in der IT-Sicherheit. Dieses Tool nutzt etablierte Hashing-Algorithmen:

* **SHA256 (Secure Hash Algorithm 256):** Ein kryptografisch sicherer Hash-Algorithmus. Er erzeugt eine nahezu eindeutige "digitale Signatur" einer Datei. Selbst kleinste Änderungen an der Datei führen zu einer komplett anderen Prüfsumme. SHA256 wird für die Überprüfung der **Integrität und Authentizität** von Daten empfohlen und ist standardmäßig für sicherheitsrelevante Prüfungen zu verwenden.
* **MD5 (Message-Digest Algorithm 5):** Ein älterer Hashing-Algorithmus. Während MD5 für einfache **Integritätsprüfungen** (z.B. nach einem Download, um festzustellen, ob die Datei vollständig übertragen wurde) weiterhin genutzt werden kann, gilt er aufgrund bekannter Kollisionsangriffe **nicht mehr als kryptografisch sicher zur Gewährleistung der Authentizität oder Fälschungssicherheit**. Für sicherheitskritische Anwendungsfälle sollte stets SHA256 oder ein stärkerer Algorithmus gewählt werden.

## Installation und Nutzung

### Voraussetzungen

* Python 3 (getestet mit Python 3.x)

### Ausführung

1.  **Herunterladen:** Lade die Datei `Prüfsummenrechner.py` herunter.
2.  **Shebang hinzufügen (Linux/macOS):** Fügen Sie als allererste Zeile im Skript hinzu:
    ```python
    #!/usr/bin/env python3
    ```
3.  **Ausführungsrechte vergeben (Linux/macOS):**
    ```bash
    chmod +x Prüfsummenrechner.py
    ```
4.  **Programm starten:**
    * **Linux/macOS (direkt):** Führen Sie die Datei direkt über das Terminal aus oder per Doppelklick im Dateimanager (ggf. "Ausführen" wählen):
        ```bash
        ./Prüfsummenrechner.py
        ```
    * **Windows (als .pyw):** Benennen Sie die Datei zu `Prüfsummenrechner.pyw` um und starten Sie sie per Doppelklick.
    * **Allgemein (via Python-Interpreter):**
        ```bash
        python Prüfsummenrechner.py
        ```
5.  Wählen Sie eine Datei aus und den gewünschten Algorithmus, um die Prüfsumme zu berechnen.

## Bezug zur Ausbildung (Fachinformatiker für Systemintegration)

Dieses Projekt ist eine direkte Anwendung und Vertiefung relevanter Lernfelder meiner Ausbildung zum Fachinformatiker für Systemintegration:

* **LF04: Schutzbedarfsanalyse im eigenen Arbeitsbereich durchführen:** Das Projekt befasst sich direkt mit der Sicherstellung der Datenintegrität, einem der fundamentalen Schutzziele in der IT-Sicherheit.
* **LF11b: Betrieb und Sicherheit vernetzter Systeme gewährleisten:** Die Überprüfung der Datenintegrität ist ein wichtiger Aspekt des sicheren Betriebs von Systemen.
* **LF10b: Serverdienste bereitstellen und Administrationsaufgaben automatisieren:** Die Fähigkeit, Python-Skripte für solche Prüfungen zu schreiben, ist direkt auf die Automatisierung von administrativen Aufgaben übertragbar.
* **Allgemeine Programmierkenntnisse & GUI-Entwicklung:** Stärkt die Problemlösungsfähigkeiten, das Verständnis für Hashing-Algorithmen und die Entwicklung von benutzerfreundlichen grafischen Oberflächen mit Tkinter.

---
