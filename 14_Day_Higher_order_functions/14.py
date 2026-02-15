
# def sum_numbers(nums):
#     return sum(nums)

# def higheer_order_function(f, list):
#     summation = f(list)
#     return summation
# result = higheer_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)

# def def_sum(nums):
#     return sum(nums)


# def higher_order(f, lst):
#     return f(lst)
# result = higher_order(def_sum, [1, 2, 3, 4, 5])
# print(result)


# def greeting():
#     return "Hello, World!"
# def uppeercase_decorator(function):
#     def wrappper():
#         func = function()
#         make_upercase = func.upper()
#         return make_upercase
#     return wrappper
# g = uppeercase_decorator(greeting)
# print(g())
# print(greeting())

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return "Hello, World!"
# print(greeting())

# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")
    
# say_hello()

# def upper_case_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# def split_string_decorator(function):
#     def wrapper():
#         func = function()
#         split_string = func.split()
#         return split_string
#     return wrapper



# @split_string_decorator
# @upper_case_decorator

# def greeting():
#     return "Hello, World!"
# print(greeting())


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Przed funkcją")
#         result = func(*args, **kwargs)
#         print("Po funkcji")
#         return result
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# @my_decorator
# def say_hello_to(name):
#     print(f"Hello, {name}!")

# say_hello_to("Rafal")


# @my_decorator
# def user_info(**kwargs):
#     print(f"Przekazane kwargs: {kwargs}")
#     if "name" in kwargs:
#         print(f"Czesc, {kwargs['name']}!")

# user_info(name="Rafal", age=30, city="Krakow")

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        result = function(para1, para2, para3)
        print("I live in {}".format(para3))
        return result
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}, I love to teach.".format(first_name,
        last_name))


print_full_name("Rafa", "Kowalski", "Poland")
