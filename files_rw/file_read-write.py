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
                line = f.readline().split('|')
                consist = {}
                consist['ingredient_name'] = line[0].split()[0]
                consist['quantity'] = line[1].split()[0]
                consist['measure'] = line[2].split('\n')[0]
                dish.append(consist)
                #print(dish)
            f.readline()

file_reader('recipes.txt')
pprint(cook_book)