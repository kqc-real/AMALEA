# Woche 4: Fortgeschrittene Algorithmen

Woche 4 vertieft klassische Verfahren und ergänzt sie um einen ersten
MLOps-Baustein. Im Mittelpunkt stehen Entscheidungsbäume, KNN,
K-Means und der nachvollziehbare Vergleich von Experimenten.

## Lernziele

- Entscheidungsbäume, KNN und K-Means fachlich einordnen
- überwachte und unüberwachte Verfahren vergleichen
- Hyperparameter bewusst variieren und Ergebnisse nachvollziehbar
  dokumentieren
- MLflow als Werkzeug für einfaches Experiment-Tracking kennenlernen

## Materialien

- `02_MLFlow_Big3_Tracking.ipynb`: MLflow-Einstieg mit den drei
  zentralen Verfahren
- `03_Bäume_Nachbarn_und_Clustering.ipynb`: vertiefende Theorie und
  praktische Beispiele
- `big3_streamlit_dashboard.py`: begleitende Visualisierung bzw. Demonstration

## Start

### Docker-Standardpfad

```bash
cd ..
docker compose --profile full up -d
```

Danach könnt ihr die Notebooks in Woche 4 in der laufenden Umgebung
öffnen, vor allem:

- `02_MLFlow_Big3_Tracking.ipynb`
- `03_Bäume_Nachbarn_und_Clustering.ipynb`

### Lokaler Zusatzpfad (nur technischer Ausnahmefall)

```bash
cd /Users/kqc/amalea
pip install -r requirements-week04.txt
cd 04_Advanced_Algorithms
jupyter notebook 02_MLFlow_Big3_Tracking.ipynb
```

## Hinweise

- Für den regulären Kursbetrieb ist auch in Woche 4 Docker der
  Standardpfad.
- MLflow kann lokal mit `file:./mlruns` genutzt werden. Wenn der Server
  läuft, ist auch `http://localhost:5001` möglich.
- Die Notebooks sind für kurze Demonstrationen ausgelegt; größere
  Hyperparameter-Raster sollten im Kurs bewusst klein gehalten werden.
- Das Modul eignet sich gut, um Modellwahl und Grenzen einzelner
  Verfahren vergleichend zu besprechen.
