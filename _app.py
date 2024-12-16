import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from datetime import datetime


st.title("Aplikasi Pertama Kita")
st.markdown(
    """
    Aplikasi ini adalah contoh sederhana untuk membuat sebuah website menggunakan Streamlit.
    Ini adalah halaman awal yang menampilkan informasi tentang Aplikasi Pertama Kita.
    # Header
    ## Sub-header

    **Teks pertama**

    *Teks kedua*

     - Teks ketiga
     - Teks keempat

    """
)

st.divider()

query = '''import pandas as pd
df =  pd.DataFrame([1,2,3])
display(df)
'''

st.code(query)

st.divider()

data = {
    "products": ["A", "B"],
    "prices": [50000, 60000],
    "stock": [1234, 789]
}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)
st.data_editor(df)

st.metric(label="Temperature", value=80, delta=5)

chart = pd.DataFrame(np.random.randn(20,3), columns=['a', 'b', 'c'])
st.area_chart(chart)
st.line_chart(chart)
st.scatter_chart(chart)

st.divider()

x = [1,2,3,4]
y = [6,7,8,9]

p = figure(title="Sample Chart", x_axis_label='x', y_axis_label='y')
p.line(x,y)

st.bokeh_chart(p)

st.divider()

# st.button

st.button("Click Me")

if st.button("Test"):
    st.write("Button has been clicked!")

# st.download_button
st.download_button(
    label = "download",
    data = df.to_csv(index = False),
    file_name ="data.csv",
    mime = "text/csv"
)

st.download_button("Download Text", "unduh data teks")

# st.date_input
a = st.date_input("Date Input", datetime.now())
st.write(f"tanggal pilihan: {a}")

# st.text_input
a = st.text_input("isi disini")
st.write(f"isian anda: {a}")

# st.file_uploader
uploaded = st.file_uploader("upload berkasmu")
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.dataframe(df)

# st.chat_input
chat_container = st.container()
prompt = chat_container.chat_input("isi chat anda disini")
if prompt:
    chat_container.chat_message("user").write(prompt)
    chat_container.chat_message("bot").write("jawaban anda: " + prompt.lower())
