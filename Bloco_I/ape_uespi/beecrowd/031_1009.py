#Beecrowd | 1009
name = input()
salary = float(input())
sells_per_month = float(input())

percentage = (sells_per_month / 100) * 15

full_salary = percentage + salary

print(f'TOTAL = R$ {full_salary:.2f}')