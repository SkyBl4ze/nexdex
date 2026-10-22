import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent /"new_database.db"

#Função principal, que estabelesce a conexão com meu banco de dados, todas as funções com alteração na base de dados dependem dela!
def connection():
    connect = sqlite3.connect(DB_PATH)
    return connect

#Aqui, é realizada a primeira operação com a conexão, uma tabela é criada na base de dados anterior.
def writeDataBase():
    connect = connection()
    cursor = connect.cursor()

#Esse objeto executa um comando direto na base de dados! cursor.execute() será muito vista a partir de aqui, repetitivo, mas funciona!
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS chamados(
               titulo TEXT NOT NULL,
               categoria TEXT NOT NULL,
               prioridade INTEGER NOT NULL,
               solicitante TEXT NOT NULL,
               tecnico TEXT NOT NULL,
               comentarios TEXT NOT NULL,
               status INTEGER,
               id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        '''
    )

    connect.commit()
    connect.close()

connection()
writeDataBase()
