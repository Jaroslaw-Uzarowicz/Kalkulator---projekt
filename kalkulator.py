def dodawnie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


def potegowanie(a, b):
    return a ** b


def pierwiastek(a,b):
    return a // b


print("Wybierz operację: ")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print("5.Potęgowanie")
print("6.Pierwiastkowanie")

while True:
    choice = input("Wybierz spośród (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print(num1, "+", num2, "=", dodawnie(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dzielenie(num1, num2))
        elif choice == '5':
            print(num1, "**", num2, "=", potegowanie(num1, num2))
        elif choice == '6':
            print(num1, "//", num2 ,"=", pierwiastek(num1, num2))
        next_calculation = input("Chcesz wykonać kolejne działanie? (tak/nie): ")
        if next_calculation == "nie":
            break
        print("Nieporpawna wartość.")
