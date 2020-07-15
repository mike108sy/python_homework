# Регулярные выражения

import re


text = 'привет! отправь, пожалуйста, письмо нашим коллегам из компаний партнеров на следующие электронные адреса: vladamir@v.ru, vladimir_e@df.ru vladlen@sdf.ru. И не забудь про Оксану и Ольгу: adidas@das.ru reebok@reb.ru'
li = text.split()
print(li)

li = [word for word in li if '@' in word]
print(li)

li = re.findall('vlad.mir', text)
print(li)

li = re.findall('\w+', text)
print(li)

li = re.findall('\w+@\w+\.\w+', text)
print(li)

text2 = 'Краснодарский край занял четвертое место среди регионов РФ по снижению зарплатного фонда по итогам марта-мая 2020 года. Показатель сократился на 13,6%, выяснили в аналитической службе международной аудиторско-консалтинговой сети FinExpertiza.\
Лидирует в антирейтинге Удмуртия — относительно прошлогодней весны зарплатный фонд снизился на 17,5%, далее следуют Пермский край (-13,9%), Тюменская область (-13,9%). В топ-5 регионов также вошел Татарстан (-13,6%). Всего в РФ весной фонд заработной платы сократился в 68 российских регионах.\
В целом по стране показатель упал на 4,7%, до 6,8 трлн рублей. Авторы исследования отмечают, что это первое сокращение весной как минимум с 2001 года.\
Подробнее на РБК:\
https://kuban.rbc.ru/krasnodar/14/07/2020/5f0d953f9a794708908fa414?from=from_main_2'

li2 = re.findall('.', text2)
print(li2)

li2 = re.findall('20..', text2)
print(li2)

li2 = re.findall('20\d\d', text2)
print(li2)

li2 = re.findall('\d\d\D', text2)
print(li2)

li2 = re.findall('20\d\d\s....', text2)
print(li2)

li2 = re.findall('\d+', text2)
print(li2)

li2 = re.findall('20?\d\d\s....', text2)
print(li2)

li2 = re.findall('20?\d*\d\s', text2)
print(li2)

li2 = re.findall('[0-9,]+', text2)
print(li2)

li2 = re.findall('[а-я]+', text2)
print(li2)

li2 = re.findall('[a-z]+', text2)
print(li2)

li2 = re.findall('20?\d*\d\s', text2)
print(li2)

li2 = re.findall('21?\d*\d|20?\d*\d', text2)
print(li2)

li2 = re.findall('\w{3}', text2)
print(li2)

li2 = re.findall('\w{3,5}', text2)
print(li2)

text3 = 'Сборная Франции одержала победу на стадионе лужники. на 28-й минуте забили гол. Опять французы победили и франция в очередной раз вышла вперед'

text3 = re.sub('Франции', 'России', text3)
print(text3)

text3 = re.sub('Франц', 'Росс', text3)
print(text3)

text3 = re.sub('[Фф]ранцузы', 'россияне', text3)
print(text3)

text3 = re.sub('[Фф]ранц', 'Росс', text3)
print(text3)

#text3 = re.sub('\d+', 'n', text3)
#print(text3)

text3 = re.sub('\d{1,2}\-[йя]', 'n', text3)
print(text3)

li4 = re.findall('[о]', text2).count('о')

print(li4)


