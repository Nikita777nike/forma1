import unittest
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format='%(levelname)s | %(message)s | %(asctime)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run_1 = Runner('John', -5)
            for i in range(10):
                run_1.walk()
            logging.info(f'"test_walk" выполнен успешно')
            self.assertEqual(run_1.distance, 50)
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run_2 = Runner(10, 10)
            for i in range(10):
                run_2.run()
                logging.info(f'"test_run" выполнен успешно')
                self.assertEqual(run_2.distance, 100)
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)



if __name__ == '__main__':
    unittest.main()