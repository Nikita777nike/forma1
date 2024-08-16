from threading import Thread
from time import sleep, time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self, enemy=100):
        print(f'{self.name} на нас напали!')
        start_time = time()
        while enemy > 0:
            enemy -= self.power
            sleep(1)
            current_time = time()
            print(f'{self.name} сражается {round(current_time-start_time)} день(дня), осталось врагов: {enemy}')
        end_time = time()
        print(f'{self.name} одержал победу спустя {round(end_time-start_time)} дней (дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
