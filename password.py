import random   
import string   

length = input("Введите длину пароля: ")

# проверка на ввод числа
if not length.isdigit():
    print("Ошибка: нужно ввести число!")
else:
    length = int(length)

    # буквы, цифры, спецсимволы
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # длина пароля
    password = ''.join(random.choice(all_chars) for _ in range(length))

    print("Ваш пароль:", password)
    with open("password.txt", "w") as file:
        file.write(password)
    print("Пароль сохранен в файл password.txt")

