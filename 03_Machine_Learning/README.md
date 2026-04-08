
# Woche 3: Klassisches Machine Learning

Woche 3 führt in den praktischen Einsatz klassischer
Machine-Learning-Verfahren ein. Im Mittelpunkt stehen Training,
Vorhersage, Modellvergleich und die Einbindung in kleine Anwendungen.

## Lernziele

- den Unterschied zwischen Training und Inferenz erklären
- Train-Test-Split und Overfitting einordnen
- Klassifikation und Regression unterscheiden
- einfache Modelle mit scikit-learn trainieren und auswerten
- ML-Funktionalität in Streamlit-Anwendungen einbinden

## Materialien

- `02_ML_in_Streamlit_fixed.ipynb`: Grundkonzepte zu `fit()`,
  `predict()`, Evaluation und Modellvergleich
- `iris_ml_app.py`: Klassifikationsbeispiel mit interaktiven Eingaben
- `housing_regression_app.py`: Regressionsbeispiel mit Modellvergleich

## Empfohlene Reihenfolge

1. `02_ML_in_Streamlit_fixed.ipynb`
2. `iris_ml_app.py`
3. `housing_regression_app.py`

## Start

### Lokal

```bash
cd 03_Machine_Learning
pip install -r requirements.txt
streamlit run iris_ml_app.py
```

Für das Regressionsbeispiel:

```bash
cd 03_Machine_Learning
streamlit run housing_regression_app.py
```

### Mit Docker

```bash
docker-compose up --build
```

## Hinweise

- Die Apps eignen sich gut, um Metriken, Eingabefeatures und
  Modellverhalten im Plenum zu diskutieren.
- Der didaktische Schwerpunkt sollte auf Modellverständnis liegen,
  nicht auf möglichst vielen Algorithmen.
