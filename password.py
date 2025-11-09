import random   # для случайных чисел
import string   # содержит буквы, цифры и символы

# --- просим пользователя ввести длину пароля ---
length = input("Введите длину пароля: ")

# проверяем, что пользователь ввёл число
if not length.isdigit():
    print("Ошибка: нужно ввести число!")
else:
    length = int(length)  # превращаем строку в число

    # набор символов: буквы, цифры, спецсимволы
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # создаём пароль нужной длины
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # выводим результат
    print("Ваш пароль:", password)
