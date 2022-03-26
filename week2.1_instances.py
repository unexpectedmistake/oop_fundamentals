# 2.1 Instances methods

class Cat:
    def hello(*args):
        print('Hello world from kitty', args)


Cat.hello()  # function
bob = Cat()
bob.hello()  # method, not function

'''
1. Method is a function stated inside the Class
2. Method refers to a specific object (connected with it), function is not
3. Using method you use related object as an argument of the function
'''

'''
Object from which method was called should be named *self*
'''


class Cat:
    breed = 'pers'

    def hello(*args):
        print('Hello world from kitty', args)

    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age


mary = Cat()
mary.show_name()
mary.name = 'Hustle'
mary.show_name()

tom = Cat()
tom.show_name()
tom.set_value('Tom')
tom.show_name()

jerry = Cat()
jerry.set_value('Jerry')
jerry.show_name()
jerry.set_value('Jerry', 120)
jerry.__dict__

# ________________________________________________________________________________
# task 2.1
# ________________________________________________________________________________
class Lion:
    def roar(self):
        print('Rrrrrrr!!!')


simba = Lion()
simba.roar()


class Counter:
    def start_from(self, num=0):
        self.counter = num

    def increment(self):
        self.counter += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.counter}')

    def reset(self):
        self.counter = 0


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, obj):
        if isinstance(obj, Point):
            return float(((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** (0.5))
        else:
            print('Передана не точка')

# 2.2 __init__ method

class Cat:

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self, name, breed='siam', age=1, colour='white'):  # return value every time when instance is created
        print('new instance is created', self)
        self.name = name
        self.age = age
        self.breed = breed
        self.colour = colour
# ________________________________________________________________________________
# task 2.2
# ________________________________________________________________________________
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

laptop1 = Laptop('asus', '____', '50000')
laptop2 = Laptop('mac', '____', '150000')

class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals=1):
        self.goals =+ goals

    def make_assist(self, assists=1):
        self.assists =+ assists

    def statistics(self):
        print( f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

class Zebra:

    def __init__(self, step=0):
        self.step = step

    def which_stripe(self, step=1):
        self.step += 1
        if self.step % 2 == 1:
            print('Полоска белая')
        else:
            print('Полоска черная')

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age >= 18

# 2.3 Creation classes and methods practice

# DRY(dont repeat yourself) principle
class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        else:
            return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5
# ________________________________________________________________________________
# task 2.3
# ________________________________________________________________________________
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'


class Stack():

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) > 0:
            return self.values.pop()
        else:
            print('Empty Stack')

    def peek(self):
        if len(self.values) > 0:
            return self.values[-1]
        else:
            print('Empty Stack')

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


# 2.4 Monostate pattern (Borg)
# When we need to set the same state for all class instances
# We are using dictionary (mutable object) so all changes will affect all instances

class Cat:
    __shared_attr = {     # create private attribute
        'breed': 'pers',
        'colour': 'black'
    }
    def __init__(self):
        self.__dict__ = Cat.__shared_attr

d = Cat()
g = Cat()
d.breed = 'siam'
d.name = 'Bob'
# changes made for old instances will be attributed to the new ones
# it was achieved by using the same class attribute
# dictionary is mutable object, so changes in dictionary will be applied for all instances
h = Cat()
h.__dict__


# 2.5 Public, private and secured attributes and methods

class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)


account1 = BankAccount('Bob', 100000, 48556909090)
account1.print_public_data()
# we have access to data outside the bank (from method print_data)
print(account1.name)
print(account1.balance)
print(account1.passport)

# create protected attribute with _
class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


account1 = BankAccount('Bob', 100000, 48556909090)
account1.print_protected_data()
# we still have access, but it's a sign that this attribute for needs inside the class, sign for other users of the code
print(account1._name)
print(account1._balance)
print(account1._passport)


# create private attribute with __
class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 100000, 48556909090)
# we have access now only through method - method for working with data - encapsulation (we cannot have direct access to attributes)
account1.print_private_data()
# so now we dont have access to private attributes
#print(account1.__name)
#print(account1.__balance)
#print(account1.__passport)

# but we still can have access if we put private method inside public one
#def print_public_data(self):
#    self.__print_private_data()





