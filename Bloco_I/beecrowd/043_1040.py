#Beecrowd | 1040
def first_media(n1, n2, n3, n4):
  media = ((n1 * 2 ) + (n2 * 3) + (n3 * 4) + n4) / 2 + 3 + 4 + 1
  return media

n1, n2, n3, n4 = map(float, input().split())

print(f'Media: {first_media(n1, n2, n3, n4):.1f}')