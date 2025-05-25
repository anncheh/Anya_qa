#создание файла
# open() - функция для открытия файла и чтения или записи
# open(filename, mode) - имя файла и режим открытия
# filename - имя ключа, который нужно открыть
#mode - режим (ключ) открытия файла (r для чтения, w для записи, a для добавления)

file = open('twxt.txt', 'w') #создание файла в проекте, с которым можно работать

#Запись данных в файл
# write() - функция для записи даных в файл
# принимает два обязательных параметра: файл (file) и данные (data), которые нужно записать

file = open('test.txt', 'w')
file.write('Hello, Worls!')
file.close()
#результат: в файле test.txt находится фраза 'Hello, Worls!' Открываем файл для записи и записываем в него строку

#замена слова в файле
file = open('test.txt', 'w')
file.write('Hello')
file.close()
#результат: в файле tset.txt находится фраза 'Hello'

#Чтение файла
file = open('test.txt', 'r')
content = file.read()
print(content)
#результат: Hello, World!
#Мы открываем файл txt.txt для чтения и читаем его содержимое

#Добавление данных в файл
file = open('test.txt', 'a')
file.write('\nHi, World!')
file.close()
#Результат: в файле test.txt Hello, World!
# Hi, World!
# Открываем файл для добавления и добавляем туда строку

#Закрытие файла
file = open('test.txt', 'r') #открываем файл
content = file.read() #читаем содержимое файла
print(content)  #печатаем содержимое файла
file.close() #закрываем файл

#Чтение файла построчно
file = open('test.txt', 'r')
first_line = file.readline()
print(first_line)

file.close()

#чтение строк и возврат в виде списка
file = open('example.txt', 'r')
lines = file.readlines() #читаем все стоки в список
file.close()
print(lines)
#Результат: ['Первая строчка\n', 'Вторая строчка\n', 'Третья строчка\n', 'Четвертая строчка\n']


file = open('example.txt', 'r') #открываем файл для чтения
lines = file.readlines() #читаем все строки в список
file.close() #закрываем файл
for i in rangw(len(lines)): #используем классическую форму цикла for
    #для вывода строк
    print(lines[i].strip()) #используем strip() для удаления символов
#новой строки