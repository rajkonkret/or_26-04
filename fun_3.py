a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj_2():
    global a  # uzycie a globalnego i jego zmiana
    a = 6
    b = 7
    print(a + b)


def dodaj_3():
    b = 7
    print(a + b)


def dodaj_4(a):
    b = 7
    print(a + b)


print("Zmienna a z góry", a)
dodaj()
print("Zmienna a z góry", a)
dodaj_2()
print("Zmienna a z góry", a)
dodaj_3()
print("Zmienna a z góry", a)
dodaj_4(a)
print("Zmienna a z góry", a)
