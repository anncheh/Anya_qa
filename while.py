# Ввод исходных данных
initial_fuel = int(input())
min_fuel = int(input())

# Инициализация переменных
current_fuel = initial_fuel
day = 0

# Пока текущий объем топлива больше минимального, продолжаем считать дни
while current_fuel > min_fuel:
    current_fuel -= initial_fuel * 0.1
    day += 1

# Вывод результата
print(day)
