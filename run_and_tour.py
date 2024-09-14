import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
        while self.participants:  # по списку участников (объектов класса Runner)
            for participant in self.participants:  # для каждого участника в списке:
                participant.run()                  # вызываем функцию бежать
                if participant.distance >= self.full_distance:  #
                    finishers[place] = participant  # в словарь finishers помещают результат забега (место:участник)
                    place += 1                      # определяем финишера на следующее место,
                    self.participants.remove(participant) # убираем финишировавшего из списка участников
        return finishers # возвращает словарь с результатами забега


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.part_1 = Runner('Усейн', 10)
        self.part_2 = Runner('Андрей', 9)
        self.part_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.part_1, self.part_3 )  # создаем объект класса Забег
        self.all_results = self.tournament_1.start() # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[max(self.all_results.keys())].name #записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[1] = self.all_results # записываем словарь с ключом 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.part_2, self.part_3 )
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.part_1, self.part_2, self.part_3 )
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results



if __name__ == '__main__':
    unittest.main()