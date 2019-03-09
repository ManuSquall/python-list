# Ecrire un programme qui  permet de remplir  une matrice d’entiers. La saisie des lignes s’arrête lorsque
# l’utilisateur  entre  la  valeur  zéro  (0) et celle des colonnes lorsqu'il entre la valeur -1
#  qui  ne  sera  pas  prise  en  compte  dans  le  tableau.Le 
# programme affiche les valeurs saisies puis détermine et affiche le plus petit nombre supérieur
# à zéro et le plus grand nombre inférieur à zéro s’ils existent



M=[]
minsup=0    #plus petit nombre superieur a zero
maxinf=0    #plus grand nombre inférieur a zero

c=-2
while c!=0:
    C=[]
    c=-2
    while c!=-1 and c!=0:
        c=int(input("Entrez la valeur de la colonne"))
        if(c!=0 and c!=-1):
            #########################################
            #   determination du minsup
            if(c>0):
                if(minsup==0):
                    minsup=c
                else:
                    if(c<minsup):
                        minsup=c
            
            #   deteermination du maxinf
            if(c<0):
                if maxinf==0:
                    maxsup=c
                else:
                    if(c>maxinf):
                        maxinf=c

            #########################################
            C.append(c)
    M.append(C)

print()
print()
###########################################################""
print("Affichage")

for i in range(len(M)):
    C=M[i]
    for j in range(len(C)):
        print(C[j], " | ", end="")
    print()
    for j in range(len(C)):
        print("____", end="")
    print()
    
###############################################################
print()
print("=================================")
print()
#   affichage du minsup et maxinf
if(maxinf==0):
    print("Pas de plus grand nombre inférieur a zero")
else:
    print("Plus grand nombre inférieur a zero = ", maxinf)
print()
if(minsup==0):
    print("Pas de plus petit nombre superieur a zero")
else:
    print("Plus petit nombre superieur a zero = ", minsup)








