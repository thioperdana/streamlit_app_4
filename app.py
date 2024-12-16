import streamlit as st
import time
from src import recomendation_system
from pathlib import Path

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

path_data = "data"
filename = "data.csv"
my_file = Path("./data/chroma.sqlite3")

if not my_file.exists():
    recomendation_system.vectorizer_data_to_memory(f"{path_data}/{filename}")

st.set_page_config(
    page_title="ChatBot"
)

def response_generator(query):
    answer = f'''
Tiga pilihan anime rekomendasi dari saya sesuai permintaan: {query}, adalah:
\n
'''
    response = recomendation_system.query_search(query)
    answer += response
    for word in answer.split():
        yield word + " "
        time.sleep(0.1)


# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#menampilkan data
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Menangkap pesan user
prompt = st.chat_input("isi chat anda disini")

#memasukkan pada list dan menampilkan chat user
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append(
        {
            "role": "user", 
            "content": prompt,
        }
    )   

    #memasukkan pada list dan menampilkan chat assistant
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))

    st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )