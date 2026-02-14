
def sum_numbers(nums):
    return sum(nums)

def higheer_order_function(f, list):
    summation = f(list)
    return summation
result = higheer_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)