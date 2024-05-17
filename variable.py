# Сложная задача

money = int(input('Введите кол-во денег '))
kg = 4.5
price = 34
change = money - kg * price
print('Сдача', change)

# Сдача всем

money = int(input('Введите кол-во денег '))
kg = int(input('Вес товара '))
price = int(input('Цена товара '))
change = money - kg * price
print('Сдача', change)

# Работаем с выводом данных

product_name = input('Название товара ')
price = int(input('Цена товара '))
product_weight = int(input('Вес товара '))
money = int(input('Количество денег у пользователя '))
total = product_weight * price
change = money - product_weight * price
print('Чек,''<', product_name, '>' ' -', '<', 'вес', '>', '-', product_weight, 'кг', '-', '<', 'цена', '>', price, 'руб/кг', 'Итого:', total, 'Руб', 'Внесено:', money, 'руб', 'Сдача:', change, 'руб')

# Самая простая задача на свете

number = int(input('Введите число '))
print('Купи конструктор! ' * number)

# Автоматизируем простоту!

number = int(input('Введите число '))
favorite_thing = input('Введите любимое дело ')
print(number * (' Обажаю писать ' + favorite_thing ))