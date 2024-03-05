# Example: Basic Input and Output in Python
# This example demonstrates how to get user input and display output.

# Requesting and displaying a simple string input
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Welcome to our Python tutorial.")

# Example: String Length, Replacement, and Slicing
# Demonstrates finding string length, replacing characters, and slicing.

sample_sentence = "Learning Python is fun!"
# Displaying the length of the string
print(f"The sentence is {len(sample_sentence)} characters long.")

# Replacing a specific character ('n' in this case) with another ('@')
modified_sentence = sample_sentence.replace('n', '@')
print(f"Modified sentence: {modified_sentence}")

# Slicing and reversing specific parts of the string
last_three = sample_sentence[-3:]  # Get last three characters
reversed_last_three = last_three[::-1]  # Reverse the slice
print(f"Last three characters reversed: {reversed_last_three}")

# Creating a new string from parts of the original
new_word = sample_sentence[:3] + sample_sentence[-2:]
print(f"New word created: {new_word}")

# Example : Working with Numbers and Basic Arithmetic
# This section shows basic arithmetic operations and working with different data types.

# Requesting numeric input and performing arithmetic operations
user_age = int(input("How old are you? "))
years_until_30 = 30 - user_age
print(f"You will be 30 in {years_until_30} years.")

# Example: Arithmetic Operations with User Input
# Demonstrates basic arithmetic operations based on user input.

# Requesting three numbers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Performing calculations
sum_numbers = num1 + num2 + num3
difference = num1 - num2
product = num3 * num1
average = sum_numbers / 3

# Displaying results
print(f"Sum: {sum_numbers}, Difference: {difference}, Product: {product}, Average: {average}")

# Example: String Manipulation Techniques
# Demonstrates simple string manipulations like slicing and replacing characters.

# Manipulating strings based on user input
favorite_word = input("Enter your favorite word: ")
# Replace 'a' with '@'
modified_word = favorite_word.replace('a', '@')
print(f"Your word with a twist: {modified_word}")

# Example 4: Conditional Statements in Python
# Shows how to use if-else statements to make decisions.

# Using conditional logic to respond to user input
if user_age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")

# Example: More on Data Types - Casting and Type Conversion
# Explains casting between different data types, such as converting strings to integers.

# Converting string input to integer and back
favorite_number = input("What is your favorite number? ")
favorite_number = int(favorite_number)  # Convert to integer
print(f"Your favorite number plus one is {favorite_number + 1}.")
# Convert back to string for concatenation
favorite_number = str(favorite_number)
print("Your favorite number in string form is " + favorite_number + ".")

# Example: Conditional Logic Based on Total Time
# Demonstrates how to use conditional logic to categorize results.

# Collecting event times from the user
swim_time = float(input("Enter swimming time in minutes: "))
cycle_time = float(input("Enter cycling time in minutes: "))
run_time = float(input("Enter running time in minutes: "))

# Calculating total time
total_time = swim_time + cycle_time + run_time

# Determining the award based on total time
if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Displaying the result
print(f"Total time: {total_time} minutes. Award: {award}.")
