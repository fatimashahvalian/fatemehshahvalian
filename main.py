
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("fatemeh shahvalian")
st.write(" private shared google sheet.")
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet=["sheet 1","sheet 2","sheet 3"])

st.dataframe(df)
st.write("Use [FOR command] to show data:")

for row in df.itertuples():
    st.write(f"Name : {row.name} , Famil: {row.famil} , city: {row.city}")





