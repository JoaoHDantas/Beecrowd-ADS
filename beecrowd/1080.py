contador = 1
x=0
maior = 0
posicao = 0
while contador <= 100:
    x = int(input())
    if x > maior:
        maior = x
        posicao = contador
        
    contador += 1
print(maior)
print(posicao)
