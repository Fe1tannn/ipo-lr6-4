search_lines = []
search_str = input("Введите строку которую хотите найти: ")
count = 0 
with open("text.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if search_str in line:
            search_lines.append(line)  
            count += 1 
    else:
            print("Строка не найдена")
print(f"Найдено таких строк: {count}")
print(f"Сортированные строки {sorted(search_lines)}")