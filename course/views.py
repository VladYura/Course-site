from django.shortcuts import render, redirect
from django.contrib import messages
from course.brain.stage_two import *
from django.contrib.auth.decorators import login_required
from course.brain.main import all_tables, all_dicts


@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def post(request):
    form = request.POST['number']

    if form == '':
        messages.error(request, 'Ты дурак? Введи хоть что-то...')
        return redirect('home')

    for j in form.split():
        for i in j:
            if i != '1' and i != '0':
                messages.error(request, 'Только 0 или 1, заебал!')
                return redirect('home')

    global number
    number = form

    return redirect('result')


@login_required
def result(request):
    global all_tables
    all_tables.clear()

    # Первая часть
    input_tree = create_input_tree(number, input_addictions)

    first_table = create_soft_l_f_table(input_tree)

    finish_table_stage1 = sort(stage1(input_addictions, input_tree))

    last_table = create_soft_l_f_table(finish_table_stage1)

    all_table = create_soft_table(all_tables)

    # Вторая часть
    Qt = choice_qt(finish_table_stage1)
    Qt0 = create_q(finish_table_stage1, 0, write_condition(finish_table_stage1))
    Qt1 = create_q(finish_table_stage1, 1, write_condition(finish_table_stage1))

    length_q = [len(Qt[0]) - x for x in range(len(Qt[0]))]

    finish_jump_table = create_output_definition_table(Qt, Qt0, Qt1, finish_table_stage1)

    maps_carno = create_output_maps_carno(Qt, Qt0, Qt1, finish_table_stage1)

    return render(request, 'result.html', {'last_table': last_table,
                                           'all_table': all_table,
                                           'first_table': first_table,
                                           'length_q': length_q,
                                           'finish_jump_table': finish_jump_table,
                                           'maps_carno': maps_carno[1],
                                           'type_of_map': maps_carno[0]})
