import lcmolde as lc
import pandas as pd
import csv

# def verAgenda ():


def verLocais(nome):
    tabelaLocal = pd.read_csv("perfilXlocais.csv", sep=";")
    try:
        a = open(nome, 'r')
    except FileNotFoundError:
        return "Deu erro na busca de Locais"
    else:
        return tabelaLocal


def verBandas(nome):
    tabelaBandas = pd.read_csv("perfilXbandas.csv", sep=";")
    try:
        a = open(nome, 'r')
    except FileNotFoundError:
        return "Deu erro na busca por Bandass "
    else:
        return tabelaBandas
    


