import streamlit as st
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , f1_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import scale
import numpy as np
import pickle
import api
import graficos


def mostra_probabilidades(dados, time_a, time_b):
    estatistica_time_a = api.dados_equipe(time_a)
    estatistica_time_b = api.dados_equipe(time_b)
    dados_times = estatistica_time_a + estatistica_time_b

    prev = np.array([dados_times]).reshape((1, -1))
    with open('modelo_RFC.sav', 'rb') as arquivo:
        modelo_carregado = pickle.load(arquivo)

    probabilidade = modelo_carregado.predict_proba(prev)
    #st.write(probabilidade)
    return probabilidade


def mostra_jogos(dados):
    quantidade_de_jogos = api.pega_numero_jogos(dados)
    vitoria_mandantes = api.pega_vitorias_casa(dados)
    vitoria_visitantes = api.pega_vitorias_fora(dados)
    empates = api.pega_empates(dados)
    col1, col2, col3 = st.columns((2.5, 2, 2))
    col1.metric(label="Rodadas disputadas", value=f"{int(quantidade_de_jogos / 10)}")
    col2.metric(label="Jogos realizados", value=f"{int(quantidade_de_jogos)}")
    col3.metric(label="Jogos realizados por rodada", value=f"{int(quantidade_de_jogos / 38)}")
    col2, col3, col4 = st.columns((2.5, 2, 2))
    col2.metric(label="Média de vitória dos mandantes por rodada", value="{: .2f}".format(vitoria_mandantes / 38))
    col3.metric(label="Média de empates por rodada", value="{: .2f}".format(empates / 38))
    col4.metric(label="Média de vitória dos visitantes por rodada", value="{: .2f}".format(vitoria_visitantes / 38))
    col1, col2, col3 = st.columns((2, 1, 1.5))
    col1.metric(label="", value="")
    col3.metric(label="", value="")
    col1.pyplot(graficos.grafico_resultados(vitoria_mandantes, vitoria_visitantes, empates))
    col3.pyplot(graficos.grafico_resultados_pizza(vitoria_mandantes, empates, vitoria_visitantes))


def mostra_cartoes(dados):
    st.subheader("Cartões apresentados na temporada")
    cartoes_amarelo = api.pega_cartoes(dados, 1)
    cartoes_vermelho = api.pega_cartoes(dados, 2)
    col1, col2, col3 = st.columns((2.5, 2.5, 2))
    col1.metric(label="Total de Cartões Apresentados", value=f"{cartoes_amarelo + cartoes_vermelho}")
    col2.metric(label="Média de Cartões Amarelos por Jogo", value="{: .2f}".format(cartoes_amarelo / 380))
    col3.metric(label="Média de Cartões Vermelho por Jogo", value="{: .2f}".format(cartoes_vermelho / 380))
    col1, col2, col3 = st.columns((2, 1, 1.5))
    col1.metric(label="", value="")
    col3.metric(label="", value="")
    col1.pyplot(graficos.grafico_cartoes(cartoes_amarelo, cartoes_vermelho))
    col3.pyplot(graficos.grafico_cartoes_pizza(cartoes_amarelo, cartoes_vermelho))


def mostra_dados_ataques(dados, estatisticas, ano):
    assistencias = api.pega_assistencias(estatisticas, ano)
    gols_marcados = api.pega_gols_feitos(dados)
    gols_mandantes = api.pega_gols_mandante(dados)
    gols_visitante = api.pega_gols_visitantes(dados)
    gols_contra = api.pega_gols_contra(estatisticas, ano)
    penaltis_convertidos = api.pega_penaltis(estatisticas, ano, 1)
    penaltis_batidos = api.pega_penaltis(estatisticas, ano, 2)
    melhores_ataques = api.pega_melhores_ataques(dados)
    ma = melhores_ataques.values.tolist()
    piores_ataques = api.pega_piores_ataques(dados)
    pa = piores_ataques.values.tolist()
    st.title("Estatísticas de Ataque")
    col1, col2 = st.columns([1, 1])
    col1.subheader("Melhores Ataques")
    for info in ma:
        col1.text(f"{info[0]} {info[1]}")
    col2.subheader("Piores Ataques")
    for info in pa:
        col2.text(f"{info[0]} {info[1]}")
    col1.metric(label="", value="")
    st.subheader("Dados de Gols")
    col1, col2, col3 = st.columns((2, 2, 2))
    col1.metric(label="Total de gols marcados", value=f"{gols_marcados}")
    col1.metric(label="Média de gols por jogo", value="{: .2f}".format(gols_marcados / 380))
    col3.metric(label="Total de Assistências", value=f"{assistencias}")
    col3.metric(label="Média de assistencias por jogo", value="{: .2f}".format(assistencias / 380))
    col1.metric(label="", value="")
    selecao = st.selectbox("Selecione qual dados quer visualizar", ["Gols Casa/Fora", "Divisão dos Gols", "Pênaltis"])
    if selecao == "Gols Casa/Fora":
        col1, col2, col3 = st.columns((2, 1, 1.5))
        col1.metric(label="Total de gols mandate", value=f"{gols_mandantes}")
        col1.metric(label="Média de gols do mandante por jogo", value="{: .2f}".format(gols_mandantes / 380))
        col3.metric(label="Total de gols visitante", value=f"{gols_visitante}")
        col3.metric(label="Média de gols do visitante por jogo", value="{: .2f}".format(gols_visitante / 380))
        col1.pyplot(graficos.grafico_gols(gols_mandantes, gols_visitante))
        col3.pyplot(graficos.grafico_gols_pizza(gols_mandantes, gols_visitante))
    elif selecao == "Divisão dos Gols":
        col1, col2, col3 = st.columns([2, 2, 1])
        col1.pyplot(graficos.grafico_divisao_gols(gols_marcados, penaltis_convertidos, gols_contra, assistencias))
    elif selecao == "Pênaltis":
        col1, col2, col3 = st.columns([2, 2, 1])
        col1.metric(label="Total de pênaltis batidos", value=f"{penaltis_batidos}")
        col2.metric(label="Total de pênaltis convertidos", value=f"{penaltis_convertidos}")
        col3.metric(label="Total de pênaltis errados", value=f"{penaltis_batidos-penaltis_convertidos}")
        col1.metric(label="", value="")
        col1.pyplot(graficos.grafico_penaltis(penaltis_batidos, penaltis_convertidos))


def mostra_dados_defesas(dados):
    st.title("Estatísticas de Defesa")
    col1, col2 = st.columns([1, 1])
    col1.subheader("Melhores Defesas")
    melhor_defesa = api.info_defesa(dados, 1)
    md = melhor_defesa.values.tolist()
    for info in md:
        col1.text(f"{info[0]} {info[1]}")
    col2.subheader("Piores Defesas")
    pior_defesa = api.info_defesa(dados, 2)
    p_def = pior_defesa.values.tolist()
    for info in p_def:
        col2.text(f"{info[0]} {info[1]}")


def mostra_dados_publico(dados, ano):
    maiores_publicos = api.pega_maiores_publicos(dados, ano)
    maiores_p = maiores_publicos.values.tolist()
    menores_publicos = api.pega_menores_publicos(dados, ano)
    menores_p = menores_publicos.values.tolist()
    st.title("Estatísticas de Público")
    col1, col2 = st.columns([1, 1])
    col1.subheader("Maiores Públicos")
    if maiores_publicos.empty:
        col1.text("Não a relato de público campeonato!")
    else:
        for info in maiores_p:
            col1.text(f"{info[0]}")
        col2.subheader("Menores Públicos")
        for info in menores_p:
            col2.text(f"{info[0]}")


def mostra_estatisticas_diversas(dados, ano):
    st.title("Estatísticas Diversas do Campeonato")
    col1, col2 = st.columns([1, 1])
    col1.subheader("Maiores Posses de Bola")
    maiores_posse = api.pega_maiores_posses(dados, ano)
    maiores_p = maiores_posse.values.tolist()
    for info in maiores_p:
        col1.text(f"{info[0]} {info[1]}")
    col2.subheader("Menores Posses de Bola")
    menores_posses = api.pega_menores_posses(dados, ano)
    menores_p = menores_posses.values.tolist()
    for info in menores_p:
        col2.text(f"{info[0]} {info[1]}")
    media_posse = api.pega_media_posse(dados, ano)
    impedimentos = api.pega_impedimentos(dados, ano)
    jogadores_utilizados = api.num_jogadores_utilizados(dados, ano)
    col1.metric(label="", value=f"")
    col2.metric(label="", value=f"")
    col1.metric(label="Média de posse de bola", value=f"{media_posse}")
    col2.metric(label="Quantidade de impedimentos", value=f"{impedimentos}")
    col2.metric(label="Média de impedimentos por jogo", value="{: .2f}".format(impedimentos / 380))
    col1.metric(label="Quantidade de jogadores utilizados", value=f"{jogadores_utilizados}")
