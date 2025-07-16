def sequence(nbr):
    seq='1'
    suiv=""
    compt=0
    if nbr<0:
        print("impossible")
        return None
    elif nbr==1:
        print(seq)
    else:
        print(seq)
        for i in range (nbr):
            rep=seq[0]
            j=0
            compt=0
            suiv=""
            while j<len(seq):
                while j<len(seq):
                    if seq[j]==rep:
                        compt+=1
                        j+=1
                    else:
                        break
                suiv+=str(compt)+rep
                if j<len(seq):
                    rep=seq[j]
                    compt=0
            seq=suiv
            print(suiv)
