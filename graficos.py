import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def grafico_resultados_pizza(vitorias_mandantes, empates, vitorias_visitante):
    numero_de_jogos = vitorias_mandantes + empates + vitorias_visitante
    porcent_vm = vitorias_mandantes / numero_de_jogos
    porcent_em = empates / numero_de_jogos
    porcent_vv = vitorias_visitante / numero_de_jogos
    porcent = [porcent_vm, porcent_em, porcent_vv]
    resultados_possiveis = ["Mandante", "Empate", "Visitante"]
    cores = ["green", "blue", "red"]
    fig, ax = plt.subplots()
    explode = (0.02, 0.02, 0.02)
    ax.pie(porcent, labels=resultados_possiveis, autopct='%1.2f%%', explode=explode, startangle=50, colors=cores)
    ax.set_title("Porcentagem dos resultados", fontsize=10)
    plt.show()


def grafico_resultados(casa_ganhou, fora_ganhou, empate):
    resultados = [casa_ganhou, empate, fora_ganhou]
    resultados_possiveis = ["Mandante", "Empate", "Visitante"]
    cores = ["green", "blue", "red"]
    fig, ax = plt.subplots()
    bar_container = ax.bar(resultados_possiveis, resultados, color=cores)
    ax.set(ylabel="Número de jogos", title='Resultados dos jogos', ylim=(0, 380))
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()


def grafico_cartoes(ca, cv):
    cartoes = [ca, cv]
    numero_de_cartoes = ca + cv
    cartoes_possiveis = ["Amarelo", "Vermelho"]
    cores = ["yellow", "red"]
    fig, ax = plt.subplots()
    bar_container = ax.bar(cartoes_possiveis, cartoes, color=cores)
    ax.set(ylabel="Número de cartões", title='Cartões aplicados', ylim=(0, numero_de_cartoes))
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()


def grafico_cartoes_pizza(ca, cv):
    numero_de_cartoes = ca + cv
    porcent_ca = ca / numero_de_cartoes
    porcent_cv = cv / numero_de_cartoes
    porcent = [porcent_ca, porcent_cv]
    cartoes_possiveis = ["Amarelo", "Vermelho"]
    cores = ["yellow", "red", 'white']
    fig, ax = plt.subplots()
    explode = (0.2, 0)
    ax.pie(porcent, labels=cartoes_possiveis, autopct='%1.1f%%', explode=explode, startangle=50, colors=cores)
    ax.set_title("Porcentagem de cartões", fontsize=10)
    plt.show()


def grafico_gols(gols_casa, gols_visitante):
    gols = [gols_casa, gols_visitante]
    gols_possiveis = ["Mandante", "Visitante"]
    cores = ["green", "red"]
    fig, ax = plt.subplots()
    bar_container = ax.bar(gols_possiveis, gols, color=cores)
    ax.set(ylabel="Número de gols", title='Gols Marcados', ylim=(0, (gols_casa + gols_visitante)))
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()


def grafico_gols_pizza(gols_casa, gols_visitante):
    numero_de_gols = gols_casa + gols_visitante
    porcent_gc = gols_casa / numero_de_gols
    porcent_gv = gols_visitante / numero_de_gols
    porcent = [porcent_gc, porcent_gv]
    gols_possiveis = ["Mandante", "Visitante"]
    cores = ["green", "red"]
    fig, ax = plt.subplots()
    explode = (0.02, 0)
    ax.pie(porcent, labels=gols_possiveis, autopct='%1.2f%%', explode=explode, startangle=50, colors=cores)
    ax.set_title("Porcentagem dos gols", fontsize=10)
    plt.show()


def grafico_divisao_gols(total_gols, gols_penalti, gols_contra, gols_com_assistencias):
    gols = (total_gols - gols_penalti) - gols_contra
    outros_gols = gols - gols_com_assistencias
    gols_divisao = [gols_com_assistencias, outros_gols, gols_penalti, gols_contra]
    gols_possiveis = ["Com Assistência", "Outros", "Penalti", "Contra"]
    cores = ["green", "blue", "yellow", "red"]
    fig, ax = plt.subplots()
    bar_container = ax.bar(gols_possiveis, gols_divisao, color=cores)
    ax.set(ylabel="Número de gols", title='Divisão dos Gols', ylim=(0, total_gols + 100))
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()


def grafico_penaltis(penaltis_batidos, penaltis_convertidos):
    penaltis_errados = penaltis_batidos - penaltis_convertidos
    porcent_pc = penaltis_convertidos / penaltis_batidos
    porcent_pe = penaltis_errados / penaltis_batidos
    porcent = [porcent_pc, porcent_pe]
    penaltis_possiveis = ["Convertidos", "Errados"]
    cores = ["green", "red"]
    fig, ax = plt.subplots()
    explode = (0.1, 0)
    ax.pie(porcent, labels=penaltis_possiveis, autopct='%1.1f%%', explode=explode, startangle=60, colors=cores)
    ax.set_title("Porcentagem dos resultados", fontsize=10)
    plt.show()
