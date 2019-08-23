def main():
    folhas = int(input("Quantas cópias você deseja? "))

    if folhas > 100:
        print("O total a ser pago é: ", folhas * 0.20)
    else:
        print("O total a ser pago é: ", folhas * 0.25)


main()

