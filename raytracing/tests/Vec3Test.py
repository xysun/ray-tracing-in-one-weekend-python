__author__ = 'jsun'

from raytracing.vec3 import Vec3

import unittest

class TestVec3(unittest.TestCase):

    def test_add(self):
        v1 = Vec3(0,1,2)
        v2 = Vec3(3,4,5)
        v3 = v1 + v2

        self.assertEqual(v3.e0, 3)
        self.assertEqual(v3.e1, 5)
        self.assertEqual(v3.e2, 7)

    def test_mul(self):
        v1 = Vec3(1,2,3)
        v3 = v1 * 2

        self.assertEqual(v3.e0, 2)
        self.assertEqual(v3.e1, 4)
        self.assertEqual(v3.e2, 6)

    def test_unit_vector(self):

        v1 = Vec3(1,2,3)
        self.assertEqual(v1.unit_vector().length, 1)

    def test_dot(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(2,3,4)
        v3 = v1.dot(v2)

        self.assertEqual(v3, 20)

    def test_divide(self):
        v1 = Vec3(1,2,3)
        v2 = v1 / 2.0

        self.assertEqual(v2.e0, 0.5)
        self.assertEqual(v2.e1, 1)
        self.assertEqual(v2.e2, 1.5)

if __name__ == '__main__':
    unittest.main()