import settings


def update(username, group_id):

    old_username = username
    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
    file.close()
    while True:
        print('Changing Firstname or Lastname will change the username.')
        print('Type new value to change it, enter to keep it')

        print('Change firstname :', data[username][0], '? ')
        user_input = input().lower()
        if user_input != '':
            firstname = user_input
        else:
            firstname = data[username][0]
        print('Change lastname :', data[username][1], '? ')
        user_input = input().upper()
        if user_input != '':
            lastname = user_input
        else:
            lastname = data[username][1]
        print('Change email :', data[username][2], '? ')
        user_input = input()
        if user_input != '':
            email = user_input
        else:
            email = data[username][2]
        if group_id == '0':
            if data[username][3] == '0':
                role_name = 'Administrator'
            else:
                role_name = 'User'
            print('Change role :', role_name, '?\n0.Administrator\n1.User\nPress enter to do nothing')
            user_input = input()
            if user_input != '':
                if user_input in ['0', '1']:
                    role = user_input
                else:
                    role = data[username][3]
            else:
                role = data[username][3]
        else:
            role = data[username][3]

        username = (firstname[0]) + lastname.replace(" ", "").lower()
        if group_id == '0':
            print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, end="")
            if role == '0':
                role_name = 'Administrator'
            else:
                role_name = 'User'
            print(" | email : ", email, " | role : ", role_name)
        else:
            print("| Username: ", username, " | Firstname: ", firstname, " | Lastname: ", lastname, " | email : ", email)
        yesno = input("Are these information correct ? y/n: ").lower()
        if yesno == 'y':
            username_available = settings.add.checkusername(username)
            if username_available == 1 and username != old_username:
                print('Username already in use, aborting')
                break
            yesno = input('Generate new password ? y/n: ').lower()
            if yesno == 'y':
                password = settings.add.random_password()
                print('The new password is: \'', password, '\'')
                password = settings.authenticate.password_hash(password)
            else:
                password = data[old_username][4]
        elif yesno == 'n':
            continue
        else:
            print("Aborting")
            break

        new_row = username + ',' + firstname + ',' + lastname + ',' + email + ',' + role + ',' + password + '\n'

        settings.delete.delete_user(old_username)

        with open(settings.CSV_FILE, 'a') as file:
            file.write(new_row)
        file.close()
        print("Informations updated...")
        input()
        break
