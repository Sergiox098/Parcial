# #punto 2 Operacion n 

num=float(input("\nIngrese un número entero postivo: "))
num=int(num)
def par(x):
    x=x/2
    return x
def impar(x):
    x=3*x+1
    return x

if (num>=0):
    while (num!=1):
        modunum=num%2
        if(modunum==0):
            num=int(par(num))
            print(num,end=" ")
        if(modunum!=0):
            num=int(impar(num))
            print(num,end=" ")
else:
    print("Este no es número entero positivo")