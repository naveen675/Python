import math


# def sqr(s):
#     for i in s:



if __name__ == '__main__':
    #l=input().split(',')
    # print(l)
    #print(','.join([str(int(i)**2) for i in input().split(',') if int(i)%2 != 0 ]))

   print(','.join(list(map(lambda x:str(int(x)**2),filter(lambda x: int(x)%2 == 0 ,input().split(','))))))

   #print(list(filter(lambda x: str(int(x)**2)if int(x)%2 == 0 else None ,input().split(','))))