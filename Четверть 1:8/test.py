import random


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = sorted(arr[:size])
        while len(pice) != 9:
            pice.insert(size - random.randrange(0, 5), '  ')
        arrs.append(pice)
        arr = arr[size:]
    while len(arr) != 9:
        arr.insert(size - random.randrange(0, 5), '  ')
    arrs.append(arr)
    print('_'*27)
    for j in arrs:
        print(' '.join(map(str, (j))))
    print('_' * 27)


x = [12, 32, 13, 4, 75, 6, 71, 18, 29, 10, 11, 82, 43, 34, 90]
print(split(x, 5))
