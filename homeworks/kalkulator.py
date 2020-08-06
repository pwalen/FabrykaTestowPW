def add(x, y):
    return  x + y

def substract(x, y):
    return  x - y

def multiply(x, y):
    return  x * y

def divide(x, y):
    return  x + y

print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        wyn = "Wynik wynosi: "

        if choice == "1":
            print(wyn, add(num1, num2))
        if choice == "2":
            print(wyn, substract(num1, num2))
        if choice == "3":
            print(wyn, multiply(num1, num2))
        if choice == "4":
            print(wyn, divide(num1, num2))
        break


    else:
        print("Błędna wartość, podaj poprawną")


