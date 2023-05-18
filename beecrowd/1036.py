valor = input().split()
a = float(valor[0])
b = float(valor[1])
c = float(valor[2])
#descobrindo delta/descobrindo a raiz quadrada
delt = (b**2)-4*a*c
if delt>0 and a != 0:
   #resolver a formula
    x1 = (-b + delt ** (1 / 2)) / (2 * a)
    x2 = (-b - delt ** (1 / 2)) / (2 * a)
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
else:
    print('Impossivel calcular')