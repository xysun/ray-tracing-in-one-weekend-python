__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray
from hit_record import Hit_record
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera
from material import *

import math
import random


def hit_sphere(center, radius, ray):

    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = oc.dot(ray.direction)
    c = oc.dot(oc) - radius*radius

    discriminant = b*b - a*c

    if discriminant > 0:
        return (-b - math.sqrt(discriminant)) / a
    else:
        return -1


def color(ray, world, depth):

    hit_record = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))

    if world.hit(ray, 0.0, 10000, hit_record):
        scattered = Ray(origin=Vec3(0,0,0), direction=Vec3(0,0,0))
        t = hit_record.material.scatter(ray, hit_record, scattered)
        if depth < 50 and t[0]:
            return color(scattered, world, depth+1).mul(t[1])
        else:
            return Vec3(0,0,0)

    else:

        unit_direction = ray.direction.unit_vector()
        t = 0.5 * (unit_direction.e1 + 1.0)

        return Vec3(1.0, 1.0, 1.0) * (1-t) + Vec3(0.5, 0.7, 1.0)*t

def main():

    with open("output.ppm", "w") as f:
        nx = 200
        ny = 100
        ns = 20

        header = "P3\n{} {}\n255\n".format(nx, ny)

        f.write(header)

        camera = Camera(Vec3(-2,2,1), Vec3(0,0,-1), Vec3(0,1,0), 90, float(nx)/float(ny))
        #demonstrate closer camera
        #camera = Camera(Vec3(-1,1,1), Vec3(0,0,-1), Vec3(0,1,0), 60, float(nx)/float(ny))

        r = math.cos(math.pi / 4.0)
        sphere1 = Sphere(Vec3(-r, 0, -1), r, Lambertian(Vec3(0,0,1)))
        sphere2 = Sphere(Vec3(r, 0, -1), r, Lambertian(Vec3(1,0,0)))
        #sphere1 = Sphere(Vec3(0.0,0.0,-1.0), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3)))
        #sphere2 = Sphere(Vec3(0.0, -100.5, -1.0), 100.0, Lambertian(Vec3(0.8, 0.8, 0.0)))
        #sphere3 = Sphere(Vec3(1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.6, 0.2)))
        #sphere4 = Sphere(Vec3(-1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.8, 0.8)))

        world = Hitable_list([sphere1, sphere2])

        for j in range(ny-1, -1, -1):

            print j

            for i in range(0, nx):


                col = Vec3(0.0, 0.0, 0.0)
                for k in range(0, ns):
                    u = float(i + random.random()) / float(nx)
                    v = float(j + random.random()) / float(ny)
                    ray = camera.get_ray(u, v)
                    col += color(ray, world, 0)

                col /= float(ns)

                col = Vec3(math.sqrt(col.e0), math.sqrt(col.e1), math.sqrt(col.e2))

                ir = int(255.99*col.e0)
                ig = int(255.99*col.e1)
                ib = int(255.99*col.e2)
                line = "{} {} {}\n".format(ir,ig,ib)
                f.write(line)



if __name__ == '__main__':
    main()