import time;
######## List Join #########

# def divisible_by_seven(num1,num2):
#     s=[]
#     for i in range(num1,num2+1):

#         if i%7 == 0 and i%5 != 0:
#             s.append(str(i))
#     print(','.join(s))   

##### end=','

def divisible_by_seven(num1,num2):
    s=[]
    for i in range(num1,num2+1):
        if i%7 == 0 and i%5!=0:
            print(i,end=',')
    print("\b")




######## list comprehension #########

# def divisible_by_seven(num1,num2):
#     t1=time.time()
#     s=[str(i) for i in range(num1,num2+1) if i%7 == 0 and i%5 !=0]
#     print(','.join(s))

#     t2 =time.time()
#     print(t2-t1)

    
#### --- Yield---- #####
# def divisible_by_seven(num1,num2):
    
    
#     for i in range(num1,num2+1):
#         if i%7 == 0 and i%5 !=0:
#             yield i

    
  
    
# t1=time.time()
# for i in divisible_by_seven(1,100000000):
#     print(i,end=',')
# print('/b')
# t2 =time.time()
# print(t2-t1)



divisible_by_seven(1,100000000)



