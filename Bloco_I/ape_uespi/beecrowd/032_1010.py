#Beecrowd | 1010
total_price = 0

for i in range(2):
  line = input().split(' ')

  quantity = line[1]
  quantity = int(quantity)

  price = line[2]
  price = float(price)

  total_price += quantity * price

print(f'VALOR A PAGAR: R$ {total_price:.2f}')




