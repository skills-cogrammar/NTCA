'''
# --------------------------------------------------------------------- #
# Create counter going down from n - 1
'''

# def countdown(n):
#     if n == 0:
#         return 

#     print(n)
#     countdown(n - 1)
    

# countdown(10)


'''
# --------------------------------------------------------------------- #
# Create a function to get the factorial for n
'''

# def factorial(n):
#     if n == 0:
#         return 1
    
#     return n * factorial(n - 1)

# print(factorial(10))

'''
# --------------------------------------------------------------------- #
# Create a string builder function that converts a list of chars to a string
'''

# char_list =['H', 'E', 'L', 'L', 'O']

# def string_builder(array: list):
#     if len(array) == 1:
#         return array[0]
    
#     return array[0] + string_builder(array[1::])

# print(string_builder(char_list))


'''
# --------------------------------------------------------------------- #
# Get substring from user input
'''
# input_string = 'HELLO'

# def get_sub_string(string: str, n: int):
#     if len(string) == n:
#         return string[:2]
    
#     length = len(string) - 1
#     return get_sub_string(string[:length], n)

# print(get_sub_string(input_string, 2))



string = "onetwothree"

print(string[::3])
print(string[:3])
print(string[3::])
print(string[3:])