
def fibo(n):

    if n==0:
        return 0
    elif n==1 or n==2:
        return 1

    return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':

    #print(fibo(int(input())))                                                  # Using Recursion function


    ####    Using Lambda    ####

    f=lambda x : 0 if x==0 else 1 if x==1 or x==2 else f(x-1)+f(x-2)
    print(','.join([str(f(i)) for i in range(int(input())+1)]))


    
