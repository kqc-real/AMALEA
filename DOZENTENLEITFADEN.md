# Dozentenleitfaden

Dieser Leitfaden richtet sich an Lehrende, die das Repository im Kurs
einsetzen oder übernehmen. Er beschreibt einen belastbaren Pflichtpfad,
reduziert technische Risiken und hilft dabei, den Kurs mit überschaubarem
Betriebsaufwand durchzuführen.

Für eine konkret taktbasiere Umsetzung ergänzt
`SITZUNGSPLAN_7_WOCHEN.md` diesen Leitfaden.

## Grundsatz

Dieses Repository ist am stärksten als Lehrsammlung mit stabilem
Kurskern in Woche 1 bis 4 und mit ergänzenden Vertiefungen in Woche 5
bis 7. Für den Kursbetrieb ist eine kuratierte Nutzung sinnvoller als
eine Vollabdeckung aller Artefakte.

Empfohlene Leitlinien:

- Docker Compose als gemeinsame Pflichtumgebung für den Kurs nutzen
- lokale Python-Setups nur als Wartungs- oder Troubleshooting-Pfad behandeln
- pro Woche genau ein Pflicht-Notebook und höchstens eine Pflicht-App
- W07 als Lehrdemo behandeln, nicht als verpflichtenden Produktivpfad
- Tooling immer dem Lernziel unterordnen

## Minimaler Kursbetrieb

Für einen stabilen Lehrbetrieb genügt in der Regel folgendes Setup:

- Docker-Compose-Slim-Profil für Woche 1 bis 4
- Docker-Compose-Full-Profil für MLflow sowie Woche 5 bis 7 bei Bedarf
- Jupyter Lab für Notebooks
- Streamlit für ausgewählte Apps
- MLflow nur in Woche 4 und Woche 7 bei Bedarf

Nicht als Pflicht voraussetzen:

- Streamlit Cloud Deployment für alle Studierenden
- externe APIs oder öffentliche Bereitstellung
- reale Hugging-Face-Inferenz im Unterrichtsbetrieb

## Installationsentscheidungen in Kürze

Für die Kursdurchführung haben sich diese Entscheidungen bewährt:

1. Standardmäßig Docker Compose als erste Lernumgebung nutzen.
2. Woche 1 bis 4 im Slim-Profil starten.
3. Für MLflow sowie Woche 5 bis 7 bei Bedarf auf das Full-Profil wechseln.
4. `requirements.txt` nur als technischen Referenzpfad für Woche 1 bis 3 behandeln.
5. Woche 5 standardmäßig nur mit `requirements-week05.txt`
  fahren; PyTorch nur bei Bedarf über
  `requirements-week05-torch.txt` ergänzen.
6. Woche 7 standardmäßig mit `requirements-week07.txt` und
  Demo-Modus betreiben; Transformers nur gezielt über
  `requirements-week07-transformers.txt` zuschalten.
7. Lokale Python-Umgebungen nur als Ausweichpfad oder für Debugging nutzen.
8. Full-Docker vor allem für Lehrende, Vorabtests und
  vorbereitete Demo-Rechner einplanen.

Die ausführlichere Matrix mit lokalem und Docker-Status steht in
`INSTALLATION.md`.

## Pflichtpfad pro Woche

### Woche 1

Pflicht:

- `01_Python_Grundlagen/01_Docker_für_Data_Science.ipynb`
- `01_Python_Grundlagen/00_Python_in_3_Stunden.ipynb`
- `01_Python_Grundlagen/03_QUA3CK_Prozessmodell.ipynb`
- `01_Python_Grundlagen/uebungs_app.py`

Optional:

- `01_Python_Grundlagen/meine_erste_app.py`

Didaktischer Fokus:

- Python-Arbeitsweise, Pandas-Grundlagen, Unterschied Notebook und App,
  QUA3CK als Prozessrahmen

### Woche 2

Pflicht:

- `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb`
- `02_Streamlit_und_Pandas/example_app.py`

Optional:

- `02_Streamlit_und_Pandas/hello_streamlit.py`

Didaktischer Fokus:

- Streamlit-Rerun-Modell, Interaktion, Datenfluss, Caching,
  Strukturierung kleiner Oberflächen

### Woche 3

Pflicht:

- `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb`
- `03_Machine_Learning/iris_ml_app.py`

Optional:

- `03_Machine_Learning/housing_regression_app.py`

Didaktischer Fokus:

- `fit()` und `predict()`, Train-Test-Split, Overfitting, Metriken,
  Klassifikation vor Regression

### Woche 4

Pflicht:

- `04_Advanced_Algorithms/02_MLFlow_Big3_Tracking.ipynb`
- `04_Advanced_Algorithms/03_Bäume_Nachbarn_und_Clustering.ipynb`

Optional:

- `04_Advanced_Algorithms/big3_streamlit_dashboard.py`

Didaktischer Fokus:

- Entscheidungsbäume, KNN, K-Means, Vergleich von Verfahren,
  Einführung in Experiment-Tracking mit MLflow

### Woche 5

Pflicht:

- `05_Neural_Networks/04_Neural_Networks_in_Streamlit.ipynb`

Optional:

- `05_Neural_Networks/neural_network_playground.py`

Didaktischer Fokus:

- Grundidee neuronaler Netze, Aktivierungsfunktionen, Backpropagation,
  Hyperparameter und Trainingsverhalten

### Woche 6

Pflicht:

- `06_Computer_Vision_NLP/06_01_neu_CNN_Basics.ipynb`
- `06_Computer_Vision_NLP/06_02_neu_OpenCV_Edge_Features.ipynb`

Optional:

- `06_Computer_Vision_NLP/06_03_neu_Data_Augmentation_Practice.ipynb`
- `06_Computer_Vision_NLP/06_04_neu_Transfer_Learning_Lite.ipynb`
- `06_Computer_Vision_NLP/06_05_neu_Image_Sampler.ipynb`

Didaktischer Fokus:

- CNN-Grundlagen, Bildmerkmale, Augmentation als Konzept,
  Transfer Learning nur als Einblick oder Vertiefung

### Woche 7

Pflicht:

- `07_Deployment_Portfolio/01_MLOps_und_Deployment.ipynb`
- `07_Deployment_Portfolio/03_QUA3CK_MLOps_Integration.ipynb`
- `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`

Optional:

- `07_Deployment_Portfolio/02_NLP_und_Text_Generation.ipynb`
- `07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py`

Didaktischer Fokus:

- API-Grundidee, Demo- gegen Live-Betrieb, Monitoring-Ideen,
  Grenzen prototypischer Deployment-Szenarien

Hinweis:

- Das Backend ist absichtlich auf Demo-Betrieb ausgelegt. Reale
  Transformers-Inferenz sollte nur gezielt und optional gezeigt werden.

## Sitzungsrhythmus

Für eine 90-minütige Sitzung ist dieses Muster belastbar:

1. 15 Minuten: Kontext, Lernziel, Begriffe
2. 30 Minuten: gemeinsames Notebook oder Live-Coding
3. 20 Minuten: App, Demo oder kontrolliertes Experiment
4. 15 Minuten: kurze Eigenarbeit mit klarer Aufgabe
5. 10 Minuten: Auswertung, Transfer, offene Fragen

Wenn weniger Zeit vorhanden ist, sollte zuerst die App-Demo gekürzt
werden, nicht die konzeptionelle Einordnung.

## Technische Risikoquellen

Besonders aufmerksam prüfen:

- lokale Python-Umgebung und passende Wochen-Requirements
- TensorFlow in Woche 5 und Transfer Learning in Woche 6 auf schwacher
  Hardware
- MLflow nur dort aktivieren, wo der Mehrwert im Unterricht erkennbar
  ist
- W07 nur im Demo-Modus als Standardpfad verwenden

## Vorbereitung vor Kursstart

1. Den Pflichtpfad einmal vollständig selbst durchlaufen.
2. Pro Woche eine Minimaldemo und eine Ausweichdemo festlegen.
3. Entscheiden, ob Docker im Kurs Pflicht, Kür oder reine Vorführung ist.
4. Die Bewertungen auf Lernprozess, Dokumentation und Nachvollziehbarkeit
   ausrichten, nicht auf technischen Ausbaugrad allein.

## Empfehlung zur Bewertung

Für Leistungsnachweise ist eine klare Trennung hilfreich:

- Pflicht: funktionierende Grundlösung, nachvollziehbare Dokumentation,
  saubere Problemdefinition
- Kür: zusätzliche App-Funktionen, Cloud-Bereitstellung,
  erweiterte Modellierung, aufwendigere Visualisierung

Eine ausformulierte Bewertungsgrundlage steht in
`BEWERTUNGSRUBRIK_PORTFOLIO.md`.

Für eine einheitliche studentische Dokumentation kann zusätzlich
`ABGABE_TEMPLATE_PORTFOLIO.md` verwendet werden.

Als gemeinsame Aufgabenbasis eignet sich
`AUFGABENSTELLUNG_PORTFOLIO.md`.

Damit bleibt der Kurs fair für Studierende mit unterschiedlicher
technischer Ausgangslage.
