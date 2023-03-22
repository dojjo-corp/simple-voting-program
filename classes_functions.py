# classes and functions to be used in voting program

import random as rn
import prettytable as pt
from password_generator import strong_gen
from users import regular, admin


class Poll:
    def __init__(self, candidates: list):
        '''candidates parameter is a list of Candidate objets'''
        self.id = f"BT_{rn.randint(1, 256)}"
        self.items = candidates

    def show_all(self) -> None:
        ballot_table = pt.PrettyTable()
        ballot_table.add_row(['Candidate Id', 'Name', 'Position'])
        for candidate in self.items:
            ballot_table.add_row([candidate.id, candidate.name, candidate.position])
        print(ballot_table)

    def delete_item(self, ballot_id: str) -> None:
        '''Removes only first instance of candidate with [ballot_id]'''
        for candidate in self.items:
            if ballot_id == candidate.id:
                if input(f'Are you sure you want to delete {candidate.name} (y/n)').lower() == 'y':
                    self.items.remove(candidate)
                    break
                else:
                    print(f'{candidate.name} not deleted!')


class Candidate:
    def __init__(self, name, position):
        self.id = f"CD_{rn.randint(1, 256)}"
        self.name = name
        self.position = position
        self.votes = 0

    def get_votes(self):
        return self.votes

    def get_id(self):
        return self.id


class Admin:
    def __init__(self, uid, email, name, passwd):
        self.id = uid
        self.email = email
        self.name = name
        self.passwd = passwd
        self.polls_created = []

    def create_poll(self, candidate_list):
        '''Returns a poll object. Must be assigned to variable'''
        poll = Poll(candidate_list)
        self.polls_created.append(poll)
        return poll

    def del_poll(self, poll_id: str) -> None:
        '''Deletes poll referenced by poll id'''
        for poll in self.polls_created:
            if poll_id == poll.id:
                self.polls_created.remove(poll)

    def mod_poll(self, poll_id: str):
        pass


class Voter:

    def __init__(self, student_id, email, name, passwd):
        self.id = student_id
        self.passwd = passwd
        self.name = name
        self.email = email
        self.votes_cast = 0
    
    # TONDO: VOTE METHOD
    def vote(self, candidate):
        candidate.votes += 1
        if self.votes_cast < 1:
            self.votes_cast += 1
        else:
            print('You can\'t vote more than once')
    
    # TODO: METHOD TO SHOW ACCOUNT PROFILE
    def show_profile(self):
        # format password to show only first 2 characters
        last_chars = ''.join(['*' for i in range(len(self.passwd[2::]))])
        temp_pass = f'{self.passwd[0:2]}{last_chars}'
        print(f'User ID: {self.id}\nEmail: {self.email}\nVotes Cast: {self.votes_cast}\nPassword: {temp_pass}')

    # TODO: METHOD TO UPDATE PROFILE - ONLY EMAIL
    def update_profile(self):
        print('You can only update your email address\n')
        self.email = input('Enter new email: ')


# generic functions (non-class functions)
# TODO: FUNCTION TO GENERATE RANDOM INTEGERS FOR PASSWORD-GENERATOR FUNCTION
def rpa():
    '''
    rpa basically stands for Random Password-Function Argument.
    This method generates a list of integers that can be used as
    arguments for the imported password-generator function
    '''
    while True:
        s = rn.randint(0, 17)
        n = rn.randint(0, 17)
        a = rn.randint(0, 17)
        final = []
        if s + n + a == 16:
            final.extend([a, n, s])
            break
    return final


# TODO: DEFINE LOGIN FUNCTION
def login() -> 'user object':
    # determine account type
    u_type = input('Select account type\n1. Regular\n2. Admin\n> ')
    if u_type == '1':
        account_dict = regular
        _type = 'regular'
    elif u_type == '2':
        account_dict = admin
        _type = 'admin'
    else:
        return login()

    user_id = input('Enter your id: ')
    # check if id exists in db
    if user_id in account_dict:
        temp_acc = account_dict[user_id]
        user_pass = input('Enter your password: ')
        if user_pass != account_dict[user_id]['pass']:
            print('Incorrect Password!')
            # second chance to be a good boy...
            return login()

        print('Login Successful!')
        if _type == 'regular':
            user_obj = Voter(user_id, temp_acc['email'], temp_acc['name'], temp_acc['pass'])
        else:
            user_obj = Admin(user_id, temp_acc['email'], temp_acc['name'], temp_acc['pass'])
        return user_obj

    else:
        print('Invalid ID!')
        # your last chance!
        return login()


# TODO: DEFINE SIGN_UP FUNCTION
def sign_up() -> dict:
    account_type = input('Choose account type:\n1. Regular\n2. Admin\n> ')
    if account_type == '1':
        account = regular
        _type = 'regular'
    elif account_type == '2':
        account = admin
        _type = 'admin'
    else:
        print('Wrong input!')
        # second chance to do the right thing
        return sign_up()

    user_id = input('Enter your id: ')
    # check if id exists already, make new entry if it doesn't
    if account.setdefault(user_id, {}):
        print('User ID already exist')
        # last chance to be human...
        return sign_up()
    else:
        user_name = input('Enter your full name as appears on your ID Card: ')
        user_email = input('Enter your email: ')
        user_pass = input('Enter your password (Enter 0 to generate one): ')

        # generate strong random password
        if user_pass.strip() == '0':
            # tup stores list of integers from rpa function
            tup = rpa()
            user_pass = strong_gen(tup[0], tup[1], tup[2])

        # add account info to entry
        account[user_id]['pass'] = user_pass
        account[user_id]['name'] = user_name
        account[user_id]['email'] = user_email

        account_d = {
            'type': _type,
            'id': user_id,
            'name': user_name,
            'email': user_email,
            'pass': user_pass
        }
    return account_d


# TODO: FUNCTION TO REMOVE IDs IN BOTH REGULAR AND ADMIN DICTIONARIES
def remove_dup(account):
    for uid in account['regular']:
        if uid in account['admin']:
            # admins can't be voters either! at least not with the same id...
            account['regular'].pop(uid)
