# hello everyone
# absolute path - C:\Users\cjfpj.Z790M\OneDrive\Desktop\HyperionDev\Lecture Code\"lecture 6.py"
# relative path - Lectuer Code\"lecture 6.py"

# Let's look at some ways we can open a file in python:

# Method: Open() - load in file as an object
# Access Modes - 'r' ; 'w' ; 'a' ;

# traditional method
file_object = open("randomOtherFolder/list_of_cats.txt", "r")
print(file_object.read())
# process file logic
file_object.close()



# context manager

with open("cat_names.txt", "r") as file_object:
    #  process your logic
    print(file_object.read())

# File Reading

# Traditional Method
# cat_names_object = open("randomOtherFolder\cat_names.txt", 'r')
cat_names_object = open("randomOtherFolder/list_of_cats.txt", 'r')
print(cat_names_object)

# Read Method
# `cat_names_read = cat_names_object.read()` is reading the entire contents of the file
# `cat_names_object` and storing it in the variable `cat_names_read`.
# cat_names_read = cat_names_object.read()
# print(cat_names_read)

# Readline Method
# `cat_names_readline = cat_names_object.readline()` is reading a single line from the file object
# `cat_names_object` and storing it in the variable `cat_names_readline`.
cat_names_readline = cat_names_object.readline()
print(cat_names_readline)

cat_names_readline = cat_names_object.readline()
print(cat_names_readline)

# Readlines Method
# `cat_names_readlines = cat_names_object.readlines()` 
# is using the `readlines()` method to read all
# the lines of the file object `cat_names_object` 
# and store them in the variable
# `cat_names_readlines`. The `readlines()` 
# method returns a list where each element is a line from the
# file.
cat_names_readlines = cat_names_object.readlines()
print(cat_names_readlines)

print(cat_names_readlines[1])

# `cat_names_object.close()` is closing the file object `cat_names_object`. This is important to do
# after reading or writing to a file, as it frees up system resources and ensures that the file is
# properly closed.
cat_names_object.close()


# Best Practice Approach 
with open("randomOtherFolder/list_of_cats.txt", 'r') as cat_names_object:

    # print(cat_names_object)

    # Read Method
    cat_names_read = cat_names_object.read()
    print("\nRead Output: ")
    print(cat_names_read)

    # `cat_names_object.seek(0)` is used to move the file pointer to the beginning of the file. This
    # allows you to read the file from the start again, even if you have already read it once before.
    # In the given code, it is used to reset the file pointer before using the `readline()` and
    # `readlines()` methods to read the file again.
    cat_names_object.seek(0)

    # Readline Method
    cat_names_readline = cat_names_object.readline()
    print("\n Readline Output: ")
    print(cat_names_readline)
    
    cat_names_object.seek(0)

    # Readlines Method
    cat_names_readlines = cat_names_object.readlines()
    print("\n Readlines Output: ")
    print(cat_names_readlines)



# Iterating Over a file
with open("randomOtherFolder/random_names.txt", 'r') as file:
    file_contents = file.readlines()
    # print(file_contents)
    for line in file_contents:
        print(line, end="")
    print(file_contents)

# Exception Handling
# FileNotFound 
# IOError  

# The code is using exception handling to handle potential errors that may occur when opening and
# reading a file.
user_file = input("Please enter the name of the file you'd like to open")

try:
    with open(user_file, 'r') as file:
        file_contents = file.readlines()
        print(file_contents)
except FileNotFoundError:
    print("File not found! ")
except IOError as e:
    print(f"Error reading the file: {e}")


# Exceptin handling with traditional approach
random_names = open("randomOtherFolder/random_names.txt", 'r')
try:
    content = random_names.read()
    print(content)
    content = random_names.read()
    print(content)
finally:
    random_names.close()
    print("Closed the file")


while True:

    user_input = input("Please enter a number or exit to quit: ")

    if user_input.strip().lower() == "exit":
        break

    try:
        user_num = float(user_input)
        print(f"Your number is: {user_num}")

    except:
        print("Sorry, your input is not a valid number")

