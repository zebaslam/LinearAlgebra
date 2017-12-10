class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        res = []
        for i in range(0, self.dimension):
            t1 = self.coordinates[i]
            t2 = v.coordinates[i]
            res.append(t1 + t2)
        return Vector(res)

    def subtract(self, v):
        res = []
        for i in range(0, self.dimension):
            t1 = self.coordinates[i]
            t2 = v.coordinates[i]
            res.append(t1 - t2)
        return Vector(res)

    def scalar(self, scale):
        return Vector(map(lambda x: scale * x, self.coordinates))

    def magnitude(self):
        res = [x**2 for x in self.coordinates]
        return (sum(res)) ** (1 / 2.0)

    def normalize(self):
        try:
            scale = 1. / self.magnitude()
            return self.scalar(scale)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
