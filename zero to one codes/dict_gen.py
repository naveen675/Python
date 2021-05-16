#this program generates dictionary of size n with key as n and value as n*n


# def dict_gen(n):
#     dic = {}
#     for i in range(1,n+1):
#         dic[i]=i*i
#     return dic

###### Using Dictionar Comprehension #######

# def dict_gen(n):
    
#     return {k:k*k for k in range(1,n+1)}





###### Using Generator #######
def dict_gen(n):
    for i in range(1,n+1):
        yield i*i


if __name__=='__main__':

    #print(dict_gen(10000000))
    n=10000000000000
    count=1
    for i in dict_gen(n):
        print(str(count) +':'+str(i)+',',end='')
        count=count+1

