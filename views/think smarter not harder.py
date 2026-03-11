import streamlit as st
import pandas as pd
import datetime
import pytz
from functions.rechner import (
    konvertiere_laenge,
    konvertiere_gewicht,
    konvertiere_temperatur,
)

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

                st.success(f"✅ {wert} {von} = **{ergebnis} {nach}**")

                # Spezieller Hinweis für Temperatur
                if kategorie.startswith("🌡️") and 20 <= ergebnis <= 30:
                    st.balloons()
                    st.info("🍹 Aperol Spritz Wetter!")

                # --- Dictionary erstellen ---
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

            except ValueError as err:
                st.error(err)

# --- Historie-Tabelle anzeigen ---
st.markdown("---")
st.caption("Erstellt mit Streamlit – einfach, schnell und hübsch 😊")
st.dataframe(st.session_state['data_df'])