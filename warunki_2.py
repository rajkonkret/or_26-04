lista = []

lang = input("Wpisz znany Ci język programowania")
match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # domyslne działanie (taki troche else)
        print("Nie znam takiego języka")

print(lista)
# from_ = "z"

