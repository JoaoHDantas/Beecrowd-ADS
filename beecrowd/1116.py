x=int(input())
y=int(input())
if y > x:
    aux = x
    x = y
    y = aux
for tempo in range (y+1, x):

     if tempo %5 == 2 or tempo %5 == 3:
        print(tempo)
