import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
conn = sqlite3.connect('data/leaks.db', check_same_thread=False)
try:
    df = pd.read_sql_query("SELECT * FROM leaks", conn)
except Exception as e:
    st.error(f"Failed to load data: {e}")
    df = pd.DataFrame(columns=['id', 'email', 'url', 'timestamp'])
st.set_page_config(page_title="DarkNet Leak Scanner", layout="wide")
st.title("🔍 DarkNet Leak Scanner")
st.caption("Monitor exposed credentials from dark web leak sources")
col1, col2 = st.columns(2)
with col1:
    date_filter = st.date_input("Filter by date range", [])
with col2:
    search_term = st.text_input("Search Email / Domain / URL")
if not df.empty:
    if date_filter:
        df['parsed_date'] = pd.to_datetime(df['timestamp']).dt.date
        if len(date_filter) == 1:
            df = df[df['parsed_date'] >= date_filter[0]]
        elif len(date_filter) == 2:
            df = df[(df['parsed_date'] >= date_filter[0]) & (df['parsed_date'] <= date_filter[1])]
    if search_term:
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        results = df[mask]
    else:
        results = df.sort_values('timestamp', ascending=False).head(100)
    if 'parsed_date' in results.columns:
        results = results.drop(columns=['parsed_date'])
    st.dataframe(results, hide_index=True, use_container_width=True)
    st.metric("🔢 Total Records", len(results))
else:
    st.warning("No data available in the database yet.")
conn.close()