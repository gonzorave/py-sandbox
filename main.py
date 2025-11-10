""""
This is a basic sample.
print('Hello, Python!')
"""

# Decorator example
def logger(func):
    def wrapper(*args, **kwargs):
        print('Calling:', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greeting():
    print('I see ya!')

@logger
def farewell():
    print('Goodbye!')

# Сalls
greeting()
farewell()