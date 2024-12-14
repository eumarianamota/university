#Beecrowd | 1036
from math import sqrt

a, b, c = map(float, input().split())

delta =(b ** 2) - (4 * a * c)

minus_b = b * - 1

if (delta < 0):
  print('Impossivel calcular')

elif a == 0:
    print('Impossivel calcular')

elif (sqrt(delta) + minus_b == 0) or (sqrt(delta) - minus_b == 0):
    print('Impossivel calcular')

else:
  root1 = (minus_b + sqrt(delta)) / (2 * a)
  root2 = (minus_b - sqrt(delta)) / (2 * a)

  print(f'R1 = {root1:.5f}')
  print(f'R2 = {root2:.5f}') 
