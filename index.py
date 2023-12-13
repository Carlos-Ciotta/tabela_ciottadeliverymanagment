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

def insere_entrega():
    nome_cliente = st.text_input("Nome cliente", key="nome_cliente_key")
    rua = st.text_input("Rua", key="rua_key")
    bairro = st.text_input("Bairro", key="bairro_key")
    telefone = st.text_input("Telefone", key="telefone_key")

    if st.button("Enviar Entrega"):
        data = {
            "nome_cliente": nome_cliente,
            "logradouro": rua,
            "bairro": bairro,
            "telefone": telefone,
            "id": 0,
            "status": "Aguardando",
            "hora": "NULL",
            "data": "NULL"
        }
        url = 'https://api-production-e20e.up.railway.app/entregas/post'
        response = requests.post(url, json=data)
        nome_cliente = ""
        rua = ""
        bairro = ""
        telefone = ""
        if response.status_code == 200:
            data = response.json()
            print("Dados da API:", data)
        else:
            print("Falha na solicitação. Código de status:", response.status_code)
            print("Conteúdo da resposta:", response.text)

        st.write(f"Resposta do servidor: {response.text}")
    
def main():
    st.title("Gestão de Entregas - Ciotta")
    with st.container():
        insere_entrega()

    with st.container():
        populate_table()
        if st.button("Atualizar"):
            populate_table()
if __name__ == "__main__":
    main()