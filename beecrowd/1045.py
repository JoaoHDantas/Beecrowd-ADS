nums = input().split()
a = float(nums[0])
b = float(nums[1])
c = float(nums[2])
if (0 < a) and (0 < b) and (0 < c):

    if a>=b+c:
        print('NAO FORMA TRIANGULO')

    if (a**2) == (b**2)+(c**2):
        print('TRIANGULO RETANGULO')

    if a**2 > (b**2) + (c**2):
        print('TRIANGULO OBTUSANGULO')

    if a**2 < (b**2) + (c**2):
        print('TRIANGULO ACUTANGULO')

    if a==b and b==c:
        print('TRIANGULO EQUILATERO')

    if (a==b or a==c or b==c) or not(a==b and a) :
        print('TRIANGULO ISOSCELES')
