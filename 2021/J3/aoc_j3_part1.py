# coding:utf-8


fic = open("input.txt", "r")

cpt = 0
epsilon = ""
gamma = ""
l = fic.read().split("\n")

for i in range(len(l[0])):
	for val in l:
		if val[i] == '1':
			cpt += 1
	if cpt > (len(l)/2):
		gamma += "1"
	else:
		gamma += "0"
	cpt = 0

for bit in gamma:
	if bit == '0':
		epsilon += "1"
	else:
		epsilon += "0"

print("gamma = ", gamma, "\tepsilon = ", epsilon)
print("gamma = ", int(gamma, 2), "\tepsilon = ", int(epsilon, 2))
print("Answer: ", int(gamma, 2)*int(epsilon, 2))

fic.close()
