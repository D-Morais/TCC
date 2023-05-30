import sqlite3


def conectar():
    return sqlite3.connect('banco_de_dados.db')


def desconectar(banco):
    banco.close()


def selecionar_dados_condicional(banco, string_sql, ident):
    with banco:
        cursor = banco.cursor()
        cursor.execute(string_sql, (ident,))
        return cursor.fetchall()


def selecionar_dados(banco, string_sql):
    with banco:
        cursor = banco.cursor()
        cursor.execute(string_sql)
        return cursor.fetchall()
