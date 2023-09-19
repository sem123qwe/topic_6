integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")
unity = all([integer, double, line])

# if all([integer, double, line]):
#     print("Да")
# else:
#     print("Нет")
match unity:
    case True:
        print("Да")
    case _:
        print("Нет")
