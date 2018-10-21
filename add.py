import settings


def random_password():
    available_char = settings.string.ascii_letters + settings.string.digits
    passwd = ""
    for i in range(8):
        passwd += available_char[settings.random.randint(0, len(available_char) - 1)]
    return passwd


def checkusername(username):

    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]

        if username not in list(data.keys()):
            present = 0
        else:
            present = 1
        file.close()
        return present


def adduser():

    while True:
        print("**************ADD A NEW USER***********")
        firstname = input("Input Firstname: ").lower()
        lastname = input("Input Lastname: ").upper()
        email = input("Input email address: ")
        username = (firstname[0])+lastname.replace(" ", "").lower()

        while True:
            group_id = input('Choose user privilege: \n0.Administrator\n1.User\n')
            if group_id in ['0', '1']:
                break
            print('Invalid selection')
        #Password is randomly generated
        # while True:
        #     password = settings.getpass('Choose a password at lest 8 character long: ')
        #     if len(password) < 8:
        #         print("Password too short")
        #         continue
        #     password2 = settings.getpass('Retype your password: ')
        #     if password == password2:
        #         break
        password = random_password()
        print("The password associated with this username is: ", password)
        input()
        print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, " | email : ", email,)
        yesno = input("Are these information correct ? y/n: ")
        if yesno.lower() == 'y':
            username_available = checkusername(username)
            if username_available == 1:
                print('Username already in use')
                continue
            break
        else:
            continue

    hashed_password = settings.authenticate.password_hash(password)
    new_row = username+','+firstname+','+lastname+','+email+','+group_id+','+hashed_password+'\n'

    with open(settings.CSV_FILE, 'a') as file:
        file.write(new_row)
    file.close()
    print("New user added...")
    input()
