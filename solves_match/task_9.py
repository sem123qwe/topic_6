integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

smart: bool = any([integer, double, line])

match smart:
    case True:
        print("Да")
    case _:
        print("Нет")
