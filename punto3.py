# #Punto 3 Población

paisA=25000000
paisB=18900000
año=2022
print("\n\nEl país A tiene 25 millones de habitantes, el país B tiene 18,9 millones de habitantes, ¿cuándo superará el país B al país A?")
def taza2(x):
    x=x+((x*2)/100)
    return x
def taza3(x):
    x=x+((x*3)/100)
    return x

while(paisA>paisB):
    paisA=int(taza2(paisA))
    paisB=int(taza3(paisB))
    año+=1

print("En el año",año,"el país B tendrá una población de:",paisB,"superando al país A con una población de:",paisA)