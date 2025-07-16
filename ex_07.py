def get_angry_dog(nbr):
    chaine=''
    for i in range(nbr):
        chaine+="woof"
    chaine+='\n'
    return chaine
        
print(get_angry_dog(9))