# Sitzungsplan für 7 Wochen

Dieser Plan übersetzt den Dozentenleitfaden in eine konkret nutzbare
Abfolge für sieben Sitzungen mit jeweils etwa 90 Minuten. Er priorisiert
einen stabilen Kursbetrieb, begrenzte technische Risiken und klar
sichtbare Lernfortschritte.

## Grundprinzip

Jede Sitzung folgt möglichst dieser Struktur:

1. 15 Minuten: Einstieg, Begriffe, Ziel der Sitzung.
2. 30 Minuten: gemeinsames Notebook oder Live-Coding.
3. 20 Minuten: App, Demo oder geführtes Experiment.
4. 15 Minuten: kurze Eigenarbeit mit klarer Abgabe.
5. 10 Minuten: Auswertung, Transfer, nächste Schritte.

## Woche 1: Python, Pandas, QUA3CK

Ziel:

- Arbeitsweise im Kurs klären.
- Python-Grundlagen und Datenzugriff sichern.
- QUA3CK als Prozessrahmen einführen.

Pflichtmaterial:

- `01_Python_Grundlagen/00_Python_in_3_Stunden.ipynb`
- `01_Python_Grundlagen/03_QUA3CK_Prozessmodell.ipynb`
- `01_Python_Grundlagen/uebungs_app.py`

Minimaldemo:

- einfache Datenmanipulation im Notebook
- kleine Streamlit-App lokal starten

Arbeitsauftrag:

- eine kleine Datenoperation dokumentieren
- eine bestehende App minimal verändern

## Woche 2: Streamlit und Datenfluss

Ziel:

- das Rerun-Modell von Streamlit verstehen
- Widget-Interaktion und Datenfluss sichtbar machen

Pflichtmaterial:

- `02_Streamlit_und_Pandas/01_Erste_Streamlit_App_fixed.ipynb`
- `02_Streamlit_und_Pandas/example_app.py`

Minimaldemo:

- Widget ändern und Reaktion der App erklären
- Caching und Datenaktualisierung unterscheiden

Arbeitsauftrag:

- eine Eingabekomponente ergänzen
- eine einfache Visualisierung oder Kennzahl hinzufügen

## Woche 3: Klassisches Machine Learning

Ziel:

- Training, Inferenz und Evaluation sauber trennen
- Klassifikation und Regression gegenüberstellen

Pflichtmaterial:

- `03_Machine_Learning/02_ML_in_Streamlit_fixed.ipynb`
- `03_Machine_Learning/iris_ml_app.py`

Minimaldemo:

- Train-Test-Split erläutern
- ein Modell trainieren und Vorhersagen erklären

Arbeitsauftrag:

- Metriken vergleichen
- einen Parameter ändern und den Effekt beschreiben

## Woche 4: Big 3 und MLflow

Ziel:

- Decision Trees, KNN und K-Means fachlich einordnen
- Experiment-Tracking als Arbeitsweise einführen

Pflichtmaterial:

- `04_Advanced_Algorithms/02_MLFlow_Big3_Tracking.ipynb`
- `04_Advanced_Algorithms/03_Bäume_Nachbarn_und_Clustering.ipynb`

Minimaldemo:

- zwei Modellläufe vergleichen
- MLflow UI oder lokale Runs kurz zeigen

Arbeitsauftrag:

- einen Modellvergleich mit Begründung dokumentieren
- Vor- und Nachteile eines Verfahrens knapp formulieren

## Woche 5: Neuronale Netze

Ziel:

- Grundidee neuronaler Netze und Training erklären
- Überfitting, Aktivierung und Hyperparameter sichtbar machen

Pflichtmaterial:

- `05_Neural_Networks/04_Neural_Networks_in_Streamlit.ipynb`

Minimaldemo:

- Trainingsverlauf zeigen
- eine Aktivierungsfunktion oder Modellgröße variieren

Arbeitsauftrag:

- ein Trainingsproblem benennen
- einen sinnvollen Gegenmaßnahmen-Vorschlag formulieren

Hinweis:

- Auf schwacher Hardware notfalls nur Teilabschnitte live ausführen.

## Woche 6: Computer Vision und NLP

Ziel:

- CNN-Grundlagen und Bildmerkmale einordnen
- Augmentation und Transfer Learning als Konzepte zeigen

Pflichtmaterial:

- `06_Computer_Vision_NLP/06_01_neu_CNN_Basics.ipynb`
- `06_Computer_Vision_NLP/06_02_neu_OpenCV_Edge_Features.ipynb`

Minimaldemo:

- Feature-Maps oder Kantenoperatoren zeigen
- Unterschiede zwischen Exploration und belastbarer Modellierung
  diskutieren

Arbeitsauftrag:

- ein Bildmerkmal fachlich beschreiben
- den Nutzen von Augmentation oder Transfer Learning knapp einordnen

## Woche 7: API, Dashboards, Deployment-Demo

Ziel:

- lokale API und Dashboard zusammendenken
- Demo-Modus und Live-Modus unterscheiden
- Grenzen prototypischer Bereitstellung benennen

Pflichtmaterial:

- `07_Deployment_Portfolio/01_MLOps_und_Deployment.ipynb`
- `07_Deployment_Portfolio/03_QUA3CK_MLOps_Integration.ipynb`
- `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`

Minimaldemo:

- `/health` und `/predict` lokal aufrufen
- Dashboard erst im Demo-, dann im Live-Modus zeigen

Arbeitsauftrag:

- Unterschiede zwischen Demo- und Live-Betrieb dokumentieren
- einen sinnvollen Einsatzfall und eine Grenze des Moduls benennen

Hinweis:

- Der heuristische Standardmodus ist für den Kursbetrieb robuster als
  reale Transformers-Inferenz.

## Reserve und Kür

Wenn Zeit oder Leistungsstand es erlauben, eignen sich besonders:

- Woche 1: Docker-Notebook als Zusatz
- Woche 3: Housing-Regression als Vergleich
- Woche 5: Streamlit-Playground als Vertiefung
- Woche 6: Transfer-Learning-Notebook als Kür
- Woche 7: NLP-Dashboard oder Cloud-Deployment als Zusatzdemonstration
