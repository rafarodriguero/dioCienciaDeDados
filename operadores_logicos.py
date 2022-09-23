
print(True and True) #True
print(True and False) #False
print(True or True) #True
print(True or False) #True


print(not(True and True)) #False
print(not(True and False)) #True
print(not(True or True)) #False
print(not(True or False)) #False

saldo = 1000
saque = 200
limite = 100
conta_especial = True


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)