num: int = int(input("Введите целое число: "))

first_various: bool = num % 2 == 0
second_various: int = num * 3 > 20

match first_various, second_various:
    case [True, False]:
        print("Число", num, "является четным")
    case [False, True]:
        print("Результат умножения", num, "на 3 больше 20")
    case _:
        print("Число", num, "не соответствует условиям")
