#Beecrowd | 3174
elfos = int(input())

bonecos = 0
desenhistas = 0
arquitetos = 0
musicos = 0

for i in range(elfos):
  name, group, hours = input().split()
  hours = int(hours)

  if group == 'bonecos':
    bonecos += hours
  elif group == 'arquitetos':
    arquitetos += hours
  elif group == 'musicos':
    musicos += hours
  elif group == 'desenhistas':
    desenhistas += hours

brinquedos = 0

brinquedos += bonecos // 8
brinquedos += desenhistas // 12
brinquedos += arquitetos // 4
brinquedos += musicos // 6

print(brinquedos)