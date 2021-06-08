from itertools import combinations_with_replacement


if __name__ == '__main__':
    
    word,r = input().split()
    
    word = sorted(list(word))
    
    ls = combinations_with_replacement(word,int(r))
    for i in ls:
        print(''.join(i))
    