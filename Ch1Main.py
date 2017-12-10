from vector.Vector import Vector


def main():
    v1 = Vector((-7.579, -7.88))
    v2 = Vector((22.737, 23.64))

    v3 = Vector((-2.328, -7.284, -1.214))
    v4 = Vector((-1.821, 1.072, -2.94))

    print v3.is_parallel(v4)
    print v3.is_orthogonal(v4)

if __name__ == '__main__':
    main()
