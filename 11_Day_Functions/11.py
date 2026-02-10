
# def generate_full_name():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     full_name = first_name + " " + last_name
#     print("Your full name is:", full_name)
#     return full_name
# generate_full_name()

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))


# def generate_full_name (first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print('Full name:', generate_full_name('Asabeneh', 'Yetayeh'))

# def sum_two_numbers(num_one, num_two):
#     space = '      '
#     sum = num_one + num_two
#     return sum
# print('The sum of 10 and 20 is:', sum_two_numbers(10, 20))


# def print_fullname(first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# print_fullname(first_name='Asabeneh', last_name='Yetayeh')

# def print_name(firstname):
#     return firstname
# print_name('Asabeneh')

# def print_full_name(firstname, lastname):
#     space = ' '
#     full_name = firstname + space + lastname
#     return full_name
# print_full_name(firstname='Asabeneh', lastname='Yetayeh')

# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(2, 3))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age
# print('Age: ', calculate_age(2019, 1819))


# def find_even_numbers(n):
#     even = []
#     for i in range(0 + 1, n + 1):
#         if i % 2 == 0:
#             even.append(i)
#     return even

# def greetings (name = 'Peter'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('Asabeneh'))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age
# print('Age: ', calculate_age(2019, 1919))

# syntax
# Declaring a function


# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num     # same as total = total + num 
#     return total
# print(sum_all_nums(2, 3, 5)) # 10

# def sum_names(*names):
#     total = []
#     for name in names:
#         total.append(name)
#     return total
# print(sum_names('Asabeneh', 'Yetayeh', 'Python')) # ['Asabeneh', 'Yetayeh', 'Python']

# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i) 
# generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# def arbitrary_named_args(**args):
#     print("I received an arbitrary number of arguments, totaling", len(args))
#     print("They are provided as a dictionary in my function:", type(args))
#     print("Let's print them:")
#     for k, v in args.items():
#         print(" * key:", k, "value:", v)
# arbitrary_named_args(name="Asabeneh", country="Finland", city="Helsinki", age=250)


def f(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict

f(10, 20, name="Rafal", age=30)

# args -> (10, 20)
# kwargs -> {'name': 'Rafal', 'age': 30}
