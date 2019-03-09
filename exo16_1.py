# Ecrire un programme qui  permet de remplir  une matrice d’entiers. La saisie des lignes s’arrête lorsque
# l’utilisateur  entre  la  valeur  zéro  (0) et celle des colonnes lorsqu'il entre la valeur -1
#  qui  ne  sera  pas  prise  en  compte  dans  le  tableau.  Le 
# programme affiche les valeurs saisies puis détermine et affiche le p



M=[]

b=-2
while b!=0:
    b=int(input("Entrez la valeur de la colonne"))
    if(b!=0):
        M.append(b)

for i in range(len(M)):
    print(M[i]," | ", end="")
    







