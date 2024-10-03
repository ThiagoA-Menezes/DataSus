# transform
import sys
sys.path.insert(0, "P:/Python - Projetos/lib/pysus")
from datasus import read_dbc
import pandas as pd

df = pd.DataFrame(read_dbc("P:/Python - Projetos/Datasus/rd/dbc/RDAC2301.dbc"))
