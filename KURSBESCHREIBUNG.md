# AMALEA 2025 - Data Analytics & Big Data

<div align="center">
  <img src="./kurs-logo.png" alt="AMALEA 2025 Logo" width="400">
</div>

## Kursbeschreibung

> **AMALEA** = **"Angewandte Machine Learning Algorithmen"**  
> Basiert auf dem erfolgreichen AMALEA-Programm des KI-Campus: [ki-campus.org/amalea](https://ki-campus.org/amalea)

### Überblick

AMALEA 2025 ist ein praxisorientierter, notebook-basierter Kurs zu Data Analytics und Machine Learning für Informatik-Studierende ab dem 5. Semester. Der Kurs baut auf dem Programm **"Angewandte Machine Learning Algorithmen"** des KI-Campus auf und ergänzt es um interaktive Web-Anwendungen, grundlegende Deployment-Szenarien und ausgewählte MLOps-Themen. Er verbindet theoretische Grundlagen mit praktischer Arbeit an Notebooks, kleinen Anwendungen und nachvollziehbaren Projektartefakten. Das Repository umfasst im aktuellen Stand **17 Jupyter-Notebooks** und **12 Streamlit-Anwendungen** unterschiedlicher Reifegrade.

### Pädagogisches Konzept

Der Kurs folgt einem projektbasierten Lernansatz. Woche für Woche werden aufeinander aufbauende Kompetenzen vermittelt: von Python-Grundlagen und Datenmanipulation über klassisches Machine Learning bis hin zu neuronalen Netzen, Computer Vision, NLP und einfachen Deployment-Szenarien. Jede Woche enthält ein klar umrissenes Lernpaket aus Notebook, Anwendung oder Demo.

Ein zentrales Merkmal des Kurses ist der Wechsel zwischen fachlichem Verständnis und sichtbaren Ergebnissen. Anstelle rein theoretischer Übungen erstellen die Studierenden kleine Anwendungen, testen Modelle an Beispieldaten und dokumentieren ihre Arbeitsschritte. So werden Analyse, Modellierung, Visualisierung und Kommunikation zusammen gedacht.

### Lernziele und Kompetenzen

Nach erfolgreichem Abschluss des Kurses verfügen die Studierenden über ein belastbares Grundgerüst für datenorientierte Softwareprojekte. Sie können Daten mit Python aufbereiten, einfache bis mittlere Machine-Learning-Pipelines entwickeln, Ergebnisse bewerten und interaktive Oberflächen mit Streamlit erstellen.

Die Teilnehmer lernen TensorFlow und Keras als Werkzeuge für neuronale Netze kennen und erhalten Einblicke in Computer Vision und Natural Language Processing. Ergänzend erwerben sie Grundlagen zu MLOps, Experiment-Tracking und API-Design. Im Deployment-Modul arbeiten sie mit einer FastAPI-Demo und zwei Dashboards; für NLP steht standardmäßig ein leichtgewichtiger Demo-Betrieb zur Verfügung, optional auch ein erweiterter Modus mit Hugging-Face-Pipelines.

### Kursstruktur und Inhalte

Der siebenwöchige Kurs ist in aufeinander aufbauende Module gegliedert, die jeweils spezifische Lernziele verfolgen. Die erste Woche etabliert solide Python-Grundlagen und führt in die Arbeit mit Pandas für Datenmanipulation ein. Ein besonderes Highlight ist das "Python in 3 Stunden" Notebook, das auch für Quereinsteiger einen schnellen, aber gründlichen Einstieg ermöglicht.

Die zweite Woche konzentriert sich auf die Entwicklung interaktiver Web-Anwendungen mit Streamlit und vertieft die Datenanalyse-Kompetenzen. Hier erstellen die Studierenden ihre erste kleine Anwendung und lernen die Grundlagen zustandsloser Web-Interaktionen kennen. Die dritte Woche führt systematisch in Machine Learning ein, wobei der Fokus auf praktischer Anwendung und der Einbindung von Modellen in einfache Benutzeroberflächen liegt.

Ein zentraler Baustein des Kurses ist die vierte Woche mit dem "Big 3"
Notebook, das eine praktische Einführung in Decision Trees,
K-Nearest Neighbors und K-Means Clustering bietet. Dieses Modul
verbindet theoretisches Verständnis mit intensiver praktischer
Anwendung.

Die fünfte Woche vertieft neuronale Netze und Deep Learning. Die sechste Woche behandelt Computer Vision und Natural Language Processing mit mehreren spezialisierten Notebooks und ergänzendem Bildmaterial. Die siebte Woche konzentriert sich auf Deployment, MLOps und Portfolio-Artefakte mit einer FastAPI-Demo, zwei Dashboards und drei kompakten Notebooks. Dabei stehen API-Handling, Monitoring-Ideen und die Einordnung eines prototypischen Deployment-Ablaufs im Vordergrund.

**Repository-Organisation:** Alle Kursmaterialien sind in wochenspezifischen Ordnern (01_Python_Grundlagen/ bis 07_Deployment_Portfolio/) strukturiert. Referenzfassungen liegen je nach Modul als `.nbconvert.ipynb`, in `executed/`-Ordnern oder als lokal erzeugbare Ausgabe vor. `datasets/` enthält die Datensätze für praktische Übungen, `Vorlesungseinheiten/` vertieft theoretische Konzepte, und `tests/` bündelt automatisierte Prüfungen für ausgewählte Teile des Repos.

### Aktuelle Kursstruktur im Detail (2025)

Der aktuelle Stand des Repositories umfasst **29 größere Lern- und Projektartefakte** in modularer Struktur:

| Woche | Thema | Core Notebooks | Streamlit Apps | Fokus |
|-------|-------|----------------|----------------|--------|
| **01** | Python Grundlagen | 4 | 3 | Foundation + QUA³CK Framework + Docker |
| **02** | Streamlit & Pandas | 1 | 3 | Interactive Web Development |
| **03** | Machine Learning | 1 | 2 | ML Pipeline Development |
| **04** | Advanced Algorithms | 2 | 1 | Ensembles & Unsupervised, MLflow/DVC Intro |
| **05** | Neural Networks | 1 | 1 | Keras Basics & Transfer Learning Lite |
| **06** | Computer Vision & NLP | 5 | 0 | CV/NLP Fundamentals + Augmentation/Transfer |
| **07** | Deployment & Portfolio | 3 | 2 | FastAPI + Monitoring Dashboards (HF-Pipelines) |

**Gesamt: 17 Core Notebooks + 12 Streamlit Apps = 29 Portfolio-Komponenten**

**Zusätzliche Ressourcen:**
- **Executed Notebooks** (`executed_notebooks/`): vorgesehener Ausgabeort für ausgeführte Notebooks; weitere Referenzfassungen liegen modulweise vor
- **Datasets** (`datasets/`): Alle Kurs-Datensätze für praktische Übungen
- **Vorlesungseinheiten** (`Vorlesungseinheiten/`): Vertiefende Vorlesungseinheiten zu theoretischen Konzepten
- **Tests** (`tests/`): Umfassende Test-Suite für Qualitätssicherung
- **Backup** (`BACKUP_Original_AMALEA_Notebooks/`): Original-Versionen für Vergleich

### QUA³CK Framework Integration

Alle Projekte folgen dem systematischen **QUA³CK Prozessmodell**:
- **Q**uestion: Business Problem Definition & Requirements Analysis
- **U**nderstand: Comprehensive Data Exploration & Statistical Analysis  
- **A**cquire & Clean: Professional Data Pipeline & ETL Development
- **A**nalyze: Machine Learning Model Development mit MLFlow Tracking
- **A**pp: Bereitstellung einer Streamlit-Anwendung oder eines Dashboards
- **C**onclusion & **K**ommunikation: Portfolio Documentation & Presentation

### Innovative Technologien und Tools

Der Kurs setzt auf verbreitete Werkzeuge aus Data Science und Machine Learning. Python 3.11+ bildet das Fundament, ergänzt durch Pandas, NumPy und Scikit-learn für klassisches Machine Learning. Für Deep Learning kommen TensorFlow und Keras zum Einsatz. Hugging Face Transformers wird als optionaler Einstieg in moderne NLP-Bibliotheken genutzt. Dependencies sind pro Woche getrennt, damit Installationen schlank und nachvollziehbar bleiben.

Ein besonderer Fokus liegt auf Streamlit als Framework für interaktive Web-Anwendungen. Docker unterstützt die lokale Reproduzierbarkeit der Umgebung. Mehrere Dockerfile-Varianten und Compose-Setups erleichtern die Arbeit mit unterschiedlichen Ressourcenprofilen.

Für Experiment-Tracking und MLOps wird MLflow eingeführt. Git und GitHub dienen der Versionskontrolle. Visualisierungen entstehen mit Plotly und Matplotlib. Qualitätssicherung erfolgt mit pytest, ruff, black und einem Makefile für wiederkehrende Abläufe.

### ML/DL-Algorithmen und Demos pro Woche (Auswahl)

- **W01–W02 (Basics & Apps):** Deskriptive Statistik, Pandas-Transformationen, einfache Visualisierungen; Streamlit-Widgets zur Datenexploration.
- **W03 (Classic ML):** Scikit-Learn Pipelines, Logistische Regression & RandomForest für Klassifikation, Lineare Regression für Housing; Hyperparameter-Playgrounds in Streamlit.
- **W04 (Advanced/MLops):** Ensembles (RandomForest/GradientBoosting-Patterns), Clustering (K-Means), Anomalie-Detektion; MLflow/DVC-Einstieg.
- **W05 (Deep Learning):** Keras-Sequential/Functional API, Dense-Netze für Tabulardaten, leichtgewichtige Transfer-Learning-Setups.
- **W06 (CV/NLP):** CNN-Grundlagen, Edge/Feature-Extraction mit OpenCV, Data Augmentation, Transfer Learning Lite; Transformers-Demo für Text (CPU-freundlich).
- **W07 (Deployment):** FastAPI-Demo mit Sklearn-Iris-Modell; NLP-Endpunkte mit leichten HF-Pipelines (Sentiment/QA/Generate) für API/Monitoring/Deployment-Übungen; zwei Streamlit-Dashboards für Monitoring & NLP.

### Studienleistung: Portfolio laut Prüfungsordnung

Die Studienleistung ist auf die Entwicklung einer zusammenhängenden MLOps-Anwendung ausgerichtet. Dazu gehören eine End-to-End-Machine-Learning-Pipeline, eine interaktive Streamlit-Web-App und ein nachvollziehbarer Deployment-Teil. Der Schwerpunkt liegt auf dem Verständnis und der Dokumentation des Gesamtprozesses, nicht auf dem Nachweis eines vollständig ausgehärteten Produktivsystems.

Die Studierenden haben maximale Freiheit bei der Themenwahl und werden ermutigt, Projekte zu entwickeln, die ihre persönlichen Interessen widerspiegeln und als Vorstudie für ihr Bachelorprojekt dienen können. Zur Inspiration werden Beispiele aus verschiedenen Bereichen angeboten: Predictive Analytics für Immobilienpreise, Computer Vision für medizinische Bildanalyse, NLP für Social Media Sentiment Analysis oder Business Intelligence Dashboards für Sales Forecasting.

### Datenquellen und Praxisbezug

Ein wesentlicher Aspekt des Kurses ist die Arbeit mit echten, großen Datensätzen aus verschiedenen Domänen. Die Studierenden lernen, öffentlich verfügbare Big Data Quellen zu nutzen, darunter Kaggle Datasets mit Millionen von Datensätzen, Google Dataset Search für spezialisierte Datenquellen, AWS Open Data für Cloud-basierte Anwendungen und Regierungsdatenportale wie Data.gov und das European Data Portal.

Für Business-Anwendungen stehen APIs wie Yahoo Finance für Finanzdaten, World Bank Open Data für wirtschaftliche Analysen und IMF-Daten für internationale Statistiken zur Verfügung. Wissenschaftliche Projekte können auf das UCI Machine Learning Repository, Papers with Code Datasets oder NASA Open Data zugreifen. Social Media und Entertainment-Anwendungen nutzen MovieLens für Empfehlungssysteme, Spotify API für Musikanalysen oder Reddit API für Social Media Analytics.

### Portfolio-Entwicklung und Karrierevorbereitung

Ein zentrales Ziel des Kurses ist der Aufbau nachvollziehbarer Arbeitsproben. Die **29 Portfolio-Komponenten** aus Notebooks und Streamlit-Anwendungen dokumentieren technische Grundlagen, Modellierungsentscheidungen und den Umgang mit Werkzeugen entlang eines kompletten Arbeitsablaufs.

Nicht alle Artefakte sind auf denselben Betriebsgrad ausgelegt. Einige Bausteine sind als Kurskern stabil einsetzbar, andere dienen bewusst als Lehrdemo oder als Ausgangspunkt für eigene Ausarbeitungen. Ergänzend bieten Referenzfassungen der Notebooks und die Vorlesungseinheiten Orientierung für Selbststudium und Wiederholung.

Diese Herangehensweise bereitet auf typische Aufgaben in Data-Science- und ML-Projekten vor. Neben der technischen Umsetzung werden auch Kommunikation, Strukturierung und Dokumentation von Ergebnissen eingeübt.

### Technische Infrastruktur und Support

Für den Kurs stehen Docker- und lokale Entwicklungswege bereit. Mit `docker-compose up` lässt sich eine gemeinsame Umgebung mit Jupyter, Streamlit und MLflow starten. Ergänzend gibt es schlankere Varianten für ressourcenschonende Setups.

Das Repository ist modular strukturiert und nutzt wochenspezifische Requirements-Dateien. Ein Makefile unterstützt wiederkehrende Aufgaben wie Installieren, Testen, Linting und Formatierung. `datasets/` enthält die Kursdaten; Referenzfassungen von Notebooks liegen je nach Modul an unterschiedlichen Stellen im Repository.

Für lokale Installationen stehen detaillierte Hinweise zu Abhängigkeiten und Startbefehlen bereit. Zusätzlich helfen Vorlesungseinheiten, Glossar, Datasets und ausgewählte Tests bei der Vertiefung und Absicherung einzelner Themen.

### Integration originaler AMALEA-Inhalte

Der Kurs baut auf dem bewährten **"Angewandte Machine Learning Algorithmen"**-Programm des KI-Campus auf und integriert die pädagogischen Konzepte in moderne, praktische Anwendungen. Die bewährten methodischen Ansätze werden beibehalten, während gleichzeitig modernste Technologien und Deployment-Strategien vermittelt werden.

### Zukunftsorientierung und Industrie-Relevanz

AMALEA 2025 orientiert sich an verbreiteten Arbeitsweisen in Data-Science- und Machine-Learning-Projekten. Die vermittelten Technologien und Methoden bereiten auf Rollen wie Data Scientist, ML Engineer oder Data Product Manager vor. Besonders wertvoll ist dabei die Verbindung von Analyse, Modellierung, Visualisierung und einfacher Bereitstellung.

Der Kurs bereitet auch auf weiterführende Studien vor, insbesondere für
Masterstudiengänge im Bereich Data Science, Artificial Intelligence oder
Machine Learning. Die erworbenen Kompetenzen in MLOps und
Cloud-Deployment sind dabei eine sinnvolle Grundlage für fortgeschrittene
Forschungsprojekte und industrielle Kooperationen.

---

*AMALEA 2025 verbindet bewährte pädagogische Konzepte mit einer modularen technischen Lernumgebung. Mit **29 Portfolio-Komponenten** aus Notebooks und Anwendungen, klarer Wochenstruktur und begleitenden Entwicklungstools eignet sich das Repository gut für einen projektorientierten Kurs in Data Analytics und Big Data.*
