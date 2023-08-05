from random import *

taille=int((input('la longueur du mot de passe: ')))

passworDefault='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

password="".join(sample(passworDefault,taille))

print(password)