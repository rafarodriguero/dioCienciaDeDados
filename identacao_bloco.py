def sacar(valor):
    
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("Valor Sacado!")
        print("Retire seu dinheiro do caixa eletrônico")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo +=valor
    print(saldo)

sacar(400)

depositar(300)