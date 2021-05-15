import time
import sys
#Recursion

# def fact_of_number(n):
#     if n==0:
#         return 1
#     else:
#         return fact_of_number(n-1)*n


#While Loop   

# def fact_of_number(n):

#     if n==0:
#         return 1
#     i=1
#     fact =1
#     while i<=n:
#         fact = fact*i
#         i=i+1
#     return fact




# t1 = time.time()
# print(fact_of_number(1000))
# t2 = time.time()
# print(t2-t1)




def fact_of_number(n):
    
    res = [None]*100000000
    res_size = 1
    res[0] = 1

    i=2
    while i<=n:
       res_size = Multiplying(i,res,res_size)
       i=i+1

    
    res_size = res_size-1

    while res_size >= 0:

        sys.stdout.write(str(res[res_size]))
        sys.stdout.flush()
        res_size = res_size-1


#Simple Multiplication by taking carry

def Multiplying(x,res,res_size):

    i=0
    carry = 0
    while i<res_size:
        prod = res[i]*x + carry
        res[i] = prod%10
        carry = prod//10
        i=i+1
    
    while carry:
        res[res_size]=carry%10
        carry = carry//10
        res_size = res_size+1
    #print(res_size)
    return res_size

fact_of_number(1000000)