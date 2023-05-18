"""
URI 1097
Fazer um progama que apresente a sequencia comforme a sequencia abaixo
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
I=5 J=11
I=5 J=10
I=5 J=9
I=7 J=13
I=7 J=12
I=7 J=11
I=9 J=15
I=9 J=14
I=9 J=13
"""



j = 7
i = 1
num = 5
while i <=9:
    while j >= num:
        print(f'I={i} J={j}')
        j -= 1
    i +=2
    #Soma 5 para aumentar o valor do j
    j+=5
    #Adicionar 2 ao num para determinar o final da repetição
    num += 2
