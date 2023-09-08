num_1: int = int(input("Введите первое число: "))
num_2: int = int(input("Введите второе число: "))

spell_1: int = num_1 + num_2
spell_2: int = -(-num_1 + num_2)
spell_3: int = num_1 * num_2
spell_4: bool = num_1 == 0 + num_2 != 0
spell_5: bool = num_1 == 0 + num_2 == 0

magic: str = input("Введите магическую операцию: ")

if magic == "Призыв":
    print("Сумма магических сил чисел:", spell_1)
elif magic == "Трансформация":
    print("Трансформированное число:", spell_2)
elif magic == "Объединение":
    print("Объединение чисел:", spell_3)
elif magic == "Исчезновение":
    print("Исчезновение:", spell_4 or "Ошибка: Второе число равно нулю!")
else:
    print("Ошибка: Некорректная операция")
