install.packages("read.dbc")
library(read.dbc)

path = "P:/Python - Projetos/Datasus/rd/dbc/RDAC2301.dbc"

df = read.dbc(path)

head(df)