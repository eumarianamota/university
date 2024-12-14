#Beecrowd | 1134

purchases ={
  1: 0,
  2: 0,
  3: 0,
}

while True:
  fuel_type = int(input())
  if fuel_type == 4:
    break

  if (fuel_type >= 1) and (fuel_type<= 3):
    purchases[fuel_type] += 1

print(f'MUITO OBRIGADO')
print(f'Alcool: {purchases[1]}')
print(f'Gasolina: {purchases[2]}')
print(f'Diesel: {purchases[3]}')
