#Beecrowd | 1150
#recebe os valores x e z
x = int(input())
z = int(input())

#repete o z até ele ser maior que x
while z <= x:
  z = int(input())

#cria uma estrutura de repetição para calcular a quantidade de somas consecutivas necessárias para ultrapassar o z
sum = x
number = 0
while sum < z:
  sum += x + 1
  x += 1
  number += 1

print(number + 1)

