import streamlit as st
from controllers import get_all,post
import pandas as pd
from PIL import Image

icon = Image.open('Logo.jpeg')
var_status = ['Em andamento', 'Aguardando']
var_status1 = ['Entregue']
st.set_page_config(
    page_title="Ciotta - Delivery Managment",
    layout="wide",
    page_icon=icon,
)

def populate_table(var):
    dados = get_all()
    colunas = ["ID", "Nome Cliente", "Rua", "Bairro", "Telefone", "Status", "Hora", "Data", "Previsão de Entrega"]
    data = pd.DataFrame(dados, columns=colunas)
    df = data[data['Status'].isin(var)]
    st.table(df)

def insere_entrega():
    nome_cliente = st.text_input("Nome cliente", key="nome_cliente_key")
    rua = st.text_input("Rua", key="rua_key")
    bairro = st.text_input("Bairro", key="bairro_key")
    telefone = st.text_input("Telefone", key="telefone_key")
    previsao = st.text_input("Previsao de Entrega", key = "previsao_key")

    if (len(telefone)==0):
        telefone = "49911111111"

    if st.button("Enviar Entrega"):
        if all(s != "" for s in [nome_cliente, rua, bairro, previsao]):
            data = {
                "nome_cliente": nome_cliente,
                "logradouro": rua,
                "bairro": bairro,
                "telefone": telefone,
                "id": 0,
                "status": "Aguardando",
                "hora": "NULL",
                "data": "NULL",
                "previsao":previsao
            }
            response = post(data)
            return response
        else:
            return st.write("Campos de texto inválidos")
    
def main():
    st.title("Gestão de Entregas - Ciotta")
    with st.container():
        insere_entrega()

    with st.container():
        populate_table(var_status)
        if st.button("Atualizar"):
            st.experimental_rerun()
    with st.container():
        if st.button("Ver entregues"):
            populate_table(var_status1)
if __name__ == "__main__":
    main()
