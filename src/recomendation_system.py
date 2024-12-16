import pandas as pd
import chromadb
from pprint import pprint

path_data = "data"
filename = "data.csv"

def read_dataset(filepath):
    return pd.read_csv(filepath)

def vectorizer_data_to_memory(filepath):
    try:
        df = read_dataset(filepath)
        df['score'] = df['score'].astype(float)
        df = df.dropna()

        client = chromadb.PersistentClient(path="./data")


        df['text'] = df['about']+" "+df['title']+" "+df['genres']+" "+df['studios']
        ids = [str(i) for i in range(1,len(df)+1)]
        metadata = df.to_dict('records')
        documents = list(df['text'].values)

        collection = client.get_or_create_collection("anime")
        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadata
        )

        print("menyimpan data")
        client.persist()
        print("Data sudah tersimpan")
    except Exception as e:
        print(f"Error: {e}")

def query_search(query):
    client = chromadb.PersistentClient(path="./data")
    collection = client.get_collection("anime")
    results = collection.query(
        query_texts=[query],
        n_results=3,
    )

    text_results = ""
    for index, dic_md in enumerate(results["metadatas"][0]):
        text_results += f"{index+1}. {dic_md['title']} : {dic_md['about']}.\n \n "

    return text_results

def run_query(query):
    result = query_search(query)
    return query

if __name__ == "__main__":
    pass
