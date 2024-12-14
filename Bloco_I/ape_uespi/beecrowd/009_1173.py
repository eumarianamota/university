#Beecrowd | 1173
n = int(input())

count = 0
for value in range(10):
  print(f'N[{count}] = {n}')
  n *= 2
  value += 1
  count += 1
