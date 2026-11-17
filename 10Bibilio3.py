import streamlit as st

# Titulo do app
st.title("Ro-1966 StreamLit")

# Entrada de dados
nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite sua idade: ", min_value=0, step=1)

# Botão de ação

if st.button("Gerar Perfil"):
    st.success(f"Ola, {nome}! Você tem {idade} anos.")
    st.balloons()
