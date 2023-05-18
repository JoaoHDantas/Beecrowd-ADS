fim  = int(input())
for tempo in range (1, fim+1):
    resultado = 0
    n1, n2, n3 = map(float,input().split())

    resultado = ((n1*2)+(n2*3)+(n3*5))/10
    print(f'{resultado:.1f}')
