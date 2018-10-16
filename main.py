import authenticate

value = authenticate.auth()
if value == 0:
    print("Authentication failure")
elif value == 1:
    print("Successfully logged as user")
else:
    print("Successfully logged as admin")