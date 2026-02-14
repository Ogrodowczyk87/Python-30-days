
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

def upper_case_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string
    return wrapper



@split_string_decorator
@upper_case_decorator

def greeting():
    return "Hello, World!"
print(greeting())


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Przed funkcją")
        result = func(*args, **kwargs)
        print("Po funkcji")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
