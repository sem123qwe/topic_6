## Домашнее задание | 6. Условные операторы

- [Задание 0](#задание-0)
- [Задание 1](#задание-1)
- [Задание 2](#задание-2)
- [Задание 3](#задание-3)
- [Задание 4](#задание-4)
- [Задание 5](#задание-5)
- [Задание 6](#задание-6)
- [Задание 7](#задание-7)
- [Задание 8](#задание-8)
- [Задание 9](#задание-9)
- [Задание 10](#задание-10)

---

### [Задание 0](task_0.py)

Напишите программу, которая принимает от пользователя его любимый цвет. Если пользователь вводит
цвет `"солнечно-желтый"` или `"небесно-голубой"`, программа должна вывести сообщение `"Это цвет радости и счастья!"`.
Для любого другого введенного цвета программа должна вывести сообщение `"Это тоже хороший цвет!"`.

**Примеры:**

| Ввод                                      | Вывод                       |
|:------------------------------------------|:----------------------------|
| Введите ваш любимый цвет: солнечно-желтый | Это цвет радости и счастья! |

| Ввод                                      | Вывод                       |
|:------------------------------------------|:----------------------------|
| Введите ваш любимый цвет: небесно-голубой | Это цвет радости и счастья! |

| Ввод                              | Вывод                  |
|:----------------------------------|:-----------------------|
| Введите ваш любимый цвет: красный | Это тоже хороший цвет! |

---

### [Задание 1](task_1.py)

Напишите программу, которая принимает от пользователя имя своего питомца. Если пользователь вводит имя `"Барсик"`
или `"Мурка"`, программа должна вывести сообщение `"У вас классное имя для питомца!"`. Для любого другого введенного
имени питомца программа должна вывести сообщение `"Это тоже хорошее имя для питомца!"`.

Примечание: Используйте тернарный оператор.

**Примеры:**

| Ввод                               | Вывод                           |
|:-----------------------------------|:--------------------------------|
| Введите имя своего питомца: Барсик | У вас классное имя для питомца! |

| Ввод                              | Вывод                           |
|:----------------------------------|:--------------------------------|
| Введите имя своего питомца: Мурка | У вас классное имя для питомца! |

| Ввод                              | Вывод                             |
|:----------------------------------|:----------------------------------|
| Введите имя своего питомца: Рыжик | Это тоже хорошее имя для питомца! |

---

### [Задание 2](task_2.py)

Напишите программу, которая принимает целое число от пользователя и проверяет, является ли оно положительным,
отрицательным или нулем.

Программа должна вывести соответствующее число:

* 1, если число положительное;
* -1, если число отрицательное;
* 0, если это число ноль.

Полезно знать: Если вы решите эту задачу с использованием условных операторов, попробуйте
также реализовать ее с помощью тернарного оператора.

**Примеры:**

| Ввод                   | Вывод |
|:-----------------------|:------|
| Введите целое число: 5 | 1     |

| Ввод                     | Вывод |
|:-------------------------|:------|
| Введите целое число: -16 | -1    |

| Ввод                   | Вывод |
|:-----------------------|:------|
| Введите целое число: 0 | 0     |

---

### [Задание 3](task_3.py)

Добро пожаловать в загадочный Лабиринт магии! Каждый уровень представляет собой испытание, соответствующее вашему
возрасту. Введите свой возраст, и программа определит, на каком уровне лабиринта вы оказались.

* Если вам меньше 18 лет, вас ждет уровень `"Инициации"` с первыми магическими заданиями и испытаниями.
* Если вам от 18 до 30 лет, вы попадете на уровень `"Приключений"` с более сложными заданиями и возможностью проявить
  свою силу.
* Если вам от 31 до 50 лет, вы войдете на уровень `"Мастерства"` с глубокими тайнами и мощными преградами.
* Если вам от 51 до 65 лет, вы достигнете уровеня `"Мудрости"` с мудрыми испытаниями и возможностью использовать свою
  жизненную опытность.
* И если вам больше 65 лет, вас ожидает уровень `"Легенд"` с самыми сложными и уникальными испытаниями, которые только
  истинный великий маг может пройти.

**Примеры:**

| Ввод                     | Вывод                               |
|:-------------------------|:------------------------------------|
| Введите свой возраст: 15 | Вы находитесь на уровне "Инициации" |

| Ввод                     | Вывод                                 |
|:-------------------------|:--------------------------------------|
| Введите свой возраст: 25 | Вы находитесь на уровне "Приключений" |

| Ввод                     | Вывод                              |
|:-------------------------|:-----------------------------------|
| Введите свой возраст: 55 | Вы находитесь на уровне "Мудрости" |

---

### [Задание 4](task_4.py)

Напишите программу, которая принимает три целых числа. Выведите наибольшее из чисел, если числа равны, выведите
соответствующее сообщение.

Примечание: Нельзя использовать встроенную функцию `max()`.

**Примеры:**

| Ввод                                                                                              | Вывод               |
|:--------------------------------------------------------------------------------------------------|:--------------------|
| Введите первое целое число: 4</br>Введите второе целое число: 9</br>Введите третье целое число: 2 | Наибольшее число: 9 |

| Ввод                                                                                                   | Вывод                |
|:-------------------------------------------------------------------------------------------------------|:---------------------|
| Введите первое целое число: -3</br>Введите второе целое число: -17</br>Введите третье целое число: -89 | Наибольшее число: -3 |

| Ввод                                                                                              | Вывод           |
|:--------------------------------------------------------------------------------------------------|:----------------|
| Введите первое целое число: 7</br>Введите второе целое число: 7</br>Введите третье целое число: 7 | Все числа равны |

---

### [Задание 5](task_5.py)

Напишите программу, которая запрашивает у пользователя целое число и выводит сообщение в зависимости от следующих
условий:

* Если число четное, выведите сообщение `"Число <число> является четным"`;
* Если число нечетное и результат умножения числа на 3 больше 20, выведите
  сообщение `"Результат умножения <число> на 3 больше 20"`;
* Во всех остальных случаях выведите сообщение `"Число <число> не соответствует условиям"`.

Примечание: Обязательно используйте оператор моржа `:=`.

**Примеры:**

| Ввод                   | Вывод                   |
|:-----------------------|:------------------------|
| Введите целое число: 4 | Число 4 является четным |

| Ввод                   | Вывод                                |
|:-----------------------|:-------------------------------------|
| Введите целое число: 7 | Результат умножения 7 на 3 больше 20 |

| Ввод                   | Вывод                             |
|:-----------------------|:----------------------------------|
| Введите целое число: 5 | Число 5 не соответствует условиям |

---

### [Задание 6](task_6.py)

Приветствуем вас в Хроноакадемии - школе магии и времени!

Ваша первая задача - расшифровать магический кристалл, который раскрывает тайны годов и месяцев.
Введите год и месяц, чтобы узнать, является ли год високосным и имеет ли месяц 31 день.

Магический кристалл скрыт в секретной пещере и обладает своими законами.
По древним преданиям, високосные года придают особую магию времени.

Для определения високосности года используйте следующие правила:

* Год, который делится на 4 без остатка, считается високосным, но есть нюанс...
* Если год делится на 100 без остатка, он не является високосным, но...
* Если год делится на 400 без остатка, то он все-таки високосный!

А месяцы с 31 днем пронизаны магией времени, и в них сокрыты силы и возможности.

Если год високосный и месяц имеет 31 день, то магический кристалл раскроет свои секреты, и на экране
вы увидите слово `"Да"`. Если же хотя бы одно из условий не соблюдается, магический кристалл останется
нерасшифрованным, и на экране отобразится слово `"Нет"`.

**Примеры:**

| Ввод                                          | Вывод |
|:----------------------------------------------|:------|
| Введите год: 2028</br>Введите номер месяца: 6 | Нет   |

Объяснение: Год 2028 является високосным, но месяц июнь имеет только 30 дней, поэтому условие не выполняется.

| Ввод                                          | Вывод |
|:----------------------------------------------|:------|
| Введите год: 2100</br>Введите номер месяца: 4 | Нет   |

Объяснение: Год 2100 не является високосным, и апрель имеет только 30 дней, поэтому условие не выполняется.

| Ввод                                           | Вывод |
|:-----------------------------------------------|:------|
| Введите год: 2400</br>Введите номер месяца: 12 | Да    |

Объяснение: Год 2400 является високосным, и декабрь имеет 31 день, поэтому оба условия выполняются.

---

### [Задание 7](task_7.py)

На вход программе подается три значения: целое число, дробное число и строка. Если все значения истинны, выведите
`"Да"`. Если хотя бы одно значение ложно, выведите `"Нет"`.

Примечание: Нельзя использовать логический оператор `and`.

**Примеры:**

| Ввод                                                                                   | Вывод |
|:---------------------------------------------------------------------------------------|:------|
| Введите целое число: -56 </br>Введите дробное число: 1E9</br>Введите строку: Developer | Да    |

Объяснение: Все три значения истинны, поэтому выводится "Да".

| Ввод                                                                                           | Вывод |
|:-----------------------------------------------------------------------------------------------|:------|
| Введите целое число: 190</br>Введите дробное число: 0.0</br>Введите строку: Frontend & Backend | Нет   |

Объяснение: Хотя целое число и строка истинны, дробное число является ложным, поэтому выводится "Нет".

---

### [Задание 8](task_8.py)

Вы попали в мир, где числа оживают и математика пронизана волшебством.
Введите два числа и выберите магическую операцию: "Призыв", "Трансформация", "Исчезновение" или "Объединение".

Магический артефакт выполнит выбранную операцию над числами и раскроет перед вами результат.

* `"Призыв"` соединит числа в магический портал и покажет сумму их магических сил;
* `"Трансформация"` превратит первое число в другое измерение и покажет его новую форму;
* `"Объединение"` соединит числа, создавая новую магическую энергию, которая будет равна произведению чисел;
* `"Исчезновение"` уменьшит первое число до нуля, ослабляя его магическую сущность.

Важно: При выборе операции `"Исчезновение"`, учтите, что второе число не должно быть равным нулю,
иначе магия оказывается несбалансированной.

**Примеры:**

| Ввод                                                                                         | Вывод                            |
|:---------------------------------------------------------------------------------------------|:---------------------------------|
| Введите первое число: 10</br>Введите второе число: 7</br>Введите магическую операцию: Призыв | Сумма магических сил чисел: 17.0 |

| Ввод                                                                                                  | Вывод                          |
|:------------------------------------------------------------------------------------------------------|:-------------------------------|
| Введите первое число: 23</br>Введите второе число: -43</br>Введите магическую операцию: Трансформация | Трансформированное число: 66.0 |

| Ввод                                                                                               | Вывод                            |
|:---------------------------------------------------------------------------------------------------|:---------------------------------|
| Введите первое число: 12</br>Введите второе число: 0</br>Введите магическую операцию: Исчезновение | Ошибка: Второе число равно нулю! |

| Ввод                                                                                       | Вывод                         |
|:-------------------------------------------------------------------------------------------|:------------------------------|
| Введите первое число: 5</br>Введите второе число: 5</br>Введите магическую операцию: Супер | Ошибка: Некорректная операция |

---

### [Задание 9](task_9.py)

На вход программе подается три значения: целое число, дробное число и строка.
Если хотя бы одно значение истинно, выведите `"Да"`. В противном случае выведите `"Нет"`.

Примечание: Нельзя использовать логический оператор `or`.

**Примеры:**

| Ввод                                                                      | Вывод |
|:--------------------------------------------------------------------------|:------|
| Введите целое число: 0</br>Введите дробное число: 0.0</br>Введите строку: | Нет   |

Объяснение: Все три значения ложны, поэтому выводится "Нет".

| Ввод                                                                             | Вывод |
|:---------------------------------------------------------------------------------|:------|
| Введите целое число: 0</br>Введите дробное число: 0.0</br>Введите строку: Junior | Да    |

Объяснение: Целое число 0 и дробное число 0.0 ложны, но строка "Junior" истинна, поэтому выводится "Да".

---

### [Задание 10](task_10.py)

Уважаемый разработчик, перед вами стоит реализация важной программы **"Буква-Детектив"**.
Её задача - определить, является ли введенная буква гласной или согласной.

Программа должна работать следующим образом:

1. Сначала пользователь выбирает алфавит:
    * Если выбран алфавит `"Латинский"`, программа продолжает работу с латинским алфавитом.
    * Если выбран алфавит `"Кириллица"`, программа продолжает работу с кириллическим алфавитом.
    * Если выбран некорректный алфавит, программа выводит сообщение
      `Упс! Выбран неверный режим. Попробуйте ещё раз..."` и завершает свою работу.
2. После выбора алфавита, программа запрашивает у пользователя ввести букву.
3. Если введенная буква является гласной в выбранном алфавите, программа
   выводит сообщение `"<буква> - гласная буква!"`.
4. Если введенная буква является согласной в выбранном алфавите, программа выводит
   сообщение `"<буква> - согласная буква!"`.
5. Если введенная буква не найдена в выбранном алфавите, программа выводит
   сообщение `"Упс! Неизвестная буква. Попробуйте другую!"` и завершает свою работу.

Примечание: Гарантируется, что на вход программе буквы будут подаваться в верхнем регистре.

Удачи в реализации программы!

**Примеры:**

| Ввод                                                                                                                                                                                    | Вывод               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| Добро пожаловать в программу "Буква-Детектив"!</br></br>Выберите алфавит:</br>1. Латинский</br>2. Кириллица</br></br>Введите номер алфавита: 1</br>Введите букву латинского алфавита: J | J - согласная буква |

| Ввод                                                                                                                                                                          | Вывод              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Добро пожаловать в программу "Буква-Детектив"!</br></br>Выберите алфавит:</br>1. Латинский</br>2. Кириллица</br></br>Введите номер алфавита: 2</br>Введите букву кириллицы: Ы | Ы - гласная буква! |

| Ввод                                                                                                                                                                                    | Вывод                                      |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| Добро пожаловать в программу "Буква-Детектив"!</br></br>Выберите алфавит:</br>1. Латинский</br>2. Кириллица</br></br>Введите номер алфавита: 1</br>Введите букву латинского алфавита: Ж | Упс! Неизвестная буква. Попробуйте другую! |

---