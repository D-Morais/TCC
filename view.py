import streamlit as st
import numpy as np
import pickle
import api
import api_banco
import graficos
from PIL import Image

logo_cbf = Image.open("logo-topo.png")


def mostra_probabilidades(time_a, time_b):
    estatistica_time_a = api.dados_equipe(time_a)
    estatistica_time_b = api.dados_equipe(time_b)
    dados_times = estatistica_time_a + estatistica_time_b

    prev = np.array([dados_times]).reshape((1, -1))
    with open('modelo_RFC.sav', 'rb') as arquivo:
        modelo_carregado = pickle.load(arquivo)

    probabilidade = modelo_carregado.predict_proba(prev)
    return probabilidade


def mostrar_tabela(mensagem, acao):

    st.text(mensagem)
    st.table(acao)


def mostrar_tabela_classificacao(tabela, tabela2, tabela3, ano):
    st.title(f"Campeonato brasileiro série A - {ano}")
    primeira_col, segunda_col, terceira_col, _ = st.columns([1, 1, 1, 9])
    classificacao_completa = primeira_col.button("Total")
    classificacao_casa = segunda_col.button("Casa")
    classificacao_fora = terceira_col.button("Fora")
    if classificacao_completa:
        mostrar_tabela(f"Classificação Completa {ano}", tabela)
    elif classificacao_casa:
        mostrar_tabela(f"Classificação Casa {ano}", tabela2)
    elif classificacao_fora:
        mostrar_tabela(f"Classificação Fora {ano}", tabela3)
    else:
        mostrar_tabela(f"Classificação Completa {ano}", tabela)


def mostra_jogos(tabela, tabela2, tabela3):
    quantidade_de_jogos = api.pega_numero_jogos(tabela)
    vitoria_mandantes = api.pega_vitorias(tabela2)
    vitoria_visitantes = api.pega_vitorias(tabela3)
    empates = api.pega_empates(tabela2)
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


def mostra_dados_ataques(tabela, tabela2, tabela3, estatisticas, ano):
    assistencias = api.pega_assistencias(estatisticas, ano)
    gols_marcados = api.pega_gols_feitos(tabela)
    gols_mandantes = api.pega_gols_feitos(tabela2)
    gols_visitante = api.pega_gols_feitos(tabela3)
    gols_contra = api.pega_gols_contra(estatisticas, ano)
    penaltis_convertidos = api.pega_penaltis(estatisticas, ano, 1)
    penaltis_batidos = api.pega_penaltis(estatisticas, ano, 2)
    melhores_ataques = api.pega_melhores_ataques(tabela)
    ma = melhores_ataques.values.tolist()
    piores_ataques = api.pega_piores_ataques(tabela)
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


def mostrar_ranking(ano):
    existe = True
    coluna1, coluna2 = st.columns([1, 4])
    coluna1.image(logo_cbf, width=100)
    coluna2.markdown(f"<h1 style='text-align: left;'>Ranking da CBF {ano}</h1>", unsafe_allow_html=True)
    lista_equipes = api_banco.pega_dados_ranking(ano)
    if not lista_equipes:
        st.warning("Nenhuma temporada cadastrada!")
        existe = False
    if existe:
        colms = st.columns((0.5, 0.5, 1, 2))
        campos = ['', 'Posição', 'Equipe', 'Pontos']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)
        for equipe in lista_equipes:
            _, col1, col2, col3 = st.columns((0.5, 0.5, 1, 2))
            col1.write(equipe[3])
            col2.write(equipe[2])
            col3.write(equipe[4])
