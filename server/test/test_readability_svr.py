import sys
import os
import unittest
fn = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(fn)      # import the root directory
fn = os.path.join(os.path.dirname(__file__), '../readability_svr/')
sys.path.append(fn)      # import the root directory
import readability_svr
from metrics.strlength import strLen

def test():
    return True;

class Simple(unittest.TestCase):

#    def setUp(self):
#        self.seq = range(10)

    def test_hello(self):
        self.assertEqual(readability_svr.hello(),"Hello World!")

    def test_strLength(self):
        self.assertEqual(strLen("1234"), 4)


if __name__ == '__main__':
    unittest.main()
