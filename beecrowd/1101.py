num1 = 0
num2 = 0
soma = 0
while True:
    num1,num2 = map(int,input().split())

    if num1 <= 0 or num2 <= 0:
        break
    
    if num2 > num1:
        num2, num1 = num1, num2
        
    soma = 0
    while num2 <= num1:
        soma += num2       
        print(f'{num2}', end =' ')
        num2 += 1

    print(f'Sum={soma}')
