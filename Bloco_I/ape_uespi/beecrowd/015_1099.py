#Beecrowd | 1099
def sum_odds(begin, end):
  sum = 0
  for number in range(min(begin, end) + 1, max(begin, end)):
    if number % 2 == 1:
      sum += number
  return sum

n = int(input())

while n > 0:
  n -= 1
  x, y = input().split()
  odd_sum = sum_odds(int(x), int(y))
  print(odd_sum)