class Human:
    default_name = 'Alex'
    default_age = 27

    def __init__(self, name, age):
        self.default_name = name
        self.default_age = age
        self.__money = 350
        self.__house = False

    def info(self):
        print(f'Имя: {self.default_name}. Возраст: {self.default_age}. Деньги: {self.__money}. Дом: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Имя: {Human.default_name}. Возраст: {Human.default_age}')

    def earn_money(self, money):
        self.__money += money

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, sale):
        price = house.final_price(sale)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Недостаточно денег!')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        final_pr = self._price - (self._price * (sale / 100))
        return final_pr


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


Human.default_info()
sergey = Human("Sergey", 31)
sergey.info()

house_1 = SmallHouse(5000)
sergey.buy_house(house_1, 11)

sergey.earn_money(8250)
sergey.info()
sergey.buy_house(house_1, 11)
sergey.info()
