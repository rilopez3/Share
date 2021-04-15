import random
def LifeDeath():
  u = random.randint(1,2) 
  if u == 1:
    return 'Vida'
  else:
    return 'Muerte'


def AllForOne():
  if random.randint(1,6) == 6:
    return 'Uno'
  else:
    return 'Todos'

def MagicN(k):
  return random.randint(1,k)


def DoublePay():
  suma = 0   
  ok = True  
  while ok:
    x1 = random.randint(1,5)
    x2 = random.randint(1,5) 
    suma = suma + x1 + x2
    if x1 != x2:
      ok = False
  return suma

def MasterK(k):
  d = 0 
  f = True 
  while f:
    d = d + 1
    x = random.randint(1,k)
    if x == 1:
      f = False
  return d