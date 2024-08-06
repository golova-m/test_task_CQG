import sys


def replacement_in_lines(lines, symbols):
    '''
    Функция замены символов (symbols) в строках (lines. И подсчет количества изменений.
    '''
    new_lines = {}
    for original_line in lines: #Обработка каждой строки по очереди
        sum_symbols = 0
        for key, value in symbols.items(): #Заполнение словаря новыми строками и количеством изменений
            sum_symbols += original_line.count(key) 
            original_line = original_line.replace(key, value)
        new_lines[original_line.replace('\n', '')] = sum_symbols
    return new_lines


def generating_replacement_symbols(lines_symbols):
    '''
    Функция генерации словаря заменяемых символов
    '''
    replacement_symbols = {}
    for line in lines_symbols:
        symbols_split = line.split('=')
        replacement_symbols[symbols_split[0]] = symbols_split[1].replace('\n', '')
    return replacement_symbols   


def reading_files(name_files):
    '''
    Функция чтения файлов. Первый аргумент - название файла с символами. Второй аргумент - название файла со строками
    '''
    with open(name_files[0], 'r') as f:
        lines_symbols = f.readlines()
    replacement_symbols = generating_replacement_symbols(lines_symbols)
    with open(name_files[1], 'r') as f:
        lines_str = f.readlines()
    return replacement_symbols, lines_str
    

def print_sorted_new_lines(sorted_new_lines):
    '''
    Функция вывода отсортированных новых строк
    '''
    for line in sorted_new_lines:
        print(line[0])


def main(input_args):
    replacement_symbols, input_str = reading_files(input_args[1:3]) #Чтение файлов
    new_lines = replacement_in_lines(input_str, replacement_symbols) #Замена символов в строках
    sorted_new_lines = sorted(new_lines.items(), key=lambda item: item[1], reverse=True) #Сортировка словаря с новыми строками на основе количества изменений
    print_sorted_new_lines(sorted_new_lines)

if __name__ == "__main__":
    main(sys.argv)