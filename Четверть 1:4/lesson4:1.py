import sys


sys.argv.insert(1, int(input('Введите выработку в часах сотрудника, руб.: ')))
sys.argv.insert(2, int(input('Введите ставку в часах сотрудника, руб.: ')))
sys.argv.insert(3, int(input('Введите размер премии сотрудника, руб.: ')))
args = sys.argv[1] * sys.argv[2] + sys.argv[3]
print('Заработная плата сотрудника составит:', args, 'рублей')
