def password_level(l):
    if len(l) < 8:
        return ("Недопустимый пароль")
    if l.isdigit() == True or l.isupper() == True or l.islower() == True:
        return ("Ненадежный пароль")
    if l.isalpha() == True:
        return ("Слабый пароль")
    else:
        return ("Надежный пароль")

p = ""
while p != "Надежный пароль":
    password = str(input("Придумайте пароль: "))
    p = password_level(password)
    print(p)

password_1 = ""
while password != password_1:
    password_1 = str(input("Подтвердите пароль: "))
    if password != password_1:
        print("Пароли не совпадают")
