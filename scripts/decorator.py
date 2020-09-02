# dekoratory to sposób aby dodać coś do możliwości funkcji ale bez zmiany tej funkcji
# jest to ważne przy złożonych projektach, gdzie ingerencje we wnętrze funkcji
# mogą wprowadzić niepożądane rezultaty w innych miejscach kodu


# def regular_function():
#     print('this is a regular function')
#
#
# def decor(function):
#     def inside():
#         print('decorate function')
#         return function()
#     return inside
#
#
# new_function = decor(regular_function)
# new_function()
#
# print('\n==============\n')

# * prostszy sposób *

def dekor(function):
    def inside():
        print('decorate function')
        return function()

    return inside()


@dekor
def regular_function():
    print('this is a regular function')
