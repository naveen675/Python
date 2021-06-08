# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

if __name__ == '__main__':
    
    shoes = int(input())
    sizes = list(map(int,input().split()))
    n = int(input())
    sizes = dict(Counter(sizes))

    
    sum= 0
    for i in range(n):
        size,price = map(int,input().split())
        # print(size,price)
        # print(sizes[size])
        if sizes.__contains__(size) and sizes[size] > 0:
            
            sum = sum+price
            sizes[size] = sizes[size]-1
        
    print(sum)
            
    