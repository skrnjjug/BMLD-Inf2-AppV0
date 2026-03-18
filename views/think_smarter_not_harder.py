import streamlit as st
import pandas as pd
import datetime
import pytz
import plotly.express as px

from functions.rechner import (
    konvertiere_laenge,
    konvertiere_gewicht,
    konvertiere_temperatur,
)
from utils.data_manager import DataManager

# --- Einheitendefinitionen ---
LAENGEN = ["m", "cm", "km"]
GEWICHT = ["kg", "g", "lb"]
TEMPERATUREN = ["°C", "°F", "K"]

# --- Session DataFrame initialisieren ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame()

# --- Überschrift ---
st.markdown('<h1 class="title">Think smarter, not harder</h1>', unsafe_allow_html=True)
st.write("Kleine Prävention für das Laborpraktikum: Damit nicht erst beim 30. Schritt auffällt, dass man einen Umrechnungsfehler gemacht hat")
st.markdown("---")

# --- Eingabecontainer ---
with st.container():
    col1, col2 = st.columns([2, 3])

    # --- linke Spalte: Inputs ---
    with col1:
        kategorie = st.radio(
            "Kategorie",
            ["🔧 Länge", "⚖️ Gewicht", "🌡️ Temperatur"],
            horizontal=True,
        )
        wert = st.number_input("Wert", value=0.0, step=0.01, format="%.2f")

        if kategorie.startswith("🔧"):
            von = st.selectbox("von", LAENGEN)
            nach = st.selectbox("nach", LAENGEN)
        elif kategorie.startswith("⚖️"):
            von = st.selectbox("von", GEWICHT)
            nach = st.selectbox("nach", GEWICHT)
        else:
            von = st.selectbox("von", TEMPERATUREN)
            nach = st.selectbox("nach", TEMPERATUREN)

        umrechnen = st.button("🎯 Umrechnen", key="convert")

    # --- rechte Spalte: Ergebnisse ---
    with col2:
        if umrechnen:
            try:
                # --- Berechnung ---
                if kategorie.startswith("🔧"):
                    ergebnis = konvertiere_laenge(wert, von, nach)
                elif kategorie.startswith("⚖️"):
                    ergebnis = konvertiere_gewicht(wert, von, nach)
                else:
                    ergebnis = konvertiere_temperatur(wert, von, nach)

                st.success(f"✅ {wert} {von} = **{ergebnis} {nach}**")

                # Spezieller Hinweis für Temperatur
                if kategorie.startswith("🌡️") and 20 <= ergebnis <= 30:
                    st.balloons()
                    st.info("🍹 Aperol Spritz Wetter!")

                # --- Dictionary erstellen (KONSISTENT BENANNT) ---
                result = {
                    "timestamp": datetime.datetime.now(pytz.timezone('Europe/Zurich')),
                    "wert": wert,
                    "von": von,
                    "nach": nach,
                    "ergebnis": ergebnis,
                    "kategorie": kategorie,
                }

                # --- DataFrame aktualisieren ---
                st.session_state['data_df'] = pd.concat(
                    [st.session_state['data_df'], pd.DataFrame([result])],
                    ignore_index=True
                )

                # --- Speichern ---
                data_manager = DataManager()
                data_manager.save_user_data(st.session_state['data_df'], 'data.csv')

            except ValueError as err:
                st.error(err)

# --- Historie-Tabelle anzeigen ---
st.markdown("---")
st.caption("Erstellt mit Streamlit – einfach, schnell und hübsch 😊")
st.dataframe(st.session_state['data_df'])

# --- Plot ---
df = st.session_state['data_df']

if not df.empty:
    # letzte verwendete Ziel-Einheit
    einheit = df.iloc[-1]["nach"]

    # nach Einheit filtern
    df_filtered = df[df["nach"] == einheit]

    fig = px.line(
        df_filtered,
        x="timestamp",
        y="wert",
        title=f"Verlauf in {einheit}"
    )

    st.plotly_chart(fig)

else:
    st.write("Keine Daten vorhanden")