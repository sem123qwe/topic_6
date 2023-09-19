integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")
smart = any([integer, double, line])

# if any([integer, double, line]):
#     print("Да")
# else:
#     print("Нет")
match smart:
    case True:
        print("Да")
    case _:
        print("Нет")

