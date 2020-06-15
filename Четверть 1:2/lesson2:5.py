my_list = [7, 5, 3, 3, 2]
print(my_list)
n = int(input('Введите натуральное число: '))
n = abs(n)
position = 0
counts_index = len(my_list)
while position != counts_index:
    if n == 1:
        my_list.append(n)
        break
    if n > my_list[position]:
        my_list.insert(position, n)
        break
    elif n == my_list[position]:
        my_list.insert(position+1, n)
        break
    else:
        position += 1
print(my_list)
