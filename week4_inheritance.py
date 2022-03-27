# Inheritance principle in OOP

# 4.1 Inheritance
# for classes with similar attributes
# we can use base class, from which it whould be inherited

class Person:  # parent class

    def can_walk(self):
        print('I can walk')


class Doctor(Person):  # subclass

    def can_cure(self):
        print('I can cure')

class Orthoped(Doctor):
    pass

class Architect(Person):  # subclass

    def can_build(self):
        print('I can build')

# we can check that one class is a subclsss of another
# Person -> Doctor -> Orthoped
d = Doctor()
a = Architect()


issubclass(Doctor, Person)
isinstance(d, Person)
isinstance(d, Doctor)


class Vehicle:
    pass
class Car(Vehicle):
    pass
class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass
class RaceCar(Car):
    pass

# 4.2 Inheritance form the object and other types
# every embedded type is a class and a subclass of the object
# any class is inherited from the object


class Person(object):
    pass
class Mylist(list):
    pass

class Doctors(Person):
    pass

class Architect(Person):
    pass


# 4.3 Overriding methods

class Person:

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print('can breathe')

    def walk(self):
        print('can walk')

    def __sleep(self):
        print('person sleeps')

    def __combo(self):
        self.breathe()
        self.walk()
        self.sleep()

class Doctor(Person):  # subclass

    def breathe(self):
        print('doctor breathe')
# переопределить родительский метод -  внутри дочернего клсса создать метод с такми же названием
# и внутри него определить другое поведение

    def __str__(self):
        return
    f'Doctor {self.name}'

d = Doctor('John')
p = Person('Adam')
p.breathe()
d.breathe()
p.walk()
d.walk()
print(p.name, d.name)

# 4.4 Extending classes
# it's applicable to subclasses
# creates method or attribute that is absent at parent class
class Person:

    def breathe(self):
        print('Person breathes')

    def sleep(self):
        print('Doctor sleeps')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()


class Doctor(Person):

    def breathe(self):
        print('Doctor breathes')

    def sleep(self):
        print('Doctor sleeps')

    def walk(self):
        print('Doctor walks')

p = Person()
p.sleep()

d = Doctor()
d.combo()


# 4.5 Delegating , super() function
# by delegating you can omit code that repeats

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

    def breathe(self):
        print('Doctor breathes')
        super().breathe()  # call method from the parent class for instance class Doctor


p = Person('Gosha', 'Kim')
d = Doctor('Masha', 'Low', 44)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()  # Person (info) -> Doctor (str)

# -----------------------------------------------------------------------
# task 4.5.1
# -----------------------------------------------------------------------


class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"

class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
        else:
            print("Ошибка заправки автомобиля")

class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"

class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"

transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 320 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

# -----------------------------------------------------------------------
# task 4.5.2
# -----------------------------------------------------------------------

class Initialization:

    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print(f'Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food

class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other,int):
            return self.capacity==other
        elif isinstance(other,(Vegetarian,MeatEater)):
            return self.capacity==other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"


    def __lt__(self, other):
        if isinstance(other,int):
            return self.capacity<other
        elif isinstance(other,(Vegetarian,MeatEater)):
            return self.capacity<other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"

    def __gt__(self, other):
        if isinstance(other,int):
            return self.capacity>other
        elif isinstance(other,(Vegetarian,MeatEater)):
            return self.capacity>other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)

v_second = Vegetarian([23], ['nothing'])
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])

s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)

print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True

# 4.6 Multiple inheritance

class Doctor:

    def __init__(self, rank, degree):
        self.rank = rank
        self.degree = degree

    def graduate(self):
        print('Hurray, Im a doctor now')

    def can_build(self):
        print('Im a doctor and I can build as well but a little bit worse')

class Builder:

    def __init__(self, rank, degree):
        self.rank = rank
        self.degree = degree

    def graduate(self):
        print('Hurray, Im a builder now')

    def can_build(self):
        print('Im a builder and I can build')

class Person(Doctor, Builder):

    def graduate(self):
        print('Lets see who I become')
        super().graduate()
        Doctor.graduate(self)

    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor. __init__(self, degree)
        self.rank = rank
        self.degree = degree

    def __str__(self):
        return f'Person {self.rank} {self.degree}'





print(Person.__mro__)  # method resolution object
# (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)

s = Person()
s.can_build()

a = Person()
a.can_build()



# 4.7 Slots
# operations with slots limit possible aittributes
# operations with slots are faster
# operations with slots use less memory

class Point:

    def __init__(self, x , y):
        self.x = x
        self.y = y

class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x , y):
        self.x = x
        self.y = y

p1 = PointSlots(3,4)
p1.x
p1.y

s = Point(3,4)
print(s.__sizeof__())
d = PointSlots(3,4)
print(d.__sizeof__())




# 4.8 Slots: property and inheritance

class Rectangle:

    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.a  = a
        self.b = b

    @property
    def  perimetr(self):
        return(self.height + self.width)*2

    @property
    def area(self):
        return  self.height * self.width

class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width  = a
        self.height = b

    @property
    def  width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


c = Rectangle(4,4)

class Square(Rectangle):

    __slots__ = 'color'

    def __init__(self, a, b, color):
        super().__init(a,b)
        self.color = color



