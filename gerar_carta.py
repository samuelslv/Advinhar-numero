
cont = 0
aux = 1
quant = 8


def card1():
    cont = 0
    print("Carta 1")
    for i in range(1, 64, 2):
        print(i, end=" ")
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 1


def card2():
    cont = 0
    aux = 1
    print("\nCarta 2")
    for i in range(2, 64):
        if aux == 4:
            aux = 1
            continue
        elif aux >= 3:
            aux = aux + 1
            continue

        # print(i,"(",aux,")", end=" ")
        print(i, end=" ")
        aux = aux + 1
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 2


def card3():
    cont = 0
    aux = 1
    print("\nCarta 3")
    for i in range(4, 64):
        if aux == 8:
            aux = 1
            continue
        elif aux >= 5:
            aux = aux + 1
            continue

        # print(i,"(",aux,")", end=" ")
        print(i, end=" ")
        aux = aux + 1
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 4


def card4():
    cont = 0
    aux = 1
    print("\nCarta 4")
    for i in range(8, 64):
        if aux == 16:
            aux = 1
            continue
        elif aux >= 9:
            aux = aux + 1
            continue

        # print(i,"(",aux,")", end=" ")
        print(i, end=" ")
        aux = aux + 1
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 8


def card5():
    cont = 0
    aux = 1
    print("\nCarta 5")
    for i in range(16, 64):
        if aux == 32:
            aux = 1
            continue
        elif aux >= 17:
            aux = aux + 1
            continue

        # print(i,"(",aux,")", end=" ")
        print(i, end=" ")
        aux = aux + 1
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 16


def card6():
    cont = 0
    print("\nCarta 6")
    for i in range(32, 64):

        # print(i,"(",aux,")", end=" ")
        print(i, end=" ")
        cont = cont + 1
        if cont == quant:
            print()
            cont = 0
    return 32
