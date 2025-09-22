# take input numbers separated by spaces
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# list comprehension to find squares
squares = [x**2 for x in nums]

print("Squares:", squares)
