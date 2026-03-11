# Konversions‑Funktionen für den Einheitenrechner

def konvertiere_laenge(wert, von, nach):
    """Länge in eine andere Einheit umrechnen.

    Akzeptierte Einheiten: Millimeter [mm], Zentimeter [cm],
    Meter [m], Kilometer [km]. Groß-/Kleinschreibung wird ignoriert.
    """
    to_meter = {
        "millimeter": 0.001, "mm": 0.001,
        "zentimeter": 0.01,   "cm": 0.01,
        "meter": 1.0,         "m": 1.0,
        "kilometer": 1000.0,  "km": 1000.0,
    }
    try:
        fv = to_meter[von.lower()]
        fn = to_meter[nach.lower()]
    except KeyError:
        raise ValueError(f"Unbekannte Längeneinheit: {von!r} oder {nach!r}")
    return wert * fv / fn


def konvertiere_gewicht(wert, von, nach):
    """Gewicht in eine andere Einheit umrechnen.

    Akzeptierte Einheiten: Milligramm [mg], Gramm [g], Kilogramm [kg],
    Tonne [t], Pfund [lb]. Groß-/Kleinschreibung wird ignoriert.
    """
    to_gram = {
        "milligramm": 0.001, "mg": 0.001,
        "gramm": 1.0,        "g": 1.0,
        "kilogramm": 1000.0, "kg": 1000.0,
        "tonne": 1_000_000.0,"t": 1_000_000.0,
        "pfund": 453.592,    "lb": 453.592,
    }
    try:
        fv = to_gram[von.lower()]
        fn = to_gram[nach.lower()]
    except KeyError:
        raise ValueError(f"Unbekannte Gewichtseinheit: {von!r} oder {nach!r}")
    return wert * fv / fn


def konvertiere_temperatur(wert, von, nach):
    """Temperatur zwischen Celsius, Fahrenheit und Kelvin umrechnen.

    Akzeptiert `°C`, `C`, `°F`, `F` und `K`. Wenn beide Einheiten gleich sind,
    wird der Eingabewert zurückgegeben.
    """
    alias = {
        "°c": "celsius", "c": "celsius",
        "°f": "fahrenheit", "f": "fahrenheit",
        "k": "kelvin", "°k": "kelvin",
    }
    v = alias.get(von.lower(), von.lower())
    n = alias.get(nach.lower(), nach.lower())

    if v == n:
        return wert

    # Zwischenwert in Celsius
    if v == "celsius":
        c = wert
    elif v == "fahrenheit":
        c = (wert - 32) * 5 / 9
    elif v == "kelvin":
        c = wert - 273.15
    else:
        raise ValueError(f"Unbekannte Temperatureinheit: {von!r}")

    if n == "celsius":
        return c
    if n == "fahrenheit":
        return c * 9 / 5 + 32
    if n == "kelvin":
        return c + 273.15

    raise ValueError(f"Unbekannte Temperatureinheit: {nach!r}")

# Die interaktive Streamlit-Oberfläche bleibt in den View-Dateien.