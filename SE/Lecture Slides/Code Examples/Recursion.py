# Recursion vS iteration 

# File searcher 

# def two_to_power_of(n):
#     if n == 0:
#         return 1
    
#     left = two_to_power_of(n-1) 
#     right = two_to_power_of(n-1)

#     return left + right

# print(two_to_power_of(4))


# Recursion vs Iteration 

# def partial_sum(n):
#     if (n == 1):
#         return 1
    
#     return n + partial_sum(n - 1)

# # print(partial_sum(6))

# def partial_sum_iterative(n):
#     total = 0

#     while n > 0:
#         total += n
#         n -= 1

#     return total

# print(partial_sum(6))

# # Is negative or positive 

# def positive(n):
#     if (n == 0):
#         return True
    
#     if (n == -1):
#         return False
    
#     return positive(n - 2)

# print(positive(9))



def two_to_the_power_of(n):
    if (n == 0):
        return 1

    left = two_to_the_power_of(n - 1) 
    right = two_to_the_power_of(n - 1)

    return left + right

print(two_to_the_power_of(26))