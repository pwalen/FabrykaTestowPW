import termcolor

def add(x, y):
    return  x + y

def substract(x, y):
    return  x - y

def multiply(x, y):
    return  x * y

def divide(x, y):
    return  x / y

print("Wybierz operację.")
print(termcolor.colored("1.Dodawanie", "green"))
print(termcolor.colored("2.Odejmowanie", "red"))
print(termcolor.colored("3.Mnożenie", "blue"))
print(termcolor.colored("4.Dzielenie", "magenta"))

while True:
    choice = input(termcolor.colored("Wybierz operację(1/2/3/4): ", attrs=['bold']))
    if choice in ("1", "2", "3", "4"):
        while True:
            num1 = input("Podaj pierwszą liczbę: ")
            try:
                num1 = int(num1)
                break
            except ValueError:
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print(termcolor.cprint("    Błędna wartość, podaj poprawną    ", "red", "on_green", attrs=['bold']))

        while True:
            num2 = input("Podaj drugą liczbę: ")
            try:
                num2 = int(num2)
                break
            except ValueError:
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print(termcolor.cprint("    Błędna wartość, podaj poprawną    ", "red", "on_green", attrs=['bold']))


        wyn = "Wynik wynosi: "

        if choice == "1":
            print(termcolor.colored(wyn + str(add(num1, num2)), "green", attrs=['bold']))
        if choice == "2":
            print(termcolor.colored(wyn + str(substract(num1, num2)), "red", attrs=['bold']))
        if choice == "3":
            print(termcolor.colored(wyn + str(multiply(num1, num2)), "blue", attrs=['bold']))
        if choice == "4":
            while num2 == 0:
                print(termcolor.colored("    Nie można dzielić przez zero!    ", 'red', attrs=['reverse', 'blink']))
                while True:
                    num2 = input("Podaj ponownie drugą liczbę: ")
                    try:
                        num2 = int(num2)
                        break
                    except ValueError:
                        try:
                            num2 = float(num2)
                            break
                        except ValueError:
                            print(termcolor.cprint("    Błędna wartość, podaj poprawną    ", "red", "on_green", attrs=['bold']))

            else:
                print(termcolor.colored(wyn + str(divide(num1, num2)), "magenta", attrs=['bold']))
        break

    else:
        print(termcolor.cprint("    Błędna wartość, podaj poprawną    ", "red", "on_green", attrs=['bold']))


