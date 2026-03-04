# Konversions-Funktionen für den Einheitenrechner

def konvertiere_laenge(wert, von, nach):
    """Länge in eine andere Einheit umrechnen."""
    to_meter = {"Millimeter": 0.001, "Zentimeter": 0.01, "Meter": 1, "Kilometer": 1000}
    return wert * to_meter[von] / to_meter[nach]

def konvertiere_gewicht(wert, von, nach):
    """Gewicht in eine andere Einheit umrechnen."""
    to_gram = {"Milligramm": 0.001, "Gramm": 1, "Kilogramm": 1000, "Tonne": 1000000}
    return wert * to_gram[von] / to_gram[nach]

def konvertiere_temperatur(wert, von, nach):
    """Temperatur zwischen Celsius und Fahrenheit umrechnen."""
    if von == nach:
        return wert
    if von == "Celsius" and nach == "Fahrenheit":
        return wert * 9/5 + 32
    elif von == "Fahrenheit" and nach == "Celsius":
        return (wert - 32) * 5/9

# Die interaktive Streamlit-Oberfläche bleibt in den View-Dateien.
