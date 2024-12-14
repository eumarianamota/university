#Beecrowd | 1021
value = float(input())

cents = int(round(value * 100))

notes = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for note in notes:
    quantity = cents // note
    print(f"{quantity} nota(s) de R$ {note / 100:.2f}")
    cents %= note

print("MOEDAS:")
for coin in coins:
    quantity = cents // coins
    print(f"{quantity} moeda(s) de R$ {coin / 100:.2f}")
    cents %= coin