secret_number = 37
n = 1
while True:
    number_user = int(input("Введи число чтобы угадать загаданное: "))
    if number_user > secret_number:
        print(f"Введи число меньше чем {number_user}")
    elif number_user < secret_number:
        print(f"Введи число больше чем {number_user}")
    else:
        print(f"Ты угадал. Использовано {n} попыток")
        break
    n += 1
