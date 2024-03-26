#Importar as bibliotecas Pandas e SQLite

import sqlite3
from sqlalchemy import create_engine
import pandas as pd

#Cria uma variável para chamar a conexão com o banco de dados

connect = sqlite3.connect('dadosCSV.db')

#Obter arquivos CSV a partir do Link

url = 'https://raw.githubusercontent.com/GuFelicio/HouseData/main/kc_house_data.csv'

#Importando o CSV para um DataFrame

df = pd.read_csv(url)

#Importando o DataFrame para dentro do BD, utilizando o Try e Except para tratar erros e descobrir se tudo ococrreu bem até esse ponto! 

try: 
  df.to_sql('dadosCSV', connect, if_exists='replace', index=False)
  print('Conexão com o BD estabelecida, o DB foi criado e o CSV foi importado para o DB! Vamos para o próximo passo!')

except Exception as e:
  print('Houve um erro ao importar o CSV para o BD! O erro é o seguinte: ', e)


#Exportando o BD para um novo arquivo CSV e importar, para utilizarmos em nosso arquivo do LookerStudio!

try:
  consultaSQL = "SELECT * FROM dadosCSV"
  dadosDB = pd.read_sql(consultaSQL, connect)

  dadosDB.to_csv('dadosCSV.csv', index=False)

  print('Tudo pronto! O DB foi exportado para um novo CSV chamado dadosCSV.csv!')

except Exception as f:
  print('Houve um erro ao exportar o DB para o CSV! O erro é o seguinte: ', f)