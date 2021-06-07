from functools import reduce

# n = input()
# def accumulator(acc,item):
#     print(acc)
#     print(int(n*item))
    #acc = acc+int(n*item)



if __name__ == '__main__':
#    n = input()
   #print(sum([1,2,3,4]))
   #print(sum(int(n*i) for i in range(1,5)) )
   n = input()
   print(reduce(lambda x,y:int(x)+int(y),[n*i for i in range(1,5)],))
