ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит: \n""1. Латинский\n""2. Кириллица\n")

choice = int(input("Введите номер алфавита: "))
if choice == 1:
    print("Латинский")
elif choice == 2:
    print("Кириллица")
else:
    print(" Упс! Выбран неверный режим. Попробуйте ещё раз...")

choice_abc = input("Введите букву латинского алфавита: ")

if choice_abc == ALPHABETS["en_vowels"]:
    print(ALPHABETS["en_vowels"],"- гласная буква")
elif choice_abc == ALPHABETS["en_consonants"]:
    print(ALPHABETS,"- согласная буква")
elif choice_abc == ALPHABETS["ru_vowels"]:
    print(ALPHABETS["ru_vowels"],"- гласная буква")
elif choice_abc == ALPHABETS["ru_consonants"]:
    print(ALPHABETS["ru_consonants"],"- согласная буква")
else:
    print("Упс! Неизвестная буква. Попробуйте другую!")
