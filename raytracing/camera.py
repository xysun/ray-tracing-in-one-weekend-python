__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray

class Camera(object):
    def __init__(self):
        self.lower_left_corner = Vec3(-2.0, -1.0, -1.0)
        self.origin = Vec3(0.0, 0.0, 0.0)
        self.horizontal = Vec3(4.0, 0.0, 0.0)
        self.vertical = Vec3(0.0, 2.0, 0.0)

    def get_ray(self, u, v):
        return Ray(origin=self.origin, direction=self.lower_left_corner + self.horizontal * u + self.vertical * v - self.origin)

