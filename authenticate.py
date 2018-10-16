import csv
import hashlib
from getpass import getpass


def password_hash(password):
    byte_password = password.encode()
    hashed_password = hashlib.md5(byte_password).hexdigest()
    return hashed_password

CSV_FILE = 'C:/Users/Benjamin/PycharmProjects/Projet1/ressources/user.csv'


def auth():

    data = {}
    with open(CSV_FILE) as fin:
        reader = csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
    cpt = 0
    while cpt < 3:
        username = input('Username (EXIT to exit):')
        if username not in list(data.keys()):
            print('user not found')
            cpt += 1
            if cpt == 3:
                print('too many try, closing now')
                return 0
        else:
            break
    cpt = 0
    while cpt < 3:
        password = getpass('Password :', stream=None)
        if password_hash(password) != data[username][4]:
            print('Wrong password')
            cpt += 1
            if cpt == 3:
                print('too many try, closing now')
                return 0
        else:
            if data[username][3] == '0':
                return 2
            else:
                return 1

