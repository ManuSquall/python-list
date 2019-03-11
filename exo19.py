# Ecrire un programme qui permet de remplir un tableau d' entiers. Le programme affiche les 
# valeurs  saisies  puis  détermine  et  affiche  le  nombre  de  présence  de  chaque  valeur  du 
# tableau.

T=[]
rep="o"
while rep=="o":

    print("Saisissez l'entier ", len(T)+1," de T")
    T.append(input())
    rep=""

    while rep!="o" and rep!="n":
        print("Voulez vous saisir un entier? [o / n]")
        rep=input()

print()
print("Affichage")
print(T)

#   pourcentage de présence de chaque valeur
#with doublon
# for i in range(len(T)):
#         cpt=T.count(T[i])
#         print()
#         print()
#         print("===============")
#         print()
#         print(T[i]," est présent ", cpt ," fois" )

#without doublon
for i in range(len(T)):
    trouve=False
    j=i+1
    #print("j=",j)
    while(j<len(T)):
        if T[j]==T[i]:
            trouve=True
        j+=1
    if(trouve==False):
        cpt=T.count(T[i])
        print()
        print()
        print("===============")
        print()
        print(T[i]," est présent ", cpt ," fois" )


