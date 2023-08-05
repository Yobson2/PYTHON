import numpy as np
affiche=["Entrez A pour la matrice A","Entrez B pour la matrice B"]

print(f'Choisir une matrice :{affiche[0]}---{affiche[1]} ')

def multi_matrice(A,B):
   return A.dot(B)


while True:
    data=input('')
    if data=="A":
       A=input(np.array())
    elif data=="B":
         A=input(np.array())
    else:
        print(f"Quitter l'application")
        
multi_matrice(A,B)
