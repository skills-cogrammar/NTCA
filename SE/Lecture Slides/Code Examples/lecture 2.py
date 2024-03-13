# Here we can see a string with a mix of uppercase or lower case letters
# but what would we do if we needed it to be lower case?
# Well we can simply use the lower method to change all the chars to lowercase
message = "PyThOn Is Fun"
print(message)
print(message.lower())

# Python supports various operations on strings and numbers.
# For strings:
message = "Python is fun"
print(message.lower())  # Converts the string to lowercase.
print(message.upper())  # Converts the string to uppercase.

# Why would we use this?
# Working with data, you might need all data to be the same, and this coudl help
# normalize your data to make sure it's accurate.
# Similarly it might be that you're creating a login page for a user
# If the user needs to enter their email the system will see an email in all lower case
# and an email that's all uppercase as two different emails
# This will help us to better validate their input

# For instance, cleaning user input for comparison:
email = "  Example@Email.com "
clean_email = email.lower().strip()
# displays the cleaned email string
print(f"Cleaned email: {clean_email}")

# Here is an live example where we can use actual user input:
example_login = "test@tester.com"
user_input = input("Please enter you email: ")

# Here we now compare the email the user entered with the email we're expecting
if user_input.lower() == user_input:
    print("Your email is correct! Welcome!")
else:
    print("Sorry wrong email!")

# Since it needs to be an exact match, let's test what happens if we add a black space
example_login = "test@tester.com "
user_input = input("Please enter you email: ")
# Here we now compare the email the user entered with the email we're expecting
if user_input.lower() == user_input:
    print("Your email is correct! Welcome!")
else:
    print("Sorry wrong email!")

# How can we fix this? 
# We can fix this by using another string method called strip
# Lets test it!
print("Retrying ...")
if user_input.lower().strip() == user_input.strip():
    print("Your email is correct! Welcome!")
else:
    print("Sorry wrong email!")


# Next lets cover conditional statements 
# To start off, we'll use an f string to display the first part of our code block
# then we'll see if the person is an adult or not and display a message based on their age
name = "Alice"
print(f"Hello, {name}!")

# Numeric data types in Python include integers and floating-point numbers.
age = 30  # This is an integer.
height = 5.9  # This is a floating-point number.
print(f"{name} is {age} years old and {height} feet tall.")

# Conditional statements allow our programs to execute different code paths based on certain conditions.
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# For numbers:
num1 = 10
num2 = 20
print(f"Sum: {num1 + num2}")  # Adds two numbers.
print(f"Division: {num2 / num1}")  # Divides num2 by num1.

# Boolean data types are True or False values, useful in conditional logic.
is_adult = age > 18
if is_adult:
    print("Access granted.")
else:
    print("Access denied.")

# The power of conditional statements with logical operators:
temperature = 30  # Celsius
if temperature > 25:
    print("It's a hot day.")
elif temperature > 15:
    print("It's a nice day.")
else:
    print("It's cold.")

# Using logical operators (and, or, not) for compound conditions:
is_raining = False
if is_adult and not is_raining:
    print("You can go outside.")
else:
    print("Stay indoors or take an umbrella.")


# And handling numeric input for conditional logic:
user_age = input("Enter your age: ")
if int(user_age) >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")