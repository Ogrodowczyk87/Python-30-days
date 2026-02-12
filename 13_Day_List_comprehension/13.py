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


def add_two_nums(a, b):
       return a + b

print (add_two_nums(2, 3))

add_two_nums = lambda a, b: a + b
print (add_two_nums(2, 3))

