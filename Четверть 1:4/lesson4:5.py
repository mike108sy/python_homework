from functools import reduce

def my_func(el1, el2):
    return el1 * el2


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, my_list))
