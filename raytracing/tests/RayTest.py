__author__ = 'jsun'

from raytracing.ray import Ray
from raytracing.vec3 import Vec3
from raytracing.main import hit_sphere

import unittest

class RayTest(unittest.TestCase):

    def test_point_at_parameter(self):

        ray = Ray(Vec3(0,0,0), Vec3(1,1,1))
        p = ray.point_at_parameter(2)

        self.assertEqual(p.e0, 2)
        self.assertEqual(p.e1, 2)
        self.assertEqual(p.e2, 2)

    def test_hit_sphere(self):

        center = Vec3(2,1,0)
        radius = 1
        origin = Vec3(0,1,0)

        dir1 = Vec3(2,2,0)
        ray1 = Ray(origin, dir1)
        self.assertFalse(hit_sphere(center, radius, ray1))

        dir2 = Vec3(2,1,0)
        ray2 = Ray(origin, dir2)
        self.assertTrue(hit_sphere(center, radius, ray2))




if __name__ == '__main__':
    unittest.main()