# # destructorization
#
# # tuple1 = (1, 2,3)
# #
# # a,b,c = tuple1
# #
# # print(a)
#
# # a = 5
# # b = 6
# # b, a = a, b
# #
# # print(a)
# # print(b)
#
#
# # l = [3, 4, 5, 6, 7, 8, 9]
# #
# # a, b, *_, z = l
# #
# # print(a)
# # print(b)
# # print(z)
# #
# # print(_)
#
# # l = 2, 3, 4, 5
# #
# # a, *_, b = l
# #
# # print(a)
# # print(b)
# # print(_)
#
#
# # def func(a, b, c=5, *args, **kwargs):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(args)
# #     print(kwargs)
# #
# #
# # func(4, 5, 8)
#
# def main(arg1='a', arg2='b', arg3='c'):
#     return arg1, arg2, arg3
#
#
# d = {
#     'arg1': 55,
#     'arg3': 77,
#     'arg2': 66,
#
# }
#
#
# # print(main(arg1=d['arg1'], arg2=d['arg2'], arg3=d['arg3']))
# # print(main(**d))
# #
# # dict2 = {**d, 'asd':99}
# #
# # print(dict2)
# #
# # l = [1,2,3,4]
# #
# # l2 = [*l, 1,2,3]
# #
# # print(l2)
#
#
# # decorators
#
# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
#
# def decor2(func):
#     def inner(*args, **kwargs):
#         print('-' * 20)
#         func(*args, **kwargs)
#         print('-' * 20)
#
#     return inner
#
#
# @decor2
# @decor
# def greeting(name):
#     print(f'Hello, {name}')
#
#
# @decor
# def sum_of(a, f, h):
#     print(sum([a, f, h]))
#
#
# sum_of(1, 2, 3)
#
# # inner = decor(greeting)
# # inner()
#
#
# greeting('Max')

# import time
#
#
# def time_decor(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print(time.time() - start)
#


#     return inner
#
# @time_decor
# def smth():
#     for i in range(1000000000):
#         ...
#         # pass
#
# smth()

# a = 5
# # scope
#
# for i in range(20):
#     print(i)
#
# print(i)
#
# print(globals())


# name ='Max'
#
# def a():
#     # name = 'Vasia'
#     # print(locals())
#
# a()
#
# print(name)
# print(globals())


# name ='Max'

# def a():
#     global name
#     name = 'Vasia'
#     print(locals())
#
# a()

# name = 'Max'
#
#
name = 'dddd'


def a():
    # name = 'Vasia'

    def b():
        # name = 'Petia'
        # print(name)
        def c():
            # global name
            print(name)

    b()
    # print(name)


a()

#
#
# a()
# print(name)

# closure

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# counter1 = counter()
# counter2 = counter()
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter2(), 'counter2')
# print(counter1())
# print(counter2(), 'counter2')
# print(counter1())
# print(counter1())


# aaa = 6
#
#
# def plus_one():
#     global aaa
#     aaa = 88
#     print(aaa + 1)
#
#
# plus_one()
# print(aaa)

# const asd = (a,b,c) => a+b+c
#
# asd = lambda a, b, c: a + b + c
#
# print(asd(1, 2, 3))
# l = [1, 2, 3, 4]
# m = list(map(lambda x: x + 1, l))
# fil = list(filter(lambda x: x % 2 == 0, l))
#
# print(fil)

# users = [
#     {'name': 'Max', 'age': 25},
#     {'name': 'Karina', 'age': 19},
#     {'name': 'Albina', 'age': 35},
# ]
#
# users.sort(key=lambda item:item['name'])
#
# print(users)


# def func(name: str):
#     print(name)
#
#
# func(555)

from typing import TypedDict, Any, Callable

# MyType = str | int | list[str]
#
#
# def func(names: tuple[str, ...]) -> MyType | None:
#     print(names)
#     return {1,2,3}
#
#
# func(('1', '1', '1'))

User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)

user: User = {"age": 25, "name": 'Max'}


def counter() -> Callable[[str, int], int]:
    count = 0

    def inner(a: str, b: int) -> int:
        nonlocal count
        count += 1
        return count

    return inner
