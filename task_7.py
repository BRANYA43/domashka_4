from random import randint

some_list_1 = [randint(0, 100) for i in range(randint(10, 50))]
some_list_2 = [randint(0, 100) for j in range(randint(10, 50))]

some_set_1 = set(some_list_1)
some_set_2 = set(some_list_2)

print(f'''Список перший: {some_list_1}''')
print(f'''Список другий: {some_list_2}''')
print(f'''Числа що є у першому та другому списках: {some_set_1 & some_set_2}''')
print(f'''Числа що є у першому списку та нема в другому: {some_set_1.difference(some_set_2)}''')
print(f'''Числа що є унікальніми для першого та другого списку: '''
      f'''{some_set_1.difference(some_set_2) | some_set_2.difference(some_set_1)}''')
