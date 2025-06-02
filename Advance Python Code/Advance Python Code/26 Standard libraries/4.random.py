import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print(f"Random integer: {random_integer}")

# Select a random item from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(f"Random choice: {random_choice}")

# Shuffle a list randomly
random.shuffle(choices)
print(f"Shuffled list: {choices}")