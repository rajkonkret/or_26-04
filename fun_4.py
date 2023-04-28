# funkcje zagnieżdzone
def fun1():
    print("To jest fun1")

    def fun2():  # funkcja zagniezdzona, dostepna tylko z fun1()
        print("To jest fun2")

    return fun2  # bez nawiasów


xFun = fun1()  # teraz tutaj mamy fun2
print(xFun)
print(type(xFun))  # <class 'function'>
# jak wywołujemy funkcje
xFun()  # wywołanie funkcji w xFun czyli dodanie nawiasów() -> xFun()
