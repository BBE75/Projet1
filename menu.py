import settings


def menu(group_id):
    choice = 'a'

    if group_id == 0:
        valid_input = ['0', '1', '2', '3', '4', '5']
    elif group_id == 1:
        valid_input = ['0', '1', '2']

    while choice not in valid_input:
        if group_id == 0:
            print("1. Add user")
            print("2. List all users")
            print("3. Edit user")
            print("4. Delete user")
            print("5. Show user's information")
            print("0. Quit")

            choice = (input("Choose between 0 and 5:\n"))

            if choice not in ['0', '1', '2', '3', '4', '5']:
                print("Error, invalid input. Select a number between 0 and 5.")

        if group_id == 1:
            print("1. Show your information")
            print("2. Edit your information")
            print("0. Quit")

            choice = (input("Choose between 0 and 2:\n"))

            if choice not in valid_input:
                print("Error, invalid input. Select a number between 0 and 2.")
            if choice != '0':
                choice = int(choice) + 5
                break
    return choice

        

       
   

        

