#Beecrowd | 1022
expressions = int(input())

while expressions > 0:
  expressions -= 1

  n1, _, d1, oper, n2, _, d2 = input().split() #criou várias variáveis for once

  n1 = int(n1)
  d1 = int(d1)
  n2 = int(n2)
  d2 = int(d2)

  if oper == '+':
    nr = (n1*d2 + n2*d1)
    dr = d1*d2
  elif oper == '-':
    nr = (n1*d2 - n2*d1)
    dr = d1*d2
  elif oper == '*':
    nr = n1*n2
    dr = d1*d2
  elif oper =='/':
    nr = n1 * d2
    dr = d1 * n2
  #nr = numerador de resultado 
  #dr = denominador do resultado

  ns = nr #ns = numerador simplificado 
  ds = dr #ds = denominador simplificado

  div = 2
  div_max = min(nr, dr)

  while div >= div_max:
    if (ns % div == 0) and (ds % div == 0):
      ns = ns // div
      ds = ds // div 
    else:
      div += 1
  
  print(f'{nr}/{dr} = {ns}/{ds}')
