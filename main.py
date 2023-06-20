import streamlit as st
from streamlit_option_menu import option_menu

import api_banco
import api
import view


ESTATISTICAS = api_banco.pega_dados(r"dataset/estatisticas.xlsx")
RESULTADOS = api_banco.pega_dados(r"dataset/resultados_br.xlsx")
GOLS = api_banco.pega_dados(r"dataset/gols.xlsx")
EQUIPES = api_banco.pega_dados(r"dataset/dados_equipes.xlsx")
CASA_23 = api_banco.pega_dados(r"dataset/classificacao_casa_23.xlsx")
FORA_23 = api_banco.pega_dados(r"dataset/classificacao_fora_23.xlsx")
MAIS_CARTOES = api_banco.pega_tabela_jogos_mais_cartoes()
MAIS_GOLS = api_banco.pega_tabela_jogos_mais_gols()
MAIORES_PLACARES = api_banco.pega_tabela_maiores_placares()
DADOS = api_banco.pega_tabela()
DADOS_CASA = api_banco.pega_tabela_casa()
DADOS_FORA = api_banco.pega_tabela_fora()

TEMPORADA_2023 = api_banco.pega_dados(r"dataset/classificacao_completa_23.xlsx")
TEMPORADA_2022, CASA_22, FORA_22 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2022)
TEMPORADA_2021, CASA_21, FORA_21 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2021)
TEMPORADA_2020, CASA_20, FORA_20 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2020)
TEMPORADA_2019, CASA_19, FORA_19 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2019)
TEMPORADA_2018, CASA_18, FORA_18 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2018)
TEMPORADA_2017, CASA_17, FORA_17 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2017)
TEMPORADA_2016, CASA_16, FORA_16 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2016)
TEMPORADA_2015, CASA_15, FORA_15 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2015)
TEMPORADA_2014, CASA_14, FORA_14 = api_banco.divide_temporada(DADOS, DADOS_CASA, DADOS_FORA, 2014)


def main():

    st.set_page_config(
        page_title="SoccerBr",
        layout="wide",
    )

    st.set_option('deprecation.showPyplotGlobalUse', False)
    hide_st_style = """
        <style> MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
    """

    # Inject CSS with Markdown
    st.markdown(hide_st_style, unsafe_allow_html=True)
    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """

    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Inicio", "Temporadas", "Ranking CBF", "Formulário"],
            icons=["house", "calendar", "trophy", "card-checklist"],
            menu_icon="cast",
            default_index=0
        )

    # if st.button("Adiciona tabela"):
        # conexao = banco.conectar()
        # query = "SELECT id_equipe, nome_equipe, posicao, pontos, temporada FROM tb_ranking"
        # df = api_banco.pega_dados(r"C:\Users\morai\PycharmProjects\TCC\dataset\mais_gols.xlsx")
        # df = pd.read_sql_query(query, conexao)
        # st.write(df)
        # df.to_sql('tb_mais_gols', conexao, if_exists='replace')
        # conexao.close()

    # if st.button("Pega tabela completa"):
        # con = banco.conectar()
        # query = "SELECT * FROM tb_mais_gols"
        # df = pd.read_sql_query(query, con)
        # con.close()
        # st.write(df)
    if selected == "Inicio":
        view.mostrar_tabela_classificacao(TEMPORADA_2023, CASA_23, FORA_23, 2023)
        j1, j2 = st.columns(2)
        lista_times, lista_times2 = api.retorna_times(TEMPORADA_2023)
        time1 = j1.selectbox('Escolha o primeiro Time', lista_times)
        lista_times2.remove(time1)
        time2 = j2.selectbox('Escolha o segundo Time', lista_times2, index=1)
        proba = view.mostra_probabilidades(time1, time2)
        j1.metric(label="", value="")
        j2.metric(label="", value="")
        st.subheader("Probabilidades")
        col1, col2, col3 = st.columns([2, 2, 1])
        for jogo in proba:
            col1.metric(label="Vitória do Mandante", value="{: .2f}%".format((jogo[2] * 100)))
            col2.metric(label="Empate", value="{: .2f}%".format((jogo[1] * 100)))
            col3.metric(label="Vitória do Visitante", value="{: .2f}%".format((jogo[0] * 100)))
        historico, historico2 = api.pega_historico_jogos(RESULTADOS, time1, time2)
        st.subheader("Últimos Confrontos")
        st.table(historico)
    if selected == "Temporadas":
        st.sidebar.subheader("Campeonato Brasileiro")
        lista_temporada = ["Brasileiro 2022", "Brasileiro 2021", "Brasileiro 2020",
                           "Brasileiro 2019", "Brasileiro 2018", "Brasileiro 2017",
                           "Brasileiro 2016", "Brasileiro 2015", "Brasileiro 2014"]
        opcao = st.sidebar.selectbox("Escolha uma temporada", lista_temporada)
        if opcao == "Brasileiro 2022":
            view.mostrar_tabela_classificacao(TEMPORADA_2022, CASA_22, FORA_22, 2022)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2022, CASA_22, FORA_22)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2022)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2022, CASA_22, FORA_22, ESTATISTICAS, 2022)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2022)
            st.markdown('---')
            mais_gols = api.pega_dado_temporada(MAIS_GOLS, 2022)
            st.table(mais_gols)
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2022)
        elif opcao == "Brasileiro 2021":
            view.mostrar_tabela_classificacao(TEMPORADA_2021, CASA_21, FORA_21, 2021)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2021, CASA_21, FORA_21)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2021)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2021, CASA_21, FORA_21, ESTATISTICAS, 2021)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2021)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2021)
        elif opcao == "Brasileiro 2020":
            view.mostrar_tabela_classificacao(TEMPORADA_2020, CASA_20, FORA_20, 2020)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2020, CASA_20, FORA_20)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2020)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2020, CASA_20, FORA_20, ESTATISTICAS, 2020)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2020)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2020)
        elif opcao == "Brasileiro 2019":
            view.mostrar_tabela_classificacao(TEMPORADA_2019, CASA_19, FORA_19, 2019)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2019, CASA_19, FORA_19)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2019)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2019, CASA_19, FORA_19, ESTATISTICAS, 2019)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2019)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2019)
        elif opcao == "Brasileiro 2018":
            view.mostrar_tabela_classificacao(TEMPORADA_2018, CASA_18, FORA_18, 2018)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2018, CASA_18, FORA_18)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2018)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2018, CASA_18, FORA_18, ESTATISTICAS, 2018)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2018)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2018)
        elif opcao == "Brasileiro 2017":
            view.mostrar_tabela_classificacao(TEMPORADA_2017, CASA_17, FORA_17, 2017)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2017, CASA_17, FORA_17)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2017)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2017, CASA_17, FORA_17, ESTATISTICAS, 2017)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2017)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2017)
        elif opcao == "Brasileiro 2016":
            view.mostrar_tabela_classificacao(TEMPORADA_2016, CASA_16, FORA_16, 2016)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2016, CASA_16, FORA_16)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2016)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2016, CASA_16, FORA_16, ESTATISTICAS, 2016)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2016)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2016)
        elif opcao == "Brasileiro 2015":
            view.mostrar_tabela_classificacao(TEMPORADA_2015, CASA_15, FORA_15, 2015)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2015, CASA_15, FORA_15)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2015)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2015, CASA_15, FORA_15, ESTATISTICAS, 2015)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2015)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2022)
        elif opcao == "Brasileiro 2014":
            view.mostrar_tabela_classificacao(TEMPORADA_2014, CASA_14, FORA_14, 2014)
            st.markdown('---')
            st.title("Resumo Estatístico")
            view.mostra_jogos(TEMPORADA_2014, CASA_14, FORA_14)
            st.markdown('---')
            view.mostra_cartoes(TEMPORADA_2014)
            st.markdown('---')
            view.mostra_dados_ataques(TEMPORADA_2014, CASA_14, FORA_14, ESTATISTICAS, 2014)
            st.markdown('---')
            view.mostra_dados_defesas(TEMPORADA_2014)
            st.markdown('---')
            # info.mostra_estatisticas_diversas(ESTATISTICAS, 2014)
    if selected == "Ranking CBF":
        st.sidebar.subheader("Ranking da CBF")
        lista_ranking = ["2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014"]
        opcao = st.sidebar.selectbox("Escolha uma temporada", lista_ranking)
        if opcao == "2023":
            view.mostrar_ranking(2023)
        elif opcao == "2022":
            view.mostrar_ranking(2022)
        elif opcao == "2021":
            view.mostrar_ranking(2021)
        elif opcao == "2020":
            view.mostrar_ranking(2020)
        elif opcao == "2019":
            view.mostrar_ranking(2019)
        elif opcao == "2018":
            view.mostrar_ranking(2018)
        elif opcao == "2017":
            view.mostrar_ranking(2017)
        elif opcao == "2016":
            view.mostrar_ranking(2016)
        elif opcao == "2015":
            view.mostrar_ranking(2015)
        elif opcao == "2014":
            view.mostrar_ranking(2014)
    if selected == "Formulário":
        st.title("Formulário de validação")
        st.text("Muito obrigado por utilizar esta ferramenta.")
        st.text("Clique no link abaixo para acessar o formulário e dar seu feedback para melhoria da ferramenta.")
        st.write("[Formulário](https://forms.gle/7DKgLM99EzmwvTxZ9)")


if __name__ == '__main__':
    main()
