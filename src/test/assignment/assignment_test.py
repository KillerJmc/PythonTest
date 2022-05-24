# encoding:utf-8
import copy
import importlib
import os
import random
import shutil
import time

# global variables
cwd = os.getcwd()


# def
def new_line():
    print("-------------------------------------------")


def new_2line():
    print()
    new_line()


def print_all(*objs):
    for o in objs:
        print(o)


def out(s, path):
    with open(path, 'w') as f:
        f.write(s)


def read(path):
    with open(path, 'r') as f:
        return f.read()


def delfs(*fs):
    for f in fs:
        if not os.path.isdir(f):
            os.remove(f)
        else:
            shutil.rmtree(f)


x = y = 123
print(x, y)
new_line()

a, b, c = 1, 2, 3
print(a, b, c)
new_line()

# variables swap
a, b = b, a
print(a, b)
new_line()

# Python doesn't exist constance (all the vars whose like const can be changed all the cases)
MAX_LENGTH = 100
MAX_LENGTH = 3459
print(MAX_LENGTH)
new_line()

# numbers
print(8 / 4)
print(8 // 4)
print(8 + 2.0)
# bigger than long, can be infinite length
# 无限长 [ˈɪnfɪnət]
print(2 ** 100)
new_line()

# divide result and mod
print(divmod(8, 5))
new_line()

# 2
print(0B101)
print(0b101)
# 8
print(0O10)
print(0o10)
# 16
print(0xff)
print(0x255)
new_line()

# type conversion
print(int(2348.344))
print(int("3323344"))
print(float("3323"))
print(str(233))
# si she wu ru (rounding)
print(round(3.5993))
new_line()

# time
print(time.time())
t = int(time.time())
totalMinutes = t // 60
totalHours = totalMinutes // 60
totalDays = totalHours // 24
print(totalDays)
totalYears = totalDays // 360
print(totalYears)
new_line()

a = True
print(a + 1)
new_line()

# logical or, and, not
print(True or 3)
print(False or 3)
print(True and 3)
print(False and 3)
print(not True)

#优先级：() > not > and > or
# -false- or -0- or -4- or -6- or -9-
# -0- or 4 or 6 or 9
# 4 or 6 or 9
# 也可以从左往右，特殊情况按优先级提前计算后面的（如本题：第一个是false, false or (0 and 1) -> false or 0 -> 0）
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
print(4 or 6 or 9)
new_line()

a = 1000
b = 1000
# "is" (pointer) is more efficient than "=="(equals fn)
print(a == b)
print(a is b)
new_line()

# ord: char -> Unicode
print(ord('搞'))
# chr: Decimal system(十进制) -> char
print(chr(88))

a = 'haahha'
a2 = "hsdowe"
a3 = """
I'm happy to see this
Oksir!
"""
print(a, a2, a3)
new_line()

print(len(a3))
a4 = ''
print(len(a4))
a5 = "哈哈"
print(len(a5))
new_line()

# append
print('h'       'p')
print('h''p')
print('h' + 'p')
print('hp' * 3)
new_line()

print("cc", end="")
print("aa", end="*")
print("bb", end="*")
print()
new_line()

"""
name = input("请输入名字：")
print(name)
new_line()
"""

a = 'abcdefghijklmnopqrstuvwxyz'
print(a[0])
# Reverse
print(a[-25])
new_line()

# return new str
print(a.replace('c', "66666666666666"))
new_line()

# slice (切片)
print(a[:])
print(a[2])
# [2, 6) means that the index is 2, 3, 4, 5
print(a[2:6])
print(a[2:123908312938921])
print(a[:2])
print(a[2:])

# step
print(a[2:6:1])
print(a[2:6:2])
print(a[-3:])
print(a[-8:-3])
print(a[::-1])
print(a[::-2])

print("To be or not to be"[::-1])
print(("jmc" * 5)[::3])
new_line()

# split
a = 'To be or not to be'
print(a.split())
print(a.split("be"))
# only a "be"
print(a.split("be", 1))
new_line()

# join
a = a.split()
print("*".join(a))
print("".join(a))
print(" ".join(a))
new_line()

"""
a = ''
t1 = time.time()
for i in range(1000000) :
    a += 'jmc'
t2 = time.time()
print(str(t2 - t1) + 's')

l = []
t1 = time.time()
for i in range(1000000):
    l.append('jmc')
t2 = time.time()
print(str(t2 - t1) + 's')
new_line()
"""

l1 = [1, 2, 'haha', 2]
l1.append('what')
print(l1)

l0 = [1, 2, 3]
l0[0] = 'this'
print(l0)

l2 = list('what the fuck?')
print(l2)
new_line()

a = range(10)
print(type(a))
print(list(a))
new_line()

print(list(range(0, 10, 1)))
print(list(range(0, 11, 2)))
print(list(range(3, 20, 2)))
print(list(range(-10, -33, -1)))
new_line()

# 1~99 * 2
print([x * 2 for x in range(100) if x % 9 == 0])
new_line()

# add at last
print(id(l1))
l1.append('DD')
print(id(l1))
print(l1)
new_line()

# rebuild and return a new list
print(id(l1))
l3 = l1 + ['JC']
print(id(l3), '\n', l3)
new_line()

# use extend fn to substitute the method above
print(id(l1))
l1.extend(['MP'])
print(id(l1), '\n', l1)
new_line()

# insert
l1.insert(2, 'hello')
print(l1)
new_line()

# repeat
print(id(l1))
print(id(l1 * 3))
print(l1 * 3)
new_line()

# delete
print(id(l1))
del (l1[3])
print(id(l1), '\n', l1)
new_line()

# delete and return
# delete the last one
l3 = l1
print(l3)

i = l3.pop()
print(i, l3)

# delete a specific one
i = l3.pop(4)
print(i, l3)

# delete a specific element who appears first
print(id(l3))
l3.remove('hello')
print(id(l3))
print(l3)
new_line()

# index
a = [10, 20, 30, 40, 50, 20, 30, 20, 30]
print(a)
# search the first one in the whole array
print(a.index(20))
# search from index 3.
print(a.index(20, 3))
# serch between index 0 and 2
print(a.index(20, 0, 2))
new_line()

# other
print(a.count(20))
# print(a.count(20) is not 0)
print(len(a))
print(20 in a, 0 in a)
print(20 in [10, 30, 40])
print(30 in [10, 30, 40])
new_line()

# list slice
a = list(range(10, 110, 10))
print(a)
print(a[0:4])
print(a[0:4:2])
print(a[1::2])
# the last one is -1
print(a[-5:-3])
print(a[::-1])

# list sort
a = [20, 10, 30, 40]
print(a)
print(id(a))
a.sort()
print(a)
print(id(a))

a.sort(reverse=True)
print(a)

random.shuffle(a)
print(a)

# return a new array
a = [20, 10, 30, 40]
print('\n', sorted(a))
print(sorted(a, reverse=True))
print(a)
new_line()

# return a reversed iterator
c = reversed(a)
print(c)
print(list(c))
print(list(c))
new_line()

# other
print(max(a))
print(min(a))
print(sum(a))
new_line()

l = [
    [1, 2, 3],
    [3, 4, 5]
]
print(l[0][2])

# tuple: an array which can't be modified(but can modify the changable objects inside it)
# quicker than list.
t = (10, 20, 30)
t = 10, 20, 30
print(type(t), "\n", t)
new_line()

# wrong
t = (20)
print(type(t))

# correct
t = (20,)
t = 20,
print(type(t))

# create
t = tuple(range(10, 110, 10))
t = tuple(list(range(10, 110, 10)))
print(t)

t = tuple('abcd')
print(t)
new_line()

# tuple has not sort fn
# it can only use sorted fn to sort
# other funcs are similar to list

# zip can iterate more than a list
# and end at the shortest one
t = zip([1, 2, 7], [3, 4, 8], [5, 6])
print(t)
print(list(t))
new_line()

# gernerate!
t = (x * 2 for x in range(6))
print(t)
print(tuple(t))
print(tuple(t))

t = (x * 2 for x in range(6))
for x in range(6):
    print(t.__next__(), end='')
print()
new_2line()

# dictionary <=> HashMap
d = dict(name='Jmc', age=18)
d = dict([('name', 'Jmc'), ('age', 18)])
d = {'name': 'Jmc', 'age': 18}
print(d)
new_line()

# zip
k = ['name', 'age', 'job']
v = ['Jmc', '18', 'stu']
dic = dict(zip(k, v))
print(d)

# values are null
d = dict.fromkeys(['a', 'b', 'c'])
print(d)
new_line()

# access
print(dic["age"])
print(dic.get('name'))
# get(key, if none return what)
print(dic.get('sjsjsj', "Doesn't exist!"))
# cause exception if not exist:
# print(dic['sjsjsj'])
new_line()

# list
# transfer to a list which has some tuples
print(dic.items())
print(dic.keys())
print(dic.values())
print(len(dic))
# if a key is in the dic
print('name' in dic)
new_line()

# add
dic['location'] = 'China'
dic['sex'] = 'man'
print(dic)
new_line()

# modify
dic['age'] = 20
print(dic)
new_line()

# del
del (dic['sex'])
print(dic.pop('location'))
print(dic)
new_line()

# update
dic2 = dict(name='JCC', sex='woman')
dic.update(dic2)
print(dic)
new_line()

# clear
print(dic2)
dic2.clear()
print(dic2)
new_line()

# random pop an element
for i in range(len(dic)):
    print(dic.popitem())
    print(dic)
new_line()

# xulie unpack
x, y, z = 10, 20, 30
x, y, z = (10, 20, 30)
(x, y, z) = (10, 20, 30)
[x, y, z] = [10, 20, 30]
print(x, y, z)
a, b, *c = 1, 2, 3, 4
print(a)
print(b)
print(c)

k = ['name', 'age', 'job']
v = ['Jmc', '18', 'stu']
d = dict(zip(k, v))
print(d)

# default unlock keys
a, b, c = d
print(a, b, c)
a, b, c = d.values()
print(a, b, c)
a, b, c = d.items()
print(a, b, c)
new_line()

# practice
""" 姓名 年龄 薪资 城市 """
p1 = {'name': 'Jmc',
      'age': 18,
      'salary': 8000,
      'city': 'FuJian'}
p2, p3, p4 = copy.deepcopy(p1), \
             copy.deepcopy(p1), \
             copy.deepcopy(p1)
p2['name'], p3['name'], p4['name'] \
    = 'Jmd', 'Jme', 'Jmf'
l = [p1, p2, p3, p4]
print(l)
new_line()

# get 2nd row's name
print('\n', l[1].get('name'))
new_line()

# print all names
for i in range(len(l)):
    print(l[i].get('name'), end='')
print()
# equals
for d in l:
    print(d.get('name'), end='')
new_2line()

for d in l:
    print(d)
new_line()

# set (jihe) <=> dic(HashMap)'s key
s1 = set([2, 3, 5])
print(s1)

s = {10, 20, 30, 'hello'}
print(s)

s.add('gg')
print(s)

s.remove(30)
print(s)

s.clear()
new_line()

# extra
a = {'he', 'she', 'it'}
b = {'you', 'they', 'it'}

print(a | b)
# eq: print(a.union(b))
print(a & b)
# eq: print(a.intersection(b))
# del the elements from a the same as in b
print(a - b)
# eq: print(a.difference(b))
new_line()

a = list(range(1, 11))
while a:
    # eq: x, a = a[0], a[1:]
    x, *a = a
    print(x, a)
new_line()

c = 9 ** 100
print('ok' if 3 < c < 6 else 'no!')

if c > 2 ** 100:
    print('too large!')
else:
    if 3 < c < 6:
        print('ok')
    elif c < 10:
        print('good')
    else:
        print('no!')
new_line()

sum_all = sum_even = sum_odd = 0
for x in range(1, 101):
    sum_all += x
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x

if not '':
    print("'' means null!")

print(
    """
100以内，数值总和为{0}，
奇数和为{1}，
偶数和为{2}。
""".format(sum_all, sum_odd, sum_even))
new_line()

# 99乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print('{0}*{1}={2}'.format(x, y, x * y), end='\t')
    print()
new_line()

# while has else as well
# do sth after end normally
for x in range(6):
    print(x, end=' ')
    # break
else:
    print('done')
new_line()

# 推导式
# list
a = [x * 2 for x in range(1, 5) \
     if x % 2 == 1]
print(a)

""" eq 
a = []
for x in range(1, 5):
    if x % 2 == 1:
        a.append(x * 2)
print(a)
"""

b = [(x, y) for x in range(1, 5) \
     for y in range(1, 5)]
print(b)

""" eq
b = []
for x in range(1, 5):
    for y in range(1, 5):
        b.append((x, y))
print(b)
"""
new_line()

# dic
str = "Hello everyone, I'm Jmc"
count = {c: str.count(c) \
         for c in str}
print(str)
print(type(count))
print(count)

""" eq 
str = str
count = {}
for c in str:
    count[c] = str.count(c)
print(count)
"""
new_line()

# set
d = {x ** x for x in range(1, 10)}
print(d)
new_line()

# tuple(iterator)
e = (x for x in range(1, 6))
print(e)
print(tuple(e))
print(tuple(e))

e = (x for x in range(1, 6))
for x in e:
    print(x, end=' ')
print()
print(tuple(e))
new_line()

a = [('a', '3'), ('b', '4'), ('c', '5')]
print(a)
for i1, i2 in a:
    print(i1 + '...' + i2)

new_line()


# def
def test01():
    """Use for returning str: test01"""
    return 'test01'


# func is an object, too!!!
print(type(test01))
print(id(test01))
help(test01)

c = test01
print(id(test01))
print(id(c))
print(type(c))
print(c())
new_line()

a = 3


def modify_a():
    # declare
    global a
    a = 30


modify_a()
print(a)
# print(locals())
# print(globals())
new_line()


# Java传递变量是直接传递内容
# py传递变量都只传递地址，但如果遇到不可变对象的改变（数字相加等），会重新创建一个新对象
# new_line()

# 浅拷贝：拷贝自身，但不拷贝子对象的内容，只拷贝子对象的引用
# 深拷贝：会连子对象的内容全都拷贝一份
# new_line()

# default parms
def f1(a, b, c=3, d=4):
    print(a, b, c, d)


f1(1, 2)
f1(1, 2, 5)
# wrong: def f(a = 1, b, c, d):*
new_line()

# named parms
f1(b=2, a=1)
new_line()


# changable parms
def f1(a, b, *c):
    print(a, b, c)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 4)


def f2(a, b, **c):
    print(a, b, c)


f2(1, 2)
f2(1, 2, x=3)
f2(1, 2, x=3, y=4)


# wrong: def f3(a, b, **c, *d)
def f3(a, b, *c, **d):
    print(a, b, c, d)


f3(1, 2, 3, 4, x=5, y=6)

# defs are object, too!!!
l = [f1, f2, f3]
l[0](1, 2, 3)
new_line()


# forced named parms
def f1(*a, b, c):
    print(a, b, c)


f1(1, b=2, c=3)
new_line()

# lambda
f = lambda a, b, c: a + b + c
print(f)
print(f(1, 2, 3))

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(g[0](1), g[1](2), g[2](3))
new_line()

# eval
eval("print('hello')")

a = 1
b = 2
c = eval("a + b")
print(c)

d = dict(a=100, b=200)
c = eval("a + b", d)
print(c)
new_line()


# 嵌套函数（内部函数）
# 只能在方法内部调用
def outer():
    print('outer...')
    a = 15

    def inner():
        print('inner...')
        nonlocal a
        print('外部的a值为{0}'.format(a))

        # 修改需要声明外层局部变量a（使用前声明）
        a = 13
        print('a被内部修改为', a)

    inner()


outer()
new_line()


# class
class T:
    def __init__(self):
        print('init...')

    def __new__(cls, *args, **kwargs):
        print('new...')
        return object.__new__(cls)


# 先创建对象再对其进行初始化
T()
new_line()


class Student:
    # class attributes
    school = 'JJSXX'

    # self must be the first parm
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{}的分数是：{}'.format(self.name, self.score))

    @staticmethod
    def do_nothing():
        pass


s1 = Student('Jmc', 88)
s1.print_score()
# get school
print(Student.school)

# attributes and fns
print(dir(s1))
# attributes
print(s1.__dict__)

# instansof in Java
print()
print(isinstance(s1, Student))
new_line()

print(type(Student))
print(id(Student))

stu = Student
s1 = stu(None, None)
print(s1)
new_line()


# class method and static method
class Emp:
    company = 'Oracle'

    # 类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
    @classmethod
    def printCompany(cls):
        print(cls.company)

    @staticmethod
    def static():
        print("static method...")


Emp.printCompany()
Emp.static()
new_line()


class Person:
    def __del__(self):
        print('销毁对象：{}'.format(self))


p = Person
p1 = p()
del p1
new_line()


# call fn makes class just like a fn
class Square:
    def __call__(self, num):
        return num ** 0.5


square = Square()
print(square(4))
new_line()


# python没有方法重载，定义多个同名方法，只有最后一个有效
# new_line()

# add fn to the class and modify the fn in the class
class Person:
    def work(self, *name):
        if len(name) == 1:
            print('{}在努力工作！'.format(name[0]))
        else:
            print('努力工作！')


def play_games(s):
    print('{}在玩游戏。'.format(s))


p = Person()
p.work('Jane')

# add method
Person.play = play_games
p.play()


# modify method
def work(self):
    print('老子今天不上班。')


Person.work = work
p.work()  # eq: Person.work(p)
new_line()


# private
class Emp:
    def __init__(self, name, tel):
        self.name = name
        # private attribute
        self.__tel = tel


e = Emp('Jmc', '138xxxx')
print(e.name)
# can not access: print(e.tel)
# the right way
print(e._Emp__tel)

print(e.__dict__)
new_line()


# property(set and get fn)
# normal
class Emp:
    def __init__(this, name, salary):
        this.name = name
        this.salary = salary

    @property
    def print_salary(self):
        print('printing salary...')
        return self.salary


e = Emp('Jmc', 50000)
print(e.name)
print(e.salary)
# can be invoked just like a fn but can't modify
print(e.print_salary)
# e.print_salary = 6
print()


class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 <= salary <= 100000:
            self.__salary = salary
        else:
            print('非法数据！')


e = Emp('Jmp', 20000)
print(e.name)
print(e.get_salary())
e.set_salary(3000)
print(e.get_salary())
print()


# property
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    # write this after @property was given
    @salary.setter
    def salary(self, salary):
        if 1000 <= salary <= 100000:
            self.__salary = salary
        else:
            print('非法数据！')


e = Emp('Jmd', 5000)
print(e.name)
print(e.salary)
e.salary = -100
e.salary = 6000
print(e.salary)
new_line()


# extend
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def eat(self):
        print('eat!')


class Stu(Person):
    """
    子类会自动调用父类init方法，
    可以不重写。
    def __init__(self, name, id, age):
        Person.__init__(self, name, id)
        self.age = age
    """
    pass


# s = Stu('Jmc', '05', 18)
s = Stu('Jmc', '05')
print(s.name)
s.eat()
new_line()


# in python the way of overriding method juat like in Java
# new_line()

# mro
class A: pass


class B(A): pass


class C(B): pass


print(C.__mro__)
print(C.mro())
new_line()


# override __str__ fn(toString fn in Java)
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Person: ' + self.name


p = Person('Jmc')
print(p)
new_line()


# extend more than one!
class A:
    def aa(self):
        print('aa')

    def say(self):
        print('say aaa')


class B:
    def bb(self):
        print('bb')

    def say(self):
        print('say bbb')


class C(A, B):
    def cc(self):
        print('cc')


c = C()
c.aa()
c.bb()
c.cc()

print()
print(C.mro())
# 从左到右查找
c.say()


class C(B, A): pass


print(C.mro())
c = C()
c.say()
new_line()


# super fn
class A:
    def say(self):
        print('A:', self)


class B(A):
    def say(self):
        # eq: A.say(self)
        super().say()
        print('B:', self)


b = B()
b.say()
new_line()


# 多态
class Person:
    def eat(self):
        print('吃饭')


class Chinese(Person):
    def eat(self):
        print('中国人用筷子吃饭')


class Indian(Person):
    def eat(self):
        print('印度人用手吃饭')


def manEat(m):
    if isinstance(m, Person):
        m.eat()
    else:
        print('类型异常')


manEat(Chinese())
manEat(Indian())
manEat(6464646)
new_line()


# 运算符重载
class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, p):
        if isinstance(p, Person):
            return self.name + p.name
        else:
            print('类型不同，不能相加')
            return None

    def __mul__(self, n):
        if isinstance(n, int):
            return self.name * n
        else:
            return None


p1 = Person('Jmc')
p2 = Person('Jmd')

print(p1 + p2)
print()
print(p1 + 'dhdhhs')
print()

print(p1 * 3)
new_line()


# singleton
class MySingleton:
    __obj = None
    __inited = False

    def __new__(cls, *args):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if not MySingleton.__inited:
            print('init...')
            self.name = name
            MySingleton.__inited = True


ms = MySingleton
ms1 = ms('a')
ms2 = ms('b')
print(ms1)
print(ms1.name)
print(ms2)
print(ms2.name)
new_line()


# # io
# # r'str' 为原始字串符（使转义字符失去作用(包括\n)，所以就可以不用双反斜杠转义了）
# try:
#     f = open(r'/sdcard/temp.txt', 'w')
#     f.write('Hello World!\n')
#     l = ['what', ' ', 'the', ' ', 'fuck']
#     f.writelines(l)
# except BaseException as e:
#     print(e)
# finally:
#     f.close()
#
# # with（上下文管理器）能管理上下文资源，不管是否中断，都能自动还原到进入该代码块的现场，可以代替try
# with open(r'/sdcard/temp.txt', 'w') as f:
#     f.write('OK Sir!')
#
# # read
# def write():
#     with open(r'/sdcard/temp.txt', 'w') as f:
#         str = """我print('lalala')
# print('papapa')
# print('hahaha')
#     """
#         f.write(str)
#
# # can read only once: like a iterator
# write()
# def read_this(mode):
#     with open(r'/sdcard/temp.txt', 'r') as f:
#         if mode == 0:
#             result = f.read()
#         elif mode == 1:
#             result = f.read(3)
#         elif mode == 2:
#             result = f.readline()
#         elif mode == 3:
#             result = f.readlines()
#         elif mode == 4:
#             for l in f: print(l, end='')
#             new_2line()
#             return
#
#         print(result)
#         new_line()
#
# for i in range(0, 5):
#     read_this(i)
#
# # enumerate(enum): add line number
# write()
# path = r'/sdcard/temp.txt'
# lq = None
# with open(path, 'r') as f:
#     l = f.readlines()
#     e = enumerate(l)
#     # print(list(e))
#     for i in e: print(i)
#
# new_line()
#
# # extend
# # str is used, so we need to del it
# del str
# k = [x + " #" + str(idx) for idx, x in enumerate(l)]
# print(k)
# new_line()
#
# # copy
# with open('/sdcard/temp.txt', 'rb') as r,open('/sdcard/test_copy.txt', 'wb') as w:
#     w.writelines(r.readlines())
#
# # other
# with open(path, 'r') as f:
#     print(f.name)
#     # tell the ptr position
#     print(f.tell())
#     print(f.readline())
#     print(f.tell())
#
#     # 2nd parm: whence
#     # 0: calculate from file head
#     # 1: calculate from here
#     # 2: calculate from file tail
#     f.seek(3)
#     print(f.readline())
#
# new_line()
#
# # serialization
# a = 'Jmc'
# b = 123
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s_path = '/sdcard/series.txt'
#
# with open(s_path, 'wb') as f:
#     # 泡菜.倾倒()
#     pickle.dump(a, f)
#     pickle.dump(b, f)
#     pickle.dump(c, f)
#
# with open(s_path,'rb') as f:
#     a = pickle.load(f)
#     b = pickle.load(f)
#     c = pickle.load(f)
#     # the id of them are different than before!
#     print_all(a, b, c)
#     new_line()
#
# # csv
# path = '/sdcard/csv.txt'
#
# out("""ID,姓名,年龄,薪资
# 1001,高琪,18,50000
# 1002,高八,18,30000
# 1003,高九,20,20000""", path)
#
# with open(path, 'r') as f:
#     a_csv = csv.reader(f)
#     # list = list(a_csv)
#     for l in a_csv: print(l)
#
# new_line()
#
# with open(path, 'w') as f:
#     b_csv = csv.writer(f)
#     b_csv.writerow(['Name', 'Sex'])
#     b_csv.writerows([['Jerry', 'Man'], ['Summer', 'Woman']])
#
# print(read(path))
# new_line()
#
# # exec system cmd
# print(os.system('cd /sdcard && ls'))
# # os.startfile('*/*.exe')
# new_line()
#
# # os
# print(os.name)
# print(os.sep)
# # repr()：将对象转化为可供解释器读取的形式。
# print(repr(os.linesep))
# print(os.stat('/sdcard/temp.txt'))
# new_line()
#
# # get current work dir
# print(os.getcwd())
# # change current work dir
# os.chdir("/sdcard")
# # mkdir in the cwd
# os.mkdir("oksir")
# # del dir(only if the dir is empty!)
# os.rmdir("oksir")
# print(os.getcwd())
# new_line()
#
# # support "../a/b/c"
# os.makedirs("a/b/c")
# # can only del empty dir
# os.removedirs("a/b/c")
#
# # rename dir or file
# # os.rename("sogou", "shit")
# """
# os.rename(old_file_path, new_file_path), 只能对相应的文件进行重命名
# os.renames(old_file_path, new_file_path), 是os.rename的升级版, 既可以重命名文件, 也可以重命名文件的上级目录名.
# """
#
# t = 'tencent'
# print(os.listdir(t))
# new_line()
#
# print(os.path.isabs(t))
# print(os.path.isdir(t))
# print(os.path.isfile(t))
# print(os.path.exists(t))
#
# print(os.path.getsize(t))
# print(os.path.abspath(t))
# print(os.path.dirname("/sdcard/tencent"))
#
# print(os.path.getctime(t))
# print(os.path.getatime(t))
# print(os.path.getmtime(t))
# new_line()
#
# path = os.path.abspath(t)
# print(os.path.split(path))
# print(os.path.splitext("/sdcard/a.txt"))
# print(os.path.join("a", "b", "c"))
# new_line()
#
# # practice : list all py files from cwd
# f_list = os.listdir(cwd)
# for f_name in f_list:
#     if (f_name.endswith('py')):
#         print(f_name)
#
# f_list2 = [f_name for f_name in os.listdir(cwd) if f_name.endswith('py')]
#
# print(f_list2)
# new_line()
#
# os.chdir(cwd)
# l = os.walk("../")
# print(l)
#
# all_fs= []
# all_dirs= []
#
# for dirpath, dirnames, filenames in l:
#     # parent path
#     #print('dirpath', dirpath)
#
#     # dirs in parent path
#     for dir in dirnames:
#         #print('dirname', dir)
#         all_fs.append(os.path.join(dirpath, dir))
#         pass
#
#     # files in parent path
#     for file in filenames:
#         #print('filename', file)
#         all_dirs.append(os.path.join(dirpath, file))
#         pass
#
# print_all(all_fs, all_dirs)
# os.chdir("/sdcard")
# new_line()
#
# os.mkdir("a")
# shutil.copyfile("temp.txt", "a/temp.txt")
#
# os.makedirs("a/b/c")
# # create file
# with open("a/b/c/ok.txt", "w") as f:
#     pass
#
#
# try:
#     # copy only des not exist
#     shutil.copytree("a/b/c", "a/oksir")
#     #shutil.copytree('y/b/c', 'y/oksir', ignore = shutil.ignore_patterns('*.txt', '*.py', '*.html'))
# except Exception as e:
#     pass
#
# # shutil.rmtree('a')
# # new_line()
#
# """
# shutil:
# copyfile(src, dst) #src, dst 都需是文件名, 如果dst 存在或无权限，会抛出异常
# copy(src, dst) #dst 可以是目录名。
# """
# # new_line()
#
# """
# shutil.make_archive(base_name, format[, root_dir[, base_dir...)
#
# "zip", "tar", "bztar"，"gztar"
# root_dir：打包的根目录（也是压缩包里的）
# base_dir：要进行压缩的源文件或者目录,
# root_dir和base_dir都默认为当前目录
# """
# # 可用...('a', 'zip', base_dir = 'did')来压缩文件或文件夹！
# shutil.make_archive("archive_a", "zip","a")
#
# shutil.rmtree("a")
#
# with zipfile.ZipFile("t.zip", "w") as z1:
#     z1.write("temp.txt")
#     z1.write("test_copy.txt")
#
# os.remove("temp.txt")
# os.remove("test_copy.txt")
#
# with zipfile.ZipFile("t.zip", "r") as z2:
#     # extract all to a path
#     z2.extractall("")
#
# delfs('csv.txt', 'series.txt', 'temp.txt', 'test_copy.txt')
# """
#
#
# del str
#
# class ShitError(Exception):
#     def __init__(self, errorInfo):
#         Exception.__init__(self)
#         self.errorInfo = errorInfo
#
#     def __str__(self):
#         return 'Shit error: that shit is illegal \'' + str(self.errorInfo) + '\''
#
#
# try:
#     raise ShitError('I wanna code')
# except Exception as e:
#     print(e)
#     new_line()
#
#
# # import
#
# # normal
# import src.com.jmc.io.files as f
# print(f)
# # from . import [module_name]
#
# # dynamic
# o = __import__('os')
# print(o)
#
# t = importlib.import_module('turtle')
# print(t)
#
# # importlib.reload('module_name')
#
# new_line()
