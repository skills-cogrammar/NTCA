
# Creating our first print output
print("Hello World!")

# Requesting input and then displaying the results
name = input("Enter your name: ")
print( "Weclome " + name)

age = input("Enter your age: ")
print(name + " you are " + age + " years old")

# We could add age in our print statement 
# because input always returns a string.
# However, after casting it to an int, we will instead get an error
# We cannot add different data types to strings
age = int(age)
# This will return an error
#print(name + " you are " + age + " years old")

# We can also hard code values to variables
current_year = 2023
# Since we cast age to an int value we can add it to other int values now
year_turn_100 = current_year + (100 - age)

# The result can then be turned into a string so that we can add it to other
# strings again
year_turn_100 = str(year_turn_100)

# Below has an example of an f string that makes it easier to format strings
# F strings can also be used to display non string values / add non string values
print("Hey " + name + " you will be 100 years old in " + year_turn_100)
print(f"Hey {name} you will be 100 years old in {year_turn_100}")

# If we want to create a string that spans multiple lines we will need to use a doc string
sentence = """Sunny days are the best. 
            I am always in the best mood when it is sunny. 
            If you ask me what the best weather is, I will say SUNNY!"""
# We can used built in string methods to make changes to our string
# The following method will change all the chars to lower case
# We will learn more about functions and methods in the future!
new_sentence = sentence.lower()

# .count will return the number of times "sunny" appears in our string
count_sunny = new_sentence.count("sunny")
print(count_sunny)

# Len is not a built in string method.
# This is why we don't use dot notation like we would with the methods related to specific data types
# The len function can also be used on lists and dictionaries and not just strings
# We will learn more about lists and dictionaries later on in the bootcamp too!
word = "Hello"
len_word = len(word)

print(len_word)


# Implicit casting is used by python when we work with two numerical data types
# In this example we're adding a float and an int.
# Python will automatically cast it to a float for us and save a float on "sum"
x = 10
y = 5.1
sum = x + y
# Displays sum as a float
print(sum)
sum = int(sum)
# Displays sum as an int after explicit casting to an int
print(sum)

# Explicit casting is when we tell python exactly which data type we want it to cast
# the variable to
num = "42"
num_int = int(num)

# We can also perform basic math opperations 
# Below are some examples along with the results of their opperations being displayed

# Adds two values together
add = 2 + 5
print(add)
# Subtract one value from another
minus = 2 - 5
print(minus)
# Multiply one value with another
product = 5*2
print(product)
# Divide one value by another
# IMPORTANT! Remember we cannot divide by 0 even when coding
# Attempting to divide by zero will always result in an error
div = 20/2
print(div)
# Will return what's left after removing the value 
# from the right as many times as possible from the value on the left
mod = 9%3
print(mod)
# The following will calculate the value of the number 
# of the left to the power of the number on the right
exponent = 6**2
print(exponent)

# Boolean values are always either true or false
# These are useful for checking certain conditions
# We will learn more about conditional statements and how to use them, later on in the bootcamp
my_bool = True
print(my_bool)
