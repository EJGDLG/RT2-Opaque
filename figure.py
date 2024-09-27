from intercep import Intercep
from math import atan2, acos, pi, sqrt

class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material
        self.type = "None"
    
    def ray_intersect(self, orig, dir):
        return None
    

class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius
        self.type = "Sphere"
    
    # Helper function to subtract two vectors
    def vector_subtract(self, v1, v2):
        return [v1[i] - v2[i] for i in range(len(v1))]

    # Helper function to add two vectors
    def vector_add(self, v1, v2):
        return [v1[i] + v2[i] for i in range(len(v1))]

    # Helper function to dot product of two vectors
    def dot_product(self, v1, v2):
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    # Helper function to multiply a vector by a scalar
    def vector_multiply(self, v, scalar):
        return [v[i] * scalar for i in range(len(v))]

    # Helper function to compute the norm (magnitude) of a vector
    def norm(self, v):
        return sqrt(sum(v[i] ** 2 for i in range(len(v))))

    # Helper function to normalize a vector
    def normalize(self, v):
        norm_v = self.norm(v)
        return [v[i] / norm_v for i in range(len(v))]

    def ray_intersect(self, orig, dir):
        # L = self.position - orig
        L = self.vector_subtract(self.position, orig)

        # tca = dot(L, dir)
        tca = self.dot_product(L, dir)

        # d = sqrt(norm(L) ^ 2 - tca ^ 2)
        d = sqrt(self.norm(L) ** 2 - tca ** 2)

        if d > self.radius:
            return None
        
        # thc = sqrt(radius ^ 2 - d ^ 2)
        thc = sqrt(self.radius ** 2 - d ** 2)

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None 

        # P = orig + dir * t0
        P = self.vector_add(orig, self.vector_multiply(dir, t0))

        # normal = (P - self.position) / norm(P - self.position)
        normal = self.vector_subtract(P, self.position)
        normal = self.normalize(normal)

        # Compute texture coordinates
        u = (atan2(normal[2], normal[0])) / (2 * pi) + 0.5
        v = acos(-normal[1]) / pi

        return Intercep(point=P,
                        normal=normal,
                        distance=t0,
                        texCoords=[u, v],
                        rayDirection=dir,
                        obj=self)
