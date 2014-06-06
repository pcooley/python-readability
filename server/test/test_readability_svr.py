import sys
import os
import unittest
fn = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(fn)      # import the root directory
import readability_svr

def test():
    return True;

class Simple(unittest.TestCase):

#    def setUp(self):
#        self.seq = range(10)

    def test_hello(self):
        self.assertEqual(readability_svr.hello(),"Hello World!")

if __name__ == '__main__':
    unittest.main()
