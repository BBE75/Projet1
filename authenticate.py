import settings


def password_hash(password):
    byte_password = password.encode()
    hashed_password = settings.hashlib.md5(byte_password).hexdigest()
    return hashed_password


def auth():

    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
        file.close()

    cpt = 0
    while cpt < 3:
        username = input('Username (EXIT to exit): ')

        if username.lower() == 'exit':
            settings.sys.exit()
        elif username not in list(data.keys()):
            print('User not found, ',3-cpt, ' try remaining')
            cpt += 1
            if cpt == 3:
                print('Too many try, closing now')
                settings.sys.exit()
        else:
            break
    cpt = 0
    while cpt < 3:
        password = settings.getpass('Password : ', stream=None)
        if password_hash(password) != data[username][4]:
            print('Wrong password, ', 3-cpt, ' try remaining')
            cpt += 1
            if cpt == 3:
                print('Too many try, closing now')
                settings.sys.exit()
        else:
            info_user = list(data[username])
            info_user.insert(0, username)
            return info_user

