__author__ = 'jsun'


def main():

    with open("output.ppm", "w") as f:
        nx = 200
        ny = 100

        header = "P3\n{} {}\n255\n".format(nx, ny)

        f.write(header)

        for j in range(ny-1, -1, -1):
            for i in range(0, nx):
                r = float(i) / float(nx)
                g = float(j) / float(ny)
                b = 0.2
                ir = int(255.99*r)
                ig = int(255.99*g)
                ib = int(255.99*b)
                line = "{} {} {}\n".format(ir,ig,ib)
                f.write(line)









if __name__ == '__main__':
    main()