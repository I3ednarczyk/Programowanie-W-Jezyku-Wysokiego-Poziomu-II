class Matrix:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = [[a, b], [c, d]]

    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    def __mul__(self, other):
        return Matrix(self.a * other.a, self.b * other.b, self.c * other.c, self.d * other.d)
    def __str__(self):
        return f"[{self.a}, {self.b};\n{self.c}, {self.d}]"
    def __repr__(self):
        return f"({self.a}, {self.b}, {self.c}, {self.d})"


