from day12 import generate_full_name
from day12 import generate_random_user_id

first_name = 'Asabeneh'
last_name = 'Yetayeh'   

full_name = generate_full_name(first_name, last_name)
print(full_name)

user_id = generate_random_user_id()
print(user_id)

import os


os.mkdir('test_folder')
print(os.getcwd())

os.chdir('test_folder')
print(os.getcwd())

os.chdir('..')
os.rmdir('test_folder')
