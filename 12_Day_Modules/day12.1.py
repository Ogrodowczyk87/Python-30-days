# from day12 import generate_full_name
# from day12 import generate_random_user_id

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'   

# full_name = generate_full_name(first_name, last_name)
# print(full_name)

# user_id = generate_random_user_id()
# print(user_id)

# import os


# os.mkdir('test_folder')
# print(os.getcwd())

# os.chdir('test_folder')
# print(os.getcwd())

# os.chdir('..')
# os.rmdir('test_folder')

# import sys

# if len(sys.argv) >= 3:
#     print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!")
# else:
#     print("Użycie: python script.py <name> <challenge>")

from statistics import *

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27]
print(mean(ages))
print(median(ages))
print(mode(ages))   
print(stdev(ages))

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base