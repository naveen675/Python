# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

if __name__ == '__main__':
    
    word,r = input().split()
    word = sorted(list(word))
    ls = list(permutations(word,int(r)))
    for i in ls:
        print(''.join(i))