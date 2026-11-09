import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "keras_model.h5"
LABELS_PATH = BASE_DIR / "labels.txt"

st.set_page_config(
    page_title="KI-Bilderkennung",
    page_icon="🛰️",
    layout="centered"
)

st.markdown("""
<style>
    .main {max-width: 900px; padding-top: 2rem;}
    .hero {
        padding: 1.5rem; border-radius: 18px;
        background: linear-gradient(120deg, #14213d, #263f68);
        color: white; margin-bottom: 1.5rem;
    }
    .small-note {color: #8b949e; font-size: 0.9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🛰️ KI-Bilderkennung</h1>
  <p>Lade ein Bild hoch und lasse es von deinem selbst trainierten Modell klassifizieren.</p>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Modelldatei nicht gefunden: {MODEL_PATH.name}")
    # compile=False: Für reine Vorhersagen werden keine Trainingsmetriken benötigt.
    return tf.keras.models.load_model(MODEL_PATH, compile=False)

def load_labels():
    if not LABELS_PATH.exists():
        raise FileNotFoundError(f"Labeldatei nicht gefunden: {LABELS_PATH.name}")

    labels = []
    for line in LABELS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        # Teachable Machine speichert Labels häufig als "0 Klassenname".
        parts = line.split(maxsplit=1)
        labels.append(parts[1].strip() if len(parts) == 2 and parts[0].isdigit() else line)
    return labels

def prepare_image(image: Image.Image):
    # Das Teachable-Machine-Bildmodell erwartet 224 x 224 RGB-Pixel.
    image = image.convert("RGB").resize((224, 224))
    image_array = np.asarray(image, dtype=np.float32)

    # Standard-Vorverarbeitung für Teachable-Machine-Keras-Bildmodelle:
    # Pixelwerte von 0..255 auf -1..1 skalieren.
    image_array = (image_array / 127.5) - 1.0
    return np.expand_dims(image_array, axis=0)

try:
    model = load_model()
    labels = load_labels()
except Exception as error:
    st.error(f"Das Modell konnte nicht geladen werden: {error}")
    st.stop()

uploaded_file = st.file_uploader(
    "Bild auswählen",
    type=["jpg", "jpeg", "png", "webp"],
    help="Wähle ein Bild aus, das dein Modell erkennen soll."
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Hochgeladenes Bild", use_container_width=True)

        if st.button("Bild analysieren", type="primary", use_container_width=True):
            with st.spinner("Dein KI-Modell analysiert das Bild …"):
                input_data = prepare_image(image)
                predictions = model.predict(input_data, verbose=0)[0]

            if len(predictions) != len(labels):
                st.error(
                    f"Das Modell gibt {len(predictions)} Werte aus, "
                    f"aber labels.txt enthält {len(labels)} Klassen. "
                    "Bitte überprüfe die Labeldatei."
                )
                st.stop()

            # Die Teachable-Machine-Ausgabe ist bei diesem Modell eine Softmax-Verteilung.
            probabilities = np.asarray(predictions, dtype=float)
            best_index = int(np.argmax(probabilities))

            st.success("Analyse abgeschlossen")
            st.subheader("Ergebnis")
            st.markdown(f"### {labels[best_index]}")
            st.metric("Höchster Modellwert", f"{probabilities[best_index] * 100:.1f} %")

            st.subheader("Alle Klassen")
            sorted_indices = np.argsort(probabilities)[::-1]
            for index in sorted_indices:
                score = float(probabilities[index])
                st.write(f"**{labels[index]}** — {score * 100:.1f} %")
                st.progress(min(max(score, 0.0), 1.0))

            st.caption(
                "Hinweis: Die Prozentwerte sind Modell-Konfidenzwerte und "
                "keine Garantie, dass die Erkennung richtig ist."
            )
    except Exception as error:
        st.error(f"Das Bild konnte nicht verarbeitet werden: {error}")
else:
    st.info("Lade oben ein Bild hoch, um die Erkennung zu starten.")

with st.expander("Über das Modell"):
    st.write("Eingabegröße: 224 × 224 Pixel, RGB")
    st.write(f"Anzahl der erkannten Klassen: {len(labels)}")
    st.write("Das Modell wurde mit Teachable Machine trainiert.")
