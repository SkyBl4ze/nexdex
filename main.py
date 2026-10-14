#SISTEMA DE GESTÃO DE CHAMADOS....
# ============================================================
# NexDesk - Sistema de Gestão de Chamados de TI
# ============================================================

# Descrição:
#     Sistema desenvolvido para gerenciar chamados de suporte
#     técnico, permitindo registrar, consultar e acompanhar
#     solicitações de atendimento de TI.

# Objetivo:
#     Desenvolver uma aplicação prática para gerenciamento
#     de chamados, aplicando conceitos de programação,
#     persistência de dados e organização de código.

# Funcionalidades planejadas:
#     - Abertura de chamados.
#     - Listagem e consulta de chamados por ID.
#     - Atualização do status dos chamados.
#     - Exclusão de chamados.
#     - Armazenamento dos dados em banco de dados.
#     - Histórico de atendimento e identificação de responsáveis
#       em versões futuras.

# Tecnologias:
#     - Python 3
#     - SQLite

# Estrutura atual:
#     - main.py: ponto de entrada e execução do sistema.
#     - helpdesk.db: banco de dados SQLite.

# Evolução planejada:
#     - Separação do código em módulos.
#     - API utilizando FastAPI.
#     - Autenticação e controle de acesso.
#     - Interface web para usuários e técnicos.
#     - Migração para PostgreSQL, se necessário.

# Versão: 0.1.0
# Status: Em desenvolvimento
# ============================================================
# Desenvolvido por Tiago Emanuel dos Santos Vieira (S4b4ton7) 
# """

import sqlite3

#Função principal, que estabelesce a conexão com meu banco de dados, todas as funções com alteração na base de dados dependem dela!
def connection():
    connect = sqlite3.connect("new_database.db")
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

writeDataBase()


#Aqui, será inserido o preenchimento da primeira solicitação (abertura de chamado)

def openTicket():
    
    print("===================================================== \n")
    print("============ NEXDEX 0.1.0 PRE ALPHA ================= \n")
    print("===================================================== \n")


    titulo = input("Título do chamado: \n")
    categoria = input("Categoria (Hardware,Internet,Impressora): \n")
    prioridade = int(input("Prioridade 0 - baixa, 1 - normal , 2 - alta : \n"))
    solicitante = input("Solicitante: \n")
    tecnico = input("Técnico responsável: \n")
    comentarios = input("Comentários: \n")
    status = int(input("Status 0 - Não resolvido 1 - Resolvido \n"))
    idChamado = int(input("ID do chamado: \n"))


    connect = connection()
    cursor = connect.cursor()

    cursor.execute((
        '''
            INSERT INTO chamados(
                titulo,
                categoria,
                prioridade,
                solicitante,
                tecnico,
                comentarios,
                status,
                id
            ) VALUES(?,?,?,?,?,?,?,?)
        '''
    ),(titulo,categoria,prioridade,solicitante,tecnico,comentarios,status,idChamado))

    print("CHAMADO REGISTRADO!!!!! > --------- < ")

    connect.commit()
    connect.close()

openTicket()