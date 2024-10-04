# install.packages("read.dbc")
# %%

# Essa parte do codigo foi criada para abrir o arquivo dbc
library(read.dbc)

load_path = "P:/Python - Projetos/Datasus/rd/dbc/RDAC2301.dbc"

export_path = "P:/Python - Projetos/Datasus/rd/csv/RDAC2301.csv"
df = read.dbc(load_path)
#head(df)
write.csv2(df, export_path, row.names=FALSE)


# %%
# Para utilizar o R no vscode, precisa declarar as libs Jsonlite e rLang
library(jsonlite)
library(rlang)

dbc_folder <- "P:/Python - Projetos/Datasus/rd/dbc/"
csv_folder <- "P:/Python - Projetos/Datasus/rd/csv/"
files <- list.files(dbc_folder)
#read.dbc(files)
#list.dirs(dbc_folder)
#list.files(dbc_folder)
#files

for(f in files){
    print(f)
    df <- read.dbc(f)
    lista <-  strsplit(f, "/")[[1]]
    file <- gsub(".dbc", ".csv", lista[length(lista)])
    write.csv2(df, paste(csv_folder, file, sep="/", row.names=FALSE))
}