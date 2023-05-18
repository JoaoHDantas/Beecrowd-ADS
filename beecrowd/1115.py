contador = 1
media = 0
while contador <= 2:
    
    nota = float(input())
    if  nota >=0 and nota <=10 :
        media +=nota
        contador += 1
    else:
        print ('nota invalida')
print (f'media = {media/2:.2f}')
