def division(name, surname, year_burth, city, email, tell):
        print(f"name - {name}, surname - {surname}, year_burth - {year_burth}, city - {city}, email - {email}, tell - {tell}")


division(name=input('Введите имя: '), surname=input('Введите фамилию: '), year_burth=int(input('Введите год рождения: ')), city=input('Введите город проживания: '), email=input('Введите email: '), tell=input('Введите телефон: '))
