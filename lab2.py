# 2. Генератор Функций - Создать функцию высшего порядка,
#    которая возвращает другую функцию для возведения числа в указанную степень.
def wrapper(power):
    return lambda x: x ** power


numbers = [1, 2, 3, 4, 5]
print(list(map(wrapper(3), numbers)))
