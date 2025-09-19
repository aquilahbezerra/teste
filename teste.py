import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_page_config(page_title='TESTE GAY', layout='wide')

cores = ['rosa', 'azul', 'preto', 'rosa choque',
         'azul marinho', 'laranja', 'verde', 'amarelo']

# print(cores)

def teste_cores(cor):
    cor = cor.lower()  # normaliza para minúsculas
    if cor not in cores:
        return "🤔 Cor não está na lista. Tente outra!"

    # Associações divertidas
    if cor == 'rosa':
        return "🌸 gay tradicional"
    elif cor == 'azul':
        return "🐉 gay encubado"
    elif cor == 'preto':
        return "🖤 Preto é misterioso e gay"
    elif cor == 'rosa choque':
        return "⚡ altamente abaitolado"
    elif cor == 'azul marinho':
        return "🌊 nem precisa falar(GAY ESPECIALISTA EM CORES)"
    elif cor == 'laranja':
        return "🍊 Gay"
    elif cor == 'verde':
        return "🌿 gay imaturo"
    elif cor == 'amarelo':
        return "☀️ gay donald trump"


st.title("Teste de Cores com Lista")

cor_input = st.text_input(
    "escolha uma dessas cores ['rosa', 'azul', 'preto', 'rosa choque', 'azul marinho', 'laranja', 'verde', 'amarelo']:")

if cor_input:
    resultado = teste_cores(cor_input)
    st.success(resultado)
