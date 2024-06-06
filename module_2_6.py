def print_params(a=1, b='Строка', c=True):
    print(a, b, c)
    values_list = [5, 'name', 'Nikita']
    print(values_list)
    values_dict = {'a': 1, 'b': 2, 'c': 3}
    print(values_dict)
    values_list_2 = [54.32, 'Строка']
    values_list_2.append(42)
    print(values_list_2)


print_params()
print_params(b=25)
print_params(c=[1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*value_list_2, 42)







