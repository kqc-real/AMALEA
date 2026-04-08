# 07 Deployment & Portfolio

Dieses Modul bündelt den produktionsnahen Teil des Kurses. Im
Mittelpunkt stehen drei Themen: eine kleine HTTP-API mit FastAPI, zwei
Streamlit-Dashboards und der Unterschied zwischen Demo-Betrieb und
Live-Betrieb.

## Einordnung

Woche 7 ist als Lehrdemo gedacht. Das Modul ist gut geeignet, um
Serving, Dashboards, lokale Ausführung und einfache
Deployment-Abläufe zu besprechen. Es ist nicht als vollständig
ausgehärteter Produktionsstack dokumentiert.

## Lernziele

- Eine einfache ML-API lokal starten und ansprechen
- Dashboards mit einer API verbinden
- Demo-Modus und Live-Modus unterscheiden
- grundlegende Deployment- und MLOps-Begriffe einordnen
- Grenzen einer prototypischen Lösung benennen

## Materialien

### Notebooks

- **01_MLOps_und_Deployment.ipynb**: kleine Iris-Demo mit Modelltraining und Artefaktexport
- **02_NLP_und_Text_Generation.ipynb**: kompakte NLP-Demo mit
  leichtgewichtigen Beispielantworten
- **03_QUA3CK_MLOps_Integration.ipynb**: Health- und Predict-Checks gegen das Backend

### Dashboards

- **04_streamlit_mlops_dashboard.py**: Dashboard für `/health` und `/predict`
- **05_streamlit_nlp_dashboard.py**: Oberfläche für `/generate`,
  `/sentiment` und `/qa`

## Empfohlener Ablauf im Kurs

1. Backend starten oder die Dashboards zunächst im Demo-Modus verwenden.
2. Das Notebook **01_MLOps_und_Deployment.ipynb** für Training, Export
   und Serving-Kontext durcharbeiten.
3. Das Notebook **02_NLP_und_Text_Generation.ipynb** als Beispiel für
   eine leichtgewichtige NLP-Demo einsetzen.
4. Das Notebook **03_QUA3CK_MLOps_Integration.ipynb** nutzen, um
   Requests und Responses gegen die API nachzuvollziehen.
5. Danach die Dashboards erst im Demo-Modus und anschließend im
   Live-Modus mit gesetzter `API_URL` öffnen.

## Backend

Die FastAPI-Demo liegt unter `backend/main.py`.

- Endpunkte: `/health`, `/predict`, `/sentiment`, `/qa`, `/generate`
- Iris-Vorhersagen laufen lokal und CPU-basiert.
- Die NLP-Endpunkte arbeiten standardmäßig in einem heuristischen
  Demo-Modus. Dadurch bleibt das Backend ohne große Modell-Downloads
  lauffähig.
- Optional kann ein Transformers-Modus aktiviert werden.

### Lokaler Start

```bash
cd 07_Deployment_Portfolio
pip install -r requirements.cloud.txt
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### Optionaler Transformers-Modus

Wer reale Hugging-Face-Pipelines demonstrieren möchte, kann zusätzliche
Abhängigkeiten installieren und den Modus explizit aktivieren:

```bash
cd 07_Deployment_Portfolio
pip install -r ../requirements-week07-transformers.txt
export AMALEA_ENABLE_TRANSFORMERS=1
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Ohne diese Zusatzschritte bleibt das Backend im heuristischen Demo-Modus.

### Start mit Docker Compose

```bash
cd 07_Deployment_Portfolio
docker compose up --build
```

Verfügbare URLs:

- API: [http://localhost:8000](http://localhost:8000)
- MLOps-Dashboard: [http://localhost:8505](http://localhost:8505)
- NLP-Dashboard: [http://localhost:8506](http://localhost:8506)

## Dashboards lokal starten

```bash
cd 07_Deployment_Portfolio
pip install -r requirements.cloud.txt

streamlit run 04_streamlit_mlops_dashboard.py --server.port 8505
streamlit run 05_streamlit_nlp_dashboard.py --server.port 8506
```

Hinweise:

- Der Demo-Modus funktioniert ohne Backend.
- Der Live-Modus erwartet eine erreichbare API unter
  `http://localhost:8000` oder unter der in der Sidebar gesetzten
  `API_URL`.
- Die Dashboards eignen sich gut für Lehre und Demonstration, nicht als
  Monitoring-Ersatz für einen echten Produktivbetrieb.

## Technische Einordnung

- **FastAPI** für HTTP-Endpunkte
- **Streamlit** für einfache Oberflächen
- **Docker Compose** für den lokalen Mehrdienstbetrieb
- **MLflow** als begleitendes Thema für Experiment- und Modellverwaltung
- **optionale Transformers-Integration** für einen erweiterten NLP-Demobetrieb

## Grenzen des Moduls

- Das Modul zeigt Grundmuster, keine vollständige Betriebsplattform.
- Die Monitoring-Ansicht arbeitet im Demo-Modus mit simulierten Daten.
- Für reale NLP-Pipelines sind zusätzliche Abhängigkeiten und meist auch
  Internetzugang erforderlich.
- Lehrwert und Nachvollziehbarkeit haben hier Vorrang vor technischer Vollständigkeit.
