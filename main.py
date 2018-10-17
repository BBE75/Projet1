import settings

settings.init()
value = settings.authenticate.auth()
if value == 2:
    print("Authentication failure")
    settings.sys.exit()
elif value == 1:
    print("Successfully logged as user")
else:
    print("Successfully logged as admin")

choice = settings.menu.menu(value)

if choice == '1':
    settings.add.adduser()
elif choice == '2':
    settings.list.listuser()
elif choice == '4':
    username = input('Input username for deletion: ')
    settings.delete.delete_user(username)
