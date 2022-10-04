def reajuste_salario (salario, reajuste):
  print(str(f"Novo salario: {salario + (salario * reajuste): .2f}").replace(".",","), end=" ")
  print(str(f"Reajuste ganho: {salario * reajuste: .2f}").replace(".",","), end=" ")
  print(str(f"Em percentual: {(reajuste): .0%}").replace(".",","))
  #novo_salario = str(f"{salario + (salario * reajuste): .2f}").replace(".",",")
  #reajuste_salario = str(f"{salario * reajuste: .2f}").replace(".",",")
  #percentual = str(f"{reajuste: .0%}").replace(".",",")
  #print("Novo salario: ",novo_salario," Reajuste ganho: ",reajuste_salario," Em percentual: ",percentual)

salario = int(input()) 

if ((salario > 0) and (salario <= 600)):
  reajuste_salario(salario, 0.17)

elif ((salario > 600) and (salario <= 900)):
  reajuste_salario(salario, 0.13)
  
elif ((salario > 900) and (salario <= 1500)):
  reajuste_salario(salario, 0.12)

elif ((salario > 1500) and (salario <= 2000)):
  reajuste_salario(salario, 0.10)

else: 
  reajuste_salario(salario, 0.05)