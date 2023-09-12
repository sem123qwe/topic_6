ALPHABETS: dict = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит: \n""1. Латинский\n""2. Кириллица\n")

choice: int = int(input("Введите номер алфавита: "))

if choice not in (1, 2):
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
else:
    # vowels: None | str = None
    # consonants: None | str = None
    # language: None | str = None
    if choice == 1:
        vowels = ALPHABETS["en_vowels"]
        consonants = ALPHABETS["en_consonants"]
        language = "Введите букву латинского алфавита: "
    else:
        vowels = ALPHABETS["ru_vowels"]
        consonants = ALPHABETS["ru_consonants"]
        language = "Введите букву кириллицы: "

    choice_abc: str = input(language)

    if choice_abc in vowels:
        print(choice_abc, "- гласная буква")
    elif choice_abc in consonants:
        print(choice_abc, "- согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
