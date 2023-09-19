your_age: int = int(input("Введите свой возраст: "))

first: bool = 0 < your_age < 18
second: bool = 18 <= your_age <= 30
therd: bool = 30 <= your_age <= 50
forth: bool = 51 <= your_age <= 65
fifth: bool = your_age > 65

# Лучше if-elif-else ^_^
match first, second, therd, forth, fifth:
    case [True, False, False, False, False]:
        print("Вы находитесь на уровне \"Инициации\"")
    case [False, True, False, False, False]:
        print("Вы находитесь на уровне \"Приключений\"")
    case [False, False, True, False, False]:
        print("Вы находитесь на уровне \"Мастерства\"")
    case [False, False, False, True, False]:
        print("Вы находитесь на уровне \"Мудрости\"")
    case [False, False, False, False, True]:
        print("Вы находитесь на уровне \"Легенда\"")
    case _:
        print("Возраст не может быть отрицательным или нулем")
