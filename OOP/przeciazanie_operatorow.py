class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            vector_3 = Vector(x, y)
            return vector_3  ##lub: Vector(self.x + other.x,y = self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            vector_3 = Vector(x, y)
            return vector_3
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            return x + y
        elif isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.length() < other.length()


def test_vector_init():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1.x == 1


def test_vector_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2
    assert vector_3.y == 4
    assert vector_1.x == 1
    assert vector_2.x == 1

    vector_1 = Vector(x=2, y=5)
    vector_2 = Vector(x=2, y=7)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2 + 2
    assert vector_3.y == 5 + 7


def test_vector_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == 0
    assert vector_3.y == 0

    vector_1 = Vector(x=5, y=0)
    vector_2 = Vector(x=3, y=2)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == 5 - 3
    assert vector_3.y == 0 - 2


def test_vector_mul_vector():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1 * vector_2 == 1 * 1 + 2 * 2


def test_vector_mul_int():
    vector_1 = Vector(x=1, y=2)
    vector_2 = vector_1 * 5
    assert vector_2.x == 5
    assert vector_2.y == 10


def test_length():
    assert Vector(3, 4).length() == 5


def test_vector_lt():
    assert Vector(1, 1) < Vector(1, 2)
    assert (Vector(6, 5) < Vector(5, 5)) == False #lub assert not (Vector(6, 5) < Vector(5, 5))
