import random


def get_view_card(card_old):
    view_card = []
    while len(card_old) > 5:
        pice = sorted(card_old[:5])
        while len(pice) != 9:
            pice.insert(5 - random.randrange(0, 5), '  ')
        view_card.append(pice)
        card_old = card_old[5:]
    card_old = sorted(card_old)
    while len(card_old) != 9:
        card_old.insert(5 - random.randrange(0, 5), '  ')
    view_card.append(card_old)
    print('_' * 27)
    for j in view_card:
        print(' '.join(map(str, (j))))
    print('_' * 27)
    return '\n'


class Gamer:

    def __init__(self, name):
        self.name = name
        self.card = []
        self.card_computer = []

    def get_card(self):
        numbers_card = [i for i in range(1, 91)]
        while len(self.card) != 15:
            number = random.choice(numbers_card)
            if number not in self.card:
                self.card.append(number)
        return self.card

    def get_card_computer(self):
        numbers_card_computer = [z for z in range(1, 91)]
        while len(self.card_computer) != 15:
            number_computer = random.choice(numbers_card_computer)
            if number_computer not in self.card_computer:
                self.card_computer.append(number_computer)
        return self.card_computer

    def game_start(self):
        numbers_box = [i for i in range(1, 91)]
        for k in range(1, 91):
            if len(self.card) == 0:
                print('\n')
                print('Вы победили! Поездка на море в 2035 году ваша!')
                print('\n')
                print('Конец игры')
                break
            if len(self.card_computer) == 0:
                print('\n')
                print('Вы проиграли! Поездка на море в 2035 году достается компьютеру!')
                print('\n')
                print('Конец игры')
                break
            number_box = random.choice(numbers_box)
            print('\n')
            print('Новый бочонок:', number_box, '(осталось {})'.format(90 - k))
            #print('Ваша карточка:', '\n', '_'*25, '\n', ' '.join(map(str, self.card)), '\n', '_'*25)
            my_list = self.card
            print('Ваша карточка:')
            print(get_view_card(self.card))
            #print('Ваша карточка:', self.card)
            print('Карточка компьютера:')
            print(get_view_card(self.card_computer))
            my_choose = ''
            my_choose = input('Зачеркнуть цифру {} в вашей карточке? (y/n): '.format(number_box))
            while True:
                if my_choose == 'n' or my_choose == 'y':
                    break
                else:
                    print('{}, я не понимаю Вас! Возможно Вы ввели некорректный ответ. Введите "y" или "n"'.format(self.name))
                    my_choose = input('Зачеркнуть цифру {} в вашей карточке? (y/n): '.format(number_box))
            if my_choose == 'y':
                try:
                    self.card.remove(number_box)
                    print('Отлично!!! Вы медленно, но уверено движитесь к победе.')
                except ValueError:
                    print('Не често!!! Не честно!!!. Такой цифры нет у вас в карточке. Вы проиграли!!!')
                    print('Конец игры')
                    break
            try:
                self.card_computer.remove(number_box)
                print('Компьютер: "Мне категорически жаль, но кажется у меня есть такая цифра в карточке! Зачеркнул"')
            except ValueError:
                print('Компьютер: "У меня нет такой цифры в карточке! Жду удачу на следующем ходе!"')
            numbers_box.remove(number_box)


name_human1 = input('Введите Ваше имя: ')
human1 = Gamer(name_human1)
human1.get_card()
human1.get_card_computer()
print(human1.game_start())
