import pandas as pd
import streamlit as st

from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# --- Page Config MUSS ganz oben stehen! ---
st.set_page_config(
    page_title="Meine App",
    page_icon=":material/home:"
)

# --- CSS-Styling ---
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: teal;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .container {
        background-color: #f0f4f8;
        padding: 1rem;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- DataManager initialisieren (SwitchDrive Verbindung) ---
data_manager = DataManager(
    fs_protocol='webdav',
    fs_root_folder="app_data"
)

# --- LoginManager initialisieren ---
login_manager = LoginManager(data_manager)
login_manager.login_register()

# --- Secrets prüfen (Username/Passwort müssen gesetzt sein) ---
creds = st.secrets.get("credentials", {})
if not creds.get("username") or not creds.get("password"):
    st.error(
        "Bitte `secrets.toml` anlegen / in Streamlit Cloud unter "
        "Manage app → Secrets die Felder `credentials.username` und "
        "`credentials.password` setzen."
    )
else:
    # --- LoginManager initialisieren ---
    login_manager = LoginManager(data_manager)
    login_manager.login_register()

# --- Nutzerdaten laden und in session_state speichern ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )

# --- Seiten definieren ---
pg_home = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

pg_second = st.Page(
    "views/think smarter not harder.py",
    title="Think Smarter",
    icon=":material/lightbulb:"
)

# --- Navigation starten ---
pg = st.navigation([pg_home, pg_second])
pg.run()