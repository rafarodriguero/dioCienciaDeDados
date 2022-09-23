MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("INFORME SUA IDADE: "))

if idade >= MAIOR_IDADE:
    print("Maior Idade, pode retirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior Idade, pode retirar a CNH")
else:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior Idade, pode retirar a CNH")
elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
    print("Pode realizar aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH.")
