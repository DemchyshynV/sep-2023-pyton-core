'''
kjshfkshfksjf
ksdfhkshfkjs
jsdfhkshdfk
'''

"""
sjdfhskfhjskf
sdfjhskfhsf
ksdfksfhk

"""

# ksjdhfksfhksjh

i = 5
f = 1.3
b = True  # False
s = 'hello world'  # "hello world"
n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))

# print('hello world')
# print(1, 2, 3, 4, 5, sep='-', end='')

# a = b = c = 10
#
# print(a, b, c)

asd = 1.5

# int1 = int(asd)
# print(type(int1))
# print(int1)

# int2 = int('1ggg23')
#
# print(type(int2))
# print(int2)

# int()
# float()
# bool()
# str()


# i = 1
# # i ++
# i += 1
# i -= 1
# i *= 1
# i /= 1
# i = i +1

a = 6
b = 5

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# print(25**25)
# print(2525**2525)


# inp = input('Enter num: ')
#
# print(inp)

# <
# >
# <=
# >=

# a = 6
# b =9
#
# print(a==b, a is b)
# print(a!=b, a is not b)

# print(isinstance('dddd', str))
# a = 7
# b = 4
# if a > b and b == 5 or a == 7:
#     print('a>b')
# elif a == b:
#     print('a==b')
# else:
#     print('a<b')

# num = int(input('Enter num: '))
#
# asd = 'yes' if num > 5 else 'no'
#
# print(asd)

# list

# l = [1, 2, 3, 4, 5]
# l2 = [1, 2, 3, 4, 5]

# print(l)
# l[2] = 55
# print(l[2])
# print(l[-2])
# # print(l[55])
# del l[2]
# print(l)


# l.append(666)
# l.insert(1,55)
# pop = l.pop()
# pop = l.pop(0)
# print(pop)
# print(l)
# l.extend(l2)
# l = [1, 2, 3, 4, 5,2,4]
# l.remove(2)
# print(l)

# l +=l2
#
# print(l)


# print(l.index(4, 5))


# l.reverse()
#
# print(l)

# print(l.count(4))

# l.sort(reverse=True)
#
# print(l)
#
# l = [1, 2, 3, 4, 5,2,4]
# #
# # print(l[::-2])
#
# l2 = l[::]
#
# l2[0]=555
#
# print(l2)
#
# print(len(l2))

# Tuple

# my_tuple = (1, 2, 3, 4)
#
# l = list(my_tuple)
# print(my_tuple)
# print(my_tuple[1])
# # del my_tuple[3]
#
# print(l)

# dictionary

user = {
    'name': 'Max',
    'age': 15
}

# print(user['age'])
# del user['name']
# user['dddd']
# print(user.get('dddd', 1515))
# print(user)

# print(user.items())
# print(user.values())
# print(user.keys())
# pop = user.pop('name')
# print(pop)
# print(user)
# user['house'] = 25
# popitem = user.popitem()
# print(popitem)
# print(user)

# user.setdefault('age3', 255)
#
# # user.update({'street':'hdjshfjhsfg'})
# user |= {'street': 'hdjshfjhsfg'}
# print(user)


# s = {1, 2, 3, 4, 5, 1, 2, 3, 5}
# s1 = {}
# s1 = set()
# print(type(s1))
#
# print(s)

# s.add(99)
#
# s.remove(5)
# s.discard(22)
# print(s)

# s1 = {4,2,8,9,88}
# s2 = {2,4,9,5}
#
# # print(s1.issubset(s2))
# # print(s1.issuperset(s2))
# # print(s1.isdisjoint(s2))
# # print(s1.intersection(s2))
# print(s1.difference(s2))

name = 'Max'
age = 18
weight = 70.5

string = 'Hello, my name is Max, I`m 18 and my weight 70.5kg'
string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + 'kg'
string = 'Hello, my name is %s, I`m %d and my weight %fkg' % (name, age, weight)
string = 'Hello, my name is {}, I`m {} and my weight {}kg'.format(name, age, weight)
string = 'Hello, my name is {name}, I`m {age} and my weight {weight}kg'.format(age=age, name=name, weight=weight)
string = f'Hello, my name is {name}, I`m {age} and my weight {weight}kg'

print(string.isdigit())

print(['    ddfjhdgf    '.strip()])
print(['    ddfjhdgf    '.lstrip()])
print(['    ddfjhdgf    '.rstrip()])
print(['aaa    ddfjhdgf    aaa'.strip('a ')])

# print('ss-d'.split('-'))
# print('ss-d'.partition('-'))

print(string[5])

print(string.count('l'))
print(string.endswith('kg'))
print(string.startswith('kg'))

print(''.join(['h', 'e', 'l', 'l', 'o']))

print(min(1, 2, 3, 4, -2))
print(max(6, 7, 3, 6))
print(sorted([1, 2, 3, 4, 5], reverse=True))
print(pow(2, 66))
print(sum([1, 2, 3, 4, 5, 6]))
print(string)

# def func(a, b, c):
#     print(a, b, c)
# def func(a, b, c, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
#
# func(1, 2, 3, 5, 6, 88, name='Max', age=15)

# i = 5

# while i > 0:
#     i -= 1
#     if i == 2:
#         break
#     print(i)
# else:
#     print('finish')

# l = [2, 5, 3, 5, 7, 8]
#
# # for i,v in enumerate(l):
# #     print(f'{i} -- {v}')
#
# for i in range(5, 10, 2):
#     print(i)

# for k, v in user.items():
#     print(f'{k} -- {v}')

# list comprehension

# l = [i ** 2 for i in range(10) if i % 2 == 0 and i != 0]
# l = ['even' if i % 2 == 0 else 'odd' for i in range(10)]


# dict1 = {'Name': 'max', 'AgE': 15}
#
# dict2 = {k.lower(): v for k, v in dict1.items()}
# print(dict2)

l = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]

# res = [i for j in l for i in j]

res = []
for j in l:
    for i in j:
        res.append(i)

print(res)

