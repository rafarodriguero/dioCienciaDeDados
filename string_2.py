nome = "Rafael"
idade = 40
profissao = "Consultor"
linguagem = "Python"


print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." 
      %(nome, idade, profissao, linguagem))
print()

nome1 = "Renata"
idade1 = 41
profissao1 = "Contadora"
linguagem1 = "Java"

dados = {"nome": nome1, "idade": idade1, "profissao": profissao1, "linguagem": linguagem1}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." 
      .format(nome1, idade1, profissao1, linguagem1))
print()
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." 
      .format(linguagem1, profissao1, idade1,nome1))
print()
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(linguagem = linguagem1, profissao = profissao1, idade = idade1, nome = nome1))
print()
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(**dados))

print()

nome2 = "Theo"
idade2 = 2
profissao2 = "Cachorro"
linguagem2 = "Au Au Au"


print(f"Olá, me chamo {nome2}. Eu tenho {idade2} anos de idade, trabalho como {profissao2} e estou matriculado no curso de {linguagem2}.")
print()

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")