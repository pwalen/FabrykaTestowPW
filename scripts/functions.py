def function_new(name, language):
    print('Hello ' + name + ' it is your first ' + language + ' function')


function_new('Pawel', 'Python')

print('\n=============================\n')


def divide(divident, divisor):
    if (divisor == 0):
        return False
    else:
        return divident / divisor


print(divide(3, 0))
print(divide(3, 4))

print('\n=============================\n')


# funkcje, których parametry mogą być opcjonalne

def my_function(arg1, arg2='Alfa Romeo'):
    return f'{arg1}{arg2}'


print(my_function(arg1='car '))
print(my_function(arg1='car ', arg2='fiat'))
print(my_function(('car ', 'fiat ')))

cars = ['Suzuki', 'VW', 'Skoda', 'Volvo']
print(my_function(arg1='car ', arg2=cars))

print('\n=============================\n')

# funkcja częściowa
from functools import partial


def division(x, y):
    return x / y


divide_by_two = partial(division, 2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))
