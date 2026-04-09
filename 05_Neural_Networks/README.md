# Woche 5: Neuronale Netze

Woche 5 führt in die Grundideen des Deep Learning ein. Behandelt werden
Aufbau und Training einfacher neuronaler Netze sowie zentrale Begriffe
wie Aktivierungsfunktion, Backpropagation und Hyperparameter.

## Lernziele

- Aufbau und Funktionsweise einfacher neuronaler Netze erklären
- Aktivierungsfunktionen und Softmax einordnen
- Backpropagation und Gradientenverfahren fachlich beschreiben
- typische Trainingsprobleme erkennen und erste Gegenmaßnahmen ableiten
- ein kleines Deep-Learning-Beispiel im Notebook und in Streamlit
  nachvollziehen

## Materialien

- `04_Neural_Networks_in_Streamlit.ipynb`: Hauptnotebook für Grundlagen
  und Beispiele
- `neural_network_playground.py`: begleitende Streamlit-Anwendung zum Experimentieren

## Start

### Docker-Standardpfad

```bash
cd ..
docker compose --profile full up -d
```

Danach arbeitet ihr in Woche 5 in der laufenden Umgebung in der Regel
mit dem Notebook `04_Neural_Networks_in_Streamlit.ipynb`.

### Streamlit-App starten

```bash
cd 05_Neural_Networks
streamlit run neural_network_playground.py
```

### Lokaler Zusatzpfad (nur technischer Ausnahmefall)

```bash
cd /Users/kqc/amalea
pip install -r requirements-week05.txt
cd 05_Neural_Networks
jupyter notebook 04_Neural_Networks_in_Streamlit.ipynb
```

## Hinweise

- Für den regulären Kursbetrieb bleibt Docker auch in Woche 5 der
  Standardpfad.
- TensorFlow ist ressourcenintensiver als die bisherigen Wochen. Für
  schwächere Rechner kann eine CPU-Ausführung mit reduzierten Parametern
  sinnvoll sein.
- PyTorch ist für dieses Modul nicht Teil der Standardinstallation.
  Wenn es gezielt für eigene Erweiterungen gebraucht wird, kann es
  zusätzlich mit `pip install -r ../requirements-week05-torch.txt`
  installiert werden.
- Für Lehrzwecke ist es meist besser, wenige Trainingsläufe bewusst zu
  analysieren, statt lange Modelle zu trainieren.
- Seeds und Versionsstände sollten bei Vorführungen mitgeführt werden,
  damit Ergebnisse nachvollziehbar bleiben.

## Typische Stolperstellen

- Wenn Pakete fehlen, sollte `requirements-week05.txt` aus dem
  Repository verwendet werden.
- Bei belegten Ports kann Streamlit mit `--server.port 8502` oder einem
  anderen freien Port gestartet werden.
- Bei langsamen Läufen helfen kleinere Datenmengen, weniger Epochen oder
  eine reduzierte Modellgröße.
