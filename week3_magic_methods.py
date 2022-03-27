# Magic methods

# 3.1 __str__ and __repr__
# magic method (or dunder method) gets functions and are called automatically at certain moment
# e.g. __init_- is called right after creation of the object and is responsible for initiation

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # how object will be displayed inside the system (for developers)
        return f'The object Lion - {self.name}'

    def __str__(self):  # object will be displayed for users
        return f'Lion - {self.name}'

# w/o __repr__ __str__ method could be called only via print(),
# while with __repr__ it could also be called as method

# -----------------------------------------------------------------------
# task 3.1
# -----------------------------------------------------------------------

class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gend = gender

    @property
    def gend(self):
        return self.gender

    @gend.setter
    def gend(self, value):
        if value not in ('male', 'female'):
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            value = 'male'
        self.gender = value

    def __str__(self):
        if self.gend == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)



# 3.2 __len__ and __abs__
# magic methods would be called in case of using len() or abs() functions

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


a = Person('fgfg', 'fhfhf')
len(a)

b = Person('1', '23')
len(a)

class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abc(self)  # self.__abc__()

    def __abs__(self):
        return abs(self.x2 - self.x1)

t = Otrezok(5,9)
len(t)

t = Otrezok(10,9)
len(t)

# 3.3 __add__ / __mul__ / __sub__ / __truediv__
# magic methods would be called in case of using respective functions

class BankAccount:
    def __init__(self, name, balance):
        print('new_obj init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):  # adding variable to the right
        print('__add__ called')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

    def __radd__(self, other):  # adding variable to the left
        print('__radd__ called')
        return self + other

    def __mul__(self, other):  # multiplication
        print('__add__ called')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented

r = BankAccount('Misha', 780)
r+12
12+r # non supported
r+'gg'
r*10
r*'tttt'

b = BankAccount('Tanya', 900)
r+b

t = BankAccount('Ivan', 200)
id(t)
t + 30
# Клиент Ivan с балансом 230
d = t + 30

# -----------------------------------------------------------------------
# task 3.3
# -----------------------------------------------------------------------

class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if self.values:
            return f"Вектор{tuple(self.values)}"
        else:
            return f"Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*(i + other for i in self.values))

        if isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*(map(sum, zip(self.values, other.values))))

        if isinstance(other, Vector) and len(self.values) != len(other.values):
            print("Сложение векторов разной длины недопустимо")

        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*(i * other for i in self.values))

        if isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*(x*y for x,y in zip(self.values, other.values)))

        if isinstance(other, Vector) and len(self.values) != len(other.values):
            print("Умножение векторов разной длины недопустимо")

        else:
            print(f"Вектор нельзя умножать с {other}")


# 3.4 Special Methods for Comparing Class Objects

# __eq__ ==
# __ne__ !=
# __lt__ <
# __le__ <=
# __gt__ >
# __ge__ >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area  # comparing by area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other


q = Rectangle(1, 2)
w = Rectangle(1, 2)
w == q

r = Rectangle(10, 2)
r == w
r != w

q < r
r > r

r < 15
15 < r # whould call an error


# 3.5 __eq__ and __hash__
# hash - function doing one side transformation x->y not x<->y

class Point:
    def __init__(self, x , y):
        self. x = x
        self.y = y

    def __eq__(self, other):  #with __eq__ you cannot find hash
        return isinstance(other, Point) and \
               self.x == other.x and \
            self.y == other.y

    def __hash__(self):
        return hash(( self.x, self.y))  # introduce hash with tuple

p1 = Point(1,2)
p2 = Point(3,4)
# unhashable objects - mutable object (list, dictionary etc)
# hashable object - immutable objects ( strings, tuples etc)


# 3.6 __bool__
# bool(78) - True
# bool(0) - False
# bool('rew') - True
# bool('') - False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return  abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0

p1 = Point(1,2)
bool(p1)

bool(Point(-5, -5))

# if __bool__ not realised => python use __len__
# if __bool__ and __len__ are absent, all intances whould be True

bool(Point(0, -5))
bool(Point(0, 0))

p2 = Point(2,3)
if p2:
    print('hello')

# -----------------------------------------------------------------------
# task 3.6
# -----------------------------------------------------------------------

class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in 'aeiou')

class Quadrilateral:
        def __init__(self):
            pass

        def __str__(self):
            pass

        def __bool__(self):
            pass

# 3.7 __call__
# call operation is expressed as ()
# classes are callable objects

class Counter:
        def __init__(self):
            self.counter = 0
            self.summa = 0
            self.length = 0
            print('init object', *args, **kwargs)

        def __call__(self, *args, **kwargs):
            self.counter += 1
            self.summa += sum(args)
            self.length += len(args)
            print(f'Our instance was called {self.counter} times')

        def average(self):
            return self.summa / self.length

from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Call function {self.fn.__name__} ')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Function worked for {finish - start}')
        return result
@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= 1
        return pr

def fib(n):
    if n<=w:
        return 1
    return fib(n-1) + fib(n-2)

# 3.8 Polymorphism

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_area(self):
        return self.a**2

class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return 3.14 * self.r ** 2

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
#print(rect1.get_rect_area(),
#      rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
#print(sq1.get_sq_area(),
#      sq2.get_sq_area())

c1 = Circle(4)
c2 = Circle(5)
#print(c1.get_circle_area(),
#      c2.get_circle_area())

figures = [rect1, rect2, sq1, sq2, c1, c2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_sq_area())
    elif isinstance(figure, Circle):
        print(figure.get_circle_area())
    else:
        print(figure.get_rect_area())

# # Polymorphism - the ability to process completely different objects by using the same method

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a}x{self.b}'

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a}x{self.a}'

    def get_area(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle radius {self.r}'

    def get_area(self):
        return 3.14 * self.r ** 2

figures = [rect1, rect2, sq1, sq2, c1, c2]

for figure in figures:
    print(figure.get_area())  # polymorphism - we use one method for different purposes depending on class


# 3.9 __getitem__ , __setitem__ and __delitem__
# for working with lists
class Vector:

    def __init__(self, *args):
        self.value = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item-1]
        else:
            raise IndexError('Index is outside the collection')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key-1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0])
            self.values[key] = value
        else:
            raise IndexError('Index is outside the collection')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index is outside the collection')

# 3.10 __iter__ and __next__

class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks(item)

    def __iter__(self):
        print('caal iter')
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

igor = Student('Igor', 'Nikolaev', [3,4,5,6,3])
for i in igor:
    print(i)
