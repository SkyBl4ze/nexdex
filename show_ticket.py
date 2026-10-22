import sqlite3
from conn_database import connection
from open_ticket import openTicket

def showTickets():
    exibirChamados = input("Gostaria de pesquisar por chamado já registrado??? (S/N): \n")

    if exibirChamados == 's' or  exibirChamados =='S':

        idChamado = int(input("Insira o ID do chamado a ser localizado: \n"))
        
        connect = connection()
        cursor = connect.cursor()

        cursor.execute(
            """
                SELECT titulo FROM chamados WHERE id = ?
            """,(idChamado,))

        chamado = cursor.fetchone() #fetchall() selecionaria todos e  retornaria como um array!!!!

        print(chamado[0])

       #YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS!

    elif exibirChamados == 'n' or exibirChamados== 'N':
        print("Bye! \n")
        openTicket()
    
    else:
        print("Favor inserir caractere válido e tentar novamente.....\n")
        showTickets()

showTickets()
