from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

# name_list = [i['first_name'] for i in students]
# counter=Counter(name_list)
# print(counter)
# for k,v in counter.items():
#   print(k,v)
# -> conver в одну строчку
for k,v in Counter([i['first_name'] for i in students]).items():
    print(k,v)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
print(f'Имя: {Counter([name['first_name'] for name in students]).most_common()[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i in enumerate(school_students,1):
    print(f'Группа: {i[0]}: {Counter([name['first_name'] for name in i[1]]).most_common()[0][0]}')

# print('\n'.join([f'Группа: {idx}: {Counter([name['first_name'] for name in students]).most_common()[0][0]}' for idx, students in enumerate(school_students, 1)]))

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???

for i in school:
    m_counter = 0
    w_counter = 0
    for s in i['students']:
        if is_male[s['first_name']]:
            m_counter +=1
        else:
            w_counter +=1
    print(f'Класс: {i['class']} мальчики:{m_counter}, девочки: {w_counter}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
for cl in school:
    m_counter = 0
    w_counter = 0
    for s in cl['students']:
        if s['first_name'] in is_male:
            m_counter +=1
        else:
            w_counter +=1
    if m_counter > w_counter:
        print(f'В классе:{cl['class']} больше всего мальчиков, аж {m_counter}')
    else:
        print(f'В классе:{cl['class']} больше всего девочек, аж {w_counter}')