ent = input().split()
x = float(ent[0])
y = float(ent[1])
if x==0 and y == 0:
    print('Origem')
elif y == 0:
    print('Eixo X')
elif x == 0:
    print('Eixo Y')
elif y > 0 and x > 0:
    print('Q1')
elif y > 0 and x < 0:
    print('Q2')
elif y < 0 and x < 0:
    print('Q3')
elif y < 0 and x > 0:
    print('Q4')
