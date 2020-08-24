import requests
import ast
import datetime
import time

my_currency = 'PLN'
my_url = f'https://api.exchangeratesapi.io/latest?symbols={my_currency}'
timeout = 0.099


def my_decorator(fn):
    def wrapper():
        while True:
            now = datetime.datetime.now()
            date_time_now = now.strftime("%m/%d/%Y, %H:%M:%S")
            try:
                start_of_execution = datetime.datetime.now()
                fn()
                end_of_execution = datetime.datetime.now()
                execution_time = start_of_execution - end_of_execution

                get_currency_txt = get_currency.text
                currency_as_dictionary = ast.literal_eval(get_currency_txt)

                print("Kurs Euro: ", currency_as_dictionary['rates']['PLN'])
                print("Data i godzina: ", date_time_now)
                print(f"Czas wykonania zapytania: {execution_time.microseconds} μs")

            except requests.Timeout:
                print('Błąd pozyskania danych')
                print("Data i godzina: ", date_time_now)
                print(f"Czas wykonania zapytania: {int(timeout * 1000000)} μs")

            print('\n=====================================\n')

            time.sleep(15)

    return wrapper()


@my_decorator
def get_currency_function():
    global get_currency
    get_currency = requests.get(my_url, timeout=timeout)
