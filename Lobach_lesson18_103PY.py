class Tomato:  # Объявление класса.
    states = {
        1: "Томат посажен.",
        2: "Появление всходов.",
        3: "Появление первого настоящего листа.",
        4: "Разрастание надземной массы и корней.",
        5: "Образование бутонов.",
        6: "Цветение.",
        7: "Формирование плодов.",
        8: "Созревание плодов."
    }  # Словарь со стадиями созревания.

    def __init__(self, index):  # Инициализация дин. методов , индекс задается
        self._index = index
        self._state = 1

    def grow(self):  # Метод отвечающий за переход на след. стадию созревания.
        if self._state < 8:  # Если номер стадии меньше 8, томат еще не спелый.
            self._state += 1  # Переход на следующую стадию.

    def is_ripe(self):  # Метод для проверки. Созрел томат или нет.
        if self._state == 8:  # Если номер стадии = 8, томат спелый.
            return True  # Возвращается TRUE
        else:  # Иначе
            return False  # False


class TomatoBush:  # Объявление класса
    def __init__(self, num):  # Инициализцаия дин. свойств класса
        self.num = num  # задается количество томатов на ветке.
        self.tomatoes = []  # Пустой список, далее список томатов (список объектов класса ТОМАТ).
        for tomato in range(0, num):  # Итератор для пополнения списка.
            self.tomatoes.append(Tomato(index=tomato))

    def grow_all(self):  # Метод, для перевода томатов на ветке на след. этап созревания.
        for tomato in self.tomatoes:  # Проходимся по списку и для каждого томата вызываем мето grow.
            tomato.grow()

    def all_are_ripe(self):  # Метод класса , для определения созрели ли томаты на ветке.
        ripe_list = []  # Пустой список , далее будет хранить True либо False (Спелый томат или нет)
        for tomato in self.tomatoes:  # Проходимся по списку с томатами
            if tomato.is_ripe():  # Если томат спелый добовляем True в список если нет , добовляем False
                ripe_list.append(True)
            else:
                ripe_list.append(False)
        return all(ripe_list)  # Функция all возвращает True если все элементы списка истины.

    def give_away_all(self):  # Метод для чистки списка томатов
        self.tomatoes = []  # передается пустой список в переменную .


class Gardener:
    def __init__(self, name, plant):  # Метод для определения дин. свойств
        self.name = name  # Имя (наверное садовника)
        self._plant = plant  # будет принимать объект класса Томат.

    def work(self):  # Метод влияющий на созревание растения
        self._plant.grow_all()  # перевод томата на следующий этап созревания.

    def harvest(self):  #  Метод проверяет, все ли плоды созрели
        if self._plant.all_are_ripe():  # Если в списке все True, то все плоды созрели.
            print("Урожай собран.")
        else:
            print("Еще не все плоды созрели!")

    @staticmethod  # Статичный метод.
    def knowledge_base():
        print("""
Помидоры снимают с куста по мере созревания, обычно каждые 3-5 дней.
При этом важно не допустить перезревания плодов, так как в таком виде
не удастся долго сохранить собранные помидоры (их сразу употребляют в пищу),
вкусовые качества томатов ухудшатся.
""")  # Выводит справку в консоль.


Gardener.knowledge_base()
tomato_1 = TomatoBush(2)
gardener_1 = Gardener("Alex", tomato_1)
gardener_1.work()
gardener_1.harvest()
gardener_1.work()
gardener_1.work()
gardener_1.work()
gardener_1.work()
gardener_1.work()
gardener_1.work()
gardener_1.harvest()
