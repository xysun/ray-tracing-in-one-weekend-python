__author__ = 'jsun'

from raytracing.ray import Ray
from raytracing.vec3 import Vec3

import unittest

class RayTest(unittest.TestCase):

    def test_point_at_parameter(self):

        ray = Ray(Vec3(0,0,0), Vec3(1,1,1))
        p = ray.point_at_parameter(2)

        self.assertEqual(p.e0, 2)
        self.assertEqual(p.e1, 2)
        self.assertEqual(p.e2, 2)


if __name__ == '__main__':
    unittest.main()