# language = "Python"
# lst = list(language)
# print(lst)

# lst = [i for i in language]
# print(type(lst))
# print(lst)

# lst = [i for i in language if i.isupper()
#        if i.isalpha()
#        if i not in "AEIOU"
#        if i not in "aeiou"
#        if i not in " "]
# print(type(lst))
# print(lst)

# numbers = [i for i in range(1, 11)]
# print(type(numbers))
# print(numbers)


# lenguage = "Ogrodowczyk + Python Developer"
# lst  = list(lenguage)
# print(lst)

# lst = [i for i in lenguage if i.isupper()
#        if i.isalpha() if i not in "AEIOU" if i not in "aeiou" if i not in " "] 
# print(type(lst)) 
# print(lst)


# def add_two_nums(a, b):
#        return a + b

# print (add_two_nums(2, 3))

# add_two_nums = lambda a, b: a + b
# print (add_two_nums(2, 3))

# def power(x):
#        return lambda n: x ** n

# cube = power(3)(4)
# print(cube)

# two_power_of_five = power(5)(2)
# print(two_power_of_five)

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# list = [i for i in numbers 
#                     if i < 0]
# print(list)

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # all_numbers = [i for sublist in list_of_lists for i in sublist]
# # print(all_numbers)

# def flat_list(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flat_list(item))
#         else:
#             result.append(item)
#     return result
    
# print(flat_list(list_of_lists))

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]

print(result)
