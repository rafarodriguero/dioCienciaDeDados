conta_normal = True
conta_universitaria = False

saldo = 200
saque = 150
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
    
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o gerente")

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
