num_1: float = float(input("Введите первое число: "))
num_2: float = float(input("Введите второе число: "))

magic: str = input("Введите магическую операцию: ")

match magic:
    case "Призыв":
        print("Сумма магических сил чисел:", num_1 + num_2)
    case "Трансформация":
        print("Трансформированное число:", num_1 - num_2)
    case "Объединение":
        print("Объединение чисел:", num_1 * num_2)
    case "Исчезновение":
        match num_2:
            case 0:
                print("Ошибка: Второе число равно нулю!")
            case _:
                print("Исчезновение:", num_1 / num_2)
    case _:
        print("Ошибка: Некорректная операция")
