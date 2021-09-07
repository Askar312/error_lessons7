print ('Бай банк!')
sum = eval(input('Введите сумму:'))
while sum < 50000:
    print('Сумма должна быть больше или равно $50,000')
    a = eval(input ('Введите сумму:$'))
if sum > 50000:
    total = sum * (3.37 / 100)
    print ('Процентная сумма  (3.37%): $', round(total, 2))