# Создаем файл и записываем первую строку
file = open('my_test_file.txt', 'w')
file.write('Доброе утро!\n')
file.close()

# Добавляем новую строку
plans = ['1.Тренировка', '2.Работа', '3.Учеба']
file = open('my_test_file.txt', 'a')
file.write('Планы на день:\n')
for plan in plans:
    file.write(plan + '\n')
file.close()

# Читаем содержимое файла
file = open('my_test_file.txt', 'r')
lines = file.readlines()
file.close()

#Выводим построчно
for line in lines:
    print(line.strip())