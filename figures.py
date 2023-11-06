from abc import ABC, abstractmethod
import math
from operator import itemgetter
from prettytable import PrettyTable

class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def display(self):
        pass


class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        return self.base + 2 * math.sqrt((self.base / 2)**2 + self.height**2)
    
    def display(self):
        print("Треугольник:")
        print(f"Основание: {self.base}")
        print(f"Высота: {self.height}")
        print(f"Периметр: {self.calculate_perimeter()}")
        print(f"Площадь: {self.calculate_area()}")
        print()


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def display(self):
        print("Круг:")
        print(f"Радиус: {self.radius}")
        print(f"Длина окружности: {self.calculate_perimeter()}")
        print(f"Площадь: {self.calculate_area()}")
        print()


class Quadrilateral(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    def calculate_area(self):
        return self.side1 * self.side2
    
    def calculate_perimeter(self):
        return 2 * (self.side1 + self.side2)
    
    def display(self):
        print("Четырехугольник:")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Периметр: {self.calculate_perimeter()}")
        print(f"Площадь: {self.calculate_area()}")
        print()


num_figures = int(input("Сколько фигур нужно? "))

figures = []
for _ in range(num_figures):
    figure_type = input("Введите тип фигуры (1 - треугольник, 2 - круг, 3 - четырехугольник): ")
    
    if figure_type == "1":
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        figure = Triangle(base, height)
        figures.append(figure)
        Triangle.display(figure)
    elif figure_type == "2":
        radius = float(input("Введите радиус круга: "))
        figure = Circle(radius)
        figures.append(figure)
        Circle.display(figure)
    elif figure_type == "3":
        side1 = float(input("Введите длину первой стороны четырехугольника: "))
        side2 = float(input("Введите длину второй стороны четырехугольника: "))
        figure = Quadrilateral(side1, side2)
        Quadrilateral.display(figure)

# Сортировка фигур по площади
figures.sort(key=lambda x: x.area())

# Создание таблицы и добавление заголовка
table = PrettyTable()
table.field_names = ["Фигура", "Площадь"]

# Добавление строк в таблицу
for figure in figures:
    table.add_row([type(figure).__name__, figure.area()])

# Вывод таблицы
print(table)
