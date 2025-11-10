""""
This is a basic sample.
print('Hello, Python!')
"""
from operators import demo_arithmetic, demo_comparisons, demo_logic

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
print(demo_arithmetic(10, 4))
print(demo_comparisons(2,1000))
print(demo_logic(False, False))
farewell()

