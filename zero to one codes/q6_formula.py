import math

def formula(l):
    c=50
    h=30

    for d in l:
       f = abs((2-c-int(d))/h)
       yield f
    
l = input().split(',')

for i in formula(l):
    print(str(i)+',',end='')

