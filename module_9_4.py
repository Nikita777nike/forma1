from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_compr = list(map(lambda x, y: x == y, first, second))
print(my_compr)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as opener:
            for line in data_set:
                if isinstance(line, str):
                    opener.write(line + '\n')
                elif isinstance(line, list):
                    for i in line:
                        opener.write(str(i) + ' ')

    return write_everything


write = get_advanced_writer('example.txt')

result = write('Это строка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        rand_word = choice(self.words)
        return rand_word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())