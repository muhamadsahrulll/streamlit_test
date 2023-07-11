import os
import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
# import pyodbc

engine = create_engine(
    # "mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]"
    "mysql+mysqlconnector://root:qTi5zejHl22POl6ZkUTa@containers-us-west-64.railway.app:7086/railway", 
)

# st.write("""# My first app""")
# st.write("DB username:", st.secrets["db_username"])
# st.write("DB password:", st.secrets["db_password"])
# # st.write("My cool secrets:", st.secrets["1234"])
# # Inisialisasi koneksi.
# # streamlit_app.py
# # st.write(
# #     "Has environment variables been set:",
# #     os.environ["username"] == st.secrets["username"],
# # )
# # Initialize connection.
# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
df = pd.read_sql('SELECT * from users;', engine)
# print(df)
# df = engine.query('SELECT * from users;', ttl=600)
# import streamlit as st
# import numpy as np

# dataframe = np.random.randn(10, 20)
st.dataframe(df)

