__author__ = 'jsun'

import math

class Vec3:
    def __init__(self, e0, e1, e2):
        self.e0 = e0
        self.e1 = e1
        self.e2 = e2

        self.length = math.sqrt(e0**2+e1**2+e2**2)

    def __add__(self, other):

        return Vec3(self.e0 + other.e0,
                    self.e1 + other.e1,
                    self.e2 + other.e2)

    def __sub__(self, other):

        return Vec3(self.e0 - other.e0,
                    self.e1 - other.e1,
                    self.e2 - other.e2)

    def __mul__(self, other):

        return Vec3(self.e0 * other,
                    self.e1 * other,
                    self.e2 * other)

    def mul(self, other):
        return Vec3(self.e0 * other.e0,
                    self.e1 * other.e1,
                    self.e2 * other.e2)

    def __div__(self, other):

        return Vec3(self.e0 / other,
                    self.e1 / other,
                    self.e2 / other)


    def unit_vector(self):

        return Vec3(self.e0/self.length,
                    self.e1/self.length,
                    self.e2/self.length)

    def dot(self, other):

        return self.e0 * other.e0 + \
                    self.e1 * other.e1 + \
                    self.e2 * other.e2

    def cross(self, other):

        return Vec3(self.e1*other.e2 - self.e2*other.e1,
                    -(self.e0*other.e2-self.e2*other.e0),
                    self.e0*other.e1-self.e1*other.e0)

