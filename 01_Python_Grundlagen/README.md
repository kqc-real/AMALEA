# Woche 1: Python-Grundlagen und QUA3CK

Woche 1 legt das Fundament für den Kurs. Im Mittelpunkt stehen Python,
Pandas, erste Streamlit-Schritte, Docker-Grundlagen und das
QUA3CK-Prozessmodell.

## Lernziele

- Python-Syntax und zentrale Datentypen sicher anwenden
- Daten mit Pandas einlesen, filtern und transformieren
- den Unterschied zwischen Notebook und Streamlit-App verstehen
- eine einfache Arbeitsumgebung mit Docker starten
- das QUA3CK-Modell als Struktur für datenorientierte Projekte einordnen

## Materialien

- `01_Docker_für_Data_Science.ipynb`: verbindlicher Setup- und
  Kontextbaustein für die Docker-basierte Kursumgebung
- `00_Python_in_3_Stunden.ipynb`: kompakter Einstieg in Python und Pandas
- `03_QUA3CK_Prozessmodell.ipynb`: methodischer Rahmen und Vorschau auf
  spätere Wochen
- `uebungs_app.py`: erste kleine Streamlit-Anwendung
- `meine_erste_app.py`: zusätzliche einfache App zum Einstieg

## Pflicht in Woche 1

Wenn du in Woche 1 nur das Wesentliche schaffen willst, arbeite in
dieser Reihenfolge:

1. Docker-Umgebung für den Kurs starten
2. `01_Docker_für_Data_Science.ipynb` mit Fokus auf Images,
   Container und Compose durcharbeiten
3. `00_Python_in_3_Stunden.ipynb` vollständig durcharbeiten
4. `meine_erste_app.py` oder `uebungs_app.py` im Docker-Kontext starten
5. `03_QUA3CK_Prozessmodell.ipynb` konzeptionell durcharbeiten

Am Ende der Woche solltest du:

- einfachen Python-Code lesen und ausführen können
- den Unterschied zwischen Notebook und Streamlit-App verstehen
- die Kursumgebung per Docker Compose starten können
- eine erste App im Docker-Setup starten können
- QUA3CK grob als Projektstruktur erklären können

Optional:

- weitere Docker-Details aus dem Notebook vertiefen
- die Compose-Dateien im Repository genauer untersuchen

## Empfohlene Reihenfolge

1. Docker Compose für Woche 1 starten
2. `01_Docker_für_Data_Science.ipynb`
3. `00_Python_in_3_Stunden.ipynb`
4. `meine_erste_app.py` oder `uebungs_app.py`
5. `03_QUA3CK_Prozessmodell.ipynb`

Als Nachschlagewerk eignet sich `../Glossar_Alle_Begriffe_erklärt.ipynb`.

## Start

### Docker-Pflichtstart

```bash
cd ..
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
```

Danach arbeitet ihr in Woche 1 in der Regel über:

- Jupyter Lab Slim: `http://localhost:8889`
- Streamlit Slim: `http://localhost:8502`

### Streamlit-App im Wochenordner starten

```bash
cd 01_Python_Grundlagen
docker compose up --build
```

### Lokaler Zusatzpfad (nur technischer Ausnahmefall)

```bash
cd 01_Python_Grundlagen
make help
make install
make run
make test
```

## Hinweise

- Streamlit-Code gehört in `.py`-Dateien und wird über das Terminal gestartet.
- Für den Kurs ist Docker der verpflichtende Standardpfad.
- Das Docker-Notebook ist in Woche 1 keine Vertiefung, sondern Teil des
  Einstiegspfads.
- Im QUA3CK-Notebook ist das Prozessverständnis wichtiger als der
  vollständige MLflow-Nachbau.
- Wenn Ports belegt sind, müssen die laufenden Dienste angepasst oder beendet werden.

## Qualitätssicherung

```bash
cd 01_Python_Grundlagen
make test
```

Bei Bedarf lassen sich Formatierung und Linting zusätzlich mit `black`,
`isort` und `flake8` lokal ausführen.
