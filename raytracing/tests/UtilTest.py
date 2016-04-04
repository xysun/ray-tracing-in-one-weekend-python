__author__ = 'jsun'

import unittest

from raytracing.material import random_in_unit_sphere

class UtilTest(unittest.TestCase):

    def test_random_in_unit_sphere(self):
        p = random_in_unit_sphere()
        self.assertLess(p.dot(p), 1.0)

if __name__ == '__main__':
    unittest.main()

