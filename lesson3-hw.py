# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
#
#   ###############################################################################
from typing import Self
from abc import ABC, abstractmethod


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other: Self):
        return self.area + other.area

    def __sub__(self, other: Self):
        return self.area - other.area

    def __eq__(self, other: Self):
        return self.area == other.area

    def __ne__(self, other: Self):
        return self.area != other.area

    def __lt__(self, other: Self):
        return self.area < other.area

    def __gt__(self, other: Self):
        return self.area > other.area

    def __len__(self):
        return (self.x + self.y) * 2


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
#

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        return cls.__count


class Prince(Human):
    def __init__(self, name, age, shoe):
        super().__init__(name, age)
        self.shoe = shoe

    def find_cinderella(self, cinderellas: list[Cinderella]) -> None:
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe:
                print(cinderella)
                return


cinderellas_list: list[Cinderella] = [
    Cinderella('Kamila', 65, 52),
    Cinderella('Albiba', 30, 32),
    Cinderella('Karina', 25, 35),
    Cinderella('Nikol', 18, 36),
]


# prince = Prince("Max", 20, 35)
# prince.find_cinderella(cinderellas_list)
# print(Cinderella.get_count())
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Book:  {self.name}')


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Magazine: {self.name}')


class Main:
    __printable_list:list[Printable] = []

    @classmethod
    def add(cls, item):
        if isinstance(item, Printable):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_books(cls):
        for book in cls.__printable_list:
            if isinstance(book, Book):
                book.print()

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.__printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()


Main.add(Book('Book1'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book3'))
Main.add(Magazine('Magazine3'))
Main.add(Book('Book4'))
Main.add(Magazine('Magazine1'))
Main.add(Book('Book2'))
Main.add(Magazine('Magazine4'))


Main.show_all_magazines()
print('-----------------------------')
Main.show_all_books()

