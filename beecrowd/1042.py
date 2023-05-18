nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
#A sendo maior
if a>b and a>c:
    if b > c:
        print(f'{c}\n{b}\n{a}')
    else:
        print(f'{b}\n{c}\n{a}')
#B sendo maior
elif b>a and b>c:
    if a > c:
        print(f'{c}\n{a}\n{b}')
    else:
        print(f'{a}\n{c}\n{b}')
#C sendo maior
elif c>a and c>b:
    if b > a:
        print(f'{a}\n{b}\n{c}')
    else:
        print(f'{b}\n{a}\n{c}')
print()
print(f'{a}\n{b}\n{c}')
