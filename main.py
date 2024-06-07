# 

# This part of the code is missing!  What do you think it will do?

# for candy in candy_list:
#     # What will happen here?
#     total_candy += 1

# candy_per_person = total_candy / 2

# print(f'Each person gets {candy_per_person} pieces of candy.')

# spider_rings = ["Black", "Green", "Orange"]

# for spider_ring in spider_rings:
#     print(f'My spider ring is {spider_ring.lower()}.')


# Generate list of spider rings, each with its own randomly selected color
import random

# Ask user how many spider rings they want/need
num_rings = int(input("How many spider rings did you collect? "))

# Create empty list for spider rings
spider_rings = []

# Color options for the rings
colors = ["Black", "Green", "Orange"]

# Loop to generate random colors and add them to the list
for i in range(num_rings):
  # Choose a random color from the list 'colors'
  random_color = random.choice(colors)
  # Add the chosen color to the spider_rings list
  spider_rings.append(random_color)

# Print message for each spider ring with its color
print(f'On Halloween, I collected {num_rings} spider rings.')
for ring in spider_rings:
  print(f"This spider ring is colored {ring.lower()}.")
