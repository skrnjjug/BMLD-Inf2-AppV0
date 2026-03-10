import streamlit as st

username = st.secrets["webdav.username"]
password = st.secrets["webdav.password"]

st.write(f"Username: {username}")
st.write(f"Password: {password}")

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/think smarter not harder.py", title="Think Smarter Not Harder", icon=":material/info:")


pg = st.navigation([pg_home, pg_second])
pg.run()