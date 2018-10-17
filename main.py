import settings

settings.init()
value = settings.authenticate.auth()
if value == 2:
    print("Authentication failure")
elif value == 1:
    print("Successfully logged as user")
else:
    print("Successfully logged as admin")

choice = settings.menu.menu(value)

if choice == '1':
    settings.add.adduser()
