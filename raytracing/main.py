__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray
from hit_record import Hit_record
from sphere import Sphere
from hitable_list import Hitable_list

import math

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


def color(ray, world):

    hit_record = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))

    if world.hit(ray, 0.0, 10000, hit_record):
        return Vec3(hit_record.normal.e0 + 1, hit_record.normal.e1 + 1, hit_record.normal.e2 + 1) * 0.5
    else:

        unit_direction = ray.direction.unit_vector()
        t = 0.5 * (unit_direction.e1 + 1.0)

        return Vec3(1.0, 1.0, 1.0) * (1-t) + Vec3(0.5, 0.7, 1.0)*t

def main():

    with open("output.ppm", "w") as f:
        nx = 200
        ny = 100

        header = "P3\n{} {}\n255\n".format(nx, ny)

        f.write(header)

        lower_left_corner = Vec3(-2.0, -1.0, -1.0)
        horizontal = Vec3(4.0, 0.0, 0.0)
        vertical = Vec3(0.0, 2.0, 0.0)
        origin = Vec3(0.0, 0.0, 0.0)

        sphere1 = Sphere(Vec3(0.0,0.0,-1.0), 0.5)
        sphere2 = Sphere(Vec3(0.0, -100.5, -1.0), 100.0)
        world = Hitable_list([sphere1, sphere2])

        for j in range(ny-1, -1, -1):
            for i in range(0, nx):

                u = float(i) / float(nx)
                v = float(j) / float(ny)

                ray = Ray(origin=origin, direction=lower_left_corner + horizontal*u + vertical*v)
                col = color(ray, world)

                ir = int(255.99*col.e0)
                ig = int(255.99*col.e1)
                ib = int(255.99*col.e2)
                line = "{} {} {}\n".format(ir,ig,ib)
                f.write(line)



if __name__ == '__main__':
    main()