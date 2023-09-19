year: int = int(input("Введите год: "))
manth: int = int(input("Введите месяц: "))

is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
unic_manth: tuple = (1, 3, 5, 7, 8, 10, 12)
gotta_go = manth in unic_manth


# if is_leap_year and (manth in unic_manth):
#     
# else:

match is_leap_year, gotta_go:
    case [True, True]:
        print("Да")
    case _:
        print("Нет")
