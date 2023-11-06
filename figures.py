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

# Треугольник
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

# Круг
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

# Четырёхугольник
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

error = ValueError # Обработка ошибки

while True:
    try:
        num_figures = int(input("Сколько фигур нужно? "))
        if num_figures <= 0:
            raise error
        break
    except error:
        print("Введите положительное целое число")
figures = []
for _ in range(num_figures):
    while True:
        try:
            figure_type = int(input("Введите тип фигуры (1 - треугольник, 2 - круг, 3 - четырехугольник): "))
            if figure_type == 1 or figure_type == 2 or figure_type == 3:
                pass
            else:
                raise error
            break
        except error:
            print("Введите 1, 2 или 3")
    
    if figure_type == 1:
        while True:
            try:
                base = float(input("Введите основание треугольника: "))
                if base <= 0:
                    raise error
                height = float(input("Введите высоту треугольника: "))
                if height <= 0:
                    raise error
                break
            except error:
                print("Введите положительное число")
        figure = Triangle(base, height)
        figures.append(figure)
    elif figure_type == 2:
        while True:
            try:
                radius = float(input("Введите радиус круга: "))
                if radius <= 0:
                    raise error
                break
            except error:
                print("Введите положительное число")
        figure = Circle(radius)
        figures.append(figure)
    elif figure_type == 3:
        while True:
            try:
                side1 = float(input("Введите длину первой стороны четырехугольника: "))
                if side1 <= 0:
                    raise error
                side2 = float(input("Введите длину второй стороны четырехугольника: "))
                if side2 <= 0:
                    raise error
                break
            except error:
                print("Введите положительное число")
        figure = Quadrilateral(side1, side2)
        figures.append(figure)

# Сортировка фигур по площади
figures.sort(key=lambda x: x.calculate_area())

# Создание таблицы и добавление заголовка
table = PrettyTable()
table.field_names = ["Фигура", "Площадь"]

# Добавление строк в таблицу
for figure in figures:
    table.add_row([type(figure).__name__, figure.calculate_area()])

# Вывод таблицы
print(table)