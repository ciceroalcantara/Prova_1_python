def main():
    print("1 - Reserva de bilhete")
    print("2 - Cancelamento de bilhete")
    print("3 - Verificacao de reserva")
    print("4 - Exibicao de passageiros")

    passageiros = []

    opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))

    while main != 4:
        if opcao == 1:
            nome = str(input("Qual o nome do passageiro? "))
            passageiros.append(nome)
            print(passageiros)
            opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))

        elif opcao == 2:
            nome_apaga = str(input("Qual nome que deseja cancelar? "))
            passageiros.remove(nome_apaga)
            print(passageiros)
            opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))

        elif opcao == 3:
            nome_consulta = str(input("Qual nome deseja consultar? "))
            posicao = passageiros.index(nome_consulta)
            print("O passageiro: ", nome_consulta, ", consta na lista, ", passageiros, ", na posicao: ", posicao + 1)
            opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))

        elif opcao == 4:
            print("A lista de passageiros em ordem alfabetica: ")
            print(sorted(passageiros))
            opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))

        else:
            print("Opcao errada!")
            opcao = int(input("Escolha uma opcao(1, 2, 3, 4)"))


main()
