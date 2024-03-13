# Let's start by having a look at a simple "while loop" example.
# While loops continue to itterate while the boolean value that's passed to them remains True.

# These variables will be used to create the boolean value for our while loop.
# We want to count to a specific number so we need 2 values: 
# 1 value to determine the desired end point and 1 value for the starting point.
num_to_count_to = 10
current_num = 1

# We start our while loop with a boolean value that must be true!
# If the boolean value we pass to our while loop is false, the loop will be skipped.
while current_num <= num_to_count_to:
    # Displays the desired end point alongside the current number
    print(f"Let's count to {num_to_count_to}! - {current_num}")
    # IMPORTANT!
    # If we don't include the following code we will get an infinite loop.
    # We need to ensure our while loop's boolean value will be set to false at some point.
    # If the boolean value is never set to false, the loop will continue infinitely.
    # This code below will increment our current number to bring us 1 digit closer to our 
    # desired end point.
    # If it's never incremented we will never reach our end point which means our boolean value 
    # will always stay True!
    current_num += 1


# While loops are mostly used when we don't know how many times to repeat a specific code block.
# For example, what if we ask the user for input, but we don't know the number of values they will add in total? 
# We can use a while loop to keep asking the user for input until they confirm they have entered everything.

# Create and empty string to store entered names in.
family_names = ""
# new_name will be used to store the current name / input from the user.
new_name = ""

# We continue to ask the user for input until they enter "exit" as their input.
# Again it's important to be able to set the boolean value to flase, or we will end up 
# with an loop that never ends!
while new_name.strip().lower() != "exit":
    # Add the most recently enter name to our string
    # This will add nothing for our starting point because both are empty
    family_names += new_name
    
    # Requests the user's input
    new_name = input("Please enter a name of someone in your famil or enter \"exit\" to stop.\nName: ")

    # If the user didn't opt to exit, we add a comma to improve formatting
    if new_name.strip().lower() != "exit":
        family_names += ", "

# Displays all the names entered by the user
print(f"Here is everyone in your family: {family_names}")


# Let's look at an example from our slide deck with some small changes

# Keeps count of number of kittens trying to take over the world
kittens = 0

# Simply adding a "True" boolean value like this will result in an endless loop ...
# UNLESS we include a break statement!
while True:

    # We ask the user for the number of kittens to add and tell them how to exit once done
    new_kitten_total = int(input("How many kittens are attempting to take over the world?\nEnter 0 to exit: "))

    # Checks if the user entered any number other than 0
    if new_kitten_total != 0:
        kittens += new_kitten_total

    # If the user entered 0, the while loop will break and exit
    else:
        break

# Finally we display to the user the number of kittens that tried to take over the world!
print(f"{kittens} are trying to take over the world!")

'''
Please take caution when creating infinite loops. As it may impact your device
    since it will become computationally expensive due to so many iterations being
        run in rapid sucession.
'''

'''while True:

    print("I am an infinite loop!")
    print("And no one can stop me!")'''

while True:

    question = input("Do you wish to stop me? (y/n) : ")

    if question == 'y':

        print("As you wish")
        break

while True:

    print("I am a loop!")
    question = input("Would you like me to continue? (y/n) : ")

    if question == "y":

        print("Back to the beginning!")
        continue

    else:

        print("I shall cease")
        break

'''
Difference with for loops is that we techically know how many times our loop will
    loop.

'''

# So instead of doing something like this :
print("Num 1")
print("Num 2")
print("Num 3")
print("Num 4")
print("Num 5")
print("Num 6")
print("Num 7")
print("Num 8")
print("Num 9")
print("Num 10")

# We could simply do :

for num in range(1, 11):
    print(f"Num {num}")
# Remember that range follows the same procedure as string slicing.
#   range(start, end, step)

string = "coffee"

for letter in string:
    print(letter)

