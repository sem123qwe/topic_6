your_age: int = int(input("Введите свой возраст: "))

if 0 < your_age < 18:
    print("Вы находитесь на уровне \"Инициации\"")
elif 18 <= your_age <= 30:
    print("Вы находитесь на уровне \"Приключений\"")
elif 30 <= your_age <= 50:
    print("Вы находитесь на уровне \"Мастерства\"")
elif 51 <= your_age <= 65:
    print("Вы находитесь на уровне \"Мудрости\"")
elif your_age > 65:
    print("Вы находитесь на уровне \"Легенда\"")
else:
    print("Возраст не может быть отрицательным или нулем")
