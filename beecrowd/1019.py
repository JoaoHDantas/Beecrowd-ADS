#pedir o tempo em segundos
nsec = int(input())
#converter segundos em horas
h = nsec//3600
#tirar oque sobra das horas
nsec %= 3600
#trasformar oque sobra das horas para minutos
m = nsec//60
#tirar os segundos dos minutos ¯\_(ツ)_/¯
nsec %= 60
print(f'{h}:{m}:{nsec}')
