import streamlit as st
from functions.rechner import (
    konvertiere_laenge,
    konvertiere_gewicht,
    konvertiere_temperatur,
)

# ------- etwas CSS für die Farbe hinterlegen -------
st.markdown(
    """
    <style>
    .title {text-align: center; color: teal;}
    .container {background-color: #f0f4f8; padding: 1rem; border-radius: 8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>🔄 Think smarter, not harder</h1>", unsafe_allow_html=True)
st.write("Kleine Prävention für das Laborpraktikum: Damit nicht erst beim 30. Schritt auffällt, dass man einen Umrechnungsfehler gemacht hat.")
st.markdown("---")

with st.container():
    col1, col2 = st.columns([2, 3])

    with col1:
        kategorie = st.radio(
            "Kategorie",
            ["🔧 Länge", "⚖️ Gewicht", "🌡️ Temperatur"],
            horizontal=True,
        )
        wert = st.number_input("Wert", value=0.0, step=0.01, format="%.2f")

        if kategorie.startswith("🔧"):
            von = st.selectbox("von", ["m", "cm", "km"])
            nach = st.selectbox("nach", ["m", "cm", "km"])
        elif kategorie.startswith("⚖️"):
            von = st.selectbox("von", ["kg", "g", "lb"])
            nach = st.selectbox("nach", ["kg", "g", "lb"])
        else:  # Temperatur
            von = st.selectbox("von", ["°C", "°F", "K"])
            nach = st.selectbox("nach", ["°C", "°F", "K"])

        umrechnen = st.button("🎯 Umrechnen", key="convert")

    with col2:
        if umrechnen:
            if kategorie.startswith("🔧"):
                ergebnis = konvertiere_laenge(wert, von, nach)
            elif kategorie.startswith("⚖️"):
                ergebnis = konvertiere_gewicht(wert, von, nach)
            else:
                ergebnis = konvertiere_temperatur(wert, von, nach)

            st.success(f"✅ {wert} {von} = **{ergebnis} {nach}**")
            st.balloons()

st.markdown("---")
st.caption("Erstellt mit Streamlit – einfach, schnell und hübsch 😊")