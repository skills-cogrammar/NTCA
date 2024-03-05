# This example demonstrates a simple program that keeps asking the user for a number until they enter a number greater than 10.

# Loop indefinitely until the user enters a number greater than 10
while True:
    # Ask the user for input
    user_input = input("Enter a number greater than 10: ")
    
    number = int(user_input)
    # Check if the number is greater than 10
    if number > 10:
        print("Thank you!")
        break  # Exit the loop
    else:
        print("The number must be greater than 10. Please try again.")

# This example asks the user for a password until they enter a valid one based on certain criteria (e.g., at least 8 characters long and contains a digit).

# Keep asking for the password until it meets the criteria
while True:
    user_password = input("Enter a new password (at least 8 characters and contains a digit): ")
    if user_password == "adm1n":
        print("Password is valid!")
        break
    else:
        print("Invalid password. Please try again.")

# In this example, users are prompted to enter data until they input a specific sentinel value to stop the input process (e.g., "done").
entries = ""

print("Enter data (type 'done' to finish):")
while True:
    entry = input()
    if entry == "done":
        break  # Exit the loop when the user enters "done"
    else:
        entries += entry  # Add the entry to the string

print("You entered the following data:")
for entry in entries:
    print(entry)

# This example shows how to create a simple square pattern of asterisks.
size = 5  # Size of the square

for i in range(size):
    for j in range(size):
        print('*', end='')  # Print asterisk without newline, end='' avoids new line after each print
    print()  # Print newline to move to the next row

# Here, we generate a right-angled triangle pattern using a for loop.
    
height = 5  # Height of the triangle

for i in range(1, height + 1):
    print('*' * i)  # Print asterisks i times

# This example demonstrates how to create a checkerboard pattern using nested loops and conditionals.

size = 8  # Size of the checkerboard

for i in range(size):
    for j in range(size):
        # Check if the sum of the indices is even or odd to decide when to print a space or asterisk
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # Move to the next line after printing one row of the checkerboard

# This example shows how to create a hollow square pattern with asterisks.
size = 5  # Size of the square

for i in range(1, size + 1):
    for j in range(1, size + 1):
        # Print asterisks for the border
        if i == 1 or i == size or j == 1 or j == size:
            print('*', end='')
        else:
            print(' ', end='')  # Print space for the inner square
    print()  # Move to the next line

# This complex example demonstrates creating a zigzag pattern across multiple lines.
    
height = 3  # Height of the zigzag pattern
length = 10  # Length of the zigzag pattern

for i in range(1, height + 1):
    for j in range(1, length + 1):
        # Check if the position is on the diagonal of a zigzag segment
        if ((j - 1) % (2 * (height - 1)) == i - 1) or ((j - 1) % (2 * (height - 1)) == 2 * (height - 1) - (i - 1)):
            print('*', end='')
        else:
            print(' ', end='')
    print()

# A simple function that takes two arguments and returns their sum.
def add_numbers(a, b):
    """Returns the sum of a and b."""
    return a + b

# Example usage
result = add_numbers(5, 3)
print(result)  # Output: 8

# This function prints a greeting message with a given name.
def greet(name):
    """Prints a greeting message with the given name."""
    print(f"Hello, {name}!")

# Example usage
greet("Alice")  # Output: Hello, Alice!

# A function to calculate the area of a circle given its radius.
def circle_area(radius):
    """Returns the area of a circle with the given radius."""
    pi = 3.14159
    return pi * radius ** 2

# Example usage
area = circle_area(5)
print(area)  # Output: 78.53975

# Conversion Between Temperature Scales
# Two functions, one to convert Celsius to Fahrenheit and another to convert Fahrenheit to Celsius. 
# Then, a third function demonstrates how to use these two functions.
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_temperatures():
    """Demonstrates the use of temperature conversion functions."""
    celsius = 20
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}C is equivalent to {fahrenheit}F")
    
    fahrenheit = 68
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}F is equivalent to {celsius}C")

# Example usage
convert_temperatures()

# Calculating Total Price with Tax
# This example shows a function to calculate tax for a given price and a function to calculate the total price including tax. 
# The second function utilizes the first.
def calculate_tax(amount, tax_rate):
    """Calculates the tax for a given amount and tax rate."""
    return amount * tax_rate / 100

def total_price_with_tax(amount, tax_rate):
    """Calculates the total price including tax."""
    tax = calculate_tax(amount, tax_rate)
    return amount + tax

# Example usage
total_price = total_price_with_tax(100, 5)
print(f"The total price with tax is: ${total_price}")  # Output: The total price with tax is: $105.0


# In this example, a user is presented with a menu of options and is asked to make a selection until they choose a valid option.
def display_menu():
    """Displays the menu of options to the user."""
    print("Please choose an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

def get_user_choice():
    """Asks the user to select a menu option."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Main program loop
while True:
    user_choice = get_user_choice()
    if user_choice == '1':
        print("Option 1 selected.")
    elif user_choice == '2':
        print("Option 2 selected.")
    elif user_choice == '3':
        print("Exiting program.")
        break  # Exit the loop
    else:
        # This should never happen due to validation, but included for completeness
        print("An unexpected error occurred.")
