n = int(input())
contador = 1
inn = 0
out = 0
while contador <= n:
    
    x = int(input())
    if x >= 10 and x <= 20:
        inn += 1
    else:
        out += 1
    contador += 1
print (f'{inn} in')
print (f'{out} out')
