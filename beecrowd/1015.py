v1 = input().split()
x1 = float(v1[0])
y1 = float(v1[1])
v2 = input().split()
x2 = float(v2[0])
y2 = float(v2[1])
distancia = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f'{distancia:.4f}')