# zrobimy sobie funkcję którą udekorujemy
# funkcja będzie zwracała wynik w określonych godzinach od godziny 6 rano do godziny dwudziestej drugiej

from datetime import datetime

def say_hello():
    print('hello my friend')

def say_goodbye():
    print('say goodbye')

def run1(function):
    def wrapper():
        if 6 <= datetime.now().hour < 22:
            function()
        else:
            pass
    return wrapper()


def run2(function):
    def wrapper():
        if 1 <= datetime.now().hour < 6:
            function()
        else:
            pass
    return wrapper()

run1(say_hello)

run2(say_goodbye)







