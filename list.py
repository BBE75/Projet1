# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

import settings

# Cette fonction affiche la liste des nom de compte présent dans le fichier CSV
def listusers():
    print('*****LIST OF ALL KNOWN USER*****')
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        # Cette ligne permet d'ignorer la prmeière ligne qui contient le nom des champs
        skipheader = next(reader)
        for row in reader:
            data[row[0]] = row[1:]
        # Cette boucle permet d'afficher le numero de ligne (index) et le nom de compte
        for index, item in enumerate(data):
            row = str(index+1)+'.'+item
            print(row)
    file.close()
    input('Press enter to continue...')

# La fonction affiche les informations associé au compte renseigné par l'argument username en entré
def userinfo(username):

    # On place le contenue du fichier CSV dans le dictionaire data
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
        file.close()
    #On affiche toutes les informations sauf le hash md5
    print("Username: ", username)
    print("Firstname: ", data[username][0])
    print("Lastname: ", data[username][1])
    print("email : ", data[username][2])
    if data[username][3] == '0':
        print("Role: Admin")
    else:
        print("Role: User")
    input('Press enter to continue...')
