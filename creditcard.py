# 1. Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками

def safe_number(number):
    return (len(number) - 4) * '*' + number[-4:]


creditcard_number = input('введите номер кредитной карты: ')

if len(creditcard_number) < 4:
    print('номер кредитной карты должен содержать не менее 4х цифр')
else:
    print(safe_number(creditcard_number))
