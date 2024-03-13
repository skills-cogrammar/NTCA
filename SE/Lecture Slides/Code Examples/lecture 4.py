import random as rd

def rock_paper_scissors(choice, win, lose):

    wins = win
    losses = lose

    select = ['rock', 'paper', 'scissors']
    cpu_choice = rd.choice(select)

    if cpu_choice == choice:
        print(f"Score - WIN:{wins}, LOSE:{losses}")
        return f"You chose {choice}, CPU chose {cpu_choice}. It's a tie!", wins, losses
    
    elif cpu_choice == 'rock' and choice == 'paper':
        wins += 1
        print(f"Score - WIN:{wins}, LOSE:{losses}")
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!", wins, losses
    
    elif cpu_choice == 'paper' and choice == 'scissors':
        wins += 1
        print(f"Score - WIN:{wins}, LOSE:{losses}")
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!", wins, losses
    
    elif cpu_choice == 'scissors' and choice == 'rock':
        wins += 1
        print(f"Score - WIN:{wins}, LOSE:{losses}")
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!", wins, losses

    else:
        losses += 1
        print(f"Score - WIN:{wins}, LOSE:{losses}")
        return f"You chose {choice}, CPU chose {cpu_choice}. The CPU wins!", wins, losses

total_wins = 0
total_lose = 0

while True:
    user_choice = input("Please enter either Rock, Paper or Scissors : ").lower()
    outcome, total_wins, total_lose = rock_paper_scissors(user_choice, total_wins, total_lose)

    print(outcome)
    
    terminate = input("Go again? (Y/N) : ").upper()
    
    if terminate == 'N':
        break
    
    elif terminate == 'Y':
        continue

        
def addition(x, y):
    value = x + y
    return value

x = int(input("Please enter a number : "))
y = int(input("Please enter a number : "))

total = addition(x, y)
print(total)


def login(username, password):
    '''
    Function takes in two string values.
    One for username and one for password.
    Returns True if the user logged in or false if they didn't.
    '''

    user = "admin" 
    security_word = "adm1n"

    if username != user:
        print('This username, does not exist!')
        return False

    elif password != security_word:
        print('Your password is incorrect!')
        return False
    
    else:
        print(f"Welcome {username}")
        return True


print("Welcome! Please login with your details!")

while True:

    user_name = input("Please enter your name :")
    pass_word = input("Please enter your password :")

    is_valid = login(user_name, pass_word)

    if is_valid:
        break


# Does nothing, because while the function is created, it's never called and cannot be called
lambda : print("Hello World!")

# Stores function in a variable for use later on
greeting = lambda : print("Hello there!")
greeting()

add_two = lambda x : x + 2
print(add_two(10))

welcome_msg = lambda name : print(f"Welcome back {name}")
welcome_msg("Bob")
welcome_msg("Bill")

