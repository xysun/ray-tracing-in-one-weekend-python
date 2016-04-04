__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray

import math

class Camera(object):
    def __init__(self, vfov, aspect):
        self.theta = vfov * math.pi/180.0
        self.half_height = math.tan(self.theta/2.0)
        self.half_width = aspect * self.half_height

        self.lower_left_corner = Vec3(-self.half_width, -self.half_height, -1.0)
        self.origin = Vec3(0.0, 0.0, 0.0)
        self.horizontal = Vec3(2.0 * self.half_width, 0.0, 0.0)
        self.vertical = Vec3(0.0, 2.0 * self.half_height, 0.0)

    def get_ray(self, u, v):
        return Ray(origin=self.origin, direction=self.lower_left_corner + self.horizontal * u + self.vertical * v - self.origin)

