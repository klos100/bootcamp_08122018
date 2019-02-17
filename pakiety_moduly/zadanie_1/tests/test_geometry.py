from mathematica.geometry import figures

def test_square_ares():
    assert figures.square_area(5)== 25

def test_trojkat():
    assert figures.triangle_area(10,2) == 10