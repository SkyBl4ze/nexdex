import sqlite3
from conn_database import connection
from open_ticket import openTicket
from edit_ticket import editTicket
from show_ticket import showTickets


# Painel Inicial 

def idleTicket():
        print("===================================================== \n")
        print("============ NEXDEX 0.1.0 PRE ALPHA ================= \n")
        print("===================================================== \n")

        idleAction = int(input("\n1 - Abrir chamado \n 2 - Exibir Cahamados \n 3 - Editar Chamados \n  0- Sair \n: Input:"))

        if idleAction == 1: 
            openTicket()
        
        elif idleAction == 2:
            showTickets();
        
        elif idleAction == 3:
            editTicket()

        elif idleAction == 0:
            print(" \n Bye!!! \n")
            quit()

        else:
            print("Please, insert a valid input and try again... \n")
            idleTicket()
        

idleTicket()
