import lcmolde as lc
import pandas as pd
import csv

# def verAgenda ():


def verLocais(nome):
    try:
        file = open(nome, 'r')
        for linha in file:
            dados_linha = linha.split(';')
            print(f'{dados_linha[2]:^15}{dados_linha[3]:^15}{dados_linha[4]:^15}{dados_linha[5]:^15}')
    except FileNotFoundError:
        return "Deu erro na busca de Locais"



def verBandas(nome):
    tabelaBandas = pd.read_csv("perfilXbandas.csv", sep=";")
    try:
        a = open(nome, 'r')
    except FileNotFoundError:
        return "Deu erro na busca por Bandass "
    else:
        return tabelaBandas
    


