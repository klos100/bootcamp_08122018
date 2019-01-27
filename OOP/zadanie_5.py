class CashMachine:

    def __init__(self):
        self._money = []

    @property  # dekoruje funkcje zamieniajac ja na atryut, wywyływana jest jako atrybut a nie funkcja
    def is_available(self):
        if self._money:
            return True
        return False

    def put_money(self, bills_list):
        self._money.extend(bills_list)

    def withdraw_money(self, x):
        money_to_withdraw = []
        for i in sorted(self._money, reverse=True):
            if sum(money_to_withdraw) + i <= x:
                money_to_withdraw.append(i)
        # tu sprawdzam czy udalo sie uzbierac
        if sum(money_to_withdraw) != x:
            return []
        #skoro uzbieralam co trzeba to usuwam to ze stanu
        for i in money_to_withdraw:
            self._money.remove(i)

        return money_to_withdraw


def test_cash_machine_is_not_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available


def test_cash_machine_withdraw_maney():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]
    assert cash_machine.withdraw_money(150) == []
