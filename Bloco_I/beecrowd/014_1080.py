#Beecrowd | 1080
n = 100
max_number = 0

for index in range(1, n+1):
  number = int(input())
  if number > max_number:
    max_number = number
    max_index = index
  

print(max_number)
print(max_index)