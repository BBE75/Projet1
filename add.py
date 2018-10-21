# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings


# La fonction permet de générer un mot de passe alétoire de 8 caractères alaphanumerique
def random_password():
    available_char = settings.string.ascii_letters + settings.string.digits
    passwd = ""
    for i in range(8):
        passwd += available_char[settings.random.randint(0, len(available_char) - 1)]
    return passwd


# La fonction permet de vérifier si le nom de compte existe bel et bien
def checkusername(username):

    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]

        # On retourne 0 si le nom n'est pas present si il est present 1.
        if username not in list(data.keys()):
            present = 0
        else:
            present = 1
        file.close()
        return present


# La fonction permet de créer une nouvelle ligne dans le fichier CSV
def adduser():

    while True:
        print("**************ADD A NEW USER***********")
        # On force les prenoms en miniscule
        firstname = input("Input Firstname: ").lower()
        # les noms en majuscules
        lastname = input("Input Lastname: ").upper()
        email = input("Input email address: ")
        username = (firstname[0])+lastname.replace(" ", "").lower()

        # Saisie sécurisé on boucle tant qu'on à pas un choix correcte
        while True:
            group_id = input('Choose user privilege: \n0.Administrator\n1.User\n')
            if group_id in ['0', '1']:
                break
            print('Invalid selection')

        # Si on génère pas le mot de passe de façon automatique, ce snippet permet de saisir et verifie le mot de passe
        # while True:
        #     password = settings.getpass('Choose a password at lest 8 character long: ')
        #     if len(password) < 8:
        #         print("Password too short")
        #         continue
        #     password2 = settings.getpass('Retype your password: ')
        #     if password == password2:
        #         break

        # On génère un mot de passe aléatoire et on l'affiche pour que l'utilisateur puisse le noter
        password = random_password()
        print("The password associated with this username is: ", password)
        input()
        # On vérifié si les informations sont correct avant d'écrire dans le fichier
        print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, " | email : ", email,)
        yesno = input("Are these information correct ? y/n: ")
        if yesno.lower() == 'y':
            # Si les informations sont correct on vérifié que le nom de compte n'est pas déjà utilisé
            username_available = checkusername(username)
            if username_available == 1:
                print('Username already in use')
                continue
            break
        else:
            continue

    # On créer le hash à partir du mot de passe
    hashed_password = settings.authenticate.password_hash(password)
    new_row = username+','+firstname+','+lastname+','+email+','+group_id+','+hashed_password+'\n'

    # On écrit dans le fichier CSV
    with open(settings.CSV_FILE, 'a') as file:
        file.write(new_row)
    file.close()
    print("New user added...")
    input()
