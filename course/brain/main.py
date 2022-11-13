from course.brain.functions import *

all_tables = []
all_dicts = []


# Главная функция скрипта
# Запускает все остальные функции в нужном порядке нужное количество раз
def stage1(names, start):
    global all_tables
    global all_dicts

    letters = ['C', 'D', 'E', 'F']

    out = start_progress(start)
    for i in out:
        print(i)

    print()
    dict_out = conclusion_dict('B', out)
    print(dict_out)

    out = group_substitution(out, names, dict_out)

    all_tables.append(copy.deepcopy(out))  # Добавление в массив для HTML

    print()
    for i in out:
        print(i)

    for letter in letters:
        print()
        out = mid_game(out, letter)
        for i in out:
            print(i)

        print()
        dict_out = conclusion_dict(letter, out)
        print(dict_out)

        out = group_substitution(out, names, dict_out)

        all_tables.append(copy.deepcopy(out))  # Добавление в массив для HTML

        print()
        for i in out:
            print(i)

    final_ans = super_last_func(out, dict_out)
    print()
    for i in final_ans:
        print(i)

    return final_ans
