def float_to_currency(value):
  man, dec = map(int, f'{value:.2f}'.split('.'))

  thousands = []
  while True:
    thousands.insert(0, str(man % 100))
    man = man // 1000
    if man == 0:
      break

  man = '.'.join(thousands)
  return f'R${man},{dec}'