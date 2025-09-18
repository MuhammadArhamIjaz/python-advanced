# Take input for list of numbers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# 1. List comprehension - squares
squares = [x**2 for x in nums]
print("Squares:", squares)

# 2. Set comprehension - unique even numbers
unique_evens = {x for x in nums if x % 2 == 0}
print("Unique evens:", unique_evens)

# 3. Dictionary comprehension - number: square
num_square_dict = {x: x**2 for x in nums}
print("Number-Square dict:", num_square_dict)

# 4. Symmetric difference - take two lists from user
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

sym_diff = {x for x in arr1 + arr2 if (x in arr1) ^ (x in arr2)}
print("Symmetric Difference:", sym_diff)
