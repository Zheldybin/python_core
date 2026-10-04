password = "Python123"
n = 1
while n <= 3:
    input_password = input("Введите пароль:")
    if input_password == password:
        print("Успешная авторизация")
        break
    elif n < 3:
        print(f"Не успешно попробуй еще раз. Осталось попыток {3 - n}")
    else:
        print("Доступ заблокирован")
    n += 1
