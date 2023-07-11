import streamlit as st



st.write("""# My first app""")

# Inisialisasi koneksi.
# streamlit_app.py

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from users;', ttl=600)

