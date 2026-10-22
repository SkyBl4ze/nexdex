import sqlite3
from conn_database import connection


def openTicket():
    
    #Variavéis que recebem os valores
    titulo = input("Título do chamado: \n")
    categoria = input("Categoria (Hardware,Internet,Impressora): \n")
    prioridade = int(input("Prioridade 0 - baixa, 1 - normal , 2 - alta : \n"))
    solicitante = input("Solicitante: \n")
    tecnico = input("Técnico responsável: \n")
    comentarios = input("Comentários: \n")
    status = int(input("Status 0 - Não resolvido 1 - Resolvido \n"))
    idChamado = int(input("ID do chamado: \n"))

    #A conexão com a base de dados é realizada novamente
    connect = connection()
    cursor = connect.cursor()

    # Ele volotu! É a mesca coisa de antes
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
    #Mentira! só muda que agora no método execute, passamos um novo parâmetro, que 
    # contém as variavéis que foram armazenadas na entrada da função, associado elas
    # com seu correspondente na nossa tabela.

    print("===== > ------ <CHAMADO REGISTRADO! > ------ < ====== \n")

    # commita as alterações na base de dados. 
    connect.commit()
    #fecha a conexão
    connect.close()

openTicket()
