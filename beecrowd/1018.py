num = int(input())
print(num)
n100 = num//100
num %= 100

n50 = num//50
num %= 50

n20 = num//20
num %= 20

n10 = num//10
num %= 10

n5 = num//5
num %= 5

n2 = num//2
num %=2

n1 = num//1
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')

