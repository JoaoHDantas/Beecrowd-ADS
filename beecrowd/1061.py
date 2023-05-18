dia1 = int(input().split()[1])
h1, min1, sec1 = map(int,input().split(':'))
t1 = sec1 + min1*60 + h1*60*60 + dia1*24*60*60

dia2 = int(input().split()[1])
h2, min2, sec2 = map(int,input().split(':'))
t2 = sec2 + min2*60 + h2*60*60 + dia2*24*60*60

diferenca = t2 - t1
d = diferenca//(24*60*60)
diferenca %= (24*60*60)

h = diferenca//(60*60)
diferenca %= (60*60)

m = diferenca//(60)
diferenca %= (60)

s = diferenca

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')
