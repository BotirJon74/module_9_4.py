from random2 import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y : x == y, first, second))
print(result)


def get_advanced_writer(fila_name):

    def write_everything(*data_set):
        file = open(fila_name, 'w', encoding='utf-8')
        for record in data_set:
            file.write(str(record) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice

class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
