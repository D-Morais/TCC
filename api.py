def dados_equipe(equipe):
    if equipe == "América - MG":
        return 19, 179060000, 30.1, 38, 113, 4, 29, 18, 156, 49
    elif equipe == "Atlético - MG":
        return 4, 601590000, 28.8, 41, 110, 10, 18, 10, 147, 40
    elif equipe == "Athletico - PR":
        return 7, 516380000, 25.7, 28, 96, 5, 18, 13, 131, 38
    elif equipe == "Bahia":
        return 13, 321400000, 25.1, 40, 126, 6, 26, 6, 160, 51
    elif equipe == "Botafogo":
        return 1, 377750000, 27.7, 30, 109, 2, 29, 12, 146, 41
    elif equipe == "Corinthians":
        return 18, 566070000, 26.6, 40, 91, 5, 15, 11, 122, 36
    elif equipe == "Coritiba":
        return 20, 230900000, 27, 29, 118, 7, 29, 12, 111, 30
    elif equipe == "Cruzeiro":
        return 5, 217540000, 27.8, 56, 105, 4, 27, 17, 163, 49
    elif equipe == "Cuiabá":
        return 14, 101790000, 27.7, 32, 93, 3, 22, 15, 124, 39
    elif equipe == "Flamengo":
        return 6, 908100000, 26.6, 41, 102, 2, 23, 13, 161, 45
    elif equipe == "Fluminense":
        return 3, 379210000, 28.7, 39, 87, 3, 29, 12, 115, 30
    elif equipe == "Fortaleza":
        return 11, 226200000, 28.8, 36, 85, 6, 28, 11, 164, 42
    elif equipe == "Goiás":
        return 16, 130900000, 27.6, 45, 107, 5, 19, 19, 135, 38
    elif equipe == "Grêmio":
        return 10, 318450000, 26.4, 34, 89, 3, 29, 11, 115, 30
    elif equipe == "Internacional":
        return 15, 376040000, 26.4, 38, 86, 2, 18, 13, 145, 43
    elif equipe == "Palmeiras":
        return 2, 908100000, 25.4, 53, 120, 6, 17, 12, 182, 53
    elif equipe == "Red Bull Bragantino":
        return 12, 486810000, 23.7, 38, 134, 3, 16, 14, 129, 35
    elif equipe == "Santos":
        return 9, 477880000, 25.1, 31, 106, 4, 30, 14, 113, 32
    elif equipe == "São Paulo":
        return 8, 490410000, 26.4, 37, 103, 2, 22, 10, 133, 35
    elif equipe == "Vasco da Gama":
        return 17, 460450000, 23.8, 41, 112, 8, 34, 12, 122, 35


def pega_historico_jogos(dados, time_a, time_b):
    tabela = dados
    tabela2 = tabela[(tabela.casa == time_a) & (tabela.visitante == time_b)]
    tabela2 = tabela2[['temporada', 'casa', 'placar', 'visitante']]
    tabela3 = tabela[(tabela.casa == time_b) & (tabela.visitante == time_a)]
    tabela3 = tabela3[['temporada', 'casa', 'placar', 'visitante']]
    return tabela2.head(), tabela3.head()


def pega_estatisticas(dados, time_a):
    tabela = dados
    tabela = tabela[tabela.Temporada == 2023]
    tabela2 = tabela[tabela.Equipe == time_a]
    posse_media_total = tabela2['Posse_Total']
    posse_media_casa = tabela2['Posse_Casa']
    return posse_media_total, posse_media_casa


def pega_dado_temporada(dados, ano):
    tabela = dados
    tabela = tabela[tabela.temporada == ano]
    tabela = tabela.drop(['temporada'], axis=1)
    return tabela


def pega_numero_jogos(dados):
    tabela = dados
    tabela = tabela['J'].mean()
    return tabela * 10


def pega_vitorias_casa(dados):
    tabela = dados
    num_vitoria_casa = tabela['v_casa'].sum()
    return num_vitoria_casa


def pega_vitorias_fora(dados):
    tabela = dados
    num_vitoria_fora = tabela['v_fora'].sum()
    return num_vitoria_fora


def pega_empates(dados):
    tabela = dados
    num_empates = tabela['e_casa'].sum()
    return num_empates


def pega_cartoes(dados, escolha):
    tabela = dados
    if escolha == 1:
        return tabela['CA'].sum()
    elif escolha == 2:
        return tabela['CV'].sum()


def info_defesa(dados, escolha):
    tabela = dados
    defesa = tabela[['Time', 'GC']]
    if escolha == 1:
        return defesa.sort_values("GC", ascending=True).head(5)
    elif escolha == 2:
        return defesa.sort_values("GC", ascending=False).head(5)


def pega_melhores_ataques(dados):
    tabela = dados
    times = tabela[['Time', 'GP']]
    times = times.sort_values("GP", ascending=False).head(5)

    return times


def pega_piores_ataques(dados):
    tabela = dados
    times = tabela[['Time', 'GP']]
    times = times.sort_values("GP", ascending=False).tail()

    return times


def pega_gols_feitos(dados):
    tabela = dados
    return tabela['GP'].sum()


def pega_gols_mandante(dados):
    tabela = dados
    gols_mandante = tabela['gols_pro_casa'].sum()
    return gols_mandante


def pega_gols_visitantes(dados):
    tabela = dados
    gols_visitante = tabela['gols_pro_fora'].sum()
    return gols_visitante


def pega_gols_contra(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    return tabela['GC'].sum()


def pega_assistencias(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    return tabela['Assis'].sum()


def pega_penaltis(dados, ano, op):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    if op == 1:
        return tabela['P_convertidos'].sum()
    elif op == 2:
        return tabela['P_batidos'].sum()


def pega_faltas(dados, ano, op):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    if op == 1:
        return tabela['Faltas_cometidas'].sum()
    elif op == 2:
        return tabela['Faltas_sofridas'].sum()


def pega_impedimentos(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    return tabela['Impedimentos'].sum()


def pega_media_posse(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    return tabela['Posse'].mean()


def pega_maiores_posses(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    times = tabela[['Equipe', 'Posse']]
    times = times.sort_values("Posse", ascending=False).head(5)

    return times


def pega_menores_posses(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    times = tabela[['Equipe', 'Posse']]
    times = times.sort_values("Posse", ascending=False).tail()

    return times


def retorna_times(dados):
    tabela = dados
    listaselecoes = tabela['Time'].tolist()
    listaselecoes.sort()
    listaselecoes2 = listaselecoes.copy()
    return listaselecoes, listaselecoes2


def pega_maiores_publicos(dados, ano):
    tabela = dados
    tabela = tabela[tabela.temporada == ano]
    publico = tabela[['publico']]
    publico = publico[publico.publico > 0]
    maiores_publicos = publico.sort_values("publico", ascending=False).head(5)

    return maiores_publicos


def pega_menores_publicos(dados, ano):
    tabela = dados
    tabela = tabela[tabela.temporada == ano]
    publico = tabela[['publico']]
    publico = publico[publico.publico > 0]
    piores_publicos = publico.sort_values("publico", ascending=False).tail(5)

    return piores_publicos


def num_jogadores_utilizados(dados, ano):
    tabela = dados
    tabela = tabela[tabela.Temporada == ano]
    return tabela['Num_jogadores'].sum()


def pega_arbitros(dados):
    tabela = dados
    listaarbitros = tabela['arbitro'].unique().tolist()
    listaarbitros.sort()
    return listaarbitros