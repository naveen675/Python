# Enter your code here. Read input from STDIN. Print output to STDOUT    

from itertools import combinations


if __name__ == '__main__':
    
    word,r = input().split()
    
    word = sorted(list(word))
   
    
    for i in range(1,int(r)+1):
        for j in combinations(word,i):
            print(''.join(j))