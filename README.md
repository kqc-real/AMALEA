# AMALEA 2025: Data Analytics & Big Data

![AMALEA 2025 Logo](./kurs-logo.png)

![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?logo=huggingface&logoColor=white)

Praxisorientierter Kurs zu Data Analytics, Machine Learning und
Deployment.

> In sieben Wochen führt das Repository von Python-Grundlagen über
> Datenanalyse und klassisches Machine Learning bis zu Dashboards, APIs
> und einfachen Deployment-Szenarien.

## Worum Es Geht

AMALEA ist als wöchentlich gegliederte Lehrsammlung aufgebaut. Der
stabile Kurskern liegt in Woche 1 bis 4. Woche 5 und 6 erweitern den
Kurs fachlich, Woche 7 dient als Lehrdemo für APIs, Dashboards und
Deployment.

- Notebooks liefern Schritt-für-Schritt-Materialien mit Erklärungen,
  Übungen und Referenzfassungen.
- Streamlit-Apps machen Modelle, Visualisierungen und Arbeitsabläufe
  direkt ausprobierbar.
- Woche 7 ergänzt eine lokale FastAPI-Demo mit Dashboards.
- Requirements-Dateien sind pro Woche getrennt, damit Installationen
  klein und nachvollziehbar bleiben.

## So Arbeitest Du Mit Dem Repository

1. Starte mit dem Kernnotebook der jeweiligen Woche.
2. Öffne danach die passende App oder Demo.
3. Variiere Parameter, halte Beobachtungen fest und vergleiche die
  Ergebnisse.
4. Nutze Woche 7 gezielt für lokale API- und Deployment-Demonstrationen.
5. Arbeite bewusst kuratiert: Nicht jedes Artefakt muss im Kursbetrieb
  verpflichtend behandelt werden.

## Pädagogische Einordnung

Jede Woche bildet ein eigenes Lernpaket aus Notebook, App oder Demo.

- Woche 1 und 2: Python, Pandas, Streamlit und QUA3CK.
- Woche 3 und 4: klassisches Machine Learning, Modellvergleich,
  Metriken und MLflow.
- Woche 5 und 6: neuronale Netze, Computer Vision und NLP.
- Woche 7: lokale API, Dashboards und prototypische Deployment-Abläufe.

Die Umgebungen bleiben durch wochenweise Requirements und Lockfiles
besser steuerbar. Für den Lehrbetrieb ist eine gemeinsame
Docker-Compose-Umgebung der verbindliche Standard, damit Notebooks,
Apps und spätere MLOps-Bausteine auf allen Rechnern gleich starten.

## Inhaltsverzeichnis

- [Tech-Stack](#tech-stack)
- [Roadmap](#roadmap)
- [Quick Start](#quick-start)
- [Student Setup](#student-setup)
- [Dependencies](#dependencies)
- [Run Cheatsheet](#run-cheatsheet)
- [Installation und Status](#support-und-ressourcen)
- [Copilot und Agenten](#copilot-und-agenten)
- [Repository-Struktur](#repository-struktur)
- [Kursinhalte](#kursinhalte)
- [Support Und Ressourcen](#support-und-ressourcen)

## Tech-Stack

- Python 3.11+, Pandas und NumPy für Datenverarbeitung und Analyse.
- scikit-learn für klassisches Machine Learning.
- TensorFlow und Keras für Deep-Learning-Einstiege.
- Streamlit für kleine interaktive Anwendungen.
- Docker und Docker Compose für reproduzierbare Umgebungen.
- MLflow für Experiment-Tracking.
- FastAPI für die lokale API-Demo in Woche 7.
- QUA3CK als Prozessrahmen für die didaktische Struktur.

## Roadmap

### Phase 1: Grundlagen

- Woche 01: Python-Grundlagen und QUA3CK.
- Woche 02: Streamlit und Pandas.

### Phase 2: Machine Learning

- Woche 03: klassisches Machine Learning mit scikit-learn.
- Woche 04: fortgeschrittene Algorithmen und MLflow.

### Phase 3: Deep Learning Und KI

- Woche 05: neuronale Netze.
- Woche 06: Computer Vision und NLP.

### Phase 4: Deployment Und Integration

- Woche 07: FastAPI-Demo, Dashboards und lokale Bereitstellung.

---

## Quick Start

### Student Setup

Für Studierende gibt es eine kurze Ein-Seiten-Anleitung in
[STUDENT_SETUP.md](STUDENT_SETUP.md).

Dort sind die Schritte für macOS und Windows zu Git,
Docker Desktop, Docker Compose und den ersten Funktionstest getrennt
beschrieben.

### Voraussetzungen

- [Docker Desktop](https://www.docker.com/products/docker-desktop) als
  verbindliche Laufzeitumgebung für den Kurs.
- [Git](https://git-scm.com/) für das Klonen des Repositories.
- Optional: Python 3.11+ nur für technische Sonderfälle,
  Troubleshooting oder lokale Wartung.

### Docker: Kursstart für Woche 1 bis 4

Der studentische Standardpfad startet die schlanke Compose-Umgebung.

```bash
# 1. Repository klonen
git clone <repository-url>
cd amalea

# 2. Docker-Umgebung für den Kurs starten
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim

# 3. Services öffnen
# Jupyter Lab: http://localhost:8889
# Streamlit App: http://localhost:8502
```

### Docker: Erweiterter Stack ab Woche 4/5

Wenn MLflow, Deep Learning oder spätere Deployment-Bausteine benötigt
werden, wechselt ihr auf das Full-Profil.

```bash
docker compose --profile full up -d
```

- Jupyter Full: [http://localhost:8888](http://localhost:8888)
- Streamlit Full: [http://localhost:8501](http://localhost:8501)
- MLflow UI: [http://localhost:5001](http://localhost:5001)

### Empfohlener Kursbetrieb

Für den regulären Lehrbetrieb gilt dieser Standard:

- Docker Compose ist der verpflichtende Laufzeitpfad für Studierende.
- Für Woche 1 bis 4 startet ihr standardmäßig das Slim-Profil.
- Für MLflow, Deep Learning und spätere Deployment-Inhalte nutzt ihr
  das Full-Profil.
- Lokale Python-Umgebungen sind kein Kursstandard, sondern nur ein
  technischer Ausnahmeweg.

### Verbindlicher Setup-Pfad für Studierende

Wenn Studierende die Entwicklungsumgebung neu aufsetzen, ist dieser
Pfad verbindlich:

```bash
# 1. Repository klonen
git clone <repository-url>
cd amalea

# 2. Standardumgebung für den Kurs starten
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim

# 3. Laufende Services prüfen
docker compose ps
```

Danach gilt für den Kursbetrieb:

1. Für Woche 1 bis 4 arbeitet ihr im Slim-Profil.
2. Für Woche 4 mit MLflow sowie für Woche 5 bis 7 startet ihr bei
   Bedarf das Full-Profil.
3. Lokale Python-Setups sind nur für Troubleshooting oder Wartung
   vorgesehen.

### Profile nach Kursphase

```bash
# Woche 1 bis 4
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim

# Woche 4 mit MLflow sowie Woche 5 bis 7
docker compose --profile full up -d

# Umgebung wieder beenden
docker compose down
```

### Minimaler Starttest

```bash
# Studentischer Pflichttest
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
docker compose ps
```

Wenn beide Services als laufend angezeigt werden und die Oberflächen
unter Port 8889 und 8502 erreichbar sind, ist die studentische
Entwicklungsumgebung korrekt eingerichtet.

### Lokaler Python-Pfad (nur technischer Ausnahmefall)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Diesen Pfad nutzt ihr nur, wenn Docker auf einem Gerät vorübergehend
nicht verfügbar ist oder wenn gezielt lokale Wartung nötig ist.

### Einzelne Container-Services

Baue nur das, was du aktuell brauchst:

```bash
# Nur Jupyter für Notebooks
docker build -f Dockerfile.jupyter -t amalea-jupyter .
docker run -p 8888:8888 amalea-jupyter

# Nur Streamlit für Apps
docker build -f Dockerfile.streamlit -t amalea-streamlit .
docker run -p 8501:8501 amalea-streamlit
```

---

## Dependencies

Das Repository verwendet modulare Requirements-Dateien.

- `requirements.txt`: leichter Standardstack für den Einstieg.
- `requirements-core.txt`: Basis-Abhängigkeiten.
- `requirements-dev.txt`: Test-, Lint- und Entwicklungswerkzeuge.
- `requirements-week01.txt` bis `requirements-week07.txt`:
  wochenspezifische Installationen.
- `requirements-*.lock.txt`: festgeschriebene Versionen für
  reproduzierbare Setups.
- `requirements.cloud.txt`: reduzierter Satz für Cloud-nahe Szenarien.

### Installationsbeispiele

```bash
# Standard für Woche 1 bis 3
pip install -r requirements-week03.txt

# Deep Learning
pip install -r requirements-week05.txt

# Computer Vision und NLP
pip install -r requirements-week06.txt

# Deployment-Demo
pip install -r requirements-week07.txt

# Entwicklungstools
pip install -r requirements-dev.txt

# Reproduzierbare Installation
pip install -r requirements-07.lock.txt
```

Installiere für den Kursbetrieb möglichst nur die Abhängigkeiten der
jeweiligen Woche.

Für Studierende ist die sicherste Reihenfolge:

1. zuerst `requirements.txt`
2. später nur bei Bedarf zusätzlich `requirements-week04.txt` bis
  `requirements-week07.txt`
3. nicht alle Wochen-Requirements gleichzeitig installieren, wenn sie
  nicht gebraucht werden

---

## Run Cheatsheet

### Docker Compose

```bash
# Volles Setup
docker-compose up --build

# Schlanke Services
docker compose up jupyter-lab-slim streamlit-slim
```

### Lokale Entwicklung

```bash
# W07 Backend
cd 07_Deployment_Portfolio
uvicorn backend.main:app --host 127.0.0.1 --port 8000

# W07 Dashboards lokal
API_URL=http://127.0.0.1:8000 \
streamlit run 04_streamlit_mlops_dashboard.py --server.port 8505

API_URL=http://127.0.0.1:8000 \
streamlit run 05_streamlit_nlp_dashboard.py --server.port 8506

# Compose für W07 (API + beide Dashboards)
docker compose up --build
```

### Notebooks

```bash
# CV-Notebooks gesammelt ausführen
./run_cv_notebooks.sh

# Beispiel: Woche 1 lokal öffnen
cd 01_Python_Grundlagen
jupyter lab
```

### Tests Und Qualität

```bash
pytest
make lint
make fmt
```

Für wiederkehrende Abläufe stehen zusätzlich `make install`,
`make test` und `make lint` bereit.

---

## Repository-Struktur

Das Repository ist nach Kurswochen gegliedert und enthält die
wichtigsten Materialien für Lehre, Übungen und Demonstrationen.

```text
amalea/
├── 01_Python_Grundlagen/
├── 02_Streamlit_und_Pandas/
├── 03_Machine_Learning/
├── 04_Advanced_Algorithms/
├── 05_Neural_Networks/
├── 06_Computer_Vision_NLP/
├── 07_Deployment_Portfolio/
├── executed_notebooks/
├── datasets/
├── Vorlesungseinheiten/
├── tests/
├── docker-compose.yml
├── Dockerfile.*
├── requirements*.txt
├── Makefile
├── pytest.ini
├── nightwatch.conf.js
├── README.md
├── DEVELOPER_GUIDE.md
├── DOZENTENLEITFADEN.md
├── KURSBESCHREIBUNG.md
└── LICENSE.md
```

---

## Kursinhalte

### Überblick Nach Wochen

- Woche 01: Python-Grundlagen, Pandas, QUA3CK und erste Apps.
- Woche 02: Streamlit-Ausführungsmodell und kleine Daten-Apps.
- Woche 03: Klassifikation, Regression und Modellintegration.
- Woche 04: Entscheidungsbäume, KNN, Clustering und MLflow.
- Woche 05: neuronale Netze und Trainingsverhalten.
- Woche 06: Computer Vision, Augmentation und Transfer Learning.
- Woche 07: lokale API, Dashboards und Deployment-Demo.

### Aktueller Stand Im Repository

- Woche 01 bis 04: stabiler Kurskern für regulären Lehrbetrieb.
- Woche 05 und 06: fachliche Vertiefungen mit höherem Ressourcenbedarf.
- Woche 07: Lehrdemo mit lokalem Backend und Dashboards.

Wichtige Beispiele:

- Woche 01:
  `00_Python_in_3_Stunden.ipynb`,
  `03_QUA3CK_Prozessmodell.ipynb`,
  `01_Python_Grundlagen/uebungs_app.py`
- Woche 02:
  `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb`,
  `02_Streamlit_und_Pandas/example_app.py`
- Woche 03:
  `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb`,
  `03_Machine_Learning/iris_ml_app.py`
- Woche 04:
  `04_Advanced_Algorithms/02_MLFlow_Big3_Tracking.ipynb`,
  `04_Advanced_Algorithms/03_Bäume_Nachbarn_und_Clustering.ipynb`
- Woche 07:
  `07_Deployment_Portfolio/01_MLOps_und_Deployment.ipynb`,
  `07_Deployment_Portfolio/backend/main.py`,
  `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`

Hinweise:

- Referenzfassungen liegen je nach Modul als `.nbconvert.ipynb`, in
  modulinternen `executed/`-Ordnern oder als lokal erzeugbare Ausgabe
  vor.
- Der Ordner `executed_notebooks/` ist als Ausgabeort vorgesehen, nicht
  als vollständiges Archiv garantiert.
- Woche 7 ist standardmäßig auf Demo-Betrieb ausgelegt. Der NLP-Teil
  arbeitet ohne Zusatzkonfiguration im heuristischen Modus.

## Copilot Und Agenten

Für Copilot-gestützte Repository-Arbeit liegen die projektweiten Regeln
und Agentenübersichten in `.github/`.

- [.github/README.md](.github/README.md): Übersicht über die
  spezialisierten Kursagenten und ihren Einsatzbereich.
- [.github/copilot-instructions.md](.github/copilot-instructions.md):
  immer geltende Repository-Regeln für Copilot im Workspace.

## Support Und Ressourcen

### Dokumentation

- [INSTALLATION.md](INSTALLATION.md): kompakte Matrix, was lokal und per
  Docker wie installierbar ist und was praktisch validiert wurde.
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md): technische Dokumentation für
  Aufbau, Betrieb und Entwicklung.
- [DOZENTENLEITFADEN.md](DOZENTENLEITFADEN.md): empfohlener Pflichtpfad
  und Hinweise für den Kursbetrieb.
- [BEWERTUNGSRUBRIK_PORTFOLIO.md](BEWERTUNGSRUBRIK_PORTFOLIO.md):
  kompakte Bewertungslogik für Portfolio- und Projektleistungen.
- [KURZGUIDE_PORTFOLIO_STUDIERENDE.md](KURZGUIDE_PORTFOLIO_STUDIERENDE.md):
  einseitige Schnellorientierung für Studierende zur Portfolioleistung.
- [ABGABE_TEMPLATE_PORTFOLIO.md](ABGABE_TEMPLATE_PORTFOLIO.md):
  kompakte Strukturvorlage für studentische Portfolio-Abgaben.
- [AUFGABENSTELLUNG_PORTFOLIO.md](AUFGABENSTELLUNG_PORTFOLIO.md):
  Rahmen für Pflichtumfang, Kür und Abgabeform der Portfolioleistung.
- [SITZUNGSPLAN_7_WOCHEN.md](SITZUNGSPLAN_7_WOCHEN.md): konkreter
  Ablaufvorschlag für sieben Lehrsitzungen.
- [KURSBESCHREIBUNG.md](KURSBESCHREIBUNG.md): formale Kursbeschreibung
  und Lernziele.
- [Makefile](Makefile): wiederkehrende Entwicklungs- und Testaufgaben.

### Bei Problemen

1. Zuerst die README-Datei des jeweiligen Wochenordners lesen.
2. Danach technische Details im `DEVELOPER_GUIDE.md` prüfen.
3. Bei Ausführungsproblemen zunächst die lokale oder schlanke Variante
   testen.
4. Nur die Requirements der gerade benötigten Woche installieren.

### Zusätzliche Materialien

- `Glossar_Alle_Begriffe_erklärt.ipynb` für Begriffe und Konzepte.
- `ML_DL_Mathematik.ipynb` für mathematische Grundlagen.
- `datasets/` für Kursdaten.
- `tests/` für automatisierte Prüfungen ausgewählter Teile des Repos.
