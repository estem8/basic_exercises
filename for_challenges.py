# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names_1 = ['Оля', 'Петя', 'Вася', 'Маша']


def first_0(list_name):
  for name in list_name:
    print(name)
    
print(f'# Задание 1')
first_0(names_1)

def first_1(list_name):
  print(*list_name, sep='\n')

print(f'# Задание 1.1')
first_1(names_1)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names_2 = ['Оля', 'Петя', 'Вася', 'Маша']


def second_0(list_name):
  for name in list_name:
    print(name,'из',len(name),'букаф')

print(f'# Задание 2')
second_0(names_2)


def second_1(list_name):
  [print(f'{name}: {len(name)}') for name in list_name]

print(f'# Задание 2_1')
second_1(names_2)

# def second_2(list_name):
#   print(''.join({name}))

# print(f'# Задание 2_1')
# second_2(names_2)


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
  if is_male[name]:
    print(name,'мужской')
  else:
    print(name,'женский')



# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
group_num = 0
item = 0

for name in groups:
  group_num +=1
  print('Группа', group_num, len(name),'ученика')
print('Всего групп:', group_num)


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

group_num = 0
item = 0
for name in groups:
  group_num +=1
  print('Группа:', group_num, ', '.join(name))
print('Всего групп:', group_num)
