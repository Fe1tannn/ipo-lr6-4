"""
Написать программу, которая:
- Запрашивает у пользователя строку для поиска.
- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.  
    [text.txt] 
- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.

"""
search_lines = [] #Список для хранения искомой подстроки 
search_str = input("Введите строку которую хотите найти: ") #Вводим искомую строку
count = 0 
with open("text.txt", 'r', encoding='utf-8') as file: #Открываем файл
    for line in file: #Перебор 
        if search_str in line: #Условие
            search_lines.append(line)  #Добавляем в список подстроку если она подхлдит под условие 
            count += 1 
    else:
            print("Строка не найдена")
print(f"Найдено таких строк: {count}")
print(f"Сортированные строки {sorted(search_lines)}")
