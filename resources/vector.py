# Introduction  >  2. The Vector Module
import math

class Vector:
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

    def __add__(self, v):
        return Vector([a + b for a, b in zip(self, v)])
    
    def __sub__(self, v):
        return Vector([a - b for a, b in zip(self, v)])

    def __getitem__(self, index):
        return self.coordinates[index]

    def __len__(self):
        return len(self.coordinates)

    def scalar_mul(self, v):
        return Vector([v * c for c in self])

    def get_magnitude(self):
        return math.sqrt(sum([math.pow(a, 2) for a in self.coordinates]))

    def get_normalization(self):
        mag = self.get_magnitude()
        return self.scalar_mul(1/mag)
    
    def dot_product(self, v):
        return sum([a * b for a, b in zip(self.coordinates, v.coordinates)])

    def get_angle_rad(self, v):
        dot_product = self.dot_product(v)
        mag1, mag2 = self.get_magnitude(), v.get_magnitude()
        #if dot_product * mag1 * mag2 == 0:
        #    return 0
        return math.acos(dot_product/(mag1*mag2))
    
    def get_angle_deg(self, v):
        rad = self.get_angle_rad(v)
        deg = rad * (180/math.pi)
        return deg
