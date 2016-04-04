__author__ = 'jsun'

from abc import ABCMeta, abstractmethod
import random
from vec3 import Vec3

def random_in_unit_sphere():

    p = Vec3(random.random(), random.random(), random.random()) * 2 - Vec3(1.0, 1.0, 1.0)

    while p.dot(p) >= 1.0:
        p = Vec3(random.random(), random.random(), random.random()) * 2 - Vec3(1.0, 1.0, 1.0)

    return p



class Material:
    __metaclass__ = ABCMeta

    @abstractmethod
    def scatter(self, ray_in, hit_record, scattered_ray):pass

    def reflect(self, v, n):
        return v - n * (v.dot(n) * 2)


class Lambertian(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit_record, scattered_ray):

        target = hit_record.p + hit_record.normal + random_in_unit_sphere()

        scattered_ray.origin = hit_record.p
        scattered_ray.direction = target - hit_record.p

        return (True, self.albedo)


class Metal(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit_record, scattered_ray):
        reflected = self.reflect(ray_in.direction.unit_vector(), hit_record.normal)
        scattered_ray.origin = hit_record.p
        scattered_ray.direction = reflected

        return (scattered_ray.direction.dot(hit_record.normal) > 0, self.albedo)
