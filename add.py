import settings


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

        while True:
            password = settings.getpass('Choose a password at lest 8 character long: ')
            if len(password) < 8:
                print("Password too short")
                continue
            password2 = settings.getpass('Retype your password: ')
            if password == password2:
                break
        print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, " | email : ", email,)
        yesno = input("Are these information correct ? y/n: ")
        if yesno.lower() == 'y':
            break

    hashed_password = settings.authenticate.password_hash(password)
    new_row = '\n'+username+','+firstname+','+lastname+','+email+','+group_id+','+hashed_password

    with open(settings.CSV_FILE, 'a') as file:
        file.write(new_row)
    file.close()
