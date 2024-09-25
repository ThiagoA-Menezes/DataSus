# %%
# Validando a URL do datasus
import urllib.request
from tqdm import tqdm

import sys

sys.path.insert(0, f"P:/Python - Projetos/lib/")

import dttools

# lib importada para fazer o processamento paralelo.
from multiprocessing import Pool 

def get_data_uf_ano_mes(uf ,ano, mes):
    url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RD{uf}{ano}{mes}.dbc"

    file = f"P:/Python - Projetos/Datasus/rd/dbc/RD{uf}{ano}{mes}.dbc"

    resp = urllib.request.urlretrieve(url, file) 

# Pega as datas e padroniza
def get_data_uf(ufs, datas):
    for i in tqdm(datas):
        ano, mes, dia = i.split("-")
        ano = ano [-2:]
        get_data_uf_ano_mes(ufs, ano, mes)

# Lista de estados Brasileiros
ufs  = ["AC", "AL", "AP", "AM", "BA", 
        "CE", "DF", "ES", "GO", "MA", 
        "MT", "MS", "MG", "PA", "PB", 
        "PR", "PE", "PI", "RJ", "RN", 
        "RS", "RO", "RR", "SC", "SP", 
        "SE", "TO"]

# Lista de datas que serão baixadas do site do Datasus.
datas = ['2023-01-01', '2023-02-01']

for uf in ufs:
    get_data_uf(ufs, datas)
data = [ ("AC", ['2023-01-01', '2023-02-01']),
         ("AM", ['2023-01-01', '2023-02-01']),
         ("AP", ['2023-01-01', '2023-02-01']),
          ("DF", ['2023-01-01', '2023-02-01']), ]
 
#with Pool(8) as pool:
#    print(ufs)
#    pool.starmap(get_data_uf,datas)
#
#import os
#
#os.listdir("P:/Python - Projetos/Datasus/rd/dbc/")
#
# Criar a pasta na pasta
#os.mkdir("P:/Python - Projetos/Datasus/rd/dbc")




# Aqui iremos colocar o array que vai fazer a baixa dos arquivos em paralelo.

#to_download = [(uf,datas) for uf in ufs]

# Inserindo a função que vai fazer o processamento paralelo.

#with Pool(2) as pool:
#    pool.starmap(get_data_uf, to_download)



# %%
