time = int(input('Введите время в секундах: '))
hours = time // 3600
ostatok_hours = time % 3600
minutos = ostatok_hours // 60
seconds = ostatok_hours % 60
h = str(hours)
m = str(minutos)
s = str(seconds)
hh = len(h)
mm = len(m)
ss = len(s)
if hh < 2:
    h = '0'+h
else:
    h = h
if mm < 2:
    m = '0'+m
else:
    m = m
if ss < 2:
    s = '0'+s
else:
    s = s
print('Время:', h+':'+m+':'+s)
