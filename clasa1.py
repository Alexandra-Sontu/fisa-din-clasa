from random import randint

nr=int(input('Introduceti numarul:'))
nr -=1
max=randint(1,20)
while nr>0: 
    a=randint(1,20)
    if a>max:
        max=a
    nr -=1
print('Cea mai mare valoare este',max)



