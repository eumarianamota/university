#Beecrowd | 1012
def regtangle_triangle(a, c):
  calc = (a * c) / 2
  return f'TRIANGULO: {calc:.3f}'

def circle(c):
  calc = 3.14159 * c**2
  return f'CIRCULO: {calc:.3f}'

def trapezoid(a, b, c):
  calc = ((a + b) * c) / 2
  return f'TRAPEZIO: {calc:.3f}'

def square(b):
  calc = b * b
  return f'QUADRADO: {calc:.3f}'

def regtangle(a, b):
  calc = a * b
  return f'RETANGULO: {calc:.3f}'

values = input().split()
a, b, c = values
a = float(a)
b = float(b)
c = float(c)

calculos = [regtangle_triangle(a, c), circle(c), trapezoid(a, b, c), square(b), regtangle(a, b)]

for calc in calculos:
  print(calc)