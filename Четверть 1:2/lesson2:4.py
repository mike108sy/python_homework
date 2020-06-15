a = [i for i in input('Введите несколько слов, разделенных пробелами: ').split()]
print(a)
for y, z in enumerate(a):
    print(y+1, z[0:10])
