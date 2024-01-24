import random

age = int(input('для участия в лотерее введите ваш возраст: '))
min_age = 18
lucky_number = int(random.randint(1, 100))


def lottery(number):
    match number:
        case i if 30 < i < 39:
            return 'неделю отпуска'
        case i if 5 < i < 50:
            return 'билет в кино'
        case i if 50 < i < 60:
            return 'тур в Париж'
        case 99:
            return '10000$$$'
        case _:
            return 'ничего'


if age < min_age:
    print(f'лицам не достигшим {min_age} лет, участвовать в лотерее запрещено')
else:
    print(f'сейчас проверим вашу удачу, Вам выпадает число >>> {lucky_number}!!!')
    print(f'Вы выиграли: {lottery(lucky_number)}')
