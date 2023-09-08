integer: int = int(input("Введите целое число: "))
double: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

link = [integer, double, line]

is_true: bool = all(link)

if is_true:
    print("Да")
else:
    print("Нет")
