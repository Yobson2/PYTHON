from random import *

consigne=[
    "0- pour quitter le programme",
    "1-pour lancez le dés"
]

print(f" cliquez sur : {consigne[0]} ou {consigne[1]}")

while True:
    x=int(input('Entrez un button '))
    if x==0:
        print('Quittez le programme')
        break
    elif x==1:
       print(f'-----{randint(1,6)}-----')

    else:
        print("je n'ai pa compris")
