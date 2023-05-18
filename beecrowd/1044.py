nums = input().split()
a = int(nums[0])
b = int(nums[1])

#Formula: a*x = b

if a > b:       #Se a for maior que B
    if a % b == 0:      #Encontrar o resto Caso der 0 e porque existe uma divisão perfeita ou uma multiplicação
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a < b:       #Se a for maior que A
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a == b:      #E multiplo por 1
    print('Sao Multiplos')
    