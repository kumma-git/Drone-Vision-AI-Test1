# Teachable Machine – Streamlit-App

## Dateien
- `app.py`: Streamlit-Oberfläche und Bildklassifizierung
- `keras_model.h5`: dein trainiertes Teachable-Machine-Modell
- `labels.txt`: Klassennamen
- `requirements.txt`: Python-Abhängigkeiten

## Lokal starten

1. Installiere Python 3.10 oder 3.11.
2. Öffne ein Terminal im Projektordner.
3. Erstelle eine virtuelle Umgebung:

   Windows:
   ```bash
   py -3.11 -m venv .venv
   .venv\Scripts\activate
   ```

   Linux/macOS:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

4. Installiere die Pakete:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Starte die App:
   ```bash
   streamlit run app.py
   ```

6. Der Browser öffnet normalerweise `http://localhost:8501`.

## Auf GitHub hochladen

1. Erstelle auf GitHub ein neues Repository, z. B. `ki-bilderkennung`.
2. Lade diese Projektdateien in das Repository hoch.
3. Achte darauf, dass `app.py`, `requirements.txt`, `keras_model.h5` und `labels.txt`
   direkt im Hauptverzeichnis liegen.

## Auf Streamlit Community Cloud veröffentlichen

1. Öffne https://share.streamlit.io/
2. Melde dich mit GitHub an.
3. Wähle **Create app**.
4. Wähle dein Repository und den Branch (normalerweise `main`).
5. Setze als Main file path `app.py`.
6. Klicke auf **Deploy**.

Streamlit installiert die Pakete aus `requirements.txt` und startet die App.
Der erste Start kann wegen TensorFlow etwas länger dauern.

## Wichtig
- Die App erwartet ein Teachable-Machine-Keras-Bildmodell mit Eingabegröße 224 × 224 × 3.
- Die Bildvorverarbeitung skaliert RGB-Pixel von 0–255 auf -1 bis 1.
- Die Modellwerte sind keine Garantie für eine korrekte Erkennung.
- Wenn du später die Klassen in Teachable Machine änderst, exportiere das Modell
  und die Labels erneut und ersetze beide Dateien.
