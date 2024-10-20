import sys


def foo():
    return 'foo'


def modify(func):
    module = sys.modules[func.__module__]
    return module


if __name__ == "__main__":
    print("THIS IS THE ANSWER", modify(foo).__package__)