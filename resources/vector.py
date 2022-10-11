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
        return 'Vector{}'.format(self.coordinates)


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

    def get_magnitude(self) -> float:
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

        #! I had a bug here because the dot product/magnitudes
        #! were returning 1.0000000000000002 instead of 1.0
        #! so I had to round them to 1.00 (2 decimal places)
        #! to get the correct answer
        return math.acos(round(dot_product / (mag1 * mag2), 2))
    
    def get_angle_deg(self, v):
        rad = self.get_angle_rad(v)
        deg = rad * (180/math.pi)
        return math.ceil(deg)
    
    def is_parallel(self, v):
        try:
            deg = self.get_angle_deg(v)
            return deg == 0 or deg == 180 or deg == 360
        except ZeroDivisionError:
            return True
    
    def is_orthogonal(self, v):
        try:
            dot_product = self.dot_product(v)
            deg = self.get_angle_deg(v)
            return dot_product == 0 or deg == 90 or deg == 270
        except ZeroDivisionError:
            return True
    
    def get_projection(self, b):
        normb = b.get_normalization()
        magvll = self.dot_product(normb)
        vll = Vector(normb.scalar_mul(magvll))
        assert vll.is_parallel(b), "vll is not parallel to b"
        return vll

    def get_orthogonal(self, v):
        proj = self.get_projection(v)
        orth = self - proj
        assert orth.is_orthogonal(v), "orth is not orthogonal to v"
        return orth
        
