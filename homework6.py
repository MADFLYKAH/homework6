my_dict = {'Oleg': 2000, 'Alex': 1980}
print(my_dict)
print(my_dict['Oleg'])
print(my_dict.get('Denis'))
my_dict.update({'Olga': 1995, 'Sasha': 1997})
a = my_dict.pop('Alex')
print(a)
print(my_dict)

my_set = {1, 1, 1, 2, 2, 'String', True, (1, 2, 3), 5, 5}
print(my_set)
my_set.update([22, 12])
my_set.remove(2)
print(my_set)
