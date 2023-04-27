while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")
    odp = input("Podaj działanie\t")
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwsza liczbe"))
        b = int(input("Podaj drugą liczbe"))
        if odp == '1':
            print("Dodawanie", a + b)
        elif odp == '2':
            print("Odejmowanie", a - b)
        elif odp == '3':
            print("Mnożenie", a * b)
        elif odp == '4':
            print("Dzielenie", a / b)
        else:
            print("Nie ma takiego działania")

    except ValueError:
        print("Bład wartości")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Bład", e)
    else:  # elsy gdzy nie ma błedu
        print("Czasami")
    finally:  # zawsze
        print("Zawsze")
# 13:20 