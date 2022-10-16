# Пользовательский интерфейс

def initial():
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    operation = input('Введите операцию ("+", "-", "/", "*"): ')
    if operation == '+':
        return a, b, operation
    elif operation == '-':
        return a, b, operation
    elif operation == '/':
        return a, b, operation
    elif operation == '*':
        return a, b, operation                
    else:
        print('Неверное значение операции!')
        return initial()
