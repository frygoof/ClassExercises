#Пример 1: Создание классов
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Меня зовут {self.name} и мне {self.age} лет.")
# person1 = Person("Иван", 30)
# person1.introduce()


#Пример 2: Создание экземпляров класса, Доступ к атрибутам
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Меня зовут {self.name} и мне {self.age} лет.")
# person1 = Person("Иван", 30)
# person2 = Person("Мария", 25)
# print(f"{person1.name} имеет возраст {person1.age} лет.")
# print(f"{person2.name} имеет возраст {person2.age} лет.")
# person1.introduce()
# person2.introduce()


#Пример 3: Встроенные атрибуты класса
# class Product:
#     """Класс для представления продукта"""
#     count = 0
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1
#     def display_count(self):
#         print('Всего продуктов: %d' % Product.count)
#     def display_product(self):
#         print('Название: {}. Цена: ${}'.format(self.name, self.price))
# print("Product.__doc__:", Product.__doc__)
# print("Product.__name__:", Product.__name__)
# print("Product.__module__:", Product.__module__)
# print("Product.__bases__:", Product.__bases__)
# print("Product.__dict__:", Product.__dict__)


#Пример 4: Удаление объектов (сбор мусора)
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def start_engine(self):
#         print(f"The {self.make} {self.model}'s engine is running.")
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(f'{class_name} destroyed')
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Civic")
# car3 = Car("Ford", "Fusion")
# car1.start_engine()
# car2.start_engine()
# car3.start_engine()
# del car1
# del car2


#Пример 5: Пример наследования класса в Python
# class Animal:
#     def __init__(self, species):
#         self.species = species
#     def speak(self):
#         print(f"Особь {self.species} издаёт звук.")
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__("Собака")
#         self.name = name
#         self.breed = breed
#     def speak(self):
#         print(f"{self.name} породы {self.breed} гавкает!")
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__("Кот")
#         self.name = name
#         self.color = color
#     def speak(self):
#         print(f"{self.name} по кличке {self.color} мяукает!")
# dog = Dog("Рэкс", "Золотистый Ретривер")
# cat = Cat("Барсик", "Серик")
# dog.speak()
# cat.speak()


#Пример 6: Переопределение методов
# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#     def area(self):
#         import math
#         return math.pi * self.radius**2
# rectangle = Rectangle("Прямоугольник", 4, 5)
# circle = Circle("Круг", 3)
# print(f"Площадь {rectangle.name}: {rectangle.area()}")
# print(f"Площадь {circle.name}: {circle.area()}")


#Пример 7: Популярные базовые методы
# class MyClass:
#     def __init__(self, arg1, arg2):
#         self.arg1 = arg1
#         self.arg2 = arg2
#     def __del__(self):
#         print(f"Удаление объекта с аргументами {self.arg1} и {self.arg2}")
#     def __repr__(self):
#         return f"MyClass({self.arg1}, {self.arg2})"
#     def __str__(self):
#         return f"MyClass объект с аргументами {self.arg1} и {self.arg2}"
# obj = MyClass(10, 20)
# print(repr(obj))
# print(str(obj))
# del obj


#Пример 8: Пример использования __add__
# class ComplexNumber:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"
#     def __add__(self, other):
#         real_sum = self.real + other.real
#         imaginary_sum = self.imaginary + other.imaginary
#         return ComplexNumber(real_sum, imaginary_sum)
# c1 = ComplexNumber(3, 4)
# c2 = ComplexNumber(1, 2)
# result = c1 + c2
# print(result)


#Пример 9: Приватные методы и атрибуты
# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         self.__account_number = account_number
#         self.__balance = initial_balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Пополнено {amount} тенге. Баланс: {self.__balance}")
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Снято {amount} тенге. Баланс: {self.__balance}")
#         else:
#             print("Недостаточно средств на счете.")
#     def get_balance(self):
#         return self.__balance
# account = BankAccount("123456789", 1000)
# account.deposit(500)
# account.withdraw(200)
# print("Текущий баланс:", account.get_balance())









