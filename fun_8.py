def allparams(a, b, /, c=42, *arg, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", arg)
    print("kwargs", kwargs)


allparams(1, 2)  # argumenty przekazane pozycyjnie
# allparams(a=1, b=2),bez / zadziała - przekazywanie po nazwie
# / - a, b tylko jako argumenty pozycyjne, nie moze byc podane po nazwie
allparams(1, 2, c=7)  # c moe byc pozycyjne lub nazwane
allparams(1, 2, 7)
allparams(1, 2, 7)
# jak chcemy przekazac parametry jako krotka w tej funkcji to "c"
#  musi byc przekazane pozycyjnie
allparams(1, 2, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 11, 1, 11, 1)
allparams(1, 2, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, d=18)
allparams(1, 2, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, d=18, user='/home')
allparams(1, 2, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, d=18, e=90, user='/home')
