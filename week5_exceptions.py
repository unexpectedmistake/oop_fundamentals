# Exceptions
# 5.1

# Exceptions appear during execution and all rows below will not be executed

# Execution exception - during code execution
# Compilation exception - before execution

print('hello')
print('hello')
print('hello')
print('hello')

try:
    int('hello')
except ValueError:
    print('wrong transformation')

try:
    [1, 2][5]
except LookupError:
    print('wrong index')
# Hierarchy: Base Exception -> Exception -> ValueError / TypeError / AttributeError / etc

t = IndexError()
t
isinstance(t, IndexError)
isinstance(t, LookupError)

# we can call exceptions
raise ValueError('wrong value')

# 5.2 Distribution of exceptions

def second():
    print('start second')
    #try:
    1/0  # expection IndentationError is distributed among rows
    #except ZeroDivisionError:
    #    print('handling')
    print('finish second')

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('handling')
    print('finish first')

print('hello')
first()


# 5.3 try-except

try:
    int('hello')  #  exception - rows below will not be executed
    1/0
    a+b
except ValueError:
    print('attention - Value Error')

try:
    1/0
    int('hello')
    a+b
except ValueError:
    print('attention - Value Error')
except ZeroDivisionError:
    print('attention - ZeroDivisionError')

s = 'hello'
try:
    s[6]
except LookupError:
    print('attention - LookUpError')

f = open('123.txt')
try:
    execute(f)
finally:
    print('end')
    f.close()

try:
    1/5
finally:
    print('end')

# 5.4 raise

raise Exception('Big error')

try:
    [1,2,3][15]
except (KeyError, IndexError) as error:
    print(f'Logging error: {repr(error)}')
    raise TypeError('Error type') from None
except ZeroDivisionError as err:
    print('ZeroDivisonError')
    print(f'Logging error: {err} {repr(err)}')

a = TypeError('Error type')
a.args


try:
    raise ValueError('Error type')
except ValueError:
    try:
        raise TypeError('Error type')
    except TypeError as second:
        raise Exception('Big exception') from second


# 5.5 User exceptions

class MyException(Exception):
    ''' this is my first exception'''

try:
    raise MyException('HELLO', 1, 2 ,3)
except Exception:
    print('done')

class SnakeTailException(SnakeTailException):
    '''Tail touches the body !!! '''

