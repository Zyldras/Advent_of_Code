#coding:utf-8


fic = open("input.txt", "r")

l = fic.read().splitlines()
li = list()
liste = list()
direction = 0
depth = 0
aim = 0

for val in l:
  v = val.split(' ')
  liste.append([v[0], int(v[1])])

for val in liste:
  if val[0] == 'forward':
    direction += val[1]
    depth += val[1]*(aim)
  if val[0] == 'down':
    aim += val[1]
  if val[0] == 'up':
    aim -= val[1]
  
print("Answer:", depth*direction)

fic.close()