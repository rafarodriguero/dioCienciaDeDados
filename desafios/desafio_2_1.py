letra = input() 


# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i,caracter in enumerate(alfabeto):
  
  if caracter == letra.upper():
    print(f"Posição: {i + 1}")