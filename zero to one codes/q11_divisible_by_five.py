
import math

def check(a) :
    sum=0
    a = list(a)
    a = a[::-1]
    for i,j in enumerate(a):
        if j=='1':
            sum = sum + math.pow(2,i)
            
    if sum%5==0:
        return True
    return False



# def div_by_five(s):
#     s = s.split(',')
#     l=[]
#     for i in s:
#         if int(i,2)%5==0:
#             l.append(i)
        
    # return ','.join(l)

# def div_by_five(s):
#     s = s.split(',')
#     l=[]
#     for i in s:
#         if check(i) == 0:
#             l.append(i)
        
#     return ','.join(l)
#check('1000') 


if __name__ == "__main__":

    #print(div_by_five(input()))

    print(','.join(list(filter(lambda a: int(a,2)%5==0,input().split(',')))))
    #print(ord('1'))


