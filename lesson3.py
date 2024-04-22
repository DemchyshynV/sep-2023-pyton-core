# class User(object):
# class User:
#     count = 1


# print(User.count)

# user1 = User()
# user2 = User()
#
# User.count = 55
# print(User.count)
# print(user2.count)


# class User:
#     __slots__ = ('__name', '_age', 'status')
#     count = 1
#
#     def __init__(self, name, age, status):
#         self.__name = name
#         self._age = age
#         self.status = status
#
#     def get_name(self):
#         return self.__name
#
#     def __str__(self):
#         return f'{self.__name} is {self.status}'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# user = User("Max", 15, True)
# user2 = User("Kira", 20, True)
#
# user.house = 25
#
# # print(user.__get_name())
# # print(user._age)
# # print(user.status)
#
# # print(user._User__name)
# users = [user, user2]
# print(users)
# print(user.house)
# # print(user2.house)

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def greeting(self):
#         print(f"Welcome to Python! From Car")
#
#
# class Greeting:
#
#     def greeting(self):
#         print(f"Welcome to Python! from Greeting")
#
#
# class ElectricCar(Car, Greeting):
#     def __init__(self, brand, capacity):
#         super().__init__(brand)
#         self.capacity = capacity
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def greeting(self):
#         Greeting.greeting(self)
#
#
# car = ElectricCar("BMW", 10000)
#
# print(car)
#
# car.greeting()


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         if self.__name == 'Kira':
#             del self.__name

# name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
# user = User("Max")
# print(user.name)
# del user.name
# print(user.name)
# user.name = "Kira"
# print(user.name)
# del user.name
# print(user.name)
# print(user.name)
# print(user.name)
# del user.name
# print(user.name)
#
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * self.c
#
#     def perimeter(self):
#         return 2 * (self.a + self.b + self.c)
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * (self.a + self.b)
#
#
# shapes: list[Shape] = [
#     Triangle(1, 2, 3),
#     Rectangle(3, 4)
# ]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())


# class User:
#     counter = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         print(self.name)
#
#     @classmethod
#     def counter_inc(cls):
#         cls.counter += 1
#
#     @staticmethod
#     def greeting():
#         print("Hello")
#
#
# user = User("max", 15)
#
# user.get_name()
# User.counter_inc()
# User.greeting()
#
# user.greeting()
#
# print(User.counter)


class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


user = User(1, 2)

user2 = User(5, 5)


# print(id(user))
# print(id(user2))
#
# print(user.a)
# print(user.b)

# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, other):
#         self.value *= other
#
#
# prod = Prod(5)
#
# print(prod.value)
# prod(6)
# print(prod.value)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} {self.age}'
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __len__(self):
#         return len(self.name)
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#
# max_ = User("Max", 15)
# karina = User("Karina", 30)
#
# print(max_ + karina)
# print(max_ - karina)
#
# print(len(max_))


class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


arr = Array(1, 2, 3, 4)

arr_map = arr.map(lambda x: x * 2)
arr_filter = arr.filter(lambda x: x>2)

print(arr_map)
print(arr_filter)

# print(arr)
# print(arr[2])
# arr[2] = 55
# del arr[2]
# print(arr[2])
#
# print(arr)
