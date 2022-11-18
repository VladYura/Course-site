from course.brain.main import stage1
from course.brain.input_data import input_addictions

number = ''
Y = ''


def logic(q1, q2):
    if q1 == 0 and q2 == 0:
        return (0, 'x')
    elif q1 == 0 and q2 == 1:
        return (1, 'x')
    elif q1 == 1 and q2 == 0:
        return ('x', 1)
    else:
        return ('x', 0)


def create_input_tree(data, addictions):
    out_lst = [[f'a{x}', (0, 0)] for x in range(1, 16)]
    for way in data.split():
        condition = 'a1'
        for i in way[:len(way) - 1]:
            if i == '0':
                condition = addictions[condition][0]
            else:
                condition = addictions[condition][1]
        index = int(condition[1:])
        if way[-1] == '0':
            out_lst[index - 1][1] = (1, 0)
        else:
            out_lst[index - 1][1] = (0, 1)

    return out_lst


# Qt4x8 = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0],
#     [0, 0, 1, 1],
#     [0, 1, 0, 0],
#     [0, 1, 0, 1],
#     [0, 1, 1, 0],
#     [0, 1, 1, 1],
#     [1, 0, 0, 0]
# ]

Qt4x8 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1]
]

# Qt4x4 = [
#     [0, 0, 0],
#     [0, 0, 1],
#     [0, 1, 0],
#     [0, 1, 1],
#     [1, 0, 0],
#     [1, 0, 1],
#     [1, 1, 0],
#     [1, 1, 1]
# ]

Qt4x4 = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 0],
]


def sort(output):
    res = []
    for i in range(15):
        for item in output:
            if item[0] == f'a{i + 1}':
                res.append(item)
    return res


def write_condition(output):
    Qt = choice_qt(output)
    q_addict = {}
    count = 0
    for i in range(15):
        for item in output:
            if item[0] == f'a{i + 1}':
                q_addict[f'a{i + 1}'] = Qt[count]
                count += 1

    print(f'КЬЮШКИ: ')
    for i in q_addict.items():
        print(i)
    print()

    return q_addict


def create_q(output, key, condition):
    q = []
    for i in range(len(output)):
        q.append(condition[output[i][1][key]])

    for i in q:
        print(i)
    return q


def choice_qt(table):
    if len(table) == 8:
        Qt = Qt4x4
        return Qt
    Qt = Qt4x8
    return Qt


def add_a(table, q):
    for i in range(len(table)):
        q[i].append(table[i][0])
    return q


def create_jump_table(q, q0, q1):
    output = []

    for j in range(len(q[0])):
        result0 = []
        result1 = []
        for i in range(len(q)):
            result0.append(logic(q[i][j], q0[i][j]))
            result1.append(logic(q[i][j], q1[i][j]))
        output.append([f'JK{len(q[0]) - j}', [result0, result1]])
        print(f'Триггер {len(q[0]) - j}')
        print('x=0    x=1')
        print(f'J{len(q[0]) - j}K{len(q[0]) - j}   J{len(q[0]) - j}K{len(q[0]) - j}')
        for k in range(len(result0)):
            print(*result0[k], '  ', *result1[k])

    return output


def create_map_carno(list_out):
    out = []
    if len(list_out[0]) == 8:
        k = 4
    else:
        k = 8
    for i in range(4):
        line = []
        for j in range(k):
            line.append('x')
        out.append(line)

    return out


# def refactor_map_carno_4x8(res_list, letter):
#     map = create_map_carno(res_list)
#     index_i = [0, 1, 3, 2]
#     index_j = [0, 1, 3, 2, 7, 6, 4, 5]
#     count = 0
#     num_lst = 0
#
#     for i in index_i:
#         if count == 16:
#             count = 0
#             num_lst = 1
#         for j in index_j:
#             try:
#                 map[i][j] = res_list[num_lst][count][letter]
#                 count += 1
#             except IndexError:
#                 map[i][j] = 'x'
#                 count += 1
#     return map


def refactor_map_carno_4x8_with_grey(res_list, letter):
    map = create_map_carno(res_list)
    index_i = [0, 1, 3, 2]
    index_j = [0, 7, 1, 4, 6, 2, 1, 0, 5]
    count = 0
    num_lst = 0
    print(res_list)

    for i in index_i[::2]:
        if count == 9:
            count = 0
            num_lst = 1
        for j in index_j:
            if count == 6 or count == 7:
                map[index_i[index_i.index(i) + 1]][j] = res_list[num_lst][count][letter]
                count += 1
            else:
                map[i][j] = res_list[num_lst][count][letter]
                count += 1
    return map


# def refactor_map_carno4x4(res_list, letter):
#     map = create_map_carno(res_list)
#     index = [0, 1, 3, 2]
#     count = 0
#     num_list = 0
#
#     for i in index:
#         if count == 8:
#             count = 0
#             num_list = 1
#         for j in index:
#             map[i][j] = res_list[num_list][count][letter]
#             count += 1
#
#     return map


def refactor_map_carno4x4_with_grey(res_list, letter):
    map = create_map_carno(res_list)
    index_i = [0, 1, 3, 2]
    index_j = [0, 0, 1, 1, 3, 2, 2, 3]
    count = 0
    num_list = 0

    for i in index_i[::2]:
        if count == 8:
            count = 0
            num_list = 1
        for j in index_j:
            if count in [1, 3, 4, 6]:
                map[index_i[index_i.index(i) + 1]][j] = res_list[num_list][count][letter]
                print(
                    f'map[{index_i[index_i.index(i) + 1]}][{j}] = {res_list[num_list][count][letter]} count = {count}')
                count += 1
            else:
                map[i][j] = res_list[num_list][count][letter]
                print(
                    f'map[{i}][{j}] = {res_list[num_list][count][letter]} count = {count}')
                count += 1
    return map


def create_soft_table(tables):
    all_table = []

    for table1 in tables:
        one_dict = {}
        for j in table1:
            one_dict[j[0]] = {x[0]: {x[1][0]: x[1][1]} for x in j[1]}
        all_table.append(one_dict)
    return all_table


def create_soft_l_f_table(tree):
    f_t = {}
    for i in tree:
        f_t[i[0]] = {str(i[1][0]): str(i[1][1])}
    return f_t


def create_output_definition_table(q, q0, q1, table):
    jump_table = create_jump_table(q, q0, q1)

    finish_jump_table = []

    for i in range(len(table)):
        lst = [
            f'{table[i][0]}',
            '   '.join([str(x) for x in q[i]]),
            '   '.join([str(x) for x in q0[i]]),
            '   '.join([str(x) for x in q1[i]]),
        ]
        for item in jump_table:
            lst.append(item[1][0][i][0])
            lst.append(item[1][0][i][1])
            lst.append((item[1][1][i][0]))
            lst.append((item[1][1][i][1]))
        finish_jump_table.append(lst)

    return finish_jump_table


def create_output_maps_carno(q, q0, q1, res_list):
    out = create_jump_table(q, q0, q1)
    JK = []

    if len(res_list) == 8:
        refactor_func = refactor_map_carno4x4_with_grey
        type_of_map = True
    else:
        refactor_func = refactor_map_carno_4x8_with_grey
        type_of_map = False

    for i in range(len(out)):
        J = refactor_func(out[i][1], 0)
        K = refactor_func(out[i][1], 1)
        JK.append([J, K])

    for index, lst in enumerate(JK):
        for i, item in enumerate(lst):
            if i == 0:
                print(f'J{len(JK) - index}')
            else:
                print(f'K{len(JK) - index}')
            for j in item:
                print(*j)
            print()

    return type_of_map, JK

# main_func(Qt, Qt0, Qt1, table)
