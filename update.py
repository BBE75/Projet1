import settings


def update(username, group_id):

    data = {}
    with open(settings.CSV_FILE) as file:
        reader = settings.csv.reader(file, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
    file.close()

    print('Changing Firstname or Lastname will change the username.')
    print('Type new value to change it, enter to keep it')

    user_input = input('Change firstname :', data[username][0], '? ')
    if user_input != '':
        firstname = user_input
    else:
        firstname = data[username][0]
    user_input = input('Change lastname :', data[username][1], '? ')
    if user_input != '':
        lastname = user_input
    else:
        lastname = data[username][1]
    user_input = input('Change email :', data[username][2], '? ')
    if user_input != '':
        email = user_input
    else:
        email = data[username][2]
    if group_id == '0':
        if data[username][3] == '0':
            role = 'Admin'
        else:
            role = 'User'
        user_input = input('Change role :', role, '?\n0.Administrator\n1.User\nPress enter to do nothing\n')
        if user_input != '':
            if role in ['1', '2']:
                role = user_input
            else:
                role = data[username][3]
        else:
            role = data[username][3]