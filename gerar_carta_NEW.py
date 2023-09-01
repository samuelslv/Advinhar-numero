cont = 0
aux = 1
quant = 8


def card_1E6(card, num_card, step):
    cont = 0

    print(f"\n Carta {num_card}")

    for i in range(card, 64, step):
        print(i, end=" ")
        cont = cont + 1

        if cont == quant:
            print()
            cont = 0

    return card


def cards(card, num_card):
    cont = 0
    aux = 1

    print(f"\n Carta {num_card}")

    for i in range(card, 64):
        if aux == card*2:
            aux = 1
            continue
        elif aux >= card+1:
            aux = aux + 1
            continue

        print(i, end=" ")
        aux = aux + 1
        cont = cont + 1

        if cont == quant:
            print()
            cont = 0

    return card
