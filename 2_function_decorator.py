#decorator 
def my_decorator(func):
    def wrapper():
        return wrapper

@my_decorator
def say_hello():
    print("hello world")

say_hello()