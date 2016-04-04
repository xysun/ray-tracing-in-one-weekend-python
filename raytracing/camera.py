__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray

import math

class Camera(object):
    def __init__(self, lookFrom, lookAt, vup, vfov, aspect):

        self.theta = vfov * math.pi/180.0
        self.half_height = math.tan(self.theta/2.0)
        self.half_width = aspect * self.half_height

        self.origin = lookFrom

        self.w = (lookFrom - lookAt).unit_vector()
        self.u = vup.cross(self.w).unit_vector()
        self.v = self.w.cross(self.u)

        self.lower_left_corner = self.origin - self.u*self.half_width - self.v*self.half_height - self.w

        self.horizontal = self.u*self.half_width*2
        self.vertical = self.v*self.half_height*2

    def get_ray(self, u, v):
        return Ray(origin=self.origin, direction=self.lower_left_corner + self.horizontal * u + self.vertical * v - self.origin)

