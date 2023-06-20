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


def pega_tabela_casa():
    conexao = banco.conectar()
    sql = "SELECT * FROM tb_classificacao_casa"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_fora():
    conexao = banco.conectar()
    sql = "SELECT * FROM tb_classificacao_fora"
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
    sql = "SELECT temporada, mandante, resultado, visitante FROM tb_mais_gols"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def pega_tabela_maiores_placares():
    conexao = banco.conectar()
    sql = "SELECT temporada, mandante, resultado, visitante FROM tb_maiores_placares"
    tabela = pd.read_sql_query(sql, conexao)
    conexao.close()
    return tabela


def divide_temporada(dados, dados_casa, dados_fora, temporada):
    tabela = dados[dados.temporada == temporada]
    tabela = deleta_colunas(tabela)
    tb_casa = dados_casa[dados_casa.temporada == temporada]
    tb_casa = deleta_colunas(tb_casa)
    tb_fora = dados_fora[dados_fora.temporada == temporada]
    tb_fora = deleta_colunas(tb_fora)
    return tabela, tb_casa, tb_fora


def pega_dados_casa(dados):
    jogos_casa = dados[['equipe_casa', 'pts_casa', 'jogos_casa', 'v_casa', 'e_casa', 'd_casa', 'gols_pro_casa',
                        'gols_contra_casa', 'sg_casa']]
    return jogos_casa


def pega_dados_visitante(dados):
    jogos_fora = dados[['equipe_fora', 'pts_fora', 'jogos_fora', 'v_fora', 'e_fora', 'd_fora', 'gols_pro_fora',
                        'gols_contra_fora', 'sg_fora']]
    return jogos_fora


def deleta_colunas(dados):
    dados = dados.drop(['temporada', 'index'], axis=1)
    return dados
