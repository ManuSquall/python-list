# Ecrire un programme qui permet de remplir un tableau d' entiers. Le programme affiche les 
# valeurs  saisies  puis  détermine  et  affiche  le  pourcentage  de  présence  de  chaque  valeur  du 
# tableau.

T=[]
rep="oui"
while rep=="oui":

    print("Saisissez l'entier ", len(T)+1," de T")
    T.append(input())
    rep=""

    while rep!="oui" and rep!="non":
        print("Voulez vous saisir un entier? [oui / non]")
        rep=input()

print()
print("Affichage")
print(T)

#   pourcentage de présence de chaque valeur
# trouve=False
# cpt=0
for i in range(len(T)):
    trouve=0
    for j in range(len(T)):
        if T[i]==T[j]:
            trouve=1
    cpt=0
    if (trouve==0):
        for x in range(len(T)):
            if T[i]==T[x]:
                cpt=cpt+1
    print()
    print()
    print("===============")
    print()
    print(T[i]," est présent ",cpt," fois" )


