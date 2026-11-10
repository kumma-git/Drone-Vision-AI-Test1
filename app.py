import streamlit as st
from PIL import Image

st.set_page_config(page_title="Bilderkennung KI", page_icon="🧠", layout="wide")

st.markdown("""
<style>
.stApp{background:radial-gradient(ellipse at 75% 0%,#17283b 0%,#08111c 50%,#060d15 100%);color:#edf5ff}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0c1724,#101e2e);border-right:1px solid #21364b}
[data-testid="stSidebar"] *{color:#e8f2ff}
.block-container{padding-top:1.5rem;max-width:1500px}
.hero{border:1px solid #20384f;border-left:6px solid #26a8f5;border-radius:16px;padding:25px 30px;margin-bottom:18px;background:linear-gradient(105deg,#0c1927,#153148)}
.hero h1{font-size:clamp(2rem,4vw,3.2rem);margin:0;color:white}
.hero p,.muted{color:#b8cadb}
.panel{background:linear-gradient(145deg,#111d2b,#0b1521);border:1px solid #20364b;border-radius:16px;padding:20px;min-height:260px}
.placeholder{border:1px dashed #3c5872;border-radius:12px;padding:38px 16px;text-align:center;color:#b8cadb;background:#08121e}
.stat{border:1px solid #24425a;border-radius:12px;padding:14px;background:#0c1d2c}
div[data-testid="stFileUploader"] section{border:1px dashed #41627e;border-radius:12px;background:#08121e}
.stButton button[kind="primary"]{background:linear-gradient(90deg,#087fc4,#22a9f5);border:0;color:white}
</style>
""",unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div style='text-align:center;padding:18px 4px 28px'><div style='font-size:3.5rem'>🧠</div><div style='font-size:1.5rem;font-weight:850'>BILDERKENNUNG<br><span style='color:#26a8f5'>KI</span></div><small>INTELLIGENTE BILDAUSWERTUNG</small></div>",unsafe_allow_html=True)
    page=st.radio("Navigation",["⌂  Startseite","▥  Analyse","ⓘ  Über das Projekt"],label_visibility="collapsed")
    st.markdown("---")
    st.markdown("<div style='border:1px solid #263d52;border-radius:12px;padding:14px;background:#101d2a'><b style='color:#8ed8ff'>Systemstatus</b><p style='color:#f5c45b;margin:8px 0'>● Designvorlage</p><small>Die Oberfläche ist bereit. Eine Klassifizierungsfunktion ist nicht verbunden.</small></div>",unsafe_allow_html=True)

st.markdown("<div class='hero'><div style='font-size:.8rem;letter-spacing:.18em;color:#55c1ff;font-weight:800'>KI-BILDERKENNUNG</div><h1>Bilderkennung <span style='color:#26a8f5'>KI</span></h1><p>Eine moderne Oberfläche zur übersichtlichen Darstellung von Bildanalysen.</p><div style='color:#e0ebf5'>Lade ein Bild hoch und nutze die Oberfläche als Grundlage für dein eigenes Klassifizierungsprojekt.</div></div>",unsafe_allow_html=True)

if page.startswith(("⌂","▥")):
    left,right=st.columns([1,1.05],gap="medium")
    with left:
        st.markdown("<div class='panel'><h3>▧ &nbsp; Bild hochladen</h3><p class='muted'>Wähle ein Bild von deinem Gerät aus.</p>",unsafe_allow_html=True)
        file=st.file_uploader("Bild auswählen",type=["jpg","jpeg","png","webp"],label_visibility="collapsed")
        if file:
            st.image(Image.open(file).convert("RGB"),caption="Ausgewähltes Bild",use_container_width=True)
            st.success("Bild wurde erfolgreich geladen.")
        else:
            st.markdown("<div class='placeholder'><div style='font-size:2.8rem;color:#32b5ff'>⇧</div><b>Bild hier ablegen oder oben auswählen</b><br><small>Unterstützte Formate: JPG, PNG, JPEG, WEBP</small></div>",unsafe_allow_html=True)
        st.markdown("<p class='muted'>Projektstatus: Designvorlage</p></div>",unsafe_allow_html=True)
    with right:
        st.markdown("<div class='panel'><h3>▥ &nbsp; Analyseergebnisse</h3><div class='placeholder'><div style='font-size:2.3rem'>📊</div><b>Noch keine Analyse vorhanden</b><br><small>Hier erscheinen später die Ergebnisse eines geeigneten Klassifizierungsmodells.</small></div><br><div class='stat'><b>Ergebnisübersicht</b><p class='muted'>Klassen und Modellwerte werden nach einer geeigneten Anbindung angezeigt.</p></div></div>",unsafe_allow_html=True)
    st.markdown("<br><div class='panel' style='min-height:unset'><h3>✦ &nbsp; Über das Projekt</h3><p class='muted'>Diese Streamlit-Vorlage bietet ein modernes Grunddesign für ein allgemeines Bilderkennungsprojekt.</p></div>",unsafe_allow_html=True)
else:
    st.markdown("<div class='panel'><h3>ⓘ &nbsp; Über das Projekt</h3><p>Diese Anwendung ist eine deutschsprachige Designvorlage für ein allgemeines Bilderkennungsprojekt.</p><p class='muted'>Die Oberfläche enthält Bild-Upload, Ergebnisbereich und Navigation. Eine konkrete Klassifizierungsfunktion ist in dieser neutralen Vorlage nicht enthalten.</p></div>",unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#70869a;font-size:.78rem;padding:22px'>BILDERKENNUNG KI · STREAMLIT-DESIGNVORLAGE</div>",unsafe_allow_html=True)

