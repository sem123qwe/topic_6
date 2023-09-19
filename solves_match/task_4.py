num_1: int = int(input("Введите первое целое число: "))
num_2: int = int(input("Введите второе целое число: "))
num_3: int = int(input("Введите третье целое число: "))

first_variant: bool = num_1 > num_2 and num_1 > num_3
second_variant: bool = num_2 > num_1 and num_2 > num_3
third_variant: bool = num_3 > num_2 and num_3 > num_1

match first_variant, second_variant, third_variant:
    case [True, False, False]:
        print("Наибольшее число:", num_1)
    case [False, True, False]:
        print("Наибольшее число:", num_2)
    case [False, False, True]:
        print("Наибольшее число:", num_3)
    case _:
        print("Все числа равны")
