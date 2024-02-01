import math
alphabet = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())

while t:
    t -= 1
    a = []
    a = [int(i) for i in input().split(' ')]
    a = sorted(a)
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
        continue
    print(f'the {11 - t} is', math.gcd(a[0], a[1], a[2]))
    

