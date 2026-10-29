import sqlite3
from conn_database import connection
from open_ticket import openTicket
from edit_ticket import editTicket
from show_ticket import showTickets


# Painel Inicial 

def idleTicket():
        print("\n===================================================== \n")
        print("============ NEXDEX 0.1.0 PRE ALPHA ================= \n")
        print("===================================================== \n")

        idleAction = int(input("\n 1 - Abrir chamado \n 2 - Exibir Chamados \n 3 - Editar Chamados \n  0 - Sair \n\n: Input:"))

        if idleAction == 1: 
            openTicket()
            idleTicket()
        
        elif idleAction == 2:
            showTickets()
            print("\n")
            idleTicket()
        
        elif idleAction == 3:
            editTicket()
            print("\n")
            idleTicket()


        elif idleAction == 0:
            print(" \n Bye!!! \n")
            quit()

        else:
            print("Please, insert a valid input and try again... \n")
            print("\n")
            idleTicket()
        

idleTicket()
