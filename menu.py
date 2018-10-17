
print("menus\n\n")

# 0 = admin , 1=user. mode user n'est pas demandé dans le sujet on abandonne ?
numID = 0
if numID == 0:
    print("Menu admin\n")
    print("1. add user")
    print("2. edit user")
    print("3. delete user")
    print("4. show user")
    print("0. quitter")
    choix = int(input("veuillez taper entre 0 et 4 pour choisir une option:\n"))
    while True:
        # si plus grand que 4
        if choix > 4:
            choix = int(input("erreur ! veuillez choisir un chiffre entre 0 et 4\n"))
            continue
        # creation de user
        elif choix == 1:
            # on ouvre le csv
            cs = open("C:/Users/phili/Desktop/user.csv", "a")
            name = input("veuillez entrer votre prenom :\n")
            lastname = input("veuillez entrer votre nom:\n")
            # prend 1ere lettre prenom + nom de famille. enleve espace nom de famille (da silva = dasilva)
            user = (name[0])+lastname.replace(" ", "")
            print("votre identifiant est :", user, "\n")
            print("génération du mot de passe.....\n")
            liste_de_caractères = string.ascii_letters+string.digits
            passwd = ""
            for i in range(8):
                passwd = liste_de_caractères[random.randint(0, len(liste_de_caractères)-1)]
                # génération du mdp chiffré
                h = settings.hashlib.md5(passwd.encode('utf-8')).hexdigest()
                continue
            print("mdp chiffré :",h)
            mail = input("entrez votre adresse mail:\n")
            ID = 1
            writer = csv.writer(cs, delimiter=";", lineterminator='\n')
            # ecrit dans le csv selon cet ordre
            writer.writerow([user, name, lastname, mail, ID, h])
            cs.close()
            break

        # consultation du csv
        elif choix == 4:
            cs = open("C:/Users/phili/Desktop/user.csv", "r+")
            ligne = csv.reader(cs)
            for row in ligne:
                # affiche toutes les lignes
                print(', '.join(row))
        break

        # quitte
        if choix == 0:
            break
        

       
   

        

