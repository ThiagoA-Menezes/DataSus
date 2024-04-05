# %%
# Validando a URL do datasus
import urllib.request
from tqdm import tqdm

def get_data_uf_ano_mes(uf ,ano, mes):
    url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RD{uf}{ano}{mes}.dbc"

    file = f"P:/Python - Projetos/Datasus/rd/dbc/RD{uf}{ano}{mes}.dbc"

    resp = urllib.request.urlretrieve(url, file) 

# Pega as datas e padroniza
def get_data_uf(ufs, datas):
    for i in tqdm(datas):
        ano, mes, dia = i.split("-")
        ano = ano [-2:]
        get_data_uf_ano_mes(uf, ano, mes)

# Lista de estados Brasileiros
ufs  = ["AC", "AL", "AP", "AM", "BA", 
        "CE", "DF", "ES", "GO", "MA", 
        "MT", "MS", "MG", "PA", "PB", 
        "PR", "PE", "PI", "RJ", "RN", 
        "RS", "RO", "RR", "SC", "SP", 
        "SE", "TO"]

# Lista de datas que serão baixadas do site do Datasus.
datas = ['2023-01-01']

for uf in ufs:
    print(uf)
    get_data_uf(ufs, datas)


# %%
## Criando um diretório para armazenamento dos dados e validando se o arquivo foi 
## armazenado corretamente no local indicado

import os

os.listdir("P:/Python - Projetos/Datasus/rd/dbc/")

# Criar a pasta na pasta
#os.mkdir("P:/Python - Projetos/Datasus/rd/dbc")

# %%
## Verificando o tamanho do arquivo



#%%
