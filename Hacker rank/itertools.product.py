# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

if __name__ == '__main__':
    
    
    ls = list(product(list(map(int,input().split())),list(map(int,input().split()))))
    
    for i in ls:
        print(i,end =' ')

    
    
    
