import streamlit as st
from streamlit_option_menu import option_menu
import api
from PIL import Image

import informacoes as info

logo_cbf = Image.open("logo-topo.png")
DADOS = api.pega_dados(r"dataset/tabela_brasileiro.xlsx")
ESTATISTICAS = api.pega_dados(r"dataset/estatisticas.xlsx")
RESULTADOS = api.pega_dados(r"dataset/resultados_br.xlsx")
MAIORES_JOGOS = api.pega_dados(r"dataset/maiores_jogos.xlsx")
GOLS = api.pega_dados(r"dataset/gols.xlsx")
EQUIPES = api.pega_dados(r"dataset/dados_equipes.xlsx")


TEMPORADA_2023 = api.divide_temporada(DADOS, 2023)
TEMPORADA_2022 = api.divide_temporada(DADOS, 2022)
TEMPORADA_2021 = api.divide_temporada(DADOS, 2021)
TEMPORADA_2020 = api.divide_temporada(DADOS, 2020)
TEMPORADA_2019 = api.divide_temporada(DADOS, 2019)
TEMPORADA_2018 = api.divide_temporada(DADOS, 2018)
TEMPORADA_2017 = api.divide_temporada(DADOS, 2017)
TEMPORADA_2016 = api.divide_temporada(DADOS, 2016)
TEMPORADA_2015 = api.divide_temporada(DADOS, 2015)
TEMPORADA_2014 = api.divide_temporada(DADOS, 2014)


def mostrar_tabela(mensagem, acao):
    st.text(mensagem)
    st.table(acao)


def mostrar_informacoes_ranking(dados, ano):
    coluna1, coluna2 = st.columns([1, 4])
    coluna1.image(logo_cbf, width=100)
    coluna2.markdown(f"<h1 style='text-align: left;'>Ranking da CBF {ano}</h1>", unsafe_allow_html=True)

    ranking = api.pega_ranking(dados)
    st.table(ranking)


def mostrar_informacoes_campeonato(dados, ano):
    st.title(f"Campeonato brasileiro série A - {ano}")
    primeira_col, segunda_col, terceira_col, _ = st.columns([1, 1, 1, 9])
    tabela_completa, tabela_casa, tabela_fora = api.divide_casa_fora(dados)
    classificacao_completa = primeira_col.button("Total")
    classificacao_casa = segunda_col.button("Casa")
    classificacao_fora = terceira_col.button("Fora")
    if classificacao_completa:
        mostrar_tabela(f"Classificação Completa {ano}", tabela_completa)
    elif classificacao_casa:
        mostrar_tabela(f"Classificação Casa {ano}", tabela_casa)
    elif classificacao_fora:
        mostrar_tabela(f"Classificação Fora {ano}", tabela_fora)
    else:
        mostrar_tabela(f"Classificação Completa {ano}", tabela_completa)


def main():

    st.set_page_config(
        page_title="SoccerBr",
        layout="wide",
    )

    st.set_option('deprecation.showPyplotGlobalUse', False)
    hide_st_style = """
        <style> MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Inicio", "Temporadas", "Outros Dados", "Ranking CBF", "Formulário"],
            icons=["house", "calendar", "search", "trophy", "card-checklist"],
            menu_icon="cast",
            default_index=0
        )


    if selected == "Inicio":
        mostrar_informacoes_campeonato(TEMPORADA_2023, 2023)
        j1, j2 = st.columns(2)
        lista_times, lista_times2 = api.retorna_times(TEMPORADA_2023)
        time1 = j1.selectbox('Escolha o primeiro Time', lista_times)
        lista_times2.remove(time1)
        time2 = j2.selectbox('Escolha o segundo Time', lista_times2, index=1)
        proba = info.mostra_probabilidades(EQUIPES, time1, time2)
        j1.metric(label="", value="")
        j2.metric(label="", value="")
        st.subheader("Probabilidades")
        col1, col2, col3 = st.columns([2, 2, 1])
        for jogo in proba:
            col1.metric(label="Vitória do Mandante", value="{: .2f}%".format((jogo[2] * 100)))
            col2.metric(label="Empate", value="{: .2f}%".format((jogo[1] * 100)))
            col3.metric(label="Vitória do Visitante", value="{: .2f}%".format((jogo[0] * 100)))
        teste, teste2 = api.pega_historico_jogos(RESULTADOS, time1, time2)
        st.subheader("Últimos Confrontos")
        st.table(teste)
    if selected == "Temporadas":
        st.sidebar.subheader("Campeonato Brasileiro")
        lista_temporada = ["Brasileiro 2022", "Brasileiro 2021", "Brasileiro 2020",
                           "Brasileiro 2019", "Brasileiro 2018", "Brasileiro 2017",
                           "Brasileiro 2016", "Brasileiro 2015", "Brasileiro 2014"]
        opcao = st.sidebar.selectbox("Escolha uma temporada", lista_temporada)
        if opcao == "Brasileiro 2022":
            mostrar_informacoes_campeonato(TEMPORADA_2022, 2022)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2022)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2022)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2022, ESTATISTICAS, 2022)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2022)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2022)
        elif opcao == "Brasileiro 2021":
            mostrar_informacoes_campeonato(TEMPORADA_2021, 2021)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2021)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2021)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2021, ESTATISTICAS, 2021)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2021)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2021)
        elif opcao == "Brasileiro 2020":
            mostrar_informacoes_campeonato(TEMPORADA_2020, 2020)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2020)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2020)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2020, ESTATISTICAS, 2020)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2020)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2020)
        elif opcao == "Brasileiro 2019":
            mostrar_informacoes_campeonato(TEMPORADA_2019, 2019)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2019)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2019)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2019, ESTATISTICAS, 2019)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2019)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2019)
        elif opcao == "Brasileiro 2018":
            mostrar_informacoes_campeonato(TEMPORADA_2018, 2018)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2018)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2018)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2018, ESTATISTICAS, 2018)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2018)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2018)
        elif opcao == "Brasileiro 2017":
            mostrar_informacoes_campeonato(TEMPORADA_2017, 2017)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2017)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2017)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2017, ESTATISTICAS, 2017)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2017)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2017)
        elif opcao == "Brasileiro 2016":
            mostrar_informacoes_campeonato(TEMPORADA_2016, 2016)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2016)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2016)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2016, ESTATISTICAS, 2016)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2016)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2016)
        elif opcao == "Brasileiro 2015":
            mostrar_informacoes_campeonato(TEMPORADA_2015, 2015)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2015)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2015)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2015, ESTATISTICAS, 2015)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2015)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2022)
        elif opcao == "Brasileiro 2014":
            mostrar_informacoes_campeonato(TEMPORADA_2014, 2014)
            st.markdown('---')
            st.title("Resumo Estatístico")
            info.mostra_jogos(TEMPORADA_2014)
            st.markdown('---')
            info.mostra_cartoes(TEMPORADA_2014)
            st.markdown('---')
            info.mostra_dados_ataques(TEMPORADA_2014, ESTATISTICAS, 2014)
            st.markdown('---')
            info.mostra_dados_defesas(TEMPORADA_2014)
            st.markdown('---')
            #info.mostra_estatisticas_diversas(ESTATISTICAS, 2014)
    if selected == "Outros Dados":
        st.sidebar.subheader("Dados do Campeonato Brasileiro")
        st.title("Em desencolvimento...")
        lista_temporada = ["Todas", 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014]
        temporada = st.sidebar.selectbox("Selecione a temporada", lista_temporada)
        if temporada == "Todas":
            temporada = 2023
        escolha = st.radio(
            "Escolha uma opção de filtro para a pesquisa",
            ('Arbitro', 'Time'),
            horizontal=True
        )

        if escolha == 'Arbitro':
            lista_arbitros = api.pega_arbitros(RESULTADOS)
            arbitro = st.selectbox('Escolha um Arbitro', lista_arbitros)
            #teste1, tabela, teste, teste5, teste6, teste7, teste8, teste9 = api.jogos_aptados(RESULTADOS, arbitro, temporada)
            #st.text(f"Quantidade de jogos apitados = {teste1}")
            #st.text(f"Jogo apitado com mais gols com vitória do time mandante = {teste}")
            #st.text(f"Jogo apitado com menos gols com vitória do time mandante = {teste5}")
            #st.text(f"Jogo apitado com mais gols com vitória do time visitante = {teste6}")
            #st.text(f"Jogo apitado com menos gols com vitória do visitante = {teste7}")
            #st.text(f"Jogo apitado com mais gols com empate entre os times = {teste8}")
            #st.text(f"Jogo apitado com menos gols com empate entre os times = = {teste9}")
            mostrar = st.checkbox('Mostrar tabela com informações dos jogos')
            if mostrar:
                pass
                #st.table(tabela)
        else:
            st.write(f"Maior público como mandante {0}")

    if selected == "Ranking CBF":
        st.sidebar.subheader("Ranking da CBF")
        lista_ranking = ["2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014"]
        opcao = st.sidebar.selectbox("Escolha uma temporada", lista_ranking)
        if opcao == "2023":
            mostrar_informacoes_ranking(TEMPORADA_2023, 2023)
        elif opcao == "2022":
            mostrar_informacoes_ranking(TEMPORADA_2022, 2022)
        elif opcao == "2021":
            mostrar_informacoes_ranking(TEMPORADA_2021, 2021)
        elif opcao == "2020":
            mostrar_informacoes_ranking(TEMPORADA_2020, 2020)
        elif opcao == "2019":
            mostrar_informacoes_ranking(TEMPORADA_2019, 2019)
        elif opcao == "2018":
            mostrar_informacoes_ranking(TEMPORADA_2018, 2018)
        elif opcao == "2017":
            mostrar_informacoes_ranking(TEMPORADA_2017, 2017)
        elif opcao == "2016":
            mostrar_informacoes_ranking(TEMPORADA_2016, 2016)
        elif opcao == "2015":
            mostrar_informacoes_ranking(TEMPORADA_2015, 2015)
        elif opcao == "2014":
            mostrar_informacoes_ranking(TEMPORADA_2014, 2014)
    if selected == "Formulário":
        st.title("Formulário de validação")
        st.text("Muito obrigado por utilizar esta ferramenta.")
        st.text("Clique no link abaixo para acessar o formulário e dar seu feedback para melhoria da ferramenta.")
        st.write("[Formulário](https://forms.gle/7DKgLM99EzmwvTxZ9)")


if __name__ == '__main__':
    main()

