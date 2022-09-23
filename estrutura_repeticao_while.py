opcao = -1

while opcao != 0:
    opcao = int(input("Digite:\n[1] Sacar \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando")

    elif opcao == 2:
        print("Extrato...")

    else:
        print("Opção Invalida")
else:
    print("Obrigado por utilizar os serviços")

    