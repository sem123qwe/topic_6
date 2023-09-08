integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

if any([integer, double, line]):
    print("Да")
else:
    print("Нет")
