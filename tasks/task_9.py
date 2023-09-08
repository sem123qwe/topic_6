integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

visual = [integer, double, line]

if any(visual):
    print("Да")
else:
    print("Нет")
