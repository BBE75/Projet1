# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings

# La fonction permet de créer un hash md5 qu'elle retourne en sortie à partir d'une chaine de caractères
def password_hash(password):
    byte_password = password.encode()
    hashed_password = settings.hashlib.md5(byte_password).hexdigest()
    return hashed_password

# La fonction def, permet de vérifier l'authentification d'un utilisateur, elle retourne ses infos de compte en sortie
def auth():

    # On créer le dictionnaire data vide, on lit le fichier CSV et on remplie data avec les lignes lues
    # Si l'authentification échoue on tue le script
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
        file.close()

    # On offre 3 essais pour la bonne saisie du nom de compte
    cpt = 0
    while cpt < 3:
        username = input('Username (EXIT to exit): ')

        if username.lower() == 'exit':
            settings.sys.exit()
        elif username not in list(data.keys()):
            print('User not found, ', 2-cpt, ' try remaining')
            cpt += 1
            if cpt == 3:
                print('Too many try, closing now')
                settings.sys.exit()
        else:
            break

    # Pareil pour le mot de passe, 3 essais
    cpt = 0
    while cpt < 3:
        password = settings.getpass('Password : ', stream=None)
        if password_hash(password) != data[username][4]:
            print('Wrong password, ', 2-cpt, ' try remaining')
            cpt += 1
            if cpt == 3:
                print('Too many try, closing now')
                settings.sys.exit()
        # On retourne les infos utilisateur sous forme de liste, il faut ajouter la clé en première valeure
        else:
            info_user = list(data[username])
            info_user.insert(0, username)
            return info_user

