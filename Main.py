# advinar numero
import gerar_carta as carta
import gerar_carta_NEW as new
import os


def main():
    soma = 0
    x = 0

    print("Pense em um numero de 1 até 63")

    x = carta.card1()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    x = carta.card2()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    x = carta.card3()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    x = carta.card4()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    x = carta.card5()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    x = carta.card6()
    opc = input("O seu numero esta nessa sequencia? S ou N: ")
    if (opc == "S" or opc == "s"):
        soma = soma + x

    print(f"O NUMERO QUE VOCE PENSOU FOI O {soma}")


def mainMELHOR():

    soma = 0
    x = 0
    pos = 1
    step = 2
    os.system('cls')
    print("PENSE EM UM NUMERO DE 1 ATÉ 63")

    for carta in range(1, 33):

        if carta in (2, 4, 8, 16):
            x = new.cards(carta, pos)
            opc = input("O seu numero esta nessa sequencia? Sim ou Não: ")
            if (opc == "Sim" or opc == "sim" or opc == "s" or opc == "S"):
                soma = soma + x
            pos = pos + 1
            os.system('cls')

        elif carta in (1, 32):
            x = new.card_1E6(carta, pos, step)
            step = step - 1
            opc = input("O seu numero esta nessa sequencia? Sim ou Não: ")
            if (opc == "Sim" or opc == "sim" or opc == "s" or opc == "S"):
                soma = soma + x
            pos = pos + 1
            os.system('cls')
        else:
            os.system('cls')
            continue

    print(f"\nO NUMERO QUE VOCE PENSOU FOI O {soma}\n")


if __name__ == "__main__":
    # main()
    mainMELHOR()
