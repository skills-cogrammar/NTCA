import json
from time import time

class SalesRep:
    def __init__(self, first_name: str, last_name: str, country: str, sales: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.sales = sales

# Read from json file and return a dict
def get_data(filename = "sales_reps.json"):
    with open(filename) as f:
        data = json.load(f)
        
    return [SalesRep(**key) for key in data]

sales_people = get_data()

'''
# --------------------------------------------------------------------- #
# Search for 'Lory Carlile'
#   - Use Linear Search O(n)
#   - Use Binary Search O(log n)
'''

# # Linear Search 
# def find_lory():
#     for person in sales_people:
#         if person.first_name == 'Lory' and person.last_name == 'Carlile':
#             return person
        
# print(find_lory().sales)


# # Binary Search !!! Won't work because the data is not sorted
# def find_lory_binary():
#     low = 0
#     high = len(sales_people) - 1
#     target = 'Lory'

#     while low <= high:
#         mid = (low + high) // 2

#         if sales_people[mid].first_name == target:
#             return sales_people[mid]
#         elif sales_people[mid].first_name < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return None

# print(find_lory_binary().sales)


'''
# --------------------------------------------------------------------- #
# Look for the highest sales number recursively
#   - Create a graph 
#   - Write the recursive function
'''


# def get_most_sales(array: list[SalesRep]):
#     if (len(array) <= 1):
#         return array[0].sales
    
#     m = len(array)// 2
#     left_array = array[:m]
#     right_array = array[m:]

#     left = get_most_sales(left_array)
#     right = get_most_sales(right_array)

#     if left > right:
#         return left
#     else:
#         return right
    
# print('Highest Sales: ', get_most_sales(sales_people))


'''
# --------------------------------------------------------------------- #
# Sort the values by the sales number using the merge sort
'''

# def merge_sort(array: list[SalesRep]):
#     if len(array) <= 1:
#         return array
    
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     return merge(left, right)

# def merge(left: list[SalesRep], right: list[SalesRep]):
#     sorted_list = []

#     i, j = 0, 0

#     while i < len(left) and j < len(right):
#         if left[i].sales < right[j].sales:
#             sorted_list.append(left[i])
#             i += 1
#         else: 
#             sorted_list.append(right[j])
#             j += 1

#     sorted_list += left[i:]
#     sorted_list += right[j:]

#     return sorted_list



# sales_people = merge_sort(sales_people)

# for person in output:
#     print(person.sales)

'''
# --------------------------------------------------------------------- #
# Create a linear sort
'''

# def insertion_sort(array: list[SalesRep]):
#     for i in range(1, len(array)):
#         pointer = array[i]
#         j = i - 1

#         while j >= 0 and pointer.sales < array[j].sales:
#             array[j + 1] = array[j]
#             j -= 1

#         array[j + 1] = pointer

#     return array




'''
# --------------------------------------------------------------------- #
# Search for a sales number of '292' in the sorted list
'''

# # Binary Search 
# def binary_search(array: list[SalesRep], low, high, x):
#     if (high >= low):
#         mid = (low + high) // 2

#         if (array[mid].sales == x):
#             return mid
        
#         elif array[mid].sales < x:
#             return binary_search(array, mid + 1, high, x)
        
#         else:
#             return binary_search(array, low, mid - 1, x)
        
#     return None

# def linear_search(x):
#     for i, person in enumerate(sales_people):
#         if person.sales == x:
#             return i
        


'''
# --------------------------------------------------------------------- #
# Compare merge sort to insertion sort
'''


# start = time()

# for i in range(1000):
#     temp = sales_people.copy()

#     merge_sort(temp)

# stop = time()

# print('Merge Sort:', stop - start)


# start = time()

# for i in range(1000):
#     temp = sales_people.copy()

#     insertion_sort(temp)

# stop = time()

# print('Insertion Sort:', stop - start)


'''
# --------------------------------------------------------------------- #
# Compare binary search to linear search 
'''



# start = time()

# for i in range(10000):
#     binary_search(sales_people, 0, len(sales_people) - 1, 292)

# stop = time()

# print('Binary Search:', stop - start)


# start = time()

# for i in range(10000):
#     linear_search(292)

# stop = time()

# print('Linear Search:', stop - start)
    
