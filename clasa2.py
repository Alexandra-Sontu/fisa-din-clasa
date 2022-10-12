from random import randint
nr=int(input('Introduceti numarul:'))
bile_albe,bile_negre=0,0
while nr>0:
    x=randint(1,2)
    if x==1:
        bile_albe +=1
    else:
        bile_negre+=1
    nr -=1
    print('Bile albe au fost extrase',bile_albe)
    print('Bile negre au fost extrase',bile_negre)