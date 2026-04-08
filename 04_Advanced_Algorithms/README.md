# Woche 4: Fortgeschrittene Algorithmen

Woche 4 vertieft klassische Verfahren und ergänzt sie um einen ersten
MLOps-Blick. Im Zentrum stehen Entscheidungsbäume, KNN, K-Means und der
saubere Vergleich von Experimenten.

## Lernziele

- Entscheidungsbäume, KNN und K-Means fachlich einordnen
- überwachte und unüberwachte Verfahren vergleichen
- Hyperparameter bewusst variieren und Ergebnisse nachvollziehbar dokumentieren
- MLflow als Werkzeug für einfaches Experiment-Tracking kennenlernen

## Materialien

- `02_MLFlow_Big3_Tracking.ipynb`: MLflow-Einstieg mit den drei zentralen Verfahren
- `03_Bäume_Nachbarn_und_Clustering.ipynb`: vertiefende Theorie und praktische Beispiele
- `big3_streamlit_dashboard.py`: begleitende Visualisierung bzw. Demonstration

## Start

```bash
cd /Users/kqc/amalea
pip install -r requirements-week04.txt
cd 04_Advanced_Algorithms
jupyter notebook 02_MLFlow_Big3_Tracking.ipynb
```

Für das zweite Notebook:

```bash
cd 04_Advanced_Algorithms
jupyter notebook 03_Bäume_Nachbarn_und_Clustering.ipynb
```

## Hinweise

- MLflow kann lokal mit `file:./mlruns` genutzt werden. Wenn der Server
  läuft, ist auch `http://localhost:5001` möglich.
- Die Notebooks sind für kurze Demonstrationen ausgelegt; größere
  Hyperparameter-Raster sollten im Kurs bewusst klein gehalten werden.
- Das Modul eignet sich gut, um Modellwahl und Grenzen einzelner
  Verfahren vergleichend zu besprechen.
