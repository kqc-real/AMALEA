# Woche 1: Python-Grundlagen und QUA3CK

Woche 1 legt das Fundament für den Kurs. Im Mittelpunkt stehen Python,
Pandas, erste Streamlit-Schritte, Docker-Grundlagen und das
QUA3CK-Prozessmodell.

## Lernziele

- Python-Syntax und zentrale Datentypen sicher anwenden
- Daten mit Pandas einlesen, filtern und transformieren
- den Unterschied zwischen Notebook und Streamlit-App verstehen
- eine einfache Arbeitsumgebung lokal oder mit Docker starten
- das QUA3CK-Modell als Struktur für datenorientierte Projekte einordnen

## Materialien

- `00_Python_in_3_Stunden.ipynb`: kompakter Einstieg in Python und Pandas
- `01_Docker_für_Data_Science.ipynb`: Grundidee containerisierter Arbeitsumgebungen
- `03_QUA3CK_Prozessmodell.ipynb`: methodischer Rahmen für spätere Wochen
- `uebungs_app.py`: erste kleine Streamlit-Anwendung
- `meine_erste_app.py`: zusätzliche einfache App zum Einstieg

## Empfohlene Reihenfolge

1. `00_Python_in_3_Stunden.ipynb`
2. `01_Docker_für_Data_Science.ipynb`
3. `03_QUA3CK_Prozessmodell.ipynb`
4. `uebungs_app.py`

Als Nachschlagewerk eignet sich `../Glossar_Alle_Begriffe_erklärt.ipynb`.

## Start

### Lokal

```bash
cd 01_Python_Grundlagen
pip install -r requirements.txt
jupyter lab
```

### Streamlit-App starten

```bash
cd 01_Python_Grundlagen
streamlit run uebungs_app.py
```

### Mit Makefile

```bash
cd 01_Python_Grundlagen
make help
make install
make run
make test
```

### Mit Docker

```bash
cd 01_Python_Grundlagen
docker-compose up --build
```

## Hinweise

- Streamlit-Code gehört in `.py`-Dateien und wird über das Terminal gestartet.
- Für den Kurs reicht in der Regel die lokale Ausführung; Docker ist eine
  zusätzliche Option.
- Wenn Ports belegt sind, müssen die laufenden Dienste angepasst oder beendet werden.

## Qualitätssicherung

```bash
cd 01_Python_Grundlagen
make test
```

Bei Bedarf lassen sich Formatierung und Linting zusätzlich mit `black`,
`isort` und `flake8` lokal ausführen.
