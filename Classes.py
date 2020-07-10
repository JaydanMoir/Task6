class Animals:
    place = "Ферма Дядюшки Джо\n"
    print(place)
    state = None
    sound = None

    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight

    def walk(self):
        self.state = "Гуляет"
        return self.state

    def eat(self):
        self.state = "Употрлебляет пищу"
        return self.state

class Gooses(Animals):
    name = "Гусь"
    sound = "Га-Га"

    def lay_eggs(self):
        self.state = "Получены гусинные яйца"
        return self.state

class Cows(Animals):
    name = "Корова"
    sound = "Му-му"

    def get_milk(self):
        self.state = "Получено коровье молоко"
        return self.state

class Sheeps(Animals):
    name = "Овца"
    sound = "Бе-Бе"

    def trim(self):
        self.state = "Подстрижен"
        return self.state

class Hens(Animals):
    name = "Курица"
    sound = "Ку-ка-ре-ку"

    def lay_eggs(self):
        self.state = "Получены куринные яйца"
        return self.state

class Goats(Animals):
    name = "Коза"
    sound = "Ме-Ме"

    def get_milk(self):
        self.state = "Получено козье молоко"
        return self.state

class Ducks(Animals):
    name = "Утка"
    sound = "Кря-Кря"

    def lay_eggs(self):
        self.state = "Получены гусинные яйца"
        return self.state


'''Объекты'''
animals_dict = {}

Goose1 = Gooses("Серый", 5)
animals_dict[Goose1.name] = Goose1.weight
print(Goose1.name)
print(Goose1.sound)
print(Goose1.walk())
print(Goose1.eat())
print(Goose1.lay_eggs())
print()

Goose2 = Gooses("Белый", 7)
animals_dict[Goose2.name] = Goose2.weight
print(Goose2.name)
print(Goose2.sound)
print(Goose2.walk())
print(Goose2.eat())
print(Goose2.lay_eggs())
print()

Cow1 = Cows("Манька", 400)
animals_dict[Cow1.name] = Cow1.weight
print(Cow1.name)
print(Cow1.sound)
print(Cow1.walk())
print(Cow1.eat())
print(Cow1.get_milk())
print()

Sheep1 = Sheeps("Барашек", 65)
animals_dict[Sheep1.name] = Sheep1.weight
print(Sheep1.name)
print(Sheep1.sound)
print(Sheep1.walk())
print(Sheep1.eat())
print(Sheep1.trim())
print()

Sheep2 = Sheeps("Кудрявый", 78)
animals_dict[Sheep2.name] = Sheep2.weight
print(Sheep2.name)
print(Sheep2.sound)
print(Sheep2.walk())
print(Sheep2.eat())
print(Sheep2.trim())
print()

Hen1 = Hens("Ко-Ко", 1.5)
animals_dict[Hen1.name] = Hen1.weight
print(Hen1.name)
print(Hen1.sound)
print(Hen1.walk())
print(Hen1.eat())
print(Hen1.lay_eggs())
print()

Hen2 = Hens("Кукареку", 2)
animals_dict[Hen2.name] = Hen2.weight
print(Hen2.name)
print(Hen2.sound)
print(Hen2.walk())
print(Hen2.eat())
print(Hen2.lay_eggs())
print()

Goat1 = Goats("Рога", 50)
animals_dict[Goat1.name] = Goat1.weight
print(Goat1.name)
print(Goat1.sound)
print(Goat1.walk())
print(Goat1.eat())
print(Goat1.get_milk())
print()

Goat2 = Goats("Копыта", 60)
animals_dict[Goat2.name] = Goat2.weight
print(Goat2.name)
print(Goat2.sound)
print(Goat2.walk())
print(Goat2.eat())
print(Goat2.get_milk())
print()

Duck1 = Ducks("Кряква", 3)
animals_dict[Duck1.name] = Duck1.weight
print(Duck1.name)
print(Duck1.sound)
print(Duck1.walk())
print(Duck1.eat())
print(Duck1.lay_eggs())
print()

print(f"Общий вес всех животных: {sum(animals_dict.values())}кг\n")

for animal, weight in animals_dict.items():
    if weight == max(animals_dict.values()):
        print(f"Самое тяжелое животное: {animal}({weight}кг)")

