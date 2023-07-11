import streamlit as st
import os


st.write("""# My first app""")
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["1234"])
# Inisialisasi koneksi.
# streamlit_app.py
st.write(
    "Has environment variables been set:",
    os.environ["username"] == st.secrets["username"],
)
# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from users;', ttl=600)

