#Beecrowd | 1164
def divisores(value):
  test = 1 
  full_value = 0

  while test < value: 
    if value % test == 0:
      full_value += test

    test += 1
  
  return full_value

enter =  int(input())  

for i in range(enter):
  value = int(input())

  if divisores(value) == value:
    print(f'{value} eh perfeito')
  else:
    print(f'{value} nao eh perfeito')
