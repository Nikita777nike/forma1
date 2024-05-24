my_dict = {'Nikita': 1999, 'Denis': 2001, 'Max': 1993}
print('Dict:',my_dict)
print('Existing value:', my_dict['Max'])
print('Not existing value:', my_dict.get('Egor'))
my_dict.update({'Sahsa': 2004,
                'Kolya': 1997})
a = my_dict.pop('Denis')
print('Modified dictionary:', my_dict)
print('Deleted value:', a)
my_set = {1, 2, 3, 2, 4, 'Апельсин', 44.233}
print(my_set)
my_set.update({5, 'Банан'})
my_set.discard(3)
print(my_set)






