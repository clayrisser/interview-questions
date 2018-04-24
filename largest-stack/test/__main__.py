import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
import test_stack, test_max_stack

if __name__ == '__main__':
  loader = unittest.TestLoader()
  suite  = unittest.TestSuite()
  suite.addTests(loader.loadTestsFromModule(test_stack))
  suite.addTests(loader.loadTestsFromModule(test_max_stack))
  runner = unittest.TextTestRunner(verbosity=3)
  result = runner.run(suite)
