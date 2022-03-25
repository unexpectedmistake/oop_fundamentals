# 2.6 Getter, setter, deliter, property attributes

# We want to create an interface enabling us to get access to specific private attribute
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get_balance')
        return self.__balance

    def set_balance(self, value):
        print('set_balance')
        if not isinstance(value, (int, float)):  # introduce a limitation
            raise ValueError('Баланс должен быть числом')
        else:
            self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # property - method used to define properties in classes
    # provides an interface for the attributes of a class instance
    # it encapsulates instance attributes and exposes properties
    # accepts get, set and delete methods as input, and returns objects of class property
    # property( fget, fset, fdel, doc)

# We not directly refer to attribute but use two methods get_balance and set_balance
b = BankAccount('Vasya', 100)
b.get_balance()
b.set_balance(140)
b.__dict__



d = BankAccount('Misha', 400)
d.balance
d.balance = 888
d.balance
del d.balance
# -----------------------------------------------------------------------
# task 2.6
# -----------------------------------------------------------------------

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if (isinstance(new_email,str)) and \
                ('.' in new_email[new_email.find('@'):]) and (new_email.count('@') == 1):
            self.__email = new_email
        else:
            print('Ошибочная почта')

    email = property( fget=get_email, fset=set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait


# 2.7 Property decorator

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get_balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set_balance')
        if not isinstance(value, (int, float)):  # introduce a limitation
            raise ValueError('Баланс должен быть числом')
        else:
            self.__balance = value

    # my_balance = my_property_balance.setter(my_balance)
    @my_balance.deleter
    def delete_balance(self):
        print('delete balance')
        del self.__balance



    # my_balance = property(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

# -----------------------------------------------------------------------
# task 2.6
# -----------------------------------------------------------------------

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = 100*dollars + cents

    @property
    def dollars(self):
        print('return_dollars')
        return self.dollars

    @dollars.getter
    def dollars(self):
        return self.dollars

    @dollars.setter
    def dollars(self, value):
        self.dollars = value


    @property
    def cents(self):
        return cents

    @cents.getter
    def cents(self):
        return self.cents

    @cents.setter
    def cents(self, value):
        self.cents = value

    def __str__(self):
        return  f'Ваше состоян е составляет {self.dollars} долларов {swlf.cents} центов'





# 2.8 Computed property

class Square:
    def __init__(self, side):
        self.side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side**2
        return self.__area

b = Square(6)
b.area

# 2.9 Classmethod and staticmethod
# staticmethod - create functions inside the class which could be called from class as well as from instance
#

class Example:
    def hello():
        print('hello')

    def instance_hello():
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')

# we created static method which is not attached to an instance or class
# staticmethod can be used when we need a function, but we want to perform it inside the class
Example.static_hello()
y = Example()
y.static_hello()

# when we want to perform operations on not only instances, but on the class entirely
Example.class_hello()
a = Example()
a.class_hello() # returns the class to which the instance belongs


# 2.10 Class namespaces
# 5 ways to get access to attributes of the class

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
# names created inside the class are unavailable for method namespace
# 1. refer by self. (e.g. self.PYTHON_DEV)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
# 2. refer directly to the class

    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
# 3. by property

    @classmethod
    def info_class(cls):
        print('info_class')
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
# 4. using classmethod

    @staticmethod
    def info_static():
        print('info_static')
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
# 5. using staticmethod

    def make_backend(self):
        print('Python and Go')

    def make_frontend(self):
        print('React')

    def hiring_pyt_dev(self):
        DepartmentIT.PYTHON_DEV = DepartmentIT.PYTHON_DEV + 1  # change PYTHON_DEV in class namespace, not in the instance namespace

it1 = DepartmentIT()
it1.info()
it1.info2()
it1.info_prop
it1.info_class()
it1.info_static()

it1.hiring_pyt_dev()
it1.__dict__

# 2.11 Property  method practice

from string import digits

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # __password - private attribute,
                                  # but to do initial check we get password property instead
                                  # so setter is called simultaneously
        self.__secret = 'stranger_things'

    @property
    def secret(self):
        s = input('Введите пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('ДОСТУП ЗАКРЫТ')

    @property
    def password(self):  # password - property
        print('getter called')
        return self.__password

    @staticmethod  # to eliminate self and get password instead
    def is_include_number(password):
        for digit in digits:  # checking for inclusion of numbers in the password
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):  # password - setter
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('ПАРОЛЬ ДОЛЖЕН БЫТЬ СТРОКОЙ')
        if len(value) < 4:
            raise ValueError('ДЛИНА ПАРОЛЯ СЛИКОМ МАЛА, МИНИМУМ 4 СИМВОЛА')
        if len(value) > 12:
            raise ValueError('ДЛИНА ПАРОЛЯ СЛИКОМ ВЕЛИКА, МАКСИМУМ 12 СИМВОЛА')
        if not User.is_include_number(value):
            raise ValueError('ПАРОЛЬ ДОЛЖЕН СОДЕРЖАТЬ ХОТЯ БЫ ОДНУ ЦИФРУ')
        self.__password = value

a = User('AAA', 1222)
a.password = 2134  # setter called
a.password  # getter called

b = User('AAA', 1222)
b.password = 'gg'
b.password = 'ggggggggggggggg'
b.password = 'ffff'
b.password = 'qwerty1'

p = User('abc', 123)

x = User('sdf', 'fgfgf4')
x.secret
# Введите пароль: >? fgfgf4
# 'stranger_things'

# -----------------------------------------------------------------------
# task 2.11
# -----------------------------------------------------------------------

class Registration:

