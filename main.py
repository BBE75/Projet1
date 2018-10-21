import settings

settings.init()
current_user_info = settings.authenticate.auth()

if current_user_info[4] == '0':
    print("Successfully logged as admin")
elif current_user_info[4] == '1':
    print("Successfully logged as user")

while True:

    choice = settings.menu.menu(current_user_info[4])

    if choice == '0':
        input('Closing script, goodbye.')
        settings.sys.exit()
    elif choice == '1':
        settings.add.adduser()
    elif choice == '2':
        settings.list.listusers()
    elif choice == '3':
        username = input('Input username: ')
        if settings.add.checkusername(username):
            settings.update.update(username, current_user_info[4])
        else:
            print('Username incorrect')
    elif choice == '4':
        username = input('Input username: ')
        if settings.add.checkusername(username):
            settings.delete.delete_user(username)
        else:
            print('Username incorrect')
    elif choice == '5':
        username = input('Input username to print its information: ')
        if settings.add.checkusername(username):
            settings.list.userinfo(username)
        else:
            print('Username incorrect')
    elif choice == '6':
        settings.list.userinfo(current_user_info[0])
    elif choice == '7':
        settings.update.update(current_user_info[0], current_user_info[4])

