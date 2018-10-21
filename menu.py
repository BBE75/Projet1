# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings


# On prend le niveau de privilege en argument d'entrée
def menu(group_id):
    choice = 'a'

    # Selon le niveau de privilege les choix possibles ne sont pas les mêmes
    if group_id == '0':
        valid_input = ['0', '1', '2', '3', '4', '5']
    elif group_id == '1':
        valid_input = ['0', '1', '2']

    # On sécurise l'input en autorisant qu'une liste de choix possible, tant que ces choix ne sont pas fait on boucle.
    while choice not in valid_input:
        if group_id == '0':
            print("1. Add user")
            print("2. List all users")
            print("3. Edit user")
            print("4. Delete user")
            print("5. Show user's information")
            print("0. Quit")

            choice = (input("Choose between 0 and 5:\n"))

            if choice not in ['0', '1', '2', '3', '4', '5']:
                print("Error, invalid input. Select a number between 0 and 5.")
                continue

        if group_id == '1':
            print("1. Show your information")
            print("2. Edit your information")
            print("0. Quit")

            choice = (input("Choose between 0 and 2:\n"))

            if choice not in valid_input:
                print("Error, invalid input. Select a number between 0 and 2.")
    # Pour éviter les doublons on ajouter 5 au choix d'un simple User (0 à 5 pour un admin)
    if group_id == '1' and choice != '0':
        choice = int(choice) + 5
    return str(choice)

        

       
   

        

