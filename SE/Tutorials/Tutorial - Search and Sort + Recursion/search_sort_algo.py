'''
# --------------------------------------------------------------------- #
# Binary Search
# - Sorted List 
# - Finds the middle point 
# - Checks if the middle point is the target value 
# - Checks if the target value is less than the middle point 
# - checks the left half if the middle point is less than the middle, lest checks the right half
# - Repeats until value is found or not found.
'''

# Iterative
def binary_search(array: list, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return array[mid]
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


'''
# --------------------------------------------------------------------- #
# Linear Search
# - Look through each element
# - If item is in list return item
'''

def linear_search(array: list, target);
    for i, element in enumerate(array):
        if element == target:
            return i
        
        return -1
    
'''
# --------------------------------------------------------------------- #
# Insertion Sort
# - Start at the first item 
# - Compare value to all values in list 
# - swap values where current value is greater than value being chekced.
'''

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key


    
'''
# --------------------------------------------------------------------- #
# Quick Sort
# - set a pivot point (typically the last element)
# - Compare each value to the pivot 
# - If value is lower than pivot, increase the value 'j' index 
# - after looking at each point, move pivot to j + 1
# - perform recursion for left and right of pivot 
'''

def partition(data, start, end):
  pivot = data[end]
  i = start - 1

  for j in range(start, end):
    if data[j] <= pivot:
      i += 1
      data[i], data[j] = data[j], data[i]

  data[i + 1], data[end] = data[end], data[i + 1]
  return i + 1

def quick_sort(data, start, end):
  if start < end:
    pivot_index = partition(data, start, end)
    quick_sort(data, start, pivot_index - 1)
    quick_sort(data, pivot_index + 1, end)



'''
# --------------------------------------------------------------------- #
# Merge Sort
# - Find the middle point 
# - Split values into left and right array 
# - repeat until we have 1 value 
# - Compare left and right values recusively 
# - Use pointer to compare values in left and right list
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result