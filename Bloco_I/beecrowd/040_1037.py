#Beecrowd | 1037

value = float(input())
if value < 0:
  result = f'Fora de intervalo'
elif value <= 25:
  result =  f'Intervalo [0,25]'
elif value <= 50:
  result =  f'Intervalo (25,50]'
elif value <= 75:
  result = f'Intervalo (50,75]'
elif value <= 100:
  result =  f'Intervalo (75,100]'
elif value > 100:
  result = f'Fora de intervalo'

print(result)