import streamlit as st
from controllers import get_all, delete_by_id, put_status
import requests
import pandas as pd
from PIL import Image
icon = Image.open('Logo.jpeg')
st.set_page_config(
    page_title="Ciotta - Delivery Managment",
    layout="wide",
    page_icon=icon,  # Você pode usar um emoji ou uma URL de uma imagem
)

def populate_table():
    dados = get_all()

    # Criar DataFrame do pandas
    colunas = ["ID", "Nome Cliente", "Rua", "Bairro", "Telefone", "Status", "Hora", "Data"]
    df = pd.DataFrame(dados, columns=colunas)

    # Exibir a tabela
    st.table(df)

def main():
    st.title("Gestão de Entregas - Ciotta")

    with st.container():
        populate_table()

if __name__ == "__main__":
    main()