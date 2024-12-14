#Beecrowd | 1018
value_ini = int(input())
value = value_ini

nota_100 = value // 100
value = value % 100

nota_50 = value // 50
value = value % 50 

nota_20 = value // 20
value = value % 20

nota_10 = value // 10
value = value % 10

nota_5 = value // 5
value = value % 5

nota_2 = value // 2
value = value % 2 

nota_1 = value // 1

print(value_ini)
print(f'{nota_100} nota(s) de R$ 100,00')
print(f'{nota_50} nota(s) de R$ 50,00')
print(f'{nota_20} nota(s) de R$ 20,00')
print(f'{nota_10} nota(s) de R$ 10,00')
print(f'{nota_5} nota(s) de R$ 5,00')
print(f'{nota_2} nota(s) de R$ 2,00')
print(f'{nota_1} nota(s) de R$ 1,00')
