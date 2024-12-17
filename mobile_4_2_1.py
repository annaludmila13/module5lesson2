class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")
# Создаем первый дом
h1 = House('ЖК Горский', 18)

# Вызываем метод go_to() для первого дома
h1.go_to(5)

# Создаем второй дом
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to() для второго дома
h2.go_to(10)
