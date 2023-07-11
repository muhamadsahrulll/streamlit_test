import streamlit as st
import pandas as pd 
import numpy as np



st.write("""# My first app""")

# Inisialisasi koneksi.
conn = st.experimental_connection('mysql', type='sql', dialect='mysql', host='containers-us-west-64.railway.app', username='root', password='qTi5zejHl22POl6ZkUTa', database='railway')

# Melakukan query.
df = conn.query('SELECT * from users;', ttl=0)