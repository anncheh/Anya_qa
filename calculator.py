try:
    num1 = float(input('Введите первое число: '))
    operation = input("Введите операцию (+, -, *, /): ")
    num2 = float(input('Введите второе число: '))

    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('Деление на ноль недоступно')
        else:
            print(num1/num2)
    else:
        print('Неверный знак')
except ValueError:
    print('Ошибка ввода')
