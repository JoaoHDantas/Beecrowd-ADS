tamanho = 0
pares = 0
impar = 0
positivo = 0
negativo = 0
for lista in range (0,5):
    x = float(input())
    if x %2 == 0:
        pares += 1
    else:
        impar += 1
    if x > 0:
        positivo += 1
    else:
        negativo += 1


print(f'{pares} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
