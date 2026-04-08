# Woche 6: Computer Vision und NLP

Woche 6 führt in ausgewählte Verfahren aus Computer Vision und NLP ein.
Das Modul ist notebook-lastig und für knappe Laufzeiten auf
CPU-Systemen vorbereitet.

## Lernziele

- Grundideen von CNNs nachvollziehen
- Kanten, Konturen und lokale Bildmerkmale mit OpenCV untersuchen
- den Effekt von Datenaugmentation praktisch sehen
- Transfer Learning als ressourcenschonenden Einstieg einordnen
- Unterschiede zwischen Lehrdemo, Exploration und belastbarer Modellierung diskutieren

## Materialien

- `06_01_neu_CNN_Basics.ipynb`: kleines CNN-Beispiel mit Feature-Maps
- `06_02_neu_OpenCV_Edge_Features.ipynb`: Kanten, Konturen und ORB-Merkmale
- `06_03_neu_Data_Augmentation_Practice.ipynb`: Vergleich von Baseline und Augmentation
- `06_04_neu_Transfer_Learning_Lite.ipynb`: leichtes Transfer Learning mit Export
- `06_05_neu_Image_Sampler.ipynb`: schneller Bildsampler für
  mitgelieferte oder eigene Beispiele

## Empfohlene Reihenfolge

1. `06_01_neu_CNN_Basics.ipynb`
2. `06_02_neu_OpenCV_Edge_Features.ipynb`
3. `06_03_neu_Data_Augmentation_Practice.ipynb`
4. `06_04_neu_Transfer_Learning_Lite.ipynb`
5. `06_05_neu_Image_Sampler.ipynb`

## Start

```bash
cd /Users/kqc/amalea
pip install -r requirements-week06.txt
cd 06_Computer_Vision_NLP
jupyter notebook 06_01_neu_CNN_Basics.ipynb
```

Die weiteren Notebooks können analog geöffnet werden.

## Hinweise

- Die Notebooks sind auf kurze CPU-Läufe ausgelegt. Bei Bedarf lassen
  sich Epochen, Sample-Größen oder Batch-Größen weiter reduzieren.
- Vortrainierte Gewichte werden beim ersten Lauf geladen und anschließend zwischengespeichert.
- Der Ordner `images/` dient als Demo-Grundlage für den Image Sampler.
- Für den Lehrbetrieb empfiehlt sich eine klare Trennung zwischen
  Pflichtmaterial und optionaler Vertiefung, insbesondere beim Transfer
  Learning.

## Didaktische Einordnung

- `06_01` und `06_02` eignen sich gut für Pflichtinhalte.
- `06_03` und `06_04` sind sinnvoll als Vertiefung oder Vergleichsmaterial.
- `06_05` eignet sich gut für kurze Demonstrationen im Plenum.
