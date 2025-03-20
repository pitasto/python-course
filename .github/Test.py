import random

# Generate a list of 20 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(50)]

# Find the maximum value
max_value = max(random_numbers)

# Print the list and the highest value
print("Random Numbers:", random_numbers)
print("Highest Value:", max_value)