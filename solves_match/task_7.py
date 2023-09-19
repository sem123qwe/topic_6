integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

unity: bool = all([integer, double, line])

match unity:
    case True:
        print("Да")
    case _:
        print("Нет")
