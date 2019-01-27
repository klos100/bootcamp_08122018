class BasketEn:
    def __init__(self,product,ilosc):
        self.product = product
        self.ilosc = ilosc

    def count_price(self):
        return self.product.cena * self.ilosc

    def raport(self):
        return  f' -{self.product.name} ({self.product.id}), cena: {self.product.cena} x {self.ilosc}\n'

class Basket:

    def __init__(self):
        self.entries = []

    # sciezka z uzyciem listy:
    # def add_product(self,product,ilosc):
    #     add = True
    #     for posision in self.entries:
    #         if posision[0] == product:
    #             posision[1] += ilosc
    #             add = False
    #     if add:
    #         self.entries.append([product,ilosc])
    #
    # def count_total_price(self):
    #     total = 0
    #     for e in self.entries:
    #         total += e[0].price *e[1]
    #
    #     return total
    def add_product(self, product, ilosc):
        basket_en = BasketEn(product,ilosc)
        for be in self.entries:
            if be.product == product:
                be.ilosc += ilosc
                break
        else:
            self.entries.append(basket_en)

    def count_total_entry(self):
        total = 0
        for e in self.entries:
            total += e.count_price()
        return total

    def generate_raport(self):
        raport = "Produkty w koszyku: \n"
        for e in self.entries:
            raport += e.raport()
        raport += f'W sumie: {self.count_total_price()}'
        return raport


class Product:

    def __init__(self, cena, nazwa, id):
        self.cena = cena
        self.nazwa = nazwa
        self.id = id


def test_init_basket():
    basket = Basket()
    assert basket.entries == []

def test_init_produkt():
    produkt = Product(10,'Woda',1)
    assert produkt.nazwa == 'Woda'
    assert produkt.id == 1
    assert produkt.cena == 10

def test_basket_add_produkt():
    basket = Basket()
    produkt = Product(10, 'Woda', 1)
    basket.add_product(produkt1,5)
    assert len(basket.entries) == 1

def test_basket_add_produkt():
    basket = Basket()
    produkt = Product(10, 'Woda', 1)
    produkt = Product(5, 'Woda', 2)
    basket.add_product(produkt,5)
    basket.add_product(produkt, 5)
    assert len(basket.entries) == 1

def test_dupa():
    basket = Basket()
    produkt = Product(10.0, 'Woda', 1)
    basket.add_product(produkt, 5)
    assert basket.generate_raport() == "