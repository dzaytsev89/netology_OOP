import os
from pprint import pprint
cook_book = {}

def file_reader(file_name):
    base_path = os.getcwd()
    with open(file_name, encoding='utf-8') as f:
        for dishes in f:
            dish = []
            cook_book[dishes.split('\n')[0]] = [dish]
            quantity = f.readline()
            for i in range(int(quantity)):
                line = f.readline().split(' | ')
                consist = {}
                consist['ingredient_name'] = line[0]
                consist['quantity'] = line[1].split()[0]
                consist['measure'] = line[2].split('\n')[0]
                dish.append(consist)
                #print(dish)
            f.readline()

file_reader('recipes.txt')
# pprint(cook_book)
ingr_counter = {}

def ingr_maker(ingr, person_count):
    if ingr.get('ingredient_name') not in list(ingr_counter.keys()):
        ingr_counter.setdefault(ingr.get('ingredient_name'), {})
        for k, v in ingr_counter.items():
            if k == ingr.get('ingredient_name'):
                v['measure'] = ingr.get('measure')
                v['quantity'] = int(ingr.get('quantity')) * int(person_count)
    elif ingr.get('ingredient_name') in list(ingr_counter.keys()):
        for k, v in ingr_counter.items():
            if k == ingr.get('ingredient_name'):
                v['quantity'] = int(v.get('quantity')) + int(ingr.get('quantity')) * int(person_count)

def get_shop_list_by_dishes(dishes, person_count):
    for pos in dishes:
        if pos in list(cook_book.keys()):
            for dish, ingr_all in cook_book.items():
                if pos == dish:
                    for ingr_id in range(len(ingr_all[0])):
                        ingr = ingr_all[0][ingr_id]
                        # print(ingr)
                        ingr_maker(ingr, person_count)
        elif pos not in list(cook_book.keys()):
            print(f'Нет такого блюда - {pos}')
    pprint(ingr_counter)
    return

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться