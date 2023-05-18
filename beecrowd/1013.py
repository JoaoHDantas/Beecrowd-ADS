#nums = input().split()
#a = int(nums[0])
#b = int(nums[1])
#c = int(nums[2])
#if a > b and c:
#    maior=a
#if b > a and c:
#    maior=b
#if c > b and a:
#    maior=c
#print(f'{maior} eh o maior')

nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
maior = (a+b+abs(a-b))/2
result = (maior+c+abs(maior-c))/2
print(f'{result:.0f} eh o maior')
