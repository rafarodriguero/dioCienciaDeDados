situacao_perna = {'esquerda':'inglês', 'direita':'francês', 'nenhuma':'português', 'ambas':'caiu'}

while True: 
    try: 
      
      perna = input()
      
      print(situacao_perna[perna])

      if perna == "ambas":
        break
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
    
    
    except EOFError: 
        break