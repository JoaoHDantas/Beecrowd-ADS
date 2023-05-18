abc = input().split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])
#Calcular tiangulo
print(f'TRIANGULO: {a*c/2:.3f}')
#Calcular o raio
print(f'CIRCULO: {3.14159*c**2:.3f}')
#Calcular trapezio
print(f'TRAPEZIO: {(a+b)*c/2:.3f}')
#Calcular quadrado
print(f'QUADRADO: {b*b:.3f}')
#Calcular retangulo
print(f'RETANGULO: {a*b:.3f}')
