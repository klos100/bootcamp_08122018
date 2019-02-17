from mathematica.geometry import figures
from mathematica.algebra import matrices

# form mathematica import algebra, geometry

###lub a = mathematica.geometry.figures.square_area(2) jesli import mathematica.geometry.figures

a = figures.square_area(2)
b = figures.triangle_area(2, 5)

print(a)
print(b)

c = matrices.add_matrices([[1, 2]], [[2, 5]])
d = matrices.sub_matrices([[1, 2]], [[2, 5]])

print(c)
print(d)
