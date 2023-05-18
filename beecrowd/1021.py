num = float(input())
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

print('NOTAS:')
print(f'{n100:.0f} nota(s) de R$ 100.00')
print(f'{n50:.0f} nota(s) de R$ 50.00')
print(f'{n20:.0f} nota(s) de R$ 20.00')
print(f'{n10:.0f} nota(s) de R$ 10.00')
print(f'{n5:.0f} nota(s) de R$ 5.00')
print(f'{n2:.0f} nota(s) de R$ 2.00')

n1 = num//1
num %= 1
c50 = num//0.5
num %= 0.5

c25 = num//0.25
num %= 0.25

c10 = num//0.10
num %= 0.10

c5 = num//0.05
num %= 0.05

c1 = num/0.01

print('MOEDAS:')
print(f'{n1:.0f} moeda(s) de R$ 1.00')
print(f'{c50:.0f} moeda(s) de R$ 0.50')
print(f'{c25:.0f} moeda(s) de R$ 0.25')
print(f'{c10:.0f} moeda(s) de R$ 0.10')
print(f'{c5:.0f} moeda(s) de R$ 0.05')
print(f'{c1:.0f} moeda(s) de R$ 0.01')

