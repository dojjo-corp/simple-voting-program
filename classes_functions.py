'''Simple Voting Program Using Oop'''

import random as rn
from password_generator import strong_gen
from users import accounts


class Ballot:
    def __init__(self):
        self.id = f"BT_{rn.randint(1, 256)}"


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


class Voter:

    def __init__(self, student_id, email):
        self.id = student_id
        self.email = email
        self.votes_cast = 0

    def vote(self, candidate):
        # use list of candidate objects
        # for candidate in candidates:
        #     if candidate.get_id == candidate_id:
        #         if self.votes_cast > 1:
        #             print('You can only vote once!')
        #         candidate.votes += 1
        Candidate.votes += 1
        self.votes_cast += 1

    def show_profile(self):
        print(f'User ID: {self.id}\nEmail: {self.email}\nVotes Cast: {self.votes_cast}')

    def update_profile(self, ):
        print('You can only update your email address\n')
        self.email = input('Enter new email: ')


# generic functions (non-class functions)
def rpa():
    '''
    rpa basically stands for Random Password-Function Argument.
    This method generates a list of integers that can be used as
    arguments to the imported password generator function
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


def login():
    user_id = input('Enter your student id: ')
    if user_id not in accounts:
        print('Incorrect ID!')
    else:
        user_pass = input('Enter your password: ')
        if user_pass != accounts[user_id]['pass']:
            print('Incorrect Password!')
        else:
            print('Login Successful!')
            return


def sign_up():
    account_type = input('Choose account type:\n1. Regular\n2. Admin\n> ')
    user_id = input('Enter your student id: ')
    if accounts.setdefault(user_id, {}):
        print('User ID already exist')
    else:
        user_name = input('Enter your full name as appears on your student ID Card: ')
        user_pass = input('Enter your password (Enter 0 to generate one): ')
        if user_pass == '0':
            # tup stores list of integers from rpa function
            tup = rpa()
            a = tup[0]
            s = tup[1]
            n = tup[2]
            user_pass = strong_gen(s, n, a)
        accounts[user_id]['pass'] = user_pass
        accounts[user_id]['name'] = user_name

    # to be able to print key without value
    keys = accounts.keys()
    for k in keys:
        if user_id == k:
            print(f"Your id: {k}\nYour password: {accounts[k]['pass']}")
