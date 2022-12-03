# coding:utf-8


fic = open("input.txt", "r")

cpt = 0
cpt2 = 0
oxygen = ""
co2 = ""
i = 0
j = 0
l = fic.read().split("\n")
l2 = l.copy()
size = len(l[0])

def majListe (_l, _bit, _i):
  for _val in _l:
    if _val[_i] != _bit:
      _l.remove(_val)

print("l = ", len(l))
while len(l) > 1:
	for i in range(size):
		for val in l:
			if val[i] == '0':
				cpt += 1
		if cpt <= (len(l)/2):
			majListe(l, '0', i)
		else:
			majListe(l, '1', i)
		cpt = 0
		print("l = ", len(l))
		if len(l) <= 1:
			break
co2 = l[0]

print("l2 = ", len(l2))
while len(l2) > 1:
	for j in range(size):
		for val2 in l2:
			if val2[j] == '1':
				cpt2 += 1
		if cpt2 >= (len(l2)/2):
			majListe(l2, "1", j)
		else:
			majListe(l2, "0", j)
		cpt2 = 0
		print("l2 = ", len(l2))
		if len(l2) <= 1:
			break
oxygen = l2[0]

print("l = ", l)
print("l2 = ", l2)

print("CO2 scrubber rating = ", co2, "\toxygen generator rating = ", oxygen)
print("CO2 scrubber rating = ", int(co2, 2), "\t\toxygen generator rating = ", int(oxygen, 2))
print("Answer: ", int(co2, 2)*int(oxygen, 2))

fic.close()
