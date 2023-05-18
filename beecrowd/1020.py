idaded = int(input())
#dias em anos
anos =  idaded//365
#trasformar o restante de dias das conversap em anos e trasformar em meses
idaded %= 365
meses = idaded // 30
#oque sobrar dos meses sao dias 
idaded %= 30
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{idaded} dia(s)')
