def main():
    print("01 - Reserva de bilhete")
    print("02 - cancelamento de bilhete")
    print("03 - Verificacao de reserva")
    print("04 - Exibicao de passageiros")

    passageiros = []

    opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))

    for i in range(0, 15):
        if opcao == 0o1:
            nome = str(input("Qual o nome do passageiro? "))
            passageiros.append(nome)
            print(passageiros)
            opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))

        elif opcao == 0o2:
            nome_apaga = str(input("Qual nome que deseja cancelar? "))
            passageiros.remove(nome_apaga)
            print(passageiros)
            opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))

        elif opcao == 0o3:
            nome_consulta = str(input("Qual nome deseja consultar? "))
            posicao = passageiros.index(nome_consulta)
            print("O passageiro: ", nome_consulta, ", ja consta na lista, ", passageiros, ", na posicao: ", posicao + 1)
            opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))

        elif opcao == 0o4:
            print("A lista de passageiros em ordem alfabetica: ")
            print(sorted(passageiros))
            opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))

        else:
            print("Opcao errada!")
            opcao = int(input("Escolha uma opcao(01, 02, 03, 04)"))


main()
