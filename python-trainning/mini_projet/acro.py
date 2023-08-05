text=str(input('Entrez un mot:  '))


def acro_word(chaine):
    across=''
    word=''
    word=text.split()
    for i in word:
        across=across+str(i[0]).upper()
    return across

print(f" l'acronime de la phrase est: {acro_word(text)}")
