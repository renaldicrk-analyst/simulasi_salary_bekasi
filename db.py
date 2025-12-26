# db.py

# import psycopg2
# import pandas as pd
# from config import DB_CONFIG

# def fetch_dataframe(query, params):
#     conn = psycopg2.connect(**DB_CONFIG)
#     df = pd.read_sql(query, conn, params=params)
#     conn.close()
#     return df
import streamlit as st
import psycopg2
import pandas as pd

def fetch_dataframe(query, params=None):
    conn = psycopg2.connect(
        host=st.secrets["db"]["host"],
        port=st.secrets["db"]["port"],
        dbname=st.secrets["db"]["dbname"],
        user=st.secrets["db"]["user"],
        password=st.secrets["db"]["password"],
        sslmode="require"
    )

    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df
