#coding:utf-8


def compteur (liste):
    cpt = 0
    for i, depth in enumerate(liste):
        if i == 0:
            print(depth, " (N/A - no previous measurement)")
        else:
            if depth > liste[i-1]:
                cpt += 1
                print(depth, " (increased)")
            else:
                print(depth, " (decreased)")
    return cpt

fic = open("input.txt", "r")

str_liste = fic.read().splitlines()
liste = list(map(int, str_liste))
groupes = list()

for i, depth in enumerate(liste):
    if i != 0 and i != 1:
        groupes.append(liste[i-2] + liste[i-1] + depth)

print("Answer: ", compteur(groupes))

fic.close()