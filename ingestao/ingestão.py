# Importando as bibliotecas
# Installing libraries.

from calendar import month
import urllib.request
import os
from matplotlib.dates import DateLocator
from tqdm import tqdm
from multiprocessing import Pool, TimeoutError, Process
import datetime

# Aqui estou importando uma lib que peguei no curso do Teo Calvo.
import sys
sys.path.insert(0, "P:/Python - Projetos/lib/")
import dttools

## Aqui vamos passar a trabalhar com as variáveis para automatizar o processo de obtenção 
## do arquivo do Datasus criando funções

def get_data_uf_ano_mes(uf, ano, mes):
    url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RD{uf}{ano}{mes}.dbc"

    file = f"P:/Python - Projetos/Datasus/rd/dbc/RD{uf}{ano}{mes}.dbc"

    try: 
        resp = urllib.request.urlretrieve(url, file)
        #print(f"Download concluído: {file}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

def get_data_uf(uf, datas):
    for i in tqdm(datas):
        #print(f"Processando UF: {uf} com datas {datas}")
        ano, mes, dia = i.split("-")
        ano = ano[-2:]
        get_data_uf_ano_mes(uf, ano, mes)
    return(uf, datas)

## Lista de estados Brasileiros
#ufs  = ["AC", "AL", "AP", "AM", "BA", 
#        "CE", "DF", "ES", "GO", "MA", 
#        "MT", "MS", "MG", "PA", "PB", 
#        "PR", "PE", "PI", "RJ", "RN", 
#        "RS", "RO", "RR", "SC", "SP", 
#        "SE", "TO"] 

#datas = ['2023-01-01', '2023-02-01']

ufs = ['PR']

#vamos colocar um range de datas:
dt_start = '2022-01-01'
dt_stop = '2023-12-01'

datas = dttools.date_range(dt_start, dt_stop, monthly = True)


to_download = [(uf, datas) for uf in ufs]

## O curso do Teo explica que colocar o pool é suficiente para 
## fazer o processamento, porém, como estou usando o sistema windows,
## preciso passar esse parâmetro por for para que a função seja executada da
## forma esperada if __name__ == '__main__':
#data = [ ("AC", ['2023-01-01', '2023-02-01']),
#         ("AP", ['2023-01-01', '2023-02-01'])]


if __name__ == '__main__':

    with Pool(5) as pool:
        pool.starmap(get_data_uf, to_download)

# Daqui em diante, já vou seguir a dinamica do curso.