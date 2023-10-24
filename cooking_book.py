import os

# current_directory = os.getcwd()
# print(current_directory)

with open('recipes.txt', 'w', encoding='utf-8') as f:
    f.write('''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт''')


def cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        while True:
            key = f.readline().strip()
            if not key:
                break
            values_number = int(f.readline().strip())
            ingredients = []
            for i in range(values_number):
                ingredient_line = f.readline().strip()
                ingredient_parts = ingredient_line.split(' | ')
                ingredient_name = ingredient_parts[0]
                quantity = int(ingredient_parts[1])
                measure = ingredient_parts[2]
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()  

            cook_book[key] = ingredients

    return cook_book

result = cook_book()
for dish, ingredients in result.items():
    print(dish)
    for ingredient in ingredients:
        print(ingredient)
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}  

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")

    return shop_list


dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2
cook_book = cook_book()  

shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)

print(shop_list)


folder_path = 'C:/Users/Асель/Desktop/netology/cooking book'


file_list = os.listdir(folder_path)


file_info_list = []


for file_name in file_list:
    if file_name in ['one.txt', 'two.txt', 'three.txt']:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file_info_list.append((file_name, len(lines), lines))


file_info_list.sort(key=lambda x: x[1])


output_file_path = 'C:/Users/Асель/Desktop/netology/cooking book/cook.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for file_name, line_count, lines in file_info_list:
        output_file.write(file_name + '\n')
        output_file.write(str(line_count) + '\n')
        output_file.writelines(lines)

print("Итоговый файл создан:", output_file_path)



 