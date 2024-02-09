import random as rd

def rock_paper_scissors(choice):
    
    games = 0
    wins = 0
    losses = 0
    
    select = ['rock', 'paper', 'scissors']
    cpu_choice = rd.choice(select)

    if cpu_choice == choice:
        return f"You chose {choice}, CPU chose {cpu_choice}. It's a tie!"
    
    elif cpu_choice == 'Rock' and choice == 'Paper':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!"
    
    elif cpu_choice == 'Paper' and choice == 'Scissors':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You win!"


while True:
    user_choice = input("Please enter either Rock, Paper or Scissors : ").lower()
    outcome = rock_paper_scissors(user_choice)

    print(outcome)
    
    terminate = input("Go again? (Y/N) : ").upper()
    
    if terminate == 'Y':
        break
    
    elif terminate == 'N':
        continue


# The other checks Nizaam was too lazy to create

def addition(x, y):

    value = x + y
    return value

x = int(input("Please enter a number : "))
y = int(input("Please enter a number : "))

total = addition(x, y)
print(total * 4)


def login(username, password):

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