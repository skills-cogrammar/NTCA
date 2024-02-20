# Example of Python sequences: lists, tuples, and dictionaries

# Lists: Ordered, mutable collection of items
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Accessing elements in a list
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing a list
print("Sliced list:", my_list[2:4])

# Modifying elements in a list
my_list[0] = 10
print("Modified list:", my_list)

# Tuples: Ordered, immutable collection of items
my_tuple = (1, 2, 3, 4, 5)
print("\nTuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Dictionaries: Unordered, mutable collection of key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:", my_dict)

# Accessing values in a dictionary
print("Value for key 'a':", my_dict['a'])

# Modifying values in a dictionary
my_dict['b'] = 20
print("Modified dictionary:", my_dict)


# Example of file I/O operations

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a tutorial on Python file I/O.")

# Reading from a file
with open("example.txt", "r") as file:
    contents = file.read()
    print("\nContents of the file:")
    print(contents)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending new content to the file.")

# Reading lines from a file
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nLines of the file:")
    for line in lines:
        print(line.strip())  # strip() removes leading/trailing whitespaces and newlines
