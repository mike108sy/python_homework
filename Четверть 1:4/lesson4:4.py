my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


my_list_new = [my_list[i] for i in range(0, len(my_list)) if my_list.count(my_list[i]) == 1]
print(my_list_new)
