from random import randint
n=['Alina','Maria','Maxim','Nicoleta','Alexandru','Ionela','Andrei','Ana']
print('Elevii sunt:',n)
x=input('Introdu numele cautat:')

def cautare():
    if x in n:
        return True
    if x not in n:
        return False
print('Numele se afla in lista',cautare())