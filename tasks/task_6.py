year = int(input("Введите год: "))
manth = int(input("Введите месяц: ")) 

leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
unic_manth = [1, 3, 5, 7, 8, 10, 12]

if leap_year and manth in unic_manth:
    print("Да")
else:
    print("Нет")
    