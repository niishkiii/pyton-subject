
while True:
 try:
    a = input("Введите ваш возраст: ")
    if int(a) < 18:
        print("Доступ запрещен.")
        break
    elif int(a) >= 18:
        print("Доступ разрешен.")
        break
    else:
        raise ValueError
 except ValueError:
    continue