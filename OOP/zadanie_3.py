class ElectricCar:
    def __init__(self, max_km):
        self.max_km = max_km
        self._licznik = 0

    # self.km = km

    def drive(self, km):
        if self.max_km < km + self._licznik:
            to_travel = self.max_km - self._licznik
            self._licznik = self.max_km
            return to_travel
        else:
            self._licznik += km
            return km

    def charge(self):
        self._licznik = 0


def test_car_init():
    car = ElectricCar(100)
    assert car.max_km == 100


def test_car_below_max_range():
    car = ElectricCar(100)
    assert car.drive(50) == 50


def test_car_over_max_range():
    car = ElectricCar(100)
    assert car.drive(150) == 0


def test_car_2_time():
    car = ElectricCar(100)
    assert car.drive(50) == 50
    assert car.drive(50) == 0


def test_electric_car_charge():
    car = ElectricCar(100)
    assert car.drive(100) == 100
    assert car.drive(1) == 0
    car.charge()
    assert car.drive(1) == 1
