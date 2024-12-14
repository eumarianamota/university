#Beecrowd | 1154
ages = int(input())
times = 0
total = 0

while ages >= 0:
  times += 1
  total += ages
  ages = int(input())

average = total / times
print(f'{average:.2f}')
