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
            return 2
        elif username not in list(data.keys()):
            print('User not found')
            cpt += 1
            if cpt == 3:
                print('Too many try, closing now')
                return 2
        else:
            break
    cpt = 0
    while cpt < 3:
        password = settings.getpass('Password : ', stream=None)
        if password_hash(password) != data[username][4]:
            print('Wrong password')
            cpt += 1
            if cpt == 3:
                print('too many try, closing now')
                return 2
        else:
            if data[username][3] == '0':
                return 0
            else:
                return 1

