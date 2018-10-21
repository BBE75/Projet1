# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings


# La fonction permet de mettre à jour les informations du compte renseigné par username et permet selon le niveau de
# privilège indiqué par group id de changer le role du compte (admin ou user)
def update(username, group_id):

    # on conserve le nom de compte originel dans une variable
    old_username = username
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
    file.close()
    while True:
        # Pour chaque champs on affiche la valeur actuel, si on appuie simplement sur entrée on garde cette valeur
        print('Changing Firstname or Lastname will change the username.')
        print('Type new value to change it, enter to keep it')

        print('Change firstname :', data[username][0], '? ')
        user_input = input().lower()
        if user_input != '':
            firstname = user_input
        else:
            firstname = data[username][0]
        print('Change lastname :', data[username][1], '? ')
        user_input = input().upper()
        if user_input != '':
            lastname = user_input
        else:
            lastname = data[username][1]
        print('Change email :', data[username][2], '? ')
        user_input = input()
        if user_input != '':
            email = user_input
        else:
            email = data[username][2]
        # Si l'utilisateur authentifié est un admin il peut changer le role du compte
        if group_id == '0':
            if data[username][3] == '0':
                role_name = 'Administrator'
            else:
                role_name = 'User'
            print('Change role :', role_name, '?\n0.Administrator\n1.User\nPress enter to do nothing')
            user_input = input()
            if user_input != '':
                if user_input in ['0', '1']:
                    role = user_input
                else:
                    role = data[username][3]
            else:
                role = data[username][3]
        else:
            role = data[username][3]

        username = (firstname[0]) + lastname.replace(" ", "").lower()
        # On affiche les nouvelles informations qui vont être entré dans le fichier selon le niveau de privilege.
        if group_id == '0':
            print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, end="")
            if role == '0':
                role_name = 'Administrator'
            else:
                role_name = 'User'
            print(" | email : ", email, " | role : ", role_name)
        else:
            print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, " | email : ", email)
        yesno = input("Are these information correct ? y/n: ").lower()
        if yesno == 'y':
            # Si les informations sont correct on vérifie que le nouvel username n'est pas déjà utilisé
            username_available = settings.add.checkusername(username)
            if username_available == 1 and username != old_username:
                print('Username already in use, aborting')
                break
            # On propose de générer un nouveau mot de passe
            yesno = input('Generate new password ? y/n: ').lower()
            if yesno == 'y':
                password = settings.add.random_password()
                print('The new password is: \'', password, '\'')
                password = settings.authenticate.password_hash(password)
            else:
                password = data[old_username][4]
        elif yesno == 'n':
            continue
        else:
            print("Aborting")
            break

        new_row = username + ',' + firstname + ',' + lastname + ',' + email + ',' + role + ',' + password + '\n'

        # On supprime d'abord les informations dans le fichier avant d'écrire les nouvelles (même si rien n'est changé)
        settings.delete.delete_user(old_username)

        with open(settings.CSV_FILE, 'a') as file:
            file.write(new_row)
        file.close()
        print("Informations updated...")
        input()
        break
