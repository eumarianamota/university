#Beecrowd | 1131
#Função para verificar se a partida deu empate ou definir o vitorioso
def vitoria(lista):
  inteiros = [int(x) for x in lista] #Fazer uma lista de numeros inteiros
  lista = inteiros

  if lista[0] > lista[-1]:
    return "inter"
  elif lista[0] < lista[1]:
    return "gremio"


#Função para definir quem foi o vitorioso de todas as partidas
def vitorioso(inter, gremio):
  if inter > gremio:
    return "Inter venceu mais"
  else:
    return "Gremio venceu mais"


repeticao = 1
grenais = 0
inter = 0
gremio = 0
empate = 0

while repeticao == 1:
  gols = input().split()

  if vitoria(gols) == "inter":
    inter += 1
  elif vitoria(gols) == "gremio":
    gremio += 1
  else:
    empate += 1

  grenais += 1

  repeticao = int(input('Novo grenal (1-sim 2-nao)\n'))

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
print(f'{vitorioso(inter, gremio)}')