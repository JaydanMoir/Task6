class Animal:
    place = "Ферма Дядюшки Джо\n"
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

    def voice(self):
        return self.sound

class Egg(Animal):
    def lay_eggs(self):
        self.state = "Получены яйца"
        return self.state

class Wool(Animal):
    def trim(self):
        self.state = "Подстрижен"
        return self.state

class Milk(Animal):
    def get_milk(self):
        self.state = "Получено молоко"
        return self.state

class Goose(Egg):
    name = "Гусь"
    sound = "Га-Га"

class Cow(Milk):
    name = "Корова"
    sound = "Му-му"

class Sheep(Wool):
    name = "Овца"
    sound = "Бе-Бе"

class Hen(Egg):
    name = "Курица"
    sound = "Ку-ка-ре-ку"

class Goat(Milk):
    name = "Коза"
    sound = "Ме-Ме"

class Duck(Egg):
    name = "Утка"
    sound = "Кря-Кря"


'''Объекты'''
print(Animal.place)
animals_dict = {}

goose1 = Goose("Серый", 5)
animals_dict[goose1.name] = goose1.weight
print(goose1.name)
print(goose1.voice())
print(goose1.walk())
print(goose1.eat())
print(goose1.lay_eggs())
print()

goose2 = Goose("Белый", 7)
animals_dict[goose2.name] = goose2.weight
print(goose2.name)
print(goose2.voice())
print(goose2.walk())
print(goose2.eat())
print(goose2.lay_eggs())
print()

cow1 = Cow("Манька", 400)
animals_dict[cow1.name] = cow1.weight
print(cow1.name)
print(cow1.voice())
print(cow1.walk())
print(cow1.eat())
print(cow1.get_milk())
print()

sheep1 = Sheep("Барашек", 65)
animals_dict[sheep1.name] = sheep1.weight
print(sheep1.name)
print(sheep1.voice())
print(sheep1.walk())
print(sheep1.eat())
print(sheep1.trim())
print()

sheep2 = Sheep("Кудрявый", 78)
animals_dict[sheep2.name] = sheep2.weight
print(sheep2.name)
print(sheep2.voice())
print(sheep2.walk())
print(sheep2.eat())
print(sheep2.trim())
print()

hen1 = Hen("Ко-Ко", 1.5)
animals_dict[hen1.name] = hen1.weight
print(hen1.name)
print(hen1.voice())
print(hen1.walk())
print(hen1.eat())
print(hen1.lay_eggs())
print()

hen2 = Hen("Кукареку", 2)
animals_dict[hen2.name] = hen2.weight
print(hen2.name)
print(hen2.voice())
print(hen2.walk())
print(hen2.eat())
print(hen2.lay_eggs())
print()

goat1 = Goat("Рога", 50)
animals_dict[goat1.name] = goat1.weight
print(goat1.name)
print(goat1.voice())
print(goat1.walk())
print(goat1.eat())
print(goat1.get_milk())
print()

goat2 = Goat("Копыта", 60)
animals_dict[goat2.name] = goat2.weight
print(goat2.name)
print(goat2.voice())
print(goat2.walk())
print(goat2.eat())
print(goat2.get_milk())
print()

duck1 = Duck("Кряква", 3)
animals_dict[duck1.name] = duck1.weight
print(duck1.name)
print(duck1.voice())
print(duck1.walk())
print(duck1.eat())
print(duck1.lay_eggs())
print()

print(f"Общий вес всех животных: {sum(animals_dict.values())}кг\n")

for animal, weight in animals_dict.items():
    if weight == max(animals_dict.values()):
        print(f"Самое тяжелое животное: {animal}({weight}кг)")

