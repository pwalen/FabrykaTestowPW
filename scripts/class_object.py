# właściwości są zmiennymi zadeklarowanymi wewnątrz klasy
# metody są funkcjami opisującymi konkretne działania

# klasa jest zbiorem funkcji i zmiennych

class MyFirstClass():
    variable1 = 1
    variable2 = 2

    def function(self):
        print('Hello World!')


object = MyFirstClass()
object.variable1

object2 = MyFirstClass()
object2.variable2

print(object.variable1)
print(object2.variable2)

# jak dostać się do funkcji?
object3 = MyFirstClass()
object3.function()

# Reasumując klasy w programach obiektowych służą do tworzenia takich szablonów
# z których będą tworzone obiekty
# z kolei te obiekty będą podstawową jednostką funkcjonalną
# Obiekty relacje między nimi będą tworzyły całą taką logikę naszego programu
# Czyli dostarczały użytkownikom funkcję / funkcjonalność
