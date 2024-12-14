#Beecrowd | 1045
def type_triangle(a, b, c):
  if a >= (b + c):
    return 'NAO FORMA TRIANGULO'
  elif a**2 == (b**2 + c**2):
    return 'TRIANGULO RETANGULO'
  elif a**2 > (b**2 + c**2):
    return 'TRIANGULO OBTUSANGULO'
  elif a**2 < (b**2 + c**2):
    return 'TRIANGULO ACUTANGULO'
  
def face_triangle(a, b, c):
  if a == b and b == c:
    return 'TRIANGULO EQUILATERO'
  elif a == b or a == c or b == c:
    return 'TRIANGULO ISOSCELES'
  else:
    return


numbers = input().split()

numbers_float = [float(number) for number in numbers]

numbers_float = sorted(numbers_float)

a = float(numbers_float[-1])
b = float(numbers_float[1])
c = float(numbers_float[0])

print(type_triangle(a, b, c))

result = face_triangle(a, b, c)
if result is not None:
  print(result)

