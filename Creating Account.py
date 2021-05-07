global user
global passw
user = 'something'
passw = 'something'
def setting():
    print('work')

def test():
    print('Welcome to the testing')

def main():
    print('Welcome to the hub')
    print('What would you like to do?')
    print('Test')
    print('Setting')
    print('Quit')
    option = True
    while option:
        choose = input('')
        if choose.lower() == 'test':
            test()
            option = False
            break
        elif choose.lower() == 'setting':
            setting()
            option = False
            break
        elif choose.lower() == 'quit':
            print('ok bye')
            option = False
            break
        else:
            print('Please type the options given to you')

# Making account
def making_the_account():
    global user
    global passw
    user = input('Make a username:')
    passw = input('Make a password:')
    print('Great you have made an account')
    print('Would you like to login now?')
    
    login = False

    while login == False:
        go_to_account = input('Yes or No')
        
        if go_to_account.lower() == 'yes':
            login_to_account()
            login = True
            break
        elif go_to_account.lower() == 'no':
            print('ok')
            login = True
            break
        else:
            print('Please pick between Yes or No')

# login 
def login_to_account():
    access_to_account = False
    while access_to_account == False:
        enter_user = input('What is your username?')
        enter_passw = input('What is your password?')
        
        if enter_user == user and enter_passw == passw:
            main()
            access_to_account = True
            break
        else:
            print('Either your username or password is incorrect please try again')



# Welcoming to appilcation

print('Hello and welcome to the hub')
print('Would you like to make an account?')
making = False

while making == False:
    make_account = input('Yes or No?')

    if make_account.lower() == 'yes':
        making_the_account()
        making = True
    elif make_account.lower() == 'no':
        login_to_account()
        making = True
    else:
        print('Please between Yes or No')