#Importar as bibliotecas Pandas e SQLite

import sqlite3
import pandas as pd

#Criar uma conexão com o banco de dados

connect = sqlite3.connect('dadosCSV.db')

#Obter arquivos CSV a partir do Link

url = 'https://raw.githubusercontent.com/alura-cursos/imersao-dados-'



