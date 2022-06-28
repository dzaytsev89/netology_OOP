# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны,
# пример для выполнения домашней работы можно взять тут
# Необходимо объединить их в один по следующим правилам:
#
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

import os

base_path = os.getcwd()
dir_name = '\\2.4_files\\sorted'
path = base_path + dir_name


def file_counter(path):  # для подсчёта служебной информации
    file_sizes = {}
    files = os.listdir(path)
    for file in files:
        with open(os.path.join(base_path + dir_name, file), encoding='utf-8') as f:
            file_sizes[file] = len(f.readlines())
    # print(file_sizes)
    sorted_file_sizes = sorted(file_sizes.items(), key=lambda v: v[1])
    return dict(sorted_file_sizes)


files = file_counter(path)


# print(files)

def sum_files(files, new_file):
    with open(new_file, 'w', encoding='utf-8') as w:
        for file, line_len in files.items():
            w.writelines(file + '\n')
            w.writelines(str(line_len) + '\n')
            with open(os.path.join(path, file), encoding='utf-8') as f:
                data = f.readlines()
                for line in data:
                    w.writelines(line)
                w.write('\n')
        return


sum_files(files, 'sum.txt')
