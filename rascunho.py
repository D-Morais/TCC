# mostrar_informacoes_ranking(TEMPORADA_2023, 2023)

'''

def mostrar_informacoes_ranking(dados, ano):
    coluna1, coluna2 = st.columns([1, 4])
    coluna1.image(logo_cbf, width=100)
    coluna2.markdown(f"<h1 style='text-align: left;'>Ranking da CBF {ano}</h1>", unsafe_allow_html=True)

    ranking = api.pega_ranking(dados)
    st.table(ranking)


def deleta_colunas(dados):
    dados = dados.drop(['Temporada', 'Ranking', 'Pontos', 'Posicao', 'Jogos_casa', 'V_casa', 'E_casa', 'D_casa',
                        'gols_pro_casa', 'gols_contra_casa', 'saldo_gols_casa', 'pontos_casa', 'media_pontos_casa',
                        'Jogos_fora', 'V_fora', 'E_fora', 'D_fora', 'gols_pro_fora', 'gols_contra_fora',
                        'saldo_gols_fora', 'pontos_fora', 'media_pontos_fora'], axis=1)
    return dados


def divide_casa_fora(dados):
    tabela = dados
    jogos_casa = pega_dados_casa(tabela)
    jogos_fora = pega_dados_visitante(tabela)
    tabela = deleta_colunas(tabela)
    tabela = redefine_nome_classificacao(tabela)
    jogos_casa = redefine_nome_coluna_casa(jogos_casa)
    jogos_fora = redefine_nome_coluna_visitante(jogos_fora)
    return tabela, jogos_casa, jogos_fora

def pega_ranking(dados):
    tabela = dados
    ranking = tabela[['Time', 'Ranking', 'Pontos']]
    ranking = ranking.sort_values("Ranking", ascending=True)
    return ranking


def pega_dados_casa(dados):
    jogos_casa = dados[['Time', 'pontos_casa', 'Jogos_casa', 'V_casa', 'E_casa', 'D_casa', 'gols_pro_casa',
                        'gols_contra_casa', 'saldo_gols_casa']]
    return jogos_casa


def pega_dados_visitante(dados):
    jogos_fora = dados[['Time', 'pontos_fora', 'Jogos_fora', 'V_fora', 'E_fora', 'D_fora', 'gols_pro_fora',
                        'gols_contra_fora', 'saldo_gols_fora']]
    return jogos_fora

#DADOS = api_banco.pega_dados(r"dataset/tabela_brasileiro.xlsx")

def mostrar_tabela(mensagem, acao):
    st.text(mensagem)
    st.table(acao)


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

'''