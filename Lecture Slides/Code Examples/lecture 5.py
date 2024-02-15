# Example Variables
name = "Jimmy"
surname = "Python"

# Below is an example of an alternative way we could format a string
print("My name is {} {}, and I am a thorough {} enjoyer \
    ".format(name, surname, surname))

print("My name is {0} {1}, and I am a thorough {1} enjoyer \
    ".format(name, surname))

# Both of these examples would be the same as the following:
print(f"My name is {name} {surname}, and I am a thorough {surname} enjoyer")

# Neither of the two examples are "wrong"
# One might read better than the other however, which is why it's 
# important to take this into consideration

x = "twenty four"
y = 39
z = 13
# Here is a different example of how we can use doc strings
# alongside formatted strings 
print("""Your order of : burger, which costs R {}
Your order of : pizza, which costs R{}
Your order of : pepsi, whcih costs R{:.2f}""".format(x, y, z))

print(f"""Your order of : burger, which costs R {x}
Your order of : pizza, which costs R{y}
Your order of : pepsi, which costs R{z:.2f}""")

# This is an example of a program that counts how many 
# instances of a character there are in a string
count = 0
sentence = input("Please enter your string : ").lower()

# We will first validate the user's input for a char to count
while True:
    character = input("Please enter the character you would like to count : ").lower()

    # We check if the user as entered more than 1 char
    if len(character) > 1:
        print("You have entered more than one character, please try again ")
    
    # If the chars are not alphabetic we notify the user
    elif not character.isalpha():
        print("You have entered a number or symbol. please try again")

    # Otherwise we default to our else
    # This will only run if the string only containt alphabetic chars
    else:
        break

# we can now loop over our sentence and count the number of chars
# Below is as example of how we can do so if we also need the index
for char in range(len(sentence)):
    print(f"iteration: {char} character : {sentence[char]}")
    if character == sentence[char]:
        count += 1 # count = count + 1

print(f"The character : {character} appeared {count} times")

# Here is a list of strings
names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
    ]

# We can also access values using their index
# If the accessed item has an index we can then access the index 
# of that value
name = names[0]
print(name)
# This will access the first string in the list
# It will then access the value in index 1 of the first string
print(names[0][1])

# We can itterate over lists using for loops to display all the values
for i in names:
    print(i)

# If we need the temporary variable to take on an int value
# We could do the following
for i in range(len(names)): # range(6)
    print(f"{names[i]} is on index {i}")
    if i % 2 == 0:
        print(f"{names[i]} is on an even index")

# We pop the string that's on index 0
popped_name = names.pop(0)
print(popped_name)

# We create a new name to include in our list
new_name = "Jimbo"
names.insert(0, new_name)
print(names)

# We can also hard code the value directly if needed
names.insert(0, "Sol")
print(names)

# Lists can contain numbers, or any other data type!
numbers = [1, 2, 3, 4, 5]
ex_numbers = [6, 7.123, "Yes", False, ["Nested", "List"]]
# we can then combine lists using the following method
numbers.extend(ex_numbers)
print(numbers)

# Can use conditions similar to how we did with strings
if "Lucy" not in names:
    print("Not in list")

# Below is an example of a dictionary
my_dictionary = {
                "name":"Terry",
                "age":23,
                "is_funny":False
                } # key : value , key : value

# We can also pop values from dictionaries same as with lists
# The main difference is we need to use keys instead of indexes
popped = my_dictionary.pop("is_funny")
print(popped)
print(my_dictionary)

# Adding values to a dictionary is simple
# We can just call the dictionary with a key and assign a value
# If the key exists, it will be overwritten
# If not, the key and value will be created in the dictionary
my_dictionary['is_funny'] = popped
print(my_dictionary)

# Here is another example on how to add a new value
my_dictionary["is_cool"] = True
print(my_dictionary)

# We can also itterate over dictionaries and get both keys and values
for i, j in my_dictionary.items(): # i = keys, j = values
    print(f"{i} : {j}")

# Here is an alternative example
# In this case our temp variable will ALWAYS take on the value of the key
# This will only itterate over keys, however, we can then use that same key
# to access a value in our dictionary
for key in my_dictionary: 
    print(f"{key} : {my_dictionary[key]}")

# We can access values in a dictionary at any time using a key
# However, doing it this way will return an eror if the key does not
# exist
reference = my_dictionary["age"]
print(reference)

# This alternatively will see if the key exists 
# If the key does not exists, it will return none
value = my_dictionary.get("name")
print(value)

# Here is a basic example of how we can turn a list into a dictionary
names = ["John Python", "Sol Badguy", "Kazuya Mishima", "Terry Bogard"]
# Change into dictionary : Key = name : value = surname
name_dictionary = {}

for i in names:
    names = i.split(" ")
    print(names)

    name = names[0]
    surname = names[1]
    print(surname)
    name_dictionary[name] = surname
    
print(name_dictionary)

# We can also do this with two lists
# Note we can have a list accorss multiple lines, thanks to our brackets
new_names_list = [
                    "John Python", 
                    "Sol Badguy", 
                    "Kazuya Mishima", 
                    "Terry Bogard"
                ]
names_ages = [18, 43, 22, 55]
# We need to create an empty dictionary first to get started
new_dictionary = {}
# We need the following approach to get values of the same index number
# from both lists
for index in range(len(new_names_list)):
    # Here we now assign the name as a key
    # We also assign the age a value
    new_dictionary[new_names_list[index]] = names_ages[index]

# Now we can display our new dictionary
print(new_dictionary)