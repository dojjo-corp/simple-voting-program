import users, password_generator
# login page
#print(users.accounts)
print('Welcome to Dojjo\'s Voting Page')
initial = input('1. Login\n2. Sign up\n> ')

if initial == '1':
    user_id = input('Enter your User ID: ')
    #if user_id not in user.accounts:
    #    print('User ID is not recognised!')
        # find a way to check if a dev-defined exception was raised 
        # to use in function for getting user input
        # eg. get_input(var_to_store_value, error_check,),,
    password = input('Enter your password: ')
    if user_id in users.accounts: 
        if users.accounts[user_id]['pass'] == password:
            print('login successful!')
        else:
            print('Wrong Password!')

    else:
        print('Wrong credentials!')
elif initial == '2':
    user_id = input('Enter your student ID (it\'ll be used as your user ID): ')
    name = input('What is your name? ')
    password = input('Enter your unique password: ')

