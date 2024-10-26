import unittest
from unit_test import TournamentTest

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)