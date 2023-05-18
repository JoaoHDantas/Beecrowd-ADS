n = int(input())
for tempo in range(1, n+1):
    valor = int(input())
    if (valor%2!=0)and (valor<0):
        print("ODD NEGATIVE")
    if(valor==0):
        print("NULL")
    if(valor%2!=0)and(valor>0):
        print("ODD POSITIVE")
    if(valor%2==0)and(valor<0):
        print("EVEN NEGATIVE")
    if(valor%2==0)and(valor>0):
        print("EVEN POSITIVE")
    