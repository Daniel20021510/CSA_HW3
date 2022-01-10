import enum
import typing
from random import randint

from functions.my_random import random_string
from functions.vovels import count_vowels


class PlantType(enum.Enum):
    TREE = 1
    BUSH = 2
    FLOWER = 3


class Plant:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def read_input(input_file) -> typing.Optional['Plant']:
        line = input_file.readline()
        plant_type = int(line)
        plant_type = PlantType(plant_type)
        if plant_type == PlantType.TREE:
            return Tree.read_input(input_file)
        elif plant_type == PlantType.BUSH:
            return Bush.read_input(input_file)
        elif plant_type == PlantType.FLOWER:
            return Flower.read_input(input_file)
        else:
            print("Error: Unknown plant type")
            return None

    @staticmethod
    def random_plant():
        plant_type = randint(1, 3)
        print(plant_type)
        plant_type = PlantType(plant_type)
        if plant_type == PlantType.TREE:
            return Tree.random_plant()
        elif plant_type == PlantType.BUSH:
            return Bush.random_plant()
        elif plant_type == PlantType.FLOWER:
            return Flower.random_plant()
        else:
            return None

    def vowels_per_size(self):
        return count_vowels(self.name) / len(self.name)

    def __str__(self):
        return f"name - {self.name}, vowels per size = {self.vowels_per_size()}, "


class Tree(Plant):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return "Tree:" + super().__str__() + f"age {self.age}"

    @staticmethod
    def random_plant() -> 'Tree':
        name = random_string(randint(1, 15))
        age = randint(1, 1000)
        print(name, age)
        return Tree(name, age)

    @staticmethod
    def read_input(input_file):
        line = input_file.readline().split()
        if len(line) != 2:
            print("Error: Incorrect tree")
            return
        name = line[0]
        age = int(line[1])
        return Tree(name, age)


class FloweringMonth(enum.Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Bush(Plant):
    def __init__(self, name: str, flowering_month):
        super().__init__(name)
        self.flowering_month = flowering_month

    def __str__(self):
        return "Bush:" + super().__str__() + f"{self.flowering_month}"

    @staticmethod
    def random_plant() -> 'Bush':
        name = random_string(randint(1, 15))
        flowering_month = randint(1, 12)
        print(name, flowering_month)
        flowering_month = FloweringMonth(flowering_month)
        return Bush(name, flowering_month)

    @staticmethod
    def read_input(input_file):
        line = input_file.readline().split()
        if len(line) != 2:
            print("Error: Incorrect bush")
            return
        if int(line[1]) < 1 or int(line[1]) > 12:
            print("Error: Incorrect bush flowering month")
            exit(0)
        name = line[0]
        flowering_month = FloweringMonth(int(line[1]))
        return Bush(name, flowering_month)


class FlowerType(enum.Enum):
    HOME = 1
    GARDEN = 2
    WILD = 3


class Flower(Plant):
    def __init__(self, name: str, flower_type):
        super().__init__(name)
        self.flower_type = flower_type

    def __str__(self):
        return "Flower:" + super().__str__() + f"{self.flower_type}"

    @staticmethod
    def random_plant() -> 'Flower':
        name = random_string(randint(1, 15))
        flower_type = randint(1, 3)
        print(name, flower_type)
        flower_type = FlowerType(flower_type)
        return Flower(name, flower_type)

    @staticmethod
    def read_input(input_file):
        line = input_file.readline().split()
        if len(line) != 2:
            print("Error: Incorrect flower")
            return
        if int(line[1]) < 1 or int(line[1]) > 3:
            print("Error: Incorrect flower type")
            exit(0)
        name = line[0]
        flower_type = FlowerType(int(line[1]))
        return Flower(name, flower_type)
