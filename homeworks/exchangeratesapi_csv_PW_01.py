import requests
import ast
import datetime
import time
import csv

my_currency = 'PLN'
my_url = f'https://api.exchangeratesapi.io/latest?symbols={my_currency}'
timeout = 0.99


def my_decorator(fn):
    def wrapper():
        # Na potrzeby zapisu w formacie CSV tworzę "listę list", ze zdefiniowanym pierszym elementem
        # czyli listą nagłówków 3 kolumn. Po każdej iteracji,  do głównej listy  ma być dodawany kolejny
        # element, czyli lista zawierająca wyniki danej iteracji (funkcja .append()).
        # Główna lista będzie na bieżąco zapisywana w trzykolumnowym pliku CSV, przy czym każdy jej element
        # w oddzielnym rzędzie pliku CSV..
        list_of_results = [['Kurs/Błąd pozyskania', 'Data i godzina', 'Czas wykonania']]
        while True:
            now = datetime.datetime.now()  # czas, w którym odbyło się zapytanie
            date_time_now = now.strftime("%d/%m/%Y, %H:%M:%S")  # sformatowany czas (w którym odbyło się zapytanie)
            try:
                start_of_execution = datetime.datetime.now()
                get_currency = fn()
                end_of_execution = datetime.datetime.now()
                execution_time = start_of_execution - end_of_execution  # czas trwania zapytania

                get_currency_txt = get_currency.text  # zwraca typ string, który wyświetla się jako słownik
                currency_as_dictionary = ast.literal_eval(get_currency_txt)  # przekształca string w słownik

                print("Kurs Euro: ",
                      currency_as_dictionary['rates']['PLN'])  # zwraca ze słownika liczbę == kurs EUR/PLN
                print("Data i godzina: ", date_time_now)
                print(f"Czas wykonania zapytania: {execution_time.microseconds} μs")
                # tworzę listę trzech elementów, która będzie dodana jako kolejny element do listy głównej
                # 'list_of_results' - docelowo będze to kolejny rząd zapisany w pliku CSV
                row_a = [currency_as_dictionary['rates']['PLN'], date_time_now, execution_time.microseconds]
                list_of_results.append(row_a)
            except requests.Timeout:
                print('Błąd pozyskania danych')
                print("Data i godzina: ", date_time_now)
                # Niestety funkcja 'execution_time' z bloku 'try' nie jest dostępna w bloku 'except,
                # dlatego w przypadku błędu Timeout  przyjąłem, że będzie to wartość wartość przypisana do zmiennej
                # 'timeout'.
                print(f"Czas wykonania zapytania: {int(timeout * 1000000)} μs")
                # tworzę listę trzech elementów, która będzie dodana jako kolejny element do listy głównej
                # 'list_of_results' - docelowo będze to kolejny rząd zapisany w pliku CSV
                row_b = ['Błąd pozyskania danych', date_time_now, timeout]
                list_of_results.append(row_b)
            print('\n=====================================\n')

            time.sleep(15)

            with open('list_of_results.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(list_of_results)

    return wrapper()


@my_decorator
def get_currency_function():
    return requests.get(my_url, timeout=timeout)
