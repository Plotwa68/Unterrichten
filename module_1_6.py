print(' Работа со словарями: ')
my_dict = {'Den' : 121298, 'Max' : 180543, 'Pedro' : 301114}
print(my_dict)
print(my_dict.get('Den'), my_dict.get('Sanja'))
my_dict.update({'Sasha' : 180322, 'Vito' : 120929})
print(my_dict)
print(my_dict.pop('Max'), ' Max')
print(my_dict)


print('Работа с множествами: ')
my_set= {1, 3, 4, 12, 43, 34, 12}
print(my_set)

my_set.add(32)
my_set.add(39)
print(my_set)

my_set.discard(1)

print(my_set)