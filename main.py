import classes_functions as vc
from users import regular, admin
from os import system as sys
# login page
print('Welcome to Dojjo\'s Voting Site')
response = input('1. Login\n2. Sign up\n> ')
if response == '1':
    user = vc.login()
elif response == '2':
    user = vc.sign_up()
else:
    quit('1')

print("\nChoose an option:\n1. Start voting\n2. Check Profile\n3. Quit (You can quit by entering x! at any prompt) ")


