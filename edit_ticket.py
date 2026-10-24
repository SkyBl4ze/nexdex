import sqlite3
from conn_database import connection


# Agora, possibilitar a EDIÇÃO de conteúdo recuperado 

def editTicket():

    editID = input("Editar chamado? (Y/N) \n") #Entrada de chamados 

    if editID == 'y' or editID == 'Y':
        idSelector = int(input("Insira um ID válido já registrado para o chamado: \n")) #Localiza pelo ID

        conn = connection() #Invoca a função de conexão 
        cursor = conn.cursor()
        
        databaseId = cursor.execute(
                '''
                    SELECT id FROM TabelaTestes(
                        id    
                    )
        
                '''
            )

        if editID == databaseId[0]: #Recebe o id da base de dados e compara com a entrada do usuário

            whichContent = input("Which content you wants to edit?... \n") # Se a comparação for positiva, acessa a base de dados e realiza a edição

            if whichContent == 'Name':

                newContent = input("Enter the new name: \n")

            
                cursor.execute((
                    '''
                        INSERT ? INTO TabelaTestes(name)
                    '''
                ),newContent)


        elif whichContent == 'Desc':
            
                newContent = input("Enter the new description: \n")
            
                        
                cursor.execute((
                                '''
                                    INSERT ? INTO TabelaTestes(desc)
                                '''
                            ),newContent)

        elif whichContent == 'it_espec':
                    
                        newContent = input("Enter the new IT worker's name: \n")
                    
                                
                        cursor.execute((
                                        '''
                                            INSERT ? INTO TabelaTestes(it_worker)
                                        '''
                                    ),newContent)
            

        
      #Código repetido.... Procurar forma de fazer melhor hahahaha   


    else:
        print('OK\n')



editTicket()