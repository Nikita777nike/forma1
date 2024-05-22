immutable_var = 1, 2, 'Никита', False
print(immutable_var) # immutable_var[0] = 4  Если мы попытаемся изменить кортеж таким образом, то получим ошибку, потому то он является неизменяемым.
mutable_list = [1, 2, 3, 'Привет', True]
print(mutable_list)
mutable_list [0] = 8
mutable_list [3] = 'Пока'
print(mutable_list)
