import pandas as pd
import banco_de_dados as banco


def pega_dados(url):
    dados = pd.read_excel(url)
    return dados


def pega_dados_ranking(ano):
    conexao = banco.conectar()
    sql = """SELECT * FROM tb_ranking WHERE temporada = ?"""
    lista_equipes = banco.selecionar_dados_condicional(conexao, sql, ano)
    banco.desconectar(conexao)
    return lista_equipes


def pega_tabela():
    conexao = banco.conectar()
    sql = "SELECT * FROM tb_completa"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_casa_fora():
    conexao = banco.conectar()
    sql = "SELECT * FROM tabela_casa_fora"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_jogos_mais_cartoes():
    conexao = banco.conectar()
    sql = "SELECT temporada, mandante, resultado, visitante, cartoes, amarelo, dois_amarelos," \
          " vermelho, arbitro FROM tb_jogos_mais_cartoes"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_jogos_mais_gols():
    conexao = banco.conectar()
    sql = "SELECT temporada, mandante, resultado, visitante FROM tb_jogos_mais_gols"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_maiores_placares():
    conexao = banco.conectar()
    sql = "SELECT temporada, mandante, resultado, visitante FROM tb_maiores_placares"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def divide_temporada(dados, dados2, temporada):
    tabela = dados[dados.Temporada == temporada]
    tabela = deleta_colunas(tabela)
    tabela2 = dados2[dados2.temporada == temporada]
    return tabela, tabela2


def pega_dados_casa(dados):
    jogos_casa = dados[['equipe_casa', 'pts_casa', 'jogos_casa', 'v_casa', 'e_casa', 'd_casa', 'gols_pro_casa',
                        'gols_contra_casa', 'sg_casa']]
    return jogos_casa


def pega_dados_visitante(dados):
    jogos_fora = dados[['equipe_fora', 'pts_fora', 'jogos_fora', 'v_fora', 'e_fora', 'd_fora', 'gols_pro_fora',
                        'gols_contra_fora', 'sg_fora']]
    return jogos_fora


def deleta_colunas(dados):
    dados = dados.drop(['Temporada', 'P'], axis=1)
    return dados


def redefine_nome_coluna_casa(dados):
    dados = dados.rename(columns={'equipe_casa': 'Time', 'jogos_casa': 'Jogos', 'v_casa': 'Vitórias',
                                  'e_casa': 'Empates', 'd_casa': 'Derrotas', 'gols_pro_casa': 'GP',
                                  'gols_contra_casa': 'GC', 'sg_casa': 'SG', 'pts_casa': 'Pontos'}, inplace=False)
    return dados


def redefine_nome_coluna_visitante(dados):
    dados = dados.rename(columns={'equipe_fora': 'Time', 'jogos_fora': 'Jogos', 'v_fora': 'Vitórias',
                                  'e_fora': 'Empates', 'd_fora': 'Derrotas', 'gols_pro_fora': 'GP',
                                  'gols_contra_fora': 'GC', 'sg_fora': 'SG', 'pts_fora': 'Pontos'}, inplace=False)
    return dados


def divide_casa_fora(dados):
    tabela = dados
    jogos_casa = pega_dados_casa(tabela)
    jogos_fora = pega_dados_visitante(tabela)
    jogos_casa = redefine_nome_coluna_casa(jogos_casa)
    jogos_fora = redefine_nome_coluna_visitante(jogos_fora)
    return jogos_casa, jogos_fora


def redefine_nome_classificacao(dados):
    dados = dados.rename(columns={'PTS': 'Pontos', 'J': 'Jogos', 'V': 'Vitórias', 'E': 'Empate', 'D': 'Derrota',
                                  '%': 'Aproveitamento'}, inplace=False)
    return dados
