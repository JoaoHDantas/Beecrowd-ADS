ini, fin = map(int,input().split())

if ini == fin:
    temp = 24

elif ini > fin:
    temp = (fin - ini) + 24

elif ini < fin:
    temp = (fin - ini)

print(f'O JOGO DUROU {temp} HORA(S)')
