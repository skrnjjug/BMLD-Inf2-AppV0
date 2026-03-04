import streamlit as st

st.title("Einheiten Umrechner")

# Konversions-Funktionen
def konvertiere_laenge(wert, von, nach):
    to_meter = {"Millimeter": 0.001, "Zentimeter": 0.01, "Meter": 1, "Kilometer": 1000}
    return wert * to_meter[von] / to_meter[nach]

def konvertiere_gewicht(wert, von, nach):
    to_gram = {"Milligramm": 0.001, "Gramm": 1, "Kilogramm": 1000, "Tonne": 1000000}
    return wert * to_gram[von] / to_gram[nach]

def konvertiere_temperatur(wert, von, nach):
    if von == nach:
        return wert
    if von == "Celsius" and nach == "Fahrenheit":
        return wert * 9/5 + 32
    elif von == "Fahrenheit" and nach == "Celsius":
        return (wert - 32) * 5/9

kategorie = st.selectbox("Kategorie auswählen", ["Länge", "Gewicht", "Temperatur"])

wert = st.number_input("Wert eingeben", step=0.01)

if kategorie == "Länge":
    einheiten = ["Millimeter", "Zentimeter", "Meter", "Kilometer"]
    von = st.selectbox("Von", einheiten)
    nach = st.selectbox("Nach", einheiten)
    if st.button("Berechnen"):
        ergebnis = konvertiere_laenge(wert, von, nach)
        st.success(f"Ergebnis: {round(ergebnis, 4)}")

elif kategorie == "Gewicht":
    einheiten = ["Milligramm", "Gramm", "Kilogramm", "Tonne"]
    von = st.selectbox("Von", einheiten)
    nach = st.selectbox("Nach", einheiten)
    if st.button("Berechnen"):
        ergebnis = konvertiere_gewicht(wert, von, nach)
        st.success(f"Ergebnis: {round(ergebnis, 4)}")

elif kategorie == "Temperatur":
    einheiten = ["Celsius", "Fahrenheit"]
    von = st.selectbox("Von", einheiten)
    nach = st.selectbox("Nach", einheiten)
    if st.button("Berechnen"):
        ergebnis = konvertiere_temperatur(wert, von, nach)
        st.success(f"Ergebnis: {round(ergebnis, 2)}")