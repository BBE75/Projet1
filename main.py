# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

# Structure du CSV : User,Name,Lastname,Email,GroupID,Hash

# Le fichier settings comporte toute les lib necessaire ainsi que les variables globales
import settings

# Fonction permettant d'initialiser la variable globale contenant le chemin relatif du fichier CSV
settings.init()
# L'utilisateur s'authentifie et on récupère ses informations pour pouvoir les utiliser par la suite
current_user_info = settings.authenticate.auth()

# On affiche un message selon le niveau de privilege
if current_user_info[4] == '0':
    print("Successfully logged as admin")
elif current_user_info[4] == '1':
    print("Successfully logged as user")

# Le menu de selection, tant qu'on ne sort pas en choissisant 0 le menu s'affiche après chaque action.
while True:

    # La fonction menu permet d'afficher les choix possibles selon le niveau de privilege passé en argument
    choice = settings.menu.menu(current_user_info[4])

    # Le choix 0 permet de quitter le script
    if choice == '0':
        input('Closing script, goodbye.')
        settings.sys.exit()
    # Le choix 1 permet d'ajouter un nouvel utilisateur pour les admins
    elif choice == '1':
        settings.add.adduser()
    # Le choix 2 permet de lister tous les utilisateurs pour les admins
    elif choice == '2':
        settings.list.listusers()
    # Le fhoix 3 permet d'éditer les infos d'un utilisateur pour les admins
    elif choice == '3':
        username = input('Input username: ')
        # On vérifie que le username renseigné existe bel et bien
        if settings.add.checkusername(username):
            settings.update.update(username, current_user_info[4])
        else:
            print('Username is incorrect')
    # Le choix 4 permet de supprimer un utilisateur pour les admins
    elif choice == '4':
        username = input('Input username: ')
        # On vérifie que le username renseigné existe bel et bien
        if settings.add.checkusername(username):
            settings.delete.delete_user(username)
        else:
            print('Username incorrect')
    # Le choix 5 permet d'afficher les infos d'un utilisateur pour les admins
    elif choice == '5':
        username = input('Input username to print its information: ')
        if settings.add.checkusername(username):
            settings.list.userinfo(username)
        else:
            print('Username incorrect')
    # Le choix 6 permet d'afficher ses infos de compte
    elif choice == '6':
        settings.list.userinfo(current_user_info[0])
    # Le choix 7 permet d'éditer ses infos de compte
    elif choice == '7':
        settings.update.update(current_user_info[0], current_user_info[4])

