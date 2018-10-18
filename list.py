import settings


def listusers():
    print('*****LIST OF ALL KNOWN USER*****')
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        skipheader = next(reader)
        for row in reader:
            data[row[0]] = row[1:]
        for index, item in enumerate(data):
            row = str(index+1)+'.'+item
            print(row)
    file.close()
    input('Press enter to continue...')


def userinfo(username):

    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
        file.close()
    print("Username: ", username)
    print("Firstname: ", data[username][0])
    print("Lastname: ", data[username][1])
    print("email : ", data[username][2])
    if data[username][3] == '0':
        print("Role: Admin")
    else:
        print("Role: User")
    input('Press enter to continue...')
