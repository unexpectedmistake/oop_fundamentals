# Introduction to classes
# Class attributes
class Person:
    name = 'Ivan'
    age = 30
# get all attributes of the class
Person.__dict__
getattr(Person, 'name')

# add new attributes
Person.new_attribute = [1, 2, 3]
setattr(Person, 'new_attr', [1, 2, 3])
Person.x = [1, 3, 5]

# delete attributes
del Person.x
delattr(Person, 'x')

# create instances
a = Person()
b = Person()

# Instances attributes
class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a2 = Car()

a1.__dict__
a1.seat = 4
a1.model = 'Lada'

'''
after deleting of attribuite from the instance, 
instance will return class aittribute
'''
del a1.model
a1.__dict__
a1.model


# Functions as a class attribute (not instance attribute)

class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print("Let's go")

Car.drive()

getattr(Car, 'drive')
getattr(Car, 'drive')()

a = Car()
a.drive # bound method, not function
a.drive()

'''
You cannot refer to function from Class via instance
You need to use decorators!!!
'''



