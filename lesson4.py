# l = [44, 5, 7, 777, 888, 9]
#
# sum_ = 0
#
# print('Hello')
#
#
# def func():
#     global sum_
#
#     for i in l:
#         if i >= 7:
#             sum_ += i
#
#     print(sum_)
#
#
# func()
#
# print('end')

# try:
#     int('ddd')
#     # print(5/0)
#     # print(ksdfhkj)
#     print('dddd')
# except NameError as err:
#     print(err)
# except ZeroDivisionError as err:
#     print(err)
# except TypeError as err:
#     print(err, 'TypeError')
# except Exception as err:
#     print(err)
# else:
#     print('alright')
# finally:
#     print('finally')
#
# print('end')


# l = [i for i in range(50000000)]
#
# input()

# gen = (i for i in range(5))
#
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
#
# for i in gen:
#     print(i)
#
# for i in gen:
#     print(i)

# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('Max')
#
# # print(next(g))
# # print('jhdfkjhdf')
# # print(next(g))
# # print('jhdfkjhdf')
# # print(next(g))
#
# print(next(g))
# print(next(g))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'Hello World!'
#
#
# g = gen()
#
#
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as e:
#     print(e)

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team-1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team-2'
#
#
# teams = [gen1(8), gen2(5)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

# class Range:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration

# def my_range(length):
#     counter = 0
#
#     while counter < length:
#         yield counter
#         counter += 1
#
#
# for i in my_range(8):
#     print(i)


# file = open('1.txt')
# print(file.read())
# file.close()

# try:
#     file = open('1.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'r') as file:
#         # print(file.read(15))
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readlines())
#         for line in file:
#             print(line)
# except Exception as e:
#     print(e)


# try:
#     with open('1.txt', 'w') as file:
#         # file.write('Python\n')
#         file.writelines(['python\n', 'java\n'])
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'a') as file:
#         # file.write('Python\n')
#         file.write('js\n')
# except Exception as e:
#     print(e)

# try:
#     with open('2.txt', 'x') as file:
#         pass
#         # file.write('Python\n')
#         # file.write('js\n')
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'r+') as file:
#         # file.write('Python\n')
#         # file.write('js\n')
#         print(file.readline())
#         file.seek(0)
#         file.write('css\n')
# except Exception as e:
#     print(e)

# try:
#     with open('1.txt', 'w') as file:
#         print('Hello World',file=file)
# except Exception as e:
#     print(e)

import json
import pickle
from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int, 'status': bool})

user: User = {
    'name': 'Max',
    'age': 15,
    'status': True
}


# try:
#     with open('user.txt', 'w') as file:
#         json.dump(user, file)
# except Exception as e:
#     print(e)
# #
# try:
#     with open('user2.data', 'wb') as file:
#         pickle.dump(user, file)
# except Exception as e:
#     print(e)

# try:
#     with open('user.txt', 'r') as file:
#         user_from_file: User = json.load(file)
#         print(user_from_file['name'])
# except Exception as e:
#     print(e)
#
# try:
#     with open('user2.data', 'rb') as file:
#         user_from_file:User = pickle.load(file)
#         print(user_from_file['name'])
# except Exception as e:
#     print(e)

class User:
    def __init__(self, name: str, age: int, status: bool):
        self.name = name
        self.age = age
        self.status = status

    @staticmethod
    def hello():
        print('hello')


users: list[User] = [
    User('Max', 15, True),
    User('Karina', 15, True)
]

# try:
#     with open('user3.data', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as e:
#     print(e)


# try:
#     with open('user3.data', 'rb') as file:
#         users_from: list[User] = pickle.load(file)
#         print(users_from)
#         print(users_from[0].name)
#         users_from[0].hello()
# except Exception as e:
#     print(e)
# p = '54'
#
# match p:
#     case '4':
#         print('hello')
#     case '5':
#         print('5')
#     case '6':
#         print('6')
#     case _:
#         print('nope')

# a = ['top', 20]
#
# match a:
#     case 'left' as action, value:
#         print(action, '1')
#         print(value)
#     case 'right'|'top' as action, 20 as value:
#         print(action, '2')
#         print(value)
#     case action,:
#         print(action, '3')


user_dict = {
    'name': 'Max',
    'age': 15,
    'status': True
}


class User:
    __match_args__ = ('name', 'age', 'status')

    def __init__(self, name: str, age: int, status: bool):
        self.name = name
        self.age = age
        self.status = status


user_class = User('Karina', 25, False)


#
# match user:
#     case {'name':str(name), 'age':int(age), 'status':bool(status)}:
#         print(name, '1')
#         print(age)
#         print(status)
#     case {'name': int(name), 'age': int(age), 'status': bool(status)}:
#         print(name, '2')
#         print(age)
#         print(status)


# def matcher(source: User | dict):
#     if isinstance(source, User):
#         print(source.name)
#     elif isinstance(source, dict):
#         print(source['name'])
#
#
# matcher(user_class)


def matcher(source: User | dict):
    match source:
        case User(name, _, _):
            print(name)
        case {'name': name}:
            print(name)


# matcher(user_dict)
matcher(user_class)
