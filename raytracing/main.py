__author__ = 'jsun'

from vec3 import Vec3
from ray import Ray

def color(ray):

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

        for j in range(ny-1, -1, -1):
            for i in range(0, nx):

                u = float(i) / float(nx)
                v = float(j) / float(ny)

                ray = Ray(origin=origin, direction=lower_left_corner + horizontal*u + vertical*v)
                col = color(ray)

                ir = int(255.99*col.e0)
                ig = int(255.99*col.e1)
                ib = int(255.99*col.e2)
                line = "{} {} {}\n".format(ir,ig,ib)
                f.write(line)









if __name__ == '__main__':
    main()