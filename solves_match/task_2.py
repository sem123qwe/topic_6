num: int = int(input("Введите целое число: "))

beger_num: bool = num > 0
smaller_num: bool = num < 0

match beger_num, smaller_num:
    case [True, False]:
        print(1)
    case [False, True]:
        print(-1)
    case _:
        print(0)
