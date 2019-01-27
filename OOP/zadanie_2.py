class Employee:

    def __init__(self, name, lastname, rate_per_houer):
        self.name = name
        self.lastname = lastname
        self.rate_per_houer = rate_per_houer   ###nazwa przy self jest dowolna i to nią posługujemy się wewnątrz klasy to to co jest po znaku = musi byc takie jak w arg klasy
        self._registered_time = 0 #podkreslinik to zmienna prywatna


    def register_time(self, x):
        self._registered_time = x

    def pay_salary(self):
        if self._registered_time > 8:
            o = self._registered_time - 8
            to_pay = self.rate_per_houer * 8 + o * self.rate_per_houer*2
        else:
            to_pay = self.rate_per_houer * self._registered_time

        self._registered_time = 0
        return to_pay






def test_employee_init():
    employee = Employee("Jan", 'Kowalski', 100)

    assert employee.name == 'Jan'
    assert employee.lastname == 'Kowalski'
    assert employee.rate_per_houer == 100

def test_bez_pracy():
    employee = Employee("Jan", 'Kowalski', 100)

def test_nadgodziny():
    employee = Employee("Jan", 'Kowalski', 100)
    employee.register_time(5) == 500
    assert  employee.pay_salary() == 500
    assert  employee.pay_salary() == 0

def test_nadgodziny():
    employee = Employee("Jan", 'Kowalski', 100)
    employee.register_time(10)

    assert  employee.pay_salary() == 1200
    assert  employee.pay_salary() == 0


