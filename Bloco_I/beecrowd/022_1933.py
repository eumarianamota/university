#Beecrowd | 1933
def melhor_carta(a, b):
  if a > b:
    return a
  elif a < b:
    return b
  else:
    return a

a, b = map(int, input().split()) #receber em duas variáveis diferentes, dois valores inteiros
melhor = melhor_carta(a, b)
print(melhor)

