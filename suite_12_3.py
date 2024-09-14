import unittest
from module_12_3 import run, run_and_tour

run_ = unittest.TestSuite()

run_.addTest(unittest.TestLoader().loadTestsFromTestCase(run.RunnerTest))
run_.addTest(unittest.TestLoader().loadTestsFromTestCase(run_and_tour.TournamentTest))


testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(run_)