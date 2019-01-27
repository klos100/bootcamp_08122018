class Employee:

    def __init__(self, name, lastname, rate_per_houer):
        self.name = name
        self.lastname = lastname
        self.rate_per_houer = rate_per_houer  ###nazwa przy self jest dowolna i to nią posługujemy się wewnątrz klasy to to co jest po znaku = musi byc takie jak w arg klasy
        self._registered_time = 0  # podkreslinik to zmienna prywatna

    def register_time(self, x):
        self._registered_time = x

    def pay_salary(self):
        if self._registered_time > 8:
            o = self._registered_time - 8
            to_pay = self.rate_per_houer * 8 + o * self.rate_per_houer * 2
        else:
            to_pay = self.rate_per_houer * self._registered_time

        self._registered_time = 0
        return to_pay


class PremiumEmployee(Employee):
    def __init__(self, name, lastname, rate_per_houer):
        Employee.__init__(self, name, lastname, rate_per_houer)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary() + self.bonus
        self.bonus = 0
        return to_pay

        # salary = super().pay_salary()
        # new_salary = salary + self.bonus
        # return new_salary


def test_prenium_give_bonus():
    employee = PremiumEmployee("Jan", 'Kowalski', 100)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500
    assert employee.pay_salary() == 0
