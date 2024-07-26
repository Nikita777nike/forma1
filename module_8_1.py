def add_everything_up(a, b):
    try:
        s = float("{:.2f}".format(a + b))
    except TypeError:
        s = str(a) + str(b)
    return s

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
