__author__ = 'jsun'


import unittest
from raytracing.sphere import Sphere
from raytracing.hit_record import Hit_record
from raytracing.vec3 import Vec3
from raytracing.ray import Ray
from raytracing.material import Lambertian

class SphereTest(unittest.TestCase):

    def test_hit(self):
        rec = Hit_record(t = 0, p = Vec3(0,0,0), normal=Vec3(0,0,0))
        sphere = Sphere(center=Vec3(2,1,0), radius=1, material=Lambertian(Vec3(1,1,1)))

        ray1 = Ray(origin=Vec3(0,1,0), direction=Vec3(2,2,0))
        self.assertFalse(sphere.hit(ray1,0,100,rec))

        ray2 = Ray(origin=Vec3(0,1,0), direction=Vec3(2,1,0))
        self.assertTrue(sphere.hit(ray2, 0, 100, rec))


if __name__ == "__main__":
    unittest.main()

