import math
from decimal import Decimal, getcontext


class Vector(object):
    getcontext().prec = 6
    CANNOT_NORMALIZE_ZERO_VECTOR_NSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        res = [x ** 2 for x in self.coordinates]
        return (sum(res)) ** (Decimal(1) / 2)

    def normalize(self):
        try:
            scale = 1 / self.magnitude()
            return self.scalar(scale)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_NSG)

    def dotProduct(self, v):
        res = [x * y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(res)

    def is_orthogonal(self, v):
        dp = self.dotProduct(v)
        if dp == 0:
            return True
        else:
            return False

    def is_parallel(self, v):
        res = set([x / y for x, y in zip(self.coordinates, v.coordinates)])
        return len(set(res)) <= 1

    def projection(self, v):
        u = v.normalize()
        product = self.dotProduct(u)
        return u.scalar(product)

    def orthogonal_to(self, v):
        projection = self.projection(v)
        return self.subtract(projection)

    def vector_angle(self, v):
        try:
            dp = self.dotProduct(v)
            smag = self.magnitude()
            vmag = Vector.magnitude(v)
            return math.acos(dp / (smag * vmag))

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_NSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
